from typing import Dict,List

from flask import request as flaskrequest

from ..infrastructure.sql_connection import SqlConnection
from ..shared.action_result import ActionResult, error, success
from .features.get_runs import GetRunsQuery, GetRunsResponse
from .features.get_shifts import GetShiftsQuery, GetShiftsResponse
from .service_base import ServiceBase


class SchedulerService(ServiceBase):
    """
        Service that runs Calendar module.
    """

    def __init__(self, db: SqlConnection):
        super().__init__(db)

    def get_runs(self, data: GetRunsQuery) -> ActionResult[GetRunsResponse]:
        result = self.db.execute_procedure(
            'getRuns', data)
        return success(result.data) if result.is_valid() else error(result.message)

    def get_shifts(self, data: GetShiftsQuery) -> ActionResult[GetShiftsResponse]:
        shifts_result = self.db.execute_procedure(
            'getShifts', {"_id_runs": data["runid"], "_userid": data["userid_for"]})
        if shifts_result.is_valid():
            for shift in result.data:
                reservations_result = self.get_reservations(
                    shift['id'], data.userid_for, data.groupid, data.mode)
                if reservations_result.is_valid():
                    shift['reservations'] = reservations_result.data
                else:
                    return error(reservations_result._message)
        return shifts_result

    def get_reservations(self, shiftid: int, userid: int, groupid: int, mode: int = 0) -> ActionResult[Dict]:
        return self.db.execute_procedure('getReservations',
                                         {
                                             "_id_shifts": id,
                                             "_userid_for": userid,
                                             "_groupid_for": groupid,
                                             "_mode": mode
                                         }
                                         )
    # def get_locked_reservations(resid: int) -> GetLockedReservationsResponse:
    #     return self.dbc.SelectProcedure('getLockedReservations',{'_id_reservations':params['id_reservations']})

    # def reserve_shifts(data: ReserveShiftsCommand) -> ReserveShiftsResponse:
    #     r=0
    #     userid_for = params['userid_for']
    #     userid_by= params['userid_by']
    #     for x in params['reservationsSelected']:
    #         r = self.dbc.SelectProcedure('reserveShifts',
    #             {
    #                 '_userid_for':userid_for,
    #                 '_userid_by':userid_by,
    #                 '_id_reservations':x,
    #                 '_groupid_for':params['groupid_for']
    #             }
    #         )
    #     return r

    # def get_institute_users(groupid: int) -> GetInstituteUsersResponse:
    #     print("getInstituteUsers" + str(groupid))

    # def get_institutes() -> GetInstitutesResponse:
    #     print("getInstitutes")

    # def cancelReservation(self,params):
    #     self.dbc.ScalarProcedure("cancelReservation",{
    #         "_id_reservations":params["_id_reservations"],
    #         "_userid_by":params["_userid_by"]
    #     })
    #     return {}
    # def cancelGroupReservation(self,params):
    #     self.dbc.ScalarProcedure("cancelGroupReservation",{
    #         "_id_reservations":params["_id_reservations"],
    #         "_userid_by":params["_userid_by"]
    #     })
    #     return {}
    # def getStatistics (self,params):
    #     runs = self.dbc.SelectProcedure("grid_Runs")
    #     ids = []
    #     ids.append({
    #                 "id":0,
    #                 "run":"All runs"
    #             })
    #     for x in runs:
    #         ids.append(
    #             {
    #                 "id":x['id'],
    #                 "run":x['Run']
    #             })
    #     ret = []
    #     for z in ids:
    #         run = z
    #         run['stats'] = self.dbc.SelectProcedure("getStats",
    #             {"_id_runs":z['id']}
    #         )
    #         ret.append(run)
    #     return ret

    # def printHtml(self,request):
    #     dbc = dbconnector(self.dbpool)
    #     d = Props(request=request).requestParams
    #     r = dbc.SelectProcedure('printWeek',d)
    #     if r.__len__()>0:
    #         return weekly_view.printHtml(d,r)
    #     else:
    #         return MessageBase(text="No shifts this week.")

    # def updateUserInfo(self,params):
    #     self.dbc.SelectProcedure('updateuserparams', params)
    #     return self.dbc.SelectProcedure('getUserParams', {'_id_personel': params['_userid']})
    # def getPersonelReservations(self,params):
    #     ret = {
    #         "personal":self.dbc.SelectProcedure('grid_personelreservations', {'_parentid': params['_userid']}),
    #         "group":self.dbc.SelectProcedure('grid_institutereservations', {'_parentid': params['_groupid']})
    #     }
    #     return ret


""" class ReserveShiftsResponse:

    result: bool = False


class GetInstituteUsersResponse:

    users: List[User] = []


class GetInstitutesResponse:

    institutes: List[Institute] = [] """
