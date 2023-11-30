import psycopg2
from dotenv import load_dotenv
import os
import psycopg2.extras

load_dotenv()  # Load environment variables from .env file if applicable

database_url = os.getenv("postgresql://postgres:12345@localhost:5432/flask_todo")  # Retrieve database URL from environment variables

try:
    with psycopg2.connect(database_url) as client:
        with client.cursor(cursor_factory=psycopg2.extras.DictCursor) as db:
            table_name = "todos"

            def create_table():
                create_todo_query = """
                CREATE TABLE IF NOT EXISTS todos (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description VARCHAR(255) NOT NULL
                );
                """
                db.execute(create_todo_query)
                print("Table Created Successfully in PostgreSQL")

            def check_if_exists(table_name):
                try:
                    db.execute("""
                                SELECT EXISTS(
                                SELECT 1 FROM information_schema.tables WHERE table_catalog='flask-todo'
                                AND table_schema='public'
                                AND table_name=%s
                                );
                               """, (table_name,))
                    return db.fetchone()[0]
                except psycopg2.Error as e:
                    print("Error:", e)
                    return False

            print(f"Table {table_name} exists: {check_if_exists(table_name)}")

            if not check_if_exists(table_name):
                create_table()
            else:
                print("Table already exists")

            print(f"Table {table_name} exists: {check_if_exists(table_name)}")
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
