from typing import Dict

from .dbpool import DbPool
from ..shared.action_result import success, error, ActionResult


class SqlConnection:
    """
        Wraps database connection
        Exposes basic db operation execute_procedure
    """
    _connection = {}

    def __init__(self, dbpool: DbPool, database_name: str):
        self._connection = dbpool.get_connection(database_name)

    def query_procedure(self, procedure_name: str, arguments: Dict) -> Dict:
        query_result = self.execute_procedure(procedure_name, arguments)
        return query_result.data if query_result.is_valid() else {}

    def command_procedure(self, procedure_name: str, arguments: Dict) -> bool:
        command_result = self.execute_procedure(procedure_name, arguments)
        return command_result.is_valid()

    def execute_procedure(self, procedure_name: str, arguments: Dict) -> ActionResult:
        sql_command = build_sql_command(procedure_name, arguments)
        return self.execute(sql_command)

    def execute(self, sql_command: str) -> ActionResult:
        try:
            return self._connection.cursor(dictionary=True).execute(sql_command).fetchall()
        except Exception as ex:
            error(ex)

    def close():
        self._connection.close()
