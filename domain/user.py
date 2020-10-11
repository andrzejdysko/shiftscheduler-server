from .base_entity import  BaseEntity
class User(BaseEntity):
    name: str

    def __init__(self, id: int = 0, name: str = ""):
        self.name = name
