from django import forms

class RegisterTurnFormWithDoc(forms.Form):

    name = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Juan Perez", "required":True}))

    email = forms.EmailField(max_length=250,
        widget=forms.TextInput(attrs={"type": "email","class": "form-control","placeholder":"juan.perez@example.com","required":True}))

    turn_date = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    turn_hour = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    turn_service = forms.IntegerField(
        widget=forms.HiddenInput())

