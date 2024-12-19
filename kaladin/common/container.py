from kaladin.common.core_factory import CoreFactory
from kaladin.common.database import build_database_connection
from kaladin.common.secrets_manager import load_secrets
from kaladin.common.use_case_factory import UseCaseFactory


def build_core_factory() -> CoreFactory:
    secrets = load_secrets()
    db_connection = build_database_connection(secrets)
    return CoreFactory(db_connection, secrets)


def build_use_case_factory() -> UseCaseFactory:
    core_factory = build_core_factory()
    return core_factory.use_case_factory
