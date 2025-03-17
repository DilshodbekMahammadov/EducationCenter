from django.core.validators import MinValueValidator
from django.db import models

GENDER_CHOISE = (('Male', 'Male'), ('Famale', 'Famale'))

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Mentor(BaseModel):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER_CHOISE)
    phone_number = models.CharField(max_length=15)
    profession = models.CharField(max_length=255)
    kpi = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class Group(BaseModel):
    name = models.CharField(max_length=255)
    time = models.TimeField(blank=True, null=True)
    finished_at = models.DateField(blank=True, null=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Student(BaseModel):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOISE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Payment(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.student.name if self.student else self.description






