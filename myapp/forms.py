from myapp.models import Register
from django.forms import ModelForm
class RegisterForm(ModelForm):
    class Meta:
        model=Register
        fields=["first_name","last_name","email"]
