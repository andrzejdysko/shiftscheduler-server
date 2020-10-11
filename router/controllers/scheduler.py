import functools
from ...service.scheduler_service import SchedulerService
from flask import (
    Blueprint,  g, redirect, render_template, request, session, url_for, Response, jsonify
)


bp = Blueprint('scheduler', __name__, url_prefix="/scheduler")


@bp.route("/<string:action>", methods=["GET", "POST"], defaults={"action": None})
def scheduler_action(action: str = "") -> Response:
    if action == None:
        return url_for(".index")
    else:
        data = SchedulerService.invoke_action(request, action)
        return jsonify(data)
