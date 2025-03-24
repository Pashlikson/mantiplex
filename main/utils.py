from time import localtime
import codecs
import re

def get_grade_by_start_year(start_year: int):
    result = {"number": 0, "is_graduated": False}
    current_year = localtime()[0]
    
    diff_years = current_year - start_year
    is_frst_part_of_year = localtime()[1] < 9

    if diff_years > 11 or (diff_years == 11 and not is_frst_part_of_year):
        result["number"] = 11
        result["is_graduated"] = True
    elif is_frst_part_of_year:
        result["number"] = diff_years
    else:        
        result["number"] = diff_years + 1
    return result

def convert_hex_into_cyrilic(hex_value = str) -> str:
    """Converts hex value into cyrillic letters: d090->А, d091->Б, d092->В, d093->Г"""

    hex_list = ['d090', 'd091', 'd092', 'd093']
    if hex_value not in hex_list:
        raise ValueError('You enteted a wrong hex number; so you can use theese hex values: d090, d091, d092, d093')
    else:
        cyrilic_result = codecs.decode(hex_value, 'hex').decode('utf-8')
        return cyrilic_result
    
def validate_profile_form(form) -> bool:
    
    def check_for_forbidden_name(str_field):
        forbidden_names = ['hitler', 'stalin', 'putin', 'moron', 'russia', 'kim_chen_in', 'kill', 'penis', 'bra', 'dictator', 'hate']
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
        if current_time[0] - date_time[0] < 6 or (current_time[0] - date_time[0] == 6 and not is_first_part_of_year):
            return False
        if current_time[0] - date_time[0] > 90 or (current_time[0] - date_time[0] == 90 and is_first_part_of_year):
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