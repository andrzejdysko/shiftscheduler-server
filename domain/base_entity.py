from datetime import datetime

class BaseEntity:
    id: int = 0
    date_created: datetime = datetime.now()
    def __init__(self, id: int=0, date_created:datetime=datetime.now()):
        self.id = id
        self.date_created = date_created
