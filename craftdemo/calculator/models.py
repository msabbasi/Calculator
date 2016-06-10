from __future__ import unicode_literals

from django.db import models    
    
class Addition(models.Model):
    num1 = models.FloatField()    
    num2 = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)

    def _get_result(self):
        return self.num1 + self.num2
    result = property(_get_result)
		
    
