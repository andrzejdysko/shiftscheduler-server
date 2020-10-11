from ...shared.action_result import ActionResult

def error(message: str = "", http_code: int=500):
    return HttpActionResult(False,{},message,http_code)

def success(data={}):
    return HttpActionResult(True,data,"")

class HttpActionResult(ActionResult):

    result: bool = True
    data = {}
    message: str = ""
    http_code: int = 200
    def __init__(self, result:bool=True, data={}, message="", http_code=200):
        super().__init__(result,data,message)
        self.http_code = http_code

    

    