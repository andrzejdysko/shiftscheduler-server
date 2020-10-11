from typing import List
from ...domain.scheduler.run import Run

class GetRunsQuery:

    userid: int = 0
    runid: int = 0


class GetRunsResponse:

    runs: List[Run] = []
