from pydantic import BaseModel, AnyUrl
from sqlalchemy import Column, DateTime, Integer, String, Table
from sqlalchemy.sql import func


class SourceSchema(BaseModel):
    name: str
    url: AnyUrl


class SourceDB(SourceSchema):
    id: int
    url: str


class Source:
    """Model for recipe source website"""

    def __init__(self, metadata):
        self.metadata = metadata

    def create_table(self):
        return Table(
            "sources",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String(50)),
            Column("url", String(255)),
            Column("created_date", DateTime, default=func.now(), nullable=False),
        )
