from time import localtime
import codecs

def get_class_number_by_current_year(start_year: int):#//TODO: Shorter name
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

def convert_hex_number_into_cyrilic(hex_value = str) -> str: #//TODO: Shorter name
    """Converts hex value into cyrillic letters: d090->А, d091->Б, d092->В, d093->Г"""

    hex_list = ['d090', 'd091', 'd092', 'd093']
    if hex_value not in hex_list:
        raise ValueError('You enteted a wrong hex number; so you can use theese hex values: d090, d091, d092, d093')
    else:
        cyrilic_result = codecs.decode(hex_value, 'hex').decode('utf-8')
        return cyrilic_result