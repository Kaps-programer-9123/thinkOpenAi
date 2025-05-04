from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class DisableCSRFMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/chunking/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
