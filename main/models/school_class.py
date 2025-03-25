from django.db import models
from ..utils import get_grade_by_start_year, convert_hex_into_cyrilic

class School_class(models.Model):
    prefix_hex = models.CharField(max_length=4, blank=False, help_text="d090->А, d091->Б, d092->В, d093->Г")#//TODO: use converted hex letter 'Hex-cyrilic enum'
    start_year = models.IntegerField(blank=False)
    room_number = models.IntegerField(blank=False)
    
    @property
    def class_number(self):
        return get_grade_by_start_year(self.start_year)
    
    @property
    def prefix_of_class(self):
        return convert_hex_into_cyrilic(self.prefix_hex)
    
    @property
    def is_class_graduated(self):
        if get_grade_by_start_year(self.start_year)["is_graduated"]:
            return ", is graduated"
        else:
            return None
    
    def __str__(self):
        return f"{'Каб № ' + str(self.room_number) + ';  '} {str(self.class_number['number']) + str(self.prefix_of_class) + str(self.is_class_graduated if self.is_class_graduated else '')}"
    
