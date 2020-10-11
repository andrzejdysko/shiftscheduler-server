from typing import Dict

from .dbpool import DbPool
from ..shared.action_result import success, error, ActionResult
from .sql_procedure_builder import  build_sql_command


class SqlConnection:
    """
        Wraps database connection
        Exposes basic db operation execute_procedure
    """
    _connection = {}

    def __init__(self, dbpool: DbPool, database_name: str):
        self._connection = dbpool.get_connection(database_name)

    def query_procedure(self, procedure_name: str, arguments: Dict) -> [Dict,str]:
        query_result = self.execute_procedure(procedure_name, arguments)
        return query_result._data if query_result.is_valid() else query_result._message

    def command_procedure(self, procedure_name: str, arguments: Dict) -> [bool,str]:
        command_result = self.execute_procedure(procedure_name, arguments)
        return command_result._message if not command_result.is_valid() else True

    def execute_procedure(self, procedure_name: str, arguments: Dict) -> ActionResult:
        sql_command = build_sql_command(self,procedure_name, arguments)
        return self.execute(sql_command)

    def execute(self, sql_command: str) -> ActionResult:
        try:
            cursor = self._connection.cursor(dictionary=True,buffered=True)           
            for result in cursor.execute(sql_command,multi=True):
                if result.with_rows:
                    data= result.fetchall() 
            return success(data)
        except Exception as ex:
            ex_message = ex.__str__
            error("Database error while running:"+ sql_command)
        finally:
            cursor.close()

    def close(self):
        self._connection.close()
