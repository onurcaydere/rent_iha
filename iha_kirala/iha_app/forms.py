from django import forms
from .models import iha_info

class giris_form(forms.Form):
    username = forms.CharField(max_length=100,
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control ",
            }
        ),
        label="",)
    your_password=forms.CharField(required=True,
widget=forms.PasswordInput(attrs={
                "placeholder": "Password",
                "class": "form-control ",
            }
        ),
        label="",)
class register_form(forms.Form):
    username = forms.CharField(max_length=50,
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "username",
                "class": "form-control ",
            }
        ),
        label="",)
    your_name = forms.CharField(max_length=50,
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control ",
            }
        ),
        label="",)
    your_surname = forms.CharField(max_length=50,
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Surname",
                "class": "form-control ",
            }
        ),
        label="",)

    your_email_reg = forms.EmailField(max_length=100,
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control ",
                "type":"email",
            }
        ),
        label="",)
    your_password_reg=forms.CharField(required=True,
widget=forms.PasswordInput(attrs={
                "placeholder": "Password",
                "class": "form-control ",
            }
        ),
        label="",)
    your_rep_password=forms.CharField(required=True,
widget=forms.PasswordInput(attrs={
                "placeholder": "Re-Password",
                "class": "form-control ",
            }
        ),
        label="",)

class add_iha(forms.ModelForm):
    iha_marka = forms.CharField(max_length=50,
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Marka",
                "class": "form-control ",
            }
        ),
        label="",)
    iha_model = forms.CharField(max_length=50,
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Model",
                "class": "form-control ",
            }
        ),
        label="",)


    iha_agr = forms.FloatField(
    required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Agırlık",
                "class": "form-control ",
            }
        ),
        label="",)
    iha_kat=forms.CharField(required=True,
widget=forms.TextInput(attrs={
                "placeholder": "Kategori",
                "class": "form-control ",
            }
        ),
        label="",)
    iha_fiyat=forms.FloatField(
widget=forms.TextInput(attrs={
                "placeholder": "Fiyatı",
                "class": "form-control ",
            }
        ),
        label="",)
    class Meta:
        model=iha_info
        exclude=("user_name","user_surname","user_email","user_password",)
class gün(forms.Form):
    iha_gun=forms.CharField( required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Kac Gün",
                "class": "form-control ",
            }
        ),
        label="",)
