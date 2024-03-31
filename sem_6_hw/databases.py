'''Создание и подключение к базе данных'''

import databases
import sqlalchemy

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32), nullable=False),
    sqlalchemy.Column("surname", sqlalchemy.String(32), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String(32), nullable=False),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column("item_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('items.id'), nullable=False),
    sqlalchemy.Column("date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String(32), nullable=False),
)

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(300), nullable=False),
    sqlalchemy.Column("price", sqlalchemy.DECIMAL, nullable=False)
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
