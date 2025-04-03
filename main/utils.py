from time import localtime
import calendar
import codecs

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

class HexLetterConventor:
    def convert_cyrilic_into_hex(letter_value) -> tuple:
        """Converts cyrillic letters value into hex: А->d090, Б->d091, В->d092, Г->d093"""

        hex_result = codecs.encode(str(letter_value).encode('utf-8'), 'hex').decode('utf-8') 
        print(hex_result)
        return hex_result
        
    def convert_hex_into_cyrilic(hex_value = str) -> str:
        """Converts hex value into cyrillic letters: d090->А, d091->Б, d092->В, d093->Г"""

        hex_list = ['d090', 'd091', 'd092', 'd093']
        if hex_value not in hex_list:
            raise ValueError('You enteted a wrong hex number; so you can use theese hex values: d090, d091, d092, d093')
        else:
            cyrilic_result = codecs.decode(hex_value, 'hex').decode('utf-8')
            return cyrilic_result
    

def filter_by_role(user_id):
    from .models.user import User
    from .models.parent import Parent
    from .models.teacher import Teacher
    from .models.student import Student

    user = User.objects.get(auth_user_id=user_id)
    if str(user.role) == 'parent':
        role_user = Parent.objects.get(user=user.id)
        return {'user': user, 'role_user': role_user}
    if str(user.role) == 'teacher':
        role_user = Teacher.objects.get(user=user.id)
        return {'user': user, 'role_user': role_user}
    if str(user.role) == 'student':
        role_user = Student.objects.get(user=user.id)
        return {'user': user, 'role_user': role_user}
    

class ConvertDatetime:
    def convert_current_day(year: int, month: int) -> list:
        first_week_day, count_month_days = calendar.monthrange(year, month)
        weeks = []
        week = [''] * first_week_day

        for day in range(1, count_month_days+1):
            week.append(day)
            if len(week) == 7:
                weeks.append(tuple(week))
                week = []

        if week:
            week.extend([''] * (7 - len(week)))
            weeks.append(tuple(week))

        return tuple(weeks)

    def convert_months(month: int):
        months = {
            1: 'Січень', 2: 'Лютий', 3: 'Березень',
            4: 'Квітень', 5: 'Травень', 6: 'Червень',
            7: 'Липень', 8: 'Серпень', 9: 'Вересень',
            10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
        }
        return months.get(month, ' ')

    def return_year_like_list(year):
        months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
    
        month_data = []
        
        for month in range(1, 13):
            first_day_of_month, num_days_in_month = calendar.monthrange(year, month)
            
            weeks = []
            week = [' ']*first_day_of_month  
            
            for day in range(1, num_days_in_month + 1):
                week.append(day)
                if len(week) == 7:  
                    weeks.append(week)
                    week = []
            
            if week:
                weeks.append(week + [' '] * (7 - len(week)))  
            
            month_data.append(weeks)
        
        return months, month_data