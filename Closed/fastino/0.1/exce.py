
class PIDException(BaseException):
    pass

class ResourceAlreadyInUse(PIDException):
    def __init__(self):
        pass
    def __str__(self):
        return "\n\nException: Resources Already In Use - terminating!"

class NoSuchUnit(PIDException):
    def __init__(self):
        pass
    def __str__(self):
        return "\n\nException: No such unit - terminating!"

class NoSuchProperty(PIDException):
    def __init__(self):
        pass
    def __str__(self):
        return "\n\nException: No such property - terminating!"