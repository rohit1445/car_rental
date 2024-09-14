from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('base/',views.base,name='base'),
    path('message/',views.msg,name='message'),
    path('',views.index, name = 'home'),
    path('home/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('car/', views.cars, name='car'),
    path('bill/', views.order,name='bill'),
    path('contact/',views.contact_us,name='contact'),
    path('adminlogin/',views.admin_login,name='adminlogin'),
    path('signup/',views.register,name='signup'),
    path('login/',views.signin,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('changepassword/', views.change_password, name="change_pass"),
    path('dashboard/', views.dashboardpage, name='dashboard'),
    path('add_car/', views.add_cars, name='add_car'),
    path('view_car/', views.view_cars, name='view_car'),
    path('edit_car/<int:pid>/', views.edit_cars, name="edit_car"),
    path('delete_car/<int:pid>/', views.delete_cars, name="delete_car"),
    path('admin_changepassword/',views.admin_changepassword, name="admin_changepass"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)