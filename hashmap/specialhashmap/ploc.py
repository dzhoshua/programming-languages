

class Ploc(dict):
    
    def __init__(self, _dict: dict):
        self._dict = _dict


    @staticmethod
    def check_condition(op, number) -> bool:
        operations = ["<", ">", "=", "<=", ">=", "<>"]
        return op in operations and number.isdigit()


    @staticmethod
    def parse_condition(_condition):
        splited_condition = "".join(_condition.split())

        res = []
        symbols = ["<", ">", "="]

        for part in splited_condition.split(","):

            condition = {"op": "", "num": ""}
            for char in part:
                if char in symbols:
                    condition["op"] += char
                elif char.isdigit():
                    condition["num"] += char

            if Ploc.check_condition(condition["op"], condition["num"]):
                condition["num"] = float(condition["num"])
                res.append(condition)
            else:
                raise SyntaxError("bad condition")

        return res


    @staticmethod
    def parse_key(key):
        keys_result = []

        if key[0] == '(':
            key_ = key[1:-1]
        else:
            key_ = key
            
        key_ = "".join(key_.split()).split(',')
        
        if len(key_) == 1 and key_[0].isdigit():
            keys_result.append(float(key_[0]))
        else:
            keys_result = [float(k) for k in key_ if k.isdigit()]

        return keys_result
    

    @staticmethod
    def compare(key, op, value):
        comparison = {
            "<": key < value,
            ">": key > value,
            "=": key == value,
            "<=": key <= value,
            ">=": key >= value,
            "<>": key != value,
        }
        return comparison[op]


    def __getitem__(self, condition):
        if not isinstance(condition, str):
            raise SyntaxError("invalid condition")

        parsed_condition = self.parse_condition(condition)
        
        answer = "{"
        for k, v in self._dict.items():
            keys = self.parse_key(k)

            if len(keys) != len(parsed_condition):
                continue

            compared = True
            for index, value in enumerate(keys):
                op = parsed_condition[index]["op"]
                number = parsed_condition[index]["num"]

                if not self.compare(value, op, number):
                    compared = False
                    break

            if compared:
                if len(answer) > 2:
                    answer += f", {k}={v}"
                else:
                    answer += f"{k}={v}"

        answer += "}"
        return answer

