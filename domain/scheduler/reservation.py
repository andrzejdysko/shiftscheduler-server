from typing import List

from ..base_entity import BaseEntity

class Reservation(BaseEntity):
    shifts: List = []

    def __init__(self, id: int = 0):
        super()
