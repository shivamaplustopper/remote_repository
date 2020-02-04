from django import forms

class Registration_form(forms.Form):
    first_name = forms.CharField(
        label='Enter Your First Name: ',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class':'form-control'
            }
        )
    )

    last_name = forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Last Name',
                'class':'form-control'
            }
        )
    )

    username = forms.CharField(
        label='Enter your user name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Username',
                'class':'form-control',
            }
        )
    )

    emailid = forms.EmailField(
        label="Enter your Mail Id",
        widget = forms.EmailInput(
            attrs={
                 'placeholder':'Your Email Id',
                'class':'form-control'
            }
        )
    )

    mobileno = forms.IntegerField(
        label= "Enter Your Mobile No",
        widget = forms.NumberInput(
            attrs={
                'placeholder':'Your Mobile No.',
                'class':'form-control'
            }
        )
    )

    password = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Your Password',
                'class':'form-control'
            }
        )

    )
