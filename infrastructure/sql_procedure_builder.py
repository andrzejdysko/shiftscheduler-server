from typing import Dict, List


def build_sql_command(connection, procedure_name: str, arguments: Dict) -> str:
    result = "call " + procedure_name + "("
    sql_params = get_params_list_from_string(connection, procedure_name)
    parsed_arguments = []
    for param in sql_params:
        result += '{}, '
        if param["name"] in arguments.keys():
            val = arguments[param["name"]]
            parsed_arguments.append(get_sql_value(val, param["type"]))
        else:
            parsed_arguments.append(get_sql_NULL_value(param["type"]))
    result = result[:-2] if sql_params.__len__() > 0 else result
    result += ");"
    result = result.format(*parsed_arguments)
    return result

def get_params_list_from_string(connection, procedure_name: str) -> List:
    params_string_result = connection.execute(
        "call getParams2('" + procedure_name + "');")
    if params_string_result.is_valid():
        params_string = params_string_result.data[0]["paramsString"]
    params_list = params_string.split(",")
    result = [make_param(
        param_string) for param_string in params_list]
    return result


def make_param(param_string: str) -> Dict:
    param = param_string[3:].split(" ")
    return {"name": param[0], "type": param[1]}


def get_sql_value(value: str, _type: str) -> str:
    try:
        if _type.find('varchar') >= 0:
            return '"' + str(value) + '"'
        elif _type.find('text') >= 0:
            return '"' + str(value) + '"'
        elif _type.find('datetime') >= 0:
            return '"' + str(value) + '"'
        elif _type.find('date') >= 0:
            return '"' + str(value) + '"'
        elif _type.find('int') >= 0:
            return str(int(value)) 
    except:
        return self.get_sql_NULL_value(_type)


def get_sql_NULL_value(_type: str) -> str:
    if _type.find('varchar') >= 0:
        return '""'
    elif _type.find('text') >= 0:
        return '""'
    elif _type.find('datetime') >= 0:
        return '""'
    elif _type.find('date') >= 0:
        return '""'
    elif _type.find('int') >= 0:
        return 'NULL'
