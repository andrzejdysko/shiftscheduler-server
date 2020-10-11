from typing import List


class GetLockedReservationsResponse:

    reservations: List[Reservation] = []


class ReserveShiftsCommand:

    userid_by: int = 0
    userid_for: int = 0
    groupid_for: int = 0
    reservationsSelected: List[Reservation] = []
