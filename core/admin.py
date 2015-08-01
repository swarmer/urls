from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        return {'owner': request.user}

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['name', 'target', 'owner']
        else:
            return ['name', 'target']

    def has_change_permission(self, request, obj=None):
        has_class_permission = super().has_change_permission(request, obj)
        if not has_class_permission:
            return False

        if obj is None:
            return True

        owns_object = request.user.id == obj.owner.id
        if request.user.is_superuser or owns_object:
            return True

        return False

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Link.objects.all()
        return Link.objects.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


admin.site.register(Link, LinkAdmin)
