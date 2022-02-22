from django.db import models
from django.forms import ModelForm, RadioSelect, TextInput, EmailInput


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    role = models.BooleanField()  # true for admin, false otherwise

    def __str__(self):
        return self.first_name + " " + self.surname


# form model
class MemberForm(ModelForm):
    # TODO clean phone_number

    class Meta:
        ROLE_CHOICES = [('False', 'Regular - Can\'t delete members'), ('True', 'Admin - Can delete members')]
        model = Member
        fields = ['first_name', 'surname', 'email', 'phone_number', 'role']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name'}),
            'surname': TextInput(attrs={'placeholder': 'Surname'}),
            'email': EmailInput(attrs={'placeholder': 'name@example.com'}),
            'phone_number': TextInput(attrs={'placeholder': '1234567890'}),
            'role': RadioSelect(choices=ROLE_CHOICES),
        }
