from datetime import datetime
from ..base_entity import BaseEntity


class Run(BaseEntity):
    id: int = 0
    name: str = ""
    date_created: datetime = datetime.now()
    date_start: datetime = datetime.now()
    end_date: datetime = datetime.now()

    def __init__(self, id: int = 0, date_created: datetime = datetime.now(), date_start: datetime = datetime.now(), end_date: datetime=datetime.now()):
        super()
        self.date_start = date_start
        self.date_end = date_end
