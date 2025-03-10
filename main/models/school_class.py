from django.db import models
from ..utils import get_class_number_by_current_year, convert_hex_number_into_cyrilic

class School_class(models.Model):
    prefix_hex = models.CharField(max_length=4, blank=False)
    start_year = models.IntegerField(blank=False)
    room_number = models.IntegerField(blank=False)
    
    @property
    def class_number(self):
        return get_class_number_by_current_year(self.start_year)
    
    @property
    def prefix_of_class(self, hex_value):
        return convert_hex_number_into_cyrilic(self.prefix_hex)
    
