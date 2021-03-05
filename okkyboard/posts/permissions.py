from rest_framework.permissions import AllowAny, IsAuthenticated


class IsAuthenticatedAndChangedOwned(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
