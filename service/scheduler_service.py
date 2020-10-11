from .service_base import service_base
from flask import request as flaskrequest


class SchedulerService(ServiceBase):
    """
        Service that runs Calendar module.
    """

    def __init__(self, db: SqlConnection):
        super(db)

    def get_runs(data: GetRunsQuery) -> GetRunsResponse:
        runs: GetRunsResponse = self.db.SelectProcedure('getRuns', params)
        for run in runs:
            run['shifts'] = self.getShifts(
                run['id'], params['_userid_for'], params['_groupid_for'], params['_mode'])
        return runs

    def get_shifts(data: GetShiftsQuery) -> GetShiftsResponse:
        shifts = self.dbc.SelectProcedure('getShifts',{"_id_runs":id,"_userid":userid})
        for shift in shifts:
            shift['reservations']=self.getShifters(shift['id'],userid,groupid,mode)
        return shifts
    def get_reservations():
        return self.dbc.SelectProcedure('getReservations',
            {
                "_id_shifts":id,
                "_userid_for":userid,
                "_groupid_for":groupid,
                "_mode":mode
            }
        )   
    def get_locked_reservations(resid: int) -> GetLockedReservationsResponse:
        return self.dbc.SelectProcedure('getLockedReservations',{'_id_reservations':params['id_reservations']})
        
    def reserve_shifts(data: ReserveShiftsCommand) -> ReserveShiftsResponse:
        r=0
        userid_for = params['userid_for']
        userid_by= params['userid_by']
        for x in params['reservationsSelected']:
            r = self.dbc.SelectProcedure('reserveShifts',
                {
                    '_userid_for':userid_for,
                    '_userid_by':userid_by,
                    '_id_reservations':x,
                    '_groupid_for':params['groupid_for']
                }
            )
        return r

    def get_institute_users(groupid: int) -> GetInstituteUsersResponse:
        print("getInstituteUsers" + str(groupid))

    def get_institutes() -> GetInstitutesResponse:
        print("getInstitutes")
        
    def cancelReservation(self,params):
        self.dbc.ScalarProcedure("cancelReservation",{
            "_id_reservations":params["_id_reservations"],
            "_userid_by":params["_userid_by"]
        })
        return {}
    def cancelGroupReservation(self,params):
        self.dbc.ScalarProcedure("cancelGroupReservation",{
            "_id_reservations":params["_id_reservations"],
            "_userid_by":params["_userid_by"]
        })
        return {}
    def getStatistics (self,params):
        runs = self.dbc.SelectProcedure("grid_Runs")
        ids = []
        ids.append({
                    "id":0,
                    "run":"All runs"
                })   
        for x in runs:     
            ids.append(
                {
                    "id":x['id'],
                    "run":x['Run']
                })
        ret = []
        for z in ids:
            run = z
            run['stats'] = self.dbc.SelectProcedure("getStats",
                {"_id_runs":z['id']}
            )
            ret.append(run)
        return ret


    def printHtml(self,request):
        dbc = dbconnector(self.dbpool)
        d = Props(request=request).requestParams
        r = dbc.SelectProcedure('printWeek',d)
        if r.__len__()>0:
            return weekly_view.printHtml(d,r)
        else:
            return MessageBase(text="No shifts this week.")

    def updateUserInfo(self,params):
        self.dbc.SelectProcedure('updateuserparams', params)
        return self.dbc.SelectProcedure('getUserParams', {'_id_personel': params['_userid']})
    def getPersonelReservations(self,params):
        ret = {
            "personal":self.dbc.SelectProcedure('grid_personelreservations', {'_parentid': params['_userid']}),
            "group":self.dbc.SelectProcedure('grid_institutereservations', {'_parentid': params['_groupid']})
        }
        return ret

class GetRunsQuery:

    userid: int = 0
    runid: int = 0


class GetRunsResponse:

    runs: List[Run] = []


class GetLockedReservationsResponse:

    reservations: List[Reservation] = []


class ReserveShiftsCommand:

    userid_by: int = 0
    userid_for: int = 0
    groupid_for: int = 0
    reservationsSelected: List[Reservation] = []


class ReserveShiftsResponse:

    result: bool = False


class GetInstituteUsersResponse:

    users: List[User] = []


class GetInstitutesResponse:

    institutes: List[Institute] = []
