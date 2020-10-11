from flask import request as flaskrequest
from typing import List
from ..shared.action_result import error,success,ActionResult


class ServiceBase:
    """
        Base object for services.
        Calls methods defined on a child object
    """
    def __init__(self, db: SqlConnection):
        self.db = db
        
    def invoke_action(request: flaskrequest, action: str) -> ActionResult:
        try:
            if validate_request(request, action):
                return success(getattr(self, action)(request.data))
            else:
                return error("Wrong action",400)
        except Exception as e:
            return error("Unhandled exception:" + e,500)
        

    def validate_request(request: flaskrequest, action: str)->bool:
        self_methods = [method_name for method_name in dir(self) if callable(getattr(self, method_name))
        self_methods = filter(lambda x:x == action, self_methods)
        return True if self_methods.__len__=1 else False


        