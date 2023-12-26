from django.urls import path
from . import views

urlpatterns = [
    path('',views.Ourchat, name="Ourchat"),
    # path('<str:room>/', views.room, name='room'),
    path('getroom/',views.getroom, name="getroom"),
    path('send/',views.send, name="send"),
    path('reload/<str:room_name>/<str:username>', views.reload, name="relo")
]