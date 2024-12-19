from kaladin.common.database import DatabaseConnection


class BaseDAO:

    def __init__(self,
                 db_connection: DatabaseConnection,
                 secrets: dict):
        self._db_connection = db_connection
        self._secrets = secrets
