import json
import sqlite3
import sys

from sqlalchemy.orm import joinedload

from connect import session
from models import Note, Tag

filtered_tags = ["food", "cooking"]


def warn_not_initialized(e: Exception):
    print("❌ Database error - not initialized or missing required tables:", e)
    print("👉 Run the following command to initialize the database:")
    print("   poetry run alembic upgrade head")


def warn_schema_outdated(e: Exception):
    print("❌ Failed to query notes:", e)
    print("👉 This likely means the database schema is outdated.")
    print("   Run: poetry run alembic upgrade head")


def warn_unseeded_data():
    print("⚠️  No notes found for tags:", ", ".join(filtered_tags))
    print("👉 The database might be empty. Did you forget to run `seeds.py`?")


def main() -> None:
    """
    # Exit codes:
    # 0 - Success
    # 1 - Database not initialized
    # 2 - Schema outdated
    # 3 - Database empty (not seeded)
    """
    notes = None
    try:
        notes = (
            session.query(Note)
            .options(joinedload(Note.tags), joinedload(Note.records))
            .order_by(Note.id)
            .filter(Note.tags.any(Tag.name.in_(filtered_tags)))
            .all()
        )
    except sqlite3.OperationalError as e:
        warn_schema_outdated(e)
        sys.exit(2)
    except Exception as e:
        warn_not_initialized(e)
        sys.exit(1)
    finally:
        session.close()

    # Check for seeded data
    if not notes:
        warn_unseeded_data()
        sys.exit(3)

    # Prepare retrieved data
    output = []
    for note in notes:
        output.append(
            {
                "note_id": note.id,
                "title": note.title,
                "description": note.description,
                "created_at": note.created_at.isoformat(),
                "updated_at": note.updated_at.isoformat(),
                "tags": sorted({tag.name for tag in note.tags}),
                "records": [
                    {
                        "description": record.description,
                        "is_done": record.is_done,
                        "order": record.order,
                    }
                    for record in note.records
                ],
            }
        )

    # Pretty-print as JSON with title
    print("✅ Showing notes related to tags:", ", ".join(filtered_tags))
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
