from typing import Generic, TypeVar

T = TypeVar("T")


class ActionResult(Generic[T]):

    result: bool = True
    data: T = {}
    message: str = ""

    def __init__(self, result: bool, data: T, message: str):
        self.result = result
        self.data = data
        self.message = message

    def is_valid(self) -> bool:
        return self.result


def error(message: str = "") -> ActionResult[str]:
    return ActionResult[str](False, {}, message)


def success(data: T = {}) -> ActionResult[T]:
    return ActionResult[T](True, data, "")
