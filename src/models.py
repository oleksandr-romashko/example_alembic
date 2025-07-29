from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Table,
    Column,
    Integer,
    PrimaryKeyConstraint,
    func,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Base class with metadata
class Base(DeclarativeBase):
    pass


# Bridge table for many-to-many relationship between notes and tags
note_tag_association_table = Table(
    "note_tag_association_table",
    Base.metadata,
    Column(
        "note_id",
        Integer,
        ForeignKey("notes.id", ondelete="CASCADE"),
    ),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE")),
    PrimaryKeyConstraint("note_id", "tag_id"),
)


class Record(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(nullable=False)
    is_done: Mapped[bool] = mapped_column(default=False, server_default=text("false"))
    note_id: Mapped[int] = mapped_column(
        ForeignKey("notes.id", ondelete="CASCADE"), index=True
    )

    note: Mapped["Note"] = relationship(back_populates="records")


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )

    records: Mapped[list["Record"]] = relationship(
        cascade="all, delete", back_populates="note"
    )
    tags: Mapped[list["Tag"]] = relationship(
        secondary=note_tag_association_table, back_populates="notes"
    )


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)

    notes: Mapped[list["Note"]] = relationship(
        secondary=note_tag_association_table, back_populates="tags"
    )
