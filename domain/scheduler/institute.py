from ..base_entity import BaseEntity
from typing import List
from .user import User

class Institute(BaseEntity):
    users: List[User] = []
    name: str = ""
    def __init__(self, id, name: str = "")
        super()
        self.name=name