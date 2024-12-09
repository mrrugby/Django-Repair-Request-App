from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..forms import EmployeeSignUpForm, TechnicanSignUpForm, AdminSignUpForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.is_admin:
            return reverse_lazy('admin_dashboard')
        elif user.is_technician:
            return reverse_lazy('technician_dashboard')
        elif user.is_employee:
            return reverse_lazy('employee_dashboard')
        return reverse_lazy('login')
    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    

class AdminSignupView(CreateView):
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Admin'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse_lazy('login')  


class TechnicianSignupView(CreateView):
    form_class = TechnicanSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Technician'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse_lazy('login')  


class EmployeeSignUpView(CreateView):
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Employee'
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('login')  
