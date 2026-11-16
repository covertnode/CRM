print("TEST FILE IS RUNNING")
from sqlalchemy import text
from app.database.connection import engine

from app.database.base import Base
from app.database.customer import Customer

print(Base.metadata.tables.keys())

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database()"))
        database_name = result.scalar()

        print("Connected successfully!")
        print("Database:", database_name)

except Exception as e:
    print("Database connection failed:")
    print(e)
