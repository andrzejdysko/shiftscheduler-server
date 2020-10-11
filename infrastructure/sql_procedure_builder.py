from typing import Dict


def build_sql_command(self, procedure_name: str, arguments: Dict) -> str:
        result = "call " + procedure_name + "("
        if arguments.keys().__len__() > 0:
            sql_params = get_params_dict_from_string(procedure_name)
            for param in sql_params:
                val = arguments[param["name"]]
                result.append(get_sql_value(val, param["type"]))
            result = result[:-2]
        return result + ")"

    def get_params_list_from_string(procedure_name: str) -> List:
        params_string = self.execute(
            "call getParams2('" + procedure_name + "');")["paramsString"]
        params_list = params_string.split(",")
        result = [ make_param(
            param_string) for param_string in params_list]
        return result

    def make_param(self, param_string: str) -> Dict:
        param = param_string[3:].split(" ")
        return {"name" = param[0], "type" = param[1]}
    def get_params__value(self, value: str, _type: str) -> str:
        try:
            if _type.find('varchar')>=0:
                return '"' + str(value) + '", '
            elif _type.find('text')>=0:
                return '"' + str(value) + '", '
            elif _type.find('datetime')>=0:
                return '"' + str(value) + '", '
            elif _type.find('date')>=0:
                return '"' + str(value) + '", '
            elif _type.find('int') >= 0:
                return str(int(value)) + ', '
        except:
            return self.get_sql_NULL_value(_type)
            
    def get_sql_NULL_value(self,_type:str)->str:
        if _type.find('varchar')>=0:
            return '"",'
        elif _type.find('text')>=0:
            return '"", '
        elif _type.find('datetime')>=0:
            return '"", '
        elif _type.find('date')>=0:
            return '"", '
        elif _type.find('int') >= 0:
            return 'NULL, '
