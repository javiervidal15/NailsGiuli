from django import forms
from django.forms.forms import NON_FIELD_ERRORS

class AddErrorMixin(object):
    def add_error(self, field, msg):
        field = field or NON_FIELD_ERRORS
        if field in self._errors:
            self._errors[field].append(msg)
        else:
            self._errors[field] = self.error_class([msg])


class LoginForm(AddErrorMixin, forms.Form):
    email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={"type":"email","class":"form-control",
                                                           "placeholder":"E-mail","required":True}))
    password = forms.CharField(max_length=128,widget=forms.TextInput(attrs={"type":"password","class":"form-control",
                                                           "placeholder":"Password","required":True}))

