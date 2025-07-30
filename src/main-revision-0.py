from connect import session
import json
from sqlalchemy.orm import joinedload

from models import Note, Tag


def main() -> None:
    try:
        filtered_tags = ["food", "cooking"]

        notes = (
            session.query(Note)
            .options(joinedload(Note.tags), joinedload(Note.records))
            .order_by(Note.id)
            .filter(Note.tags.any(Tag.name.in_(filtered_tags)))
            .all()
        )

        session.close()

        # Prepare data
        output = []
        for note in notes:
            output.append(
                {
                    "note_id": note.id,
                    "title": note.title,
                    "created_at": note.created_at.isoformat(),
                    "updated_at": note.updated_at.isoformat(),
                    "tags": sorted({tag.name for tag in note.tags}),
                    "records": [
                        {"description": record.description, "is_done": record.is_done}
                        for record in note.records
                    ],
                }
            )

        # Pretty-print as JSON
        print("Showing notes related to the following tags:", ", ".join(filtered_tags))
        print(json.dumps(output, indent=2, ensure_ascii=False))
    except Exception as e:
        print("❌ Failed to query notes:", e)
    finally:
        session.close()


if __name__ == "__main__":
    main()
