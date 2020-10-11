import functools
from ...service.scheduler_service import SchedulerService
from flask import (
    Blueprint,  g, redirect, render_template, request, session, url_for, Response, jsonify
)
from ...infrastructure.db import get_db

bp = Blueprint('scheduler', __name__, url_prefix="/scheduler")


@bp.route("/<string:action>", methods=["GET", "POST"])
def scheduler_action(action: str = "") -> Response:
    if action == None:
        return url_for(".index")
    else:
        result = SchedulerService(
            get_db("PRODUCTION_DATABASE")).invoke_action(request, action)
        response = jsonify(result.__dict__)
        response.status_code=result.http_code
        return response
