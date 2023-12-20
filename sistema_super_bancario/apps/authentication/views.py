from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.context_data['errors'] = form.errors
        return response


class CustomLogoutView(LogoutView):
    next_page = 'main'
