from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class LoginRequiredView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)