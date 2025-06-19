from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CostomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CostomUser
        fields = ("username","email")
        
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CostomUser
        fields = ("username", "email")
