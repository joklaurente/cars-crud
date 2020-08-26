from django.urls import path
from django.conf.urls import url
  
# importing views from views..py 
from .views import create_car, list_car, update_car, delete_car
  
urlpatterns = [ 
    # path('cars/', view=create_view, name="create_view"),
    # url(r'^$', views.clup_index, name='clup_index')
    url(r'^$', view=list_car, name="list_car"),
    url(r'create/', view=create_car, name="create_car"),
    url(r'^(?P<id>\d+)/?$', view=update_car, name="update_car"),
    url(r'^(?P<id>\d+)/delete/', view=delete_car, name="delete_car"),
    # path('appointments/', views.AppointmentList.as_view()),
    # path('<id>', detail_view ),
] 