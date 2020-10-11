from typing import List
from ...domain.scheduler.shift import Shift

class GetShiftsQuery:
    runid: int = 0,
    userid_for: int = 0
    groupid_for: int = 0
    mode: int = 0
    
class GetShiftsResponse:
    shifts:List[Shift]