# 🧪 Example Alembic Project

This project demonstrates a minimal setup using **SQLAlchemy 2.0**, **Alembic** for migrations, and **SQLite** as the database.

It's a simple, self-contained TODOs / notes app that features:

- ✅ TODOs / Notes with multiple records (like steps or tasks)
- ✅ A tagging system (multiple tags per note)
- ✅ JSON output for filtered results

> ⚠️ **Note**: This is not a complete app or a full-featured CLI. It's meant to demonstrate how to set up and manage database versioning with Alembic and SQLAlchemy.

---

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
- [data/](./data/) — Directory to hold the SQLite database file (empty except for `.gitkeep`).
- [seeds.py](./src/seeds.py) — Seeds the DB with initial data.
- [main.py](./src/main.py) — Queries notes with the query to retrieve data.

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

This will create the SQLite database inside the `data/` directory and apply all migrations.

### 3. Seed the database

```bash
poetry run python ./src/seeds.py
```

This will add sample data to the to database tables.

## ▶️ Run the App

### 1. Run the sample query

```bash
poetry run python ./src/main.py
```

## 📝 Notes

* `.gitkeep` is used to keep the `data/` directory in Git, though the actual database file is `.gitignored`.
* Make sure your database file exists under `data/` before querying using `main.py`.
* To rerun `seeds.py`, you'll need to clear the DB or add duplicate handling.
* This project is meant for learning purposes and can be extended into a full app.

## ⚙️ Requirements

* [Python 3.11+](https://www.python.org/downloads/) (tested on 3.12.11)
* [Poetry](https://python-poetry.org/) (tested on 2.1.3)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) (tested on 1.16)

## 📄 Licence

[MIT License](./LICENSE) · Happy hacking!
