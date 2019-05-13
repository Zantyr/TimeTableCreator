DEVICE OBJECT:
    name = ""
    inputs = []
    outputs = []
    resources = []
    headers = ""
    setup = ""
    fndefs = ""
    loop = ""
    replacements = {}
    libs = []

PODSTAWIENIA:
    "%dev_name%":self.name
    "%res_0%":self.resources[0].name
    "%in_0%":self.inputs[0].name
    "%out_0%":self.outputs[0].name
    "%dev_var%":self.name+"_var_"
    "%%":self.name
    r"\p":r"%"
    r"\s":"\\"