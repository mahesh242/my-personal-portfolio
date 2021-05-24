from django.contrib.auth import authenticate
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm)

from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, 
                                       UserChangeForm, PasswordResetForm, 
                                       SetPasswordForm, PasswordChangeForm)
from django import forms
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from master.models import StateMaster,CityMaster
from dal import autocomplete
from user_profile.models import UserDetails


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label=_("Username or Email"), max_length=254, widget=forms.TextInput(attrs={'class':'form-control','placeholder': _('Username or Email')}))
    password = forms.CharField(required=True, label=_("Password"), widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder': _('Password')}))
   
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
        return self.cleaned_data
    
"""For password reset form having email field"""
class PasswordResetFormUnique(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.TextInput(attrs={'class':'email form-control', 'placeholder':_('Email'), 'style':'text-transform:none;'}))
    def clean(self):
        cleaned_data = super(PasswordResetFormUnique, self).clean()
        email = cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("Email address not recognized. There is no account linked to this email."))
        return cleaned_data


"""For password reset form having passwords field"""    
class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New Password"),
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'newpassword1', 'placeholder': _('New Password')})
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'newpassword2', 'placeholder': _('Confirm New Password')})
    )
    old_password = forms.CharField(
        label=_("Current Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'oldpassword', 'placeholder': _('Current Password')}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']
    
    
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), widget=forms.PasswordInput(attrs={'class':'form-control resetpassword ','id':'newpassword1', 'placeholder': _('New Password')}))
    new_password2 = forms.CharField(label=_("Confirm New Password"), widget=forms.PasswordInput(attrs={'class':'form-control confirm-password-reset','id':'newpassword2', 'placeholder': _('Confirm New Password')}))  
    


# # Customizing user creation form starts here
# class UserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         # self.fields['groups'].required = False
#         self.fields['first_name'].required = False
#         self.fields['last_name'].required = False
#         self.fields['email'].required = True
#         self.fields['password1'].required = False
#         self.fields['password2'].required = False
#         self.fields['is_active'].required = True
#         # If one field gets auto completed but not the other, our 'neither
#         # password or both password' validation will be triggered.
#         self.fields['password1'].widget.attrs['autocomplete'] = 'off'
#         self.fields['password2'].widget.attrs['autocomplete'] = 'off'
        
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         try:
#             user = User.objects.exclude(pk=self.instance.pk).get(email=email)
#         except User.DoesNotExist:
#             return email
#         raise forms.ValidationError(u'Email %s is already in use.' % email)
    
    
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         try:
#             user = User.objects.exclude(pk=self.instance.pk).get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError(u'Username %s is already in use.' % username)
# # Customizing user creation form ends here

class UserDetailsForm(forms.Form):
    # user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select", label=_("User"), widget=forms.HiddenInput(attrs={'class':'form-control'}))
    profile_photo = forms.FileField(label='Profile Photo', widget=forms.ClearableFileInput(attrs={'class':'form-control', 'placeholder':_('Profile Photo')}))
    mobile_no = forms.CharField(label='Primary Mobile No',max_length='10', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Mobile No Pincode')}))
    additional_mobile_no = forms.CharField(label='Alternate Mobile No',max_length='10', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Mobile No Alternate')}))

    address_line_1   =  forms.CharField(label="Permanant Address", widget=forms.Textarea(attrs={'class':'form-control','rows':'3', 'cols':'25', 'placeholder':_('Permanant Address')})) 
    address_line_2   =  forms.CharField(label="Secondary Address", widget=forms.Textarea(attrs={'class':'form-control','rows':'3', 'cols':'25', 'placeholder':_('Secondary Address')})) 
    pincode = forms.CharField(label='Pincode', max_length='6', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Pincode')}))
    state = forms.ModelChoiceField(label=_("State"),
        queryset=StateMaster.objects.all(),
        widget=autocomplete.ModelSelect2(url='master:state-autocomplete' ,attrs={'class':'form-control', 'data-placeholder': 'State', 'data-minimum-input-length': 2})
    )
    city = forms.ModelChoiceField(label=_("City"),
        queryset=CityMaster.objects.all(),
        widget=autocomplete.ModelSelect2(url='master:city-autocomplete' ,attrs={'class':'form-control', 'data-placeholder': 'City', 'data-minimum-input-length': 2})
    )

    class Meta:
        model = UserDetails
        fields = ['profile_photo','mobile_no','additional_mobile_no',
            'address_line_1', 'address_line_2','pincode','state','city',]
            # 'profile_approved_datetime', 'profile_approved_remarks','profile_dis_opt_by_status',
            # 'profile_dis_opt_by_remarks','profile_dis_opt_by_datetime','profile_dis_by_remarks',
            # 'profile_dis_by_datetime','profile_approved_by','profile_dis_by']    
    
    
    
