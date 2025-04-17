from rest_framework import permissions






class SuperUserOrReceptionistRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and (
                request.user.is_superuser or 
                request.user.groups.filter(name="Receptionist_name").exists()
            )
        )
        
        
        
        
class SuperUserOrDoctorRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and (
                request.user.is_superuser or 
                request.user.groups.filter(name="Doctor_profile").exists()
            )
        )
        

class IsSuperUserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and (
                request.user.is_superuser
            )
        )
        
class PatientEditOnly_SuperuserReceptionistDoctorViewOnly(permissions.BasePermission):
   

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user.is_superuser or 
                request.user.groups.filter(name="Receptionist").exists()
                or request.user.groups.filter(name="Doctor").exists()  
            )

        return obj.patient == request.user

