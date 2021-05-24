from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect, HttpResponse, response
from django.urls.base import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from user_profile.forms import LoginForm,UserDetailsForm,CustomPasswordChangeForm,PasswordResetFormUnique
from django.contrib.auth.forms import UserCreationForm
from user_profile.models import UserDetails

"""User Login Functionality - starts"""
@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        login_form = LoginForm()
        success_msg = request.session.pop('success_msg', None)
        return render(request, "user_profile/login.html", {'login_form':login_form,
                                                        'success_msg':success_msg,
                                                })
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']    
        user=authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return HttpResponseRedirect('/en/admin/')
            else:
                return HttpResponseRedirect(reverse_lazy('home:home'))
        else:
            request.session['success_msg'] = _("Please check username and password.")
            return HttpResponseRedirect(reverse_lazy('user_profile:login',  kwargs={}))
"""User Login Functionality - ends"""

"""User Logout Functionality - starts"""
def logout_view(request):
    logout(request)
    return HttpResponseRedirect()
"""User Logout Functionality - ends"""

"""User Registrations Functionality - starts"""
@csrf_exempt
def user_registrations(request):
    if request.method == 'GET':
        success_msg = request.session.pop('success_msg', None)
        user_details_form = UserDetailsForm()
        return render(request, "user_profile/registration.html", {'user_details_form':user_details_form,
                                                                'success_msg':success_msg,
                                                            })
    if request.method == 'POST':
        # form = UserDetailsForm(request.POST)
        # if form.is_valid():
            # data = {k: v for k, v in form.cleaned_data.items()}
        form = 'form'
        if form:
            if User.objects.filter(username=request.POST.get('username')).exists():
                request.session['success_msg'] = _("Username already exists.")
                return HttpResponseRedirect(reverse_lazy('user_profile:user_registrations',  kwargs={}))
            elif User.objects.filter(email=request.POST.get('email')).exists():
                request.session['success_msg'] = _("Email already exists.")
                return HttpResponseRedirect(reverse_lazy('user_profile:user_registrations',  kwargs={}))
            # elif UserDetails.objects.filter(email=request.POST.get('mobile_no')).exists():
            #     request.session['success_msg'] = _("Mobile number already exists.")
            #     return HttpResponseRedirect(reverse_lazy('user_profile:registrations',  kwargs={}))
            else:
                user_id = User.objects.create_user(first_name=request.POST.get('first_name'),
                            last_name = request.POST.get('last_name'),
                            email = request.POST.get('email'),
                            username = request.POST.get('username'),
                            is_active = 0,
                            password =request.POST.get('password'))
                
                # additiona_prf = UserDetails.objects.create(user = user_id,**data)
                return HttpResponseRedirect(reverse_lazy('home:home',))
        else:
            success_msg = _("Please verify the details.")
            return render(request, "user_profile/registration.html", {'user_details_form':form,
                                                                        'success_msg':success_msg,
                                                                    })


"""Change Password functionality. - Starts"""
@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            success= _('Password has been changed successfully.')
            logout(request)
            return render(request, 'user_profile/password_change.html', {'form': form,
                                                                        'note':success,
                                                                        'login_url':settings.LOGOUT_REDIRECT_URL})
        else:
            return render(request, 'user_profile/password_change.html', {'form': form })
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'user_profile/password_change.html', {'form': form })

"""Change Password functionality. - Ends"""

"""Forgot Password functionality. - Starts"""
def password_forgot(request):
    fp_form = PasswordResetFormUnique()
    form = PasswordResetFormUnique()
    success = request.session.pop('success', None)
    error_email = request.session.pop('error_email', None)
    if request.method == 'GET':
        return render(request, 'base.html',{'form':form,
                                            'fpform':fp_form,
                                            'success':success,
                                            'error_email':error_email,
                                            })
    
    elif request.method == 'POST':
        user_json = {}
        form = PasswordResetFormUnique(request.POST)
        if form.is_valid():
            data = {'email':request.POST.get('email')}
            response = requests.post(url = API_DOMAIN+API_URL+'reset-password/', data=data)
            try:
                result = response.json()
            except:
                result = []
            try:
                email_msg = result['email']
            except:
                email_msg = None
            try:
                status = result['status']
            except:
                status = None
            if status == 'OK':
                user_json['success'] = "We have sent a link to change your password. Kindly check your email."
            elif email_msg:
                user_json['error_email'] = "There is no active user associated with this e-mail address."
            else:
                user_json['error_email'] = "Failed, Please Try Again"
            return JsonResponse(user_json)
        else:
            user_json['error_email'] = request.POST
            return JsonResponse(user_json)
        
"""Forgot Password functionality. - Ends"""
