from django.contrib import admin
from .models import RepairRequest, Employee, Technician, User, StatusHistory

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'technician', 'status', 'created_at', 'updated_at', 'image')
    list_filter = ('status','technician')
    search_fields = ('description', 'employee__user__username', 'technician__user__username')
    autocomplete_fields = ('employee', 'technician')  
    fields = ('employee', 'technician', 'description', 'status', 'image') 
   
   
    actions = ['assign_technician']
    
    def assign_technician(self, request, queryset):
       self.message_user(request, "assign technican directly by editing the list view")
           
    
    
    list_editable = ('technician',)
    assign_technician.short_description = "assign tech"

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
    

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)  

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_employee', 'is_technician', 'is_admin')

@admin.register(StatusHistory)
class StatusHistoryAdmin(admin.ModelAdmin):
    list_display = ('repair_request', 'status', 'updated_at')
