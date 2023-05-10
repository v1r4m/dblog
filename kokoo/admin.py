from django.contrib import admin
from .models import Template, TextField, SelectField, Selection 

admin.site.register(Template)
admin.site.register(TextField)
admin.site.register(SelectField)
admin.site.register(Selection)

# Register your models here.
