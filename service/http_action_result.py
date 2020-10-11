def error(message: str = "", http_code: int):
    return HttpActionResult(False,{},message,http_code)

def success(data={}):
    return HttpActionResult(True,data,"")

class HttpActionResult(ActionResult):

    _result: bool = True
    _data = {}
    _message: str = ""
    _http_code: int = 200
    def __init__(self, result, data, message, http_code=200):
        super(result, data, message)
        #self._result = result
        #self._data = data
        #self._message = message
        self._http_code = http_code

    

    