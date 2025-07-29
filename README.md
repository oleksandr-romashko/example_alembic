# Example Alembic Project

This project demonstrates a minimal setup of SQLAlchemy 2.0 with Alembic migrations and SQLite.

## 📦 Features

- ✅ SQLAlchemy 2.0+ (async/modern API)
- ✅ Alembic for database schema migrations
- ✅ SQLite as a simple local database
- ✅ Poetry for dependency and environment management

## 📂 Project Structure

- `models.py` — defines ORM models.
- `db.py` — sets up the database engine and session.
- `main.py` — main entry point (could be CLI, test runner, etc).
- `migrations/` — Alembic migration scripts.
- `data/` — holds the SQLite database file (empty except for `.gitkeep`).

## 🛠️ Setup

### 1. Install dependencies

```bash
poetry install
```

### 2. Initialize DB and run migrations

```bach
poetry run alembic upgrade head
```

This will create the SQLite database in the data/ directory and apply all migrations.

### 3. Create new revision (after model change)

```bash
poetry run alembic revision --autogenerate -m "Your message"
```

### 4. Apply new migration

```bash
poetry run alembic upgrade head
```

## ⚙️ Requirements

* Python 3.11+ (tested on 3.12.11)
* Poetry
* SQLAlchemy 2.0+
* Alembic 1.16+

## 📝 Notes

* `.gitkeep` is used to keep the `data/` directory in Git, though the actual database file is usually `.gitignored`.
* This project is meant for learning purposes and can be extended into a full app.

## 📄 Licence

[MIT License](./LICENSE) · Happy hacking!
