from datetime import datetime
from typing import List

from ..base_entity import BaseEntity
from .reservation import Reservation


class Shift(BaseEntity):
    reservations: List[Reservation] = []
    date_start: datetime = datetime.now()
    shift_type: str = ""

    def __init__(self, id: int = 0, date_created: datetime = datetime.now(), shift_type: str = "", date_start: datetime = datetime.now()):
        super()
        self.date_start = date_start
        self.shift_type = shift_type
