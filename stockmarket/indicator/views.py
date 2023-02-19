from .views import home

urlpatterns = [
    path('', home, name='home'),
]