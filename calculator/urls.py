from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('calc', views.greetings),
    path('calculation',views.calculation)
]
