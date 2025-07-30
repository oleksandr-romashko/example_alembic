# 🧪 SQLAlchemy + Alembic Example Project (with SQLite) <!-- omit in toc -->

This project demonstrates a minimal setup using **SQLAlchemy 2.0**, **Alembic** for schema migrations, and **SQLite** as the database engine.

It serves as a guided example for learning how to manage ORM-based database versioning. The schema is based on a simple TODO/notes system with:

* Notes with multiple records (like steps or tasks)
* A flexible tagging system (multiple tags per note)
* JSON output for clear results

> ⚠️ **Note**
> This is not a full-featured application or CLI tool.
> It's a learning-oriented project designed to help you understand and practice Alembic migrations with SQLAlchemy. It's meant to demonstrate how to set up and manage database versioning with Alembic and SQLAlchemy.
> You can use it as a base to build and experiment with more advanced setups.

---

## 📚 Table of Contents <!-- omit in toc -->

- [🎯 Purpose](#-purpose)
- [📦 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🛠️ Setup](#️-setup)
  - [1. Install dependencies](#1-install-dependencies)
  - [2. Initialize the database and run migrations](#2-initialize-the-database-and-run-migrations)
  - [3. Seed the database](#3-seed-the-database)
  - [4. Run the sample query to test if everything is working](#4-run-the-sample-query-to-test-if-everything-is-working)
- [📘 Schema Change \& Revision Walkthrough](#-schema-change--revision-walkthrough)
  - [1. Step 1: Modify the models](#1-step-1-modify-the-models)
  - [2. Step 2: Generate a new revision](#2-step-2-generate-a-new-revision)
  - [3. Step 3: Apply the migration](#3-step-3-apply-the-migration)
  - [4. Step 4: Run the sample query to test if everything worked out](#4-step-4-run-the-sample-query-to-test-if-everything-worked-out)
  - [🧭 Inspecting database revision state](#-inspecting-database-revision-state)
    - [🔍 See current revision](#-see-current-revision)
    - [📜 See revision history](#-see-revision-history)
  - [↩️ Reverting changes](#️-reverting-changes)
- [⚙️ Requirements](#️-requirements)
- [📄 License](#-license)


## 🎯 Purpose

This repository serves as an example in a form of a **progressive walkthrough** for **Alembic migrations tool** — starting from a working schema and guiding you through common database development workflows using Alembic and SQLAlchemy.

You'll see examples and learn how to:

1. Initialize and run Alembic migrations
2. Seed example data
3. Query and filter related data
4. Create and modify your models (e.g., adding new fields)
5. Generate new migrations from model changes
6. Apply migrations safely
7. Observe and understand schema/data evolution

This is a great starting point if you're:
- New to SQLAlchemy 2.0 or Alembic
- Prototyping a relational app with structured migrations

---

## 📦 Features

- SQLAlchemy ORM with relationships
- SQLite database
- Alembic migrations
- Data seeding
- Queries via SQLAlchemy Core

## 📂 Project Structure

- [models.py](./src/models.py) — defines ORM models (`Note`, `Record`, `Tag`).
- [connect.py](./src/connect.py) — DB connection and session setup.
- [migrations/](./migrations/) — Alembic migration scripts directory.
- [data/](./data/) — Directory to hold the SQLite database file (empty except for `.gitkeep` to keep the `data/` directory in Git).
- [seeds.py](./src/seeds.py) — Seeds the DB with initial data.
- [query-revision-0.py](./src/query-revision-0.py) — Queries notes with the query to retrieve seeded data (db schema revision 0 - initial).
- [query-revision-1.py](./src/query-revision-1.py) — Queries notes with the query to retrieve seeded data (db schema revision 1 - added note description and record order).

## 🛠️ Setup

### 1. Install dependencies

```bash
poetry install
```

This will install all necessary project dependencies.

### 2. Initialize the database and run migrations

```bash
poetry run alembic upgrade head
```

This will create the SQLite database `mynotes.db` inside the `data/` directory and apply all currently available migrations (this will bring your database to revision 0, representing the initial schema version used in this project).

Current database structure is based on provided ORM models located in `src/models.py`.

Initial revision database schema:

![ER-Diagram-initial-revision](./assets/uml/ER-Diagram-initial-revision.jpg)

### 3. Seed the database

```bash
poetry run python ./src/seeds.py
```

This will add sample data to the database tables.

> **Note**: To rerun `seeds.py`, you'll need to delete `data/mynotes.db` file and initialize the database (previous step) again.

### 4. Run the sample query to test if everything is working

> **Note**: Make sure your database file exists under `data/` before querying using `query-revision-0.py`.

```bash
poetry run python ./src/query-revision-0.py
```

This will show current notes data, filtered by "food" and "cooking" tags and displayed in JSON format for easier reading.

<details> <summary>Click to expand and see easy to read JSON-like output</summary>

```bash
✅ Showing notes related to tags: food, cooking
[
  {
    "note_id": 1,
    "title": "Buy ingredients for supper",
    "created_at": "2025-07-30T14:35:15",
    "updated_at": "2025-07-30T14:35:15",
    "tags": [
      "food",
      "groceries"
    ],
    "records": [
      {
        "description": "Buy chicken breast, 500g",
        "is_done": false
      },
      {
        "description": "Buy potatoes, 1kg",
        "is_done": false
      },
      {
        "description": "Buy garlic and parsley",
        "is_done": false
      },
      {
        "description": "Buy sour cream",
        "is_done": false
      }
    ]
  },
  {
    "note_id": 2,
    "title": "Cook supper: Chicken with potatoes",
    "created_at": "2025-07-30T14:35:15",
    "updated_at": "2025-07-30T14:35:15",
    "tags": [
      "cooking",
      "dinner"
    ],
    "records": [
      {
        "description": "Clean and slice the potatoes, 1kg",
        "is_done": false
      },
      {
        "description": "Season the chicken breast (500g) and fry lightly",
        "is_done": false
      },
      {
        "description": "Bake everything together for 60 minutes at 180°C",
        "is_done": false
      },
      {
        "description": "Garnish with parsley and serve",
        "is_done": false
      }
    ]
  }
]
```
</details>

## 📘 Schema Change & Revision Walkthrough

This guide will walk you through a staged database evolution process using Alembic. You'll start with a minimal schema and later upgrade it via revision-based migrations.

The following shows database versioning in case of any changes to ORM models.

### 1. Step 1: Modify the models

  > ℹ️ After completing these demo steps, you can continue practicing database schema evolution by introducing your own changes to the ORM models and following the same revision process shown below.

  To demonstrate how Alembic tracks database revisions, we'll now extend the schema by introducing two new fields in the `models.py` file:

  - `Note.description` — adds a longer text field to describe the note.
  - `Record.order` — allows prioritizing or sorting records within a note.

  These fields are already present in the code but commented out for this demo. To enable them, uncomment the following lines in `models.py`:

  ```python
  class Record(Base):
      ...
      # order: Mapped[int] = mapped_column(
      #     nullable=False, default=-1, server_default=text("-1")
      # )
      ...

  class Note(Base):
      ...
      # description: Mapped[str] = mapped_column(
      #     nullable=False, default="", server_default=text("''")
      # )
      ...
  ```

  Your updated schema should now look like this:

  ![ER-Diagram-revision-1](./assets/uml/ER-Diagram-revision-1.jpg)

  > ⚠️  **Important**:
  > At this point, your ORM model structure no longer matches the actual database schema — the new fields exist in the Python code but **not yet** in the database.
  Any code that attempts to access these fields (like `query-revision-0.py`) will raise errors until you apply the migration in the next steps.
  > 
  > This is expected. You'll fix it by generating and applying a migration shortly.

### 2. Step 2: Generate a new revision

  Now that you've updated the models, it's time to generate a migration script that captures the changes you've made.

  Run the following command:

  ```bash
  poetry run alembic revision --autogenerate -m "Add description to Note and order to Record"
  ```

  > **Note**:  
  > If you make your own changes to the models in future, update the message after `-m` accordingly — it should describe the changes made since the previous revision.

  This will create a new migration file in the `migrations/versions/` directory.

  > ⚠️ This step only *generates* the migration script.  
  > The actual database structure will not change until you **apply** the migration in the next step.

### 3. Step 3: Apply the migration

  Now that you've generated the migration script, it's time to apply it and update the actual database schema.

  Run the following command:
      
  ```bash
  poetry run alembic upgrade head
  ```

  This will apply the latest migration and bring your database schema in sync with the updated models.

  >ℹ️ You can re-run this command any time to ensure the database is up to date with the latest revision.

### 4. Step 4: Run the sample query to test if everything worked out

  Now that the migration has been applied, let's run the sample script to verify that your updated database schema is working as expected.

  Run the following command:

  ```bash
  poetry run python ./src/query-revision-1.py
  ```

  This will fetch and display the current notes data, now including the newly added `description` and `order` fields.

  ✅ If you see the new fields without any errors, the migration was successful!

  <details> <summary>Click to expand and see easy to read JSON-like output</summary>

  ```bash
  ✅ Showing notes related to tags: food, cooking
  [
    {
      "note_id": 1,
      "title": "Buy ingredients for supper",
      "description": "",      // ← NEW FIELD
      ...
      "records": [
        {
          "description": "Buy chicken breast, 500g",
          "is_done": false,
          "order": -1      // ← NEW FIELD
        },
        ...
      ]
    },
    ...
  ]
  ```
  </details>

  > 🧪 Want to keep practicing?
  > Go back to Step 1 and try introducing your own changes to the database schema to see how Alembic tracks and applies revisions.

### 🧭 Inspecting database revision state

After running a migration, you might want to inspect the current state of your database or view the full revision history. Alembic provides handy commands for this.

#### 🔍 See current revision

Check which migration is currently applied to your database:

```bash
poetry run alembic current
```

This shows the current revision ID that your database is at.

#### 📜 See revision history

List all available migrations and their order:

```bash
poetry run alembic history
```

This helps you understand the full chain of revisions and where your current state fits in.

> ℹ️ These commands are especially helpful when debugging version mismatches or when working in a team to verify everyone's database is in sync.

### ↩️ Reverting changes

If something went wrong or you want to undo the latest schema changes, you can roll back the last migration:

```bash
poetry run alembic downgrade -1
```

This will revert database schema, but seeded data (unless removed manually) will stay.

> ℹ️ This rolls back just the *last* applied migration.
> You can chain this with multiple `-1` steps or use full revision identifiers as needed.


> ⚠️ **Caution**:
> Downgrading can lead to **data loss** — for example, if you added a column and inserted values, both the column and the data will be dropped.
> Consider backing up your database before running a downgrade in production or critical environments.

## ⚙️ Requirements

* [Python 3.11+](https://www.python.org/downloads/) (tested on 3.12.11)
* [Poetry](https://python-poetry.org/) (tested on 2.1.3)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) (tested on 1.16)

## 📄 License

[MIT License](./LICENSE) · Happy hacking!
