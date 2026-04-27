from django.db import models

class ExamForm(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    exam_date = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.course}"
    
    class Meta:
        ordering = ['-created_at']
