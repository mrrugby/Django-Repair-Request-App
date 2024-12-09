from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import CreateView
from django.db.models import Count
from ..forms import AdminSignUpForm
from ..models import Technician, RepairRequest, User


class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Admin account created successfully!")
        return redirect('admin_dashboard')

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect(login)
    
    all_requests = RepairRequest.objects.all()
    technicians = Technician.objects.all()
    
    technician_perfomance = technicians.annotate(
        assigned_tasks = Count('assigned_requests')
    )
    context = {
        'all_requests' : all_requests,
        'technician_perfomance' : technician_perfomance,
    }
    
    return render(request, 'admin/admin_dashboard.html', context)
    
    
    
    
@login_required
def view_request_details(request, request_id):
    if not request.user.is_admin:
        return redirect('login')
    
    repair_request = get_object_or_404(RepairRequest, id=request_id)
    
    context = {
        'repair_request' : repair_request,
    }
    
    return render(request, 'admin/view_request_details.html', context)


# Update Request Status 
@login_required
def update_request_status(request, request_id):
    if not request.user.is_admin:
        return redirect('login')

    repair_request = get_object_or_404(RepairRequest, id=request_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        repair_request.status = new_status
        repair_request.save()
        return redirect('admin_dashboard')

    context = {
        'repair_request': repair_request,
    }
    return render(request, 'admin/update_request_status.html', context)