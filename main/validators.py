from time import localtime
import re
from main.models.school_class import School_class
from main.models.user import User
from main.models.parent import Parent
from .utils import get_grade_by_start_year

# Validators:
def profile_validation(form) -> bool:
    
    def check_for_forbidden_name(str_field):
        forbidden_names = ['hitler', 'stalin', 'lenin', 'putin', 'moron', 'russia', 'kim_chen_in', 'kill', 'penis', 'bra', 'dictator', 'hate', 'devil', 'satan']
        firstname_lower = str(form.cleaned_data.get(str_field, '')).strip().lower()

        for forbidden_name in forbidden_names:
            pattern = re.escape(forbidden_name) 

            if re.search(pattern, firstname_lower):
                return False
        return True
    
    def check_possible_time(datetime_field):
        datetime = str(form.cleaned_data.get(datetime_field)).strip().split('-')
        date_time = [int(datetime[0]), int(datetime[1]), int(datetime[2])]
        current_time = [localtime()[0], localtime()[1], localtime()[2]]

        is_first_part_of_year = current_time[1] > 9
        age = current_time[0] - date_time[0]

        if (current_time[1], current_time[2]) < (date_time[1], date_time[2]):
            age -= 1

        if age < 6 or (age - date_time[0] == 6 and not is_first_part_of_year):
            return False
        if age > 90 or (age == 90 and is_first_part_of_year):
            return False
        return True

    def check_role_age_permission(datetime_field, role_field):
        datetime = str(form.cleaned_data.get(datetime_field)).strip().split('-')
        date_time = [int(datetime[0]), int(datetime[1]), int(datetime[2])]
        current_time = [localtime()[0], localtime()[1], localtime()[2]]
        role = str(form.cleaned_data.get(role_field)).strip()

        is_first_part_of_year = current_time[1] > 9
        if (current_time[0] - date_time[0] < 18 or (current_time[0] - date_time[0] == 18 and not is_first_part_of_year))\
            and role != 'student':
            return False
        if (current_time[0] - date_time[0] > 18 or (current_time[0] - date_time[0] == 18 and is_first_part_of_year))\
            and role == 'student':
            return False
        return True

    if not check_for_forbidden_name('first_name'):
        return False
    if not check_for_forbidden_name('last_name'):
        return False
    if not check_possible_time('birth_date'):
        return False
    if not check_role_age_permission('birth_date', 'role'):
        return False
    return True

def student_validation(form, main_user) -> bool:
    
    def check_class_to_age():
        class_school = School_class.objects.get(id=form.cleaned_data['school_class'].id)
        class_grade = get_grade_by_start_year(class_school.start_year)
        student_auth_user = User.objects.get(id=main_user.id)
        birth_date = student_auth_user.birth_date
        current_time = [localtime()[0], localtime()[1], localtime()[2]]

        age = current_time[0] - birth_date.year
        if current_time[1] < birth_date.month or (current_time[1] == birth_date.month and current_time[2] < birth_date.day):
            age -= 1

        if age - 5 != class_grade['number'] and age - 6 != class_grade['number']:
            return False
        return True

    def no_parent_duplicates():
        first_guardian_parent = Parent.objects.get(user_id=form.cleaned_data['first_guardian'].user.id)
        second_guardian_parent = Parent.objects.get(user_id=form.cleaned_data['second_guardian'].user.id)
        first_guardian = first_guardian_parent.user
        second_guardian = second_guardian_parent.user
        
        if first_guardian.first_name == second_guardian.first_name and\
          first_guardian.last_name == second_guardian.last_name:
            return False
        return True
    
    if not check_class_to_age():
        return False
    if not no_parent_duplicates():
        return False
    return True

def parent_check(form) -> bool:
    
    def check_teacher():
        if str(form.cleaned_data['job']).strip().lower() == 'teacher':
            return False
        return True

    if not check_teacher():
        return False
    return True

def teacher_validation(form, main_user) -> bool:
    
    def employment_year_check():
        employment_year = int(form.cleaned_data['employment_year'])
        teacher_auth_user = User.objects.get(id=main_user.id)
        datetime_list = str(teacher_auth_user.birth_date).strip().split('-')
        date_time = [int(datetime_list[0]), int(datetime_list[1]), int(datetime_list[2])]
        current_time = [localtime()[0], localtime()[1], localtime()[2]]

        is_first_part_of_year = current_time[1] > 9
        employment_time = current_time[0] - employment_year

        age = current_time[0] - date_time[0]
        if current_time[1] < date_time[1]:
            age -= 1

        if employment_time > 90 or (employment_time == 90 and is_first_part_of_year):
            return False
        if age - employment_time < 18 or (age - employment_time == 18 and not is_first_part_of_year):
            return False
        return True
    
    if not employment_year_check():
        return False
    return True

# Redirects:
def redirect_profile_by_role(form) -> str:
    role = str(form.cleaned_data.get('role')).strip()
    if role == 'student':
        return 'student'
    if role == 'parent':
        return 'parent'
    if role == 'teacher':
        return 'teacher'
    return 'default_profile'