from typing import Any

import psycopg2
import psycopg2.extras


class DatabaseConnection:
    def __init__(self, connection: Any):
        self.connection = connection

    def _execute(self, query: str, *args: Any, **kwargs: Any) -> Any:
        cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(query, *args)
        return cursor

    def fetch_one(self, sql: str, *args: Any) -> dict:
        cursor = self._execute(sql, *args)
        result = cursor.fetchone()
        cursor.close()
        return result

    def fetch_all(self, sql: str, *args: Any) -> list[dict]:
        cursor = self._execute(sql, *args)
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert_record(self, sql: str, *args: Any) -> None:
        cursor = self._execute(sql, *args)
        self.connection.commit()
        cursor.close()


def build_database_connection(secrets: dict) -> DatabaseConnection:
    return DatabaseConnection(connection=psycopg2.connect(
        database=secrets["db_name"],
        user=secrets["db_username"],
        password=secrets["db_password"],
        host=secrets["db_hostname"],
        port=secrets["db_port"]
    ))


