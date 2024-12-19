from kaladin.common.dao_factory import DaoFactory
from kaladin.common.database import DatabaseConnection
from kaladin.common.use_case_factory import UseCaseFactory


class CoreFactory:

    def __init__(self,
                 db_connection: DatabaseConnection,
                 secrets: dict):
        self._db_connection = db_connection
        self._secrets = secrets

    @property
    def dao_factory(self) -> DaoFactory:
        return DaoFactory(self._db_connection, self._secrets)

    @property
    def use_case_factory(self) -> UseCaseFactory:
        return UseCaseFactory(self.dao_factory)
