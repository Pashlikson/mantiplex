from enum import IntEnum

class UserRole(IntEnum):
    STUDENT = 1
    TEACHER = 2
    PARENT = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]