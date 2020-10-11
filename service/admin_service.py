from .service_base import service_base
from flask import request as flaskrequest


class AdminService(ServiceBase):
    """
        Service that runs admin module.
    """
    def get_forms(appid: int) -> GetFormsResponse:
        print("get_forms: " % str(appid))

    def get_controls(formid: int) -> GetControlsResponse:
        print("get_controls: " % str(appid))

    def form_action(data: FormActionCommand, method: str) -> FormActionResponse:
        print("form_action")


class FormActionCommand:

    recid: int = 0
    formid: int = 0
    id_controls: int = 0
    values: Dict[string, string] = {}
    parentid: int = 0


class FormActionResponse:

    result: bool = False
    messages: List[str] = []


class GetFormsResponse:

    forms: List[Form] = []


class GetControlsResponse:

    controls: List[Control] = []
