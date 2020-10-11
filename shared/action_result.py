def error(message: str = ""):
    return ActionResult(False,{},message)

def success(data={}):
    return ActionResult(True,data,"")

class ActionResult:

    _result: bool = True
    _data = {}
    _message: str = ""
    
    def __init__(self, result, data, message):
        self._result = result
        self._data = data
        self._message = message
        

    def is_valid():
        return result

    