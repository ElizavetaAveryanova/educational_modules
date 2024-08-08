from django.urls import path

from modules.views import IndexView

app_name = 'modules'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]