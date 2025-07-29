from connect import session
from models import Note, Record, Tag

if __name__ == "__main__":
    try:
        if session.query(Note).first():
            print("⚠️  Database already seeded. Skipping...")
            session.close()
            exit()
    except Exception as e:
        print(f"❌ Failed to seed the database: {e}")
        session.rollback()

    print("Seeding database...")

    # Create tags
    tag_groceries = Tag(name="groceries")
    tag_food = Tag(name="food")
    tag_cooking = Tag(name="cooking")
    tag_dinner = Tag(name="dinner")

    # Note 1: Buy groceries
    groceries_note = Note(title="Buy ingredients for supper")
    groceries_note.tags = [tag_groceries, tag_food]

    groceries_note.records = [
        Record(description="Buy chicken breast, 500g"),
        Record(description="Buy potatoes, 1kg"),
        Record(description="Buy garlic and parsley"),
        Record(description="Buy sour cream"),
    ]

    # Note 2: Cook supper
    cook_note = Note(title="Cook supper: Chicken with potatoes")
    cook_note.tags = [tag_cooking, tag_dinner]

    cook_rec1 = Record(description="Clean and slice the potatoes, 1kg", note=cook_note)
    cook_rec2 = Record(
        description="Season the chicken breast (500g) and fry lightly", note=cook_note
    )
    cook_rec3 = Record(
        description="Bake everything together for 60 minutes at 180°C", note=cook_note
    )
    cook_rec4 = Record(description="Garnish with parsley and serve", note=cook_note)

    # Save all to DB
    try:
        session.add_all([groceries_note, cook_note])
        session.commit()
        print("✅ Database seeded successfully.")
    except Exception as e:
        print(f"❌ Failed to seed the database: {e}")
        session.rollback()
    finally:
        session.close()
