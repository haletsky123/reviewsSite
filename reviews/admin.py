from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Review, Person, DictCurse, DictExceptions
from django import forms

# class DifferentlySizedTextarea(forms.Textarea):
#   def __init__(self, *args, **kwargs):
#     attrs = kwargs.setdefault('attrs', {})
#     attrs.setdefault('cols', 70)
#     attrs.setdefault('rows', 6)
#     super(DifferentlySizedTextarea, self).__init__(*args, **kwargs)

class ReviewAdmin(admin.ModelAdmin):
   # formfield_overrides = {
   #      models.CharField: {'widget': TextInput(attrs={'size':'20'})},
   #      models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':50})},
   #  }

   # formfield_overrides = {models.TextField: {'widget': DifferentlySizedTextarea}}

   raw_id_fields = ('author',)
   list_display = ( 'text_before', 'text_after', 'author',  'pub_date',)
   readonly_fields = ('pub_date',)

   # def get_form(self, request, obj=None, **kwargs):
   #     form = super(YourModelAdmin, self).get_form(request, obj, **kwargs)
   #     form.base_fields['myfield'].widget.attrs['style'] = 'width: 45em;'
   #     return form

admin.site.register(Review, ReviewAdmin)
admin.site.register(DictCurse)
admin.site.register(DictExceptions)


#
# from django.contrib import admin
# from .models import review
#
#
#
# admin.site.register(review)
#


