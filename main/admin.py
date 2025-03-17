from django.contrib import admin

from main.models import *

admin.site.register([Mentor, Student, Payment, Group])