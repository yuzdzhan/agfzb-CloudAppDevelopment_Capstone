from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path(route='', view=views.get_dealerships, name='index'),
    #week 1 T4
    path(route='about', view=views.about, name='about'),
    # path for contact us view
    path(route='contact', view=views.contact, name='contact'),

    # path for registration
    #week 2 t7
    path('registration/', view=views.registration_request, name='registration'),

    # path for login
    #week 2 t 5
    path(route='login/', view=views.login_request, name='login'),

    # path for logout
    #week 2 t 5
    path(route='logout/', view=views.logout_request, name='logout'),

    

    # path for dealer reviews view
    path('dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),
    # path for add a review view
    path(route='addreview/<int:dealer_id>/', view=views.add_review, name='add_review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)