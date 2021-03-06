from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    NVARCHAR,
    DateTime,
    Boolean,
)


meta = MetaData()


def upgrade(migrate_engine):
    meta.bind = migrate_engine

    t = Table(
        "table",
        meta,
        Column("id", Integer, primary_key=True),
        Column("name", NVARCHAR(100), index=True, nullable=False, unique=True),
        Column("filename", NVARCHAR(500), nullable=False),
        Column("created_datetime", DateTime, nullable=False),
    )
    t.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    t = Table("table", meta, autoload=True)
    t.drop()