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
    """Base class for all ORM models with metadata."""

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
    """
    Represents a single record or step within a Note.

    Attributes:
        id (int): Primary key.
        description (str): Text description of the record.
        is_done (bool): Completion status of the record.
        # order (int): Ordering index for sorting records within a note.
        note_id (int): Foreign key referencing the parent Note.
        note (Note): Relationship back to the parent Note.
    """

    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(nullable=False)
    is_done: Mapped[bool] = mapped_column(default=False, server_default=text("false"))
    # TODO: Uncomment this field after applying revision 1
    # order: Mapped[int] = mapped_column(
    #     nullable=False, default=-1, server_default=text("-1")
    # )
    note_id: Mapped[int] = mapped_column(
        ForeignKey("notes.id", ondelete="CASCADE"), index=True
    )

    note: Mapped["Note"] = relationship(back_populates="records")


class Note(Base):
    """
    Represents a Note which can contain multiple Records and multiple Tags.

    Attributes:
        id (int): Primary key.
        title (str): Title of the note.
        # description (str): Extended description or details of the note.
        created_at (datetime): Timestamp when note was created.
        updated_at (datetime): Timestamp when note was last updated.
        records (List[Record]): Related Records belonging to the Note.
        tags (List[Tag]): Tags associated with the Note.
    """

    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    # TODO: Uncomment this field after applying revision 1
    # description: Mapped[str] = mapped_column(
    #     nullable=False, default="", server_default=text("''")
    # )
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
    """
    Represents a Tag for categorizing Notes.

    Attributes:
        id (int): Primary key.
        name (str): Unique tag name.
        notes (List[Note]): Notes associated with this Tag.
    """

    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)

    notes: Mapped[list["Note"]] = relationship(
        secondary=note_tag_association_table, back_populates="tags"
    )
