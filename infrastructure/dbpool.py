from flask import g
from typing import Dict
from mysql.connector.pooling import MySQLConnectionPool, PooledMySQLConnection


class DbPool:
    """
        MySql db pool
        Pools connections for databases defined in config
    """
    _databases: Dict[str, MySQLConnectionPool] = {}

    def __init__(self, config: dict):
        for db in config.keys():
            self._databases[db] = MySQLConnectionPool(
                pool_size=5, pool_name=db, **self.make_connection_string(config[db]))

    def get_connection(self, database_name: str) -> PooledMySQLConnection:
        return self._databases[database_name].get_connection()

    def make_connection_string(self, config_db: object) -> object:
        return {
            "host": config_db["HOST"],
            "port": config_db["PORT"],
            "user": config_db["USER"],
            "password": config_db["PASSWORD"],
            "database": config_db["NAME"]
        }


def get_dbpool(config={}) -> DbPool:
    return DbPool(config)
