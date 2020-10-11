from flask import request as flaskrequest
from typing import List
from ..router.controllers.http_action_result import error, success, HttpActionResult
from ..infrastructure.sql_connection import SqlConnection

class ServiceBase(object):
    """
        Base object for services.
        Calls methods defined on a child object
    """

    def __init__(self, db: SqlConnection):
        self.db = db

    def invoke_action(self, request: flaskrequest, action: str) -> HttpActionResult:
        try:
            if self.validate_request(request, action):
                data = request.args if request.method == "GET" else request.data
                result = getattr(self, action)(data)
                return success(result.data) if result.is_valid else error(result.message, 400)
            else:
                return error("Wrong action", 400)
        except Exception as e:
            message = "Unhandled exception:" + e.__str__()
            return error(message, 500)

    def validate_request(self, request: flaskrequest, action: str) -> bool:
        self_methods = [method_name for method_name in dir(self) if callable(getattr(self, method_name))]
        return True if action in self_methods else False
