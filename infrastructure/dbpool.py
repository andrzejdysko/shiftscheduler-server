from flask import g
from typing import Dict
from mysql.connector import pooling


class DbPool:
    """
        MySql db pool
        Pools connections for databases defined in config
    """
    _databases: Dict[str, MySQLConnectionPool] = []

    def __init__(self, config: dict):
        config_dbs = config["DATABASES"]
        for db in config_dbs.keys():
            self._databases[db] = MySQLConnectionPool(100, config_dbs[db])

    def get_connection(database_name: str) -> PooledMySQLConnection:
        return self._databases[database_name].get_connection()

    def make_connection_string(config_db: object) -> object:
        return {
            host = config_db.HOST,
            port = config_db.PORT,
            user = config_db.USER,
            password = config_db.PASSWORD,
            database = config_db.NAME
        }


def get_dbpool(config):
    return DbPool(config)
