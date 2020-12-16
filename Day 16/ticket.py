from collections import defaultdict

class Rule():
    def __init__(self, raw: str):
        # departure location: 50-692 or 705-969
        self.field = raw.split(":")[0]
        self.ranges = [list(map(int, x.split("-"))) for x in raw.split(": ")[1].split(" or ")]


class Ticket():
    def __init__(self, raw: str):
        # 460,805,566,621,266,233,771,202,368,751,150,558,184,248,457,424,351,184,821,623
        self.values = list(map(int, raw.split(",")))

    def validate(self, rules: [Rule]) -> int:
        validations = defaultdict(list)
        for rule in rules:
            for _range in rule.ranges:
                for value in self.values:
                    if not _range[0] <= value <= _range[1]:
                        validations[value].append(False)
                    else:
                        validations[value].append(True)

        errorRate = 0
        for validation in validations.items():
            if True not in validation[1]:
                errorRate += validation[0]

        return errorRate

    def findValidFields(self, rules: [Rule]) -> dict:
        validFields = defaultdict(list)
        for rule in rules:
            for _range in rule.ranges:
                for value in enumerate(self.values):
                    if _range[0] <= value[1] <= _range[1]:
                        validFields[rule.field].append(value[0])

        return validFields
