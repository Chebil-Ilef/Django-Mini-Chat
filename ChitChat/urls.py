from django.urls import path, include
from ChitChat import views as chat_views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),
    path("auth/login/", LoginView.as_view(template_name="chat/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),

]

# NOTE: By default, LoginView looks for a template named registration/login.html. 
# If you want to use a custom template for your login page, you need to specify the template_name attribute.
# LogoutView is a bit different because it doesn't need a template to render a form.