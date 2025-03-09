from enum import Enum

class UserRole(str, Enum):
    STUDENT = 'Student'
    TEACHER = 'Teacher'
    PARENT = 'Parent'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
class TeacherRole(str, Enum):
    TEACHER = 'Teacher'
    HEADMASTER = 'Headmaster'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class TeacherSubject(str, Enum):
    ALGEBRA = 'Algebra'
    GEOMETRY = 'Geometry'
    CHEMISTRY = 'Chemistry'
    PHYSICS = 'Physics'
    GEOGRAPHY = 'Geography'
    BIOLOGY = 'Biology'
    INFORMATION_TECHNOLOGY = 'Information Technology'
    PHYSICAL_EXERSICE = 'Physical Exersice'
    HEALTHCARE = 'Healthcare'
    HISTORY = 'History'
    UKRANIAN = 'Ukranian language'
    ENGLISH = 'English language'
    UKRAINIAN_LITERATURE = 'Ukranian literature'
    FOREGIN_LITERATURE = 'World literature'
    ART_AND_DESIGH = 'Art and desigh'
    WORKSHOP = 'Workshop'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]