from django.urls import path
from . import views
urlpatterns = [
    path("",views.giris,name="login"),
    path("AdminAnasayfa",views.index,name="index"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path("Anasayfa",views.user_page,name="user"),
    path("Siparis",views.siparis,name="siparis"),


    path('kirala/<int:id>', views.kirala, name='kirala'),

]