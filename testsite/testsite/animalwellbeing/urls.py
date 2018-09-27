from django.urls import path

from . import views
app_name = 'awb'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login', views.login_view, name='login'),
    path('accounts/logout',views.logout_view, name='logout'),
    path('createcoversheet',views.form_creation, name='createcoversheet'),
    path('<int:coversheet_id>/', views.view_coversheet, name='detail'),
    path('accounts/createresearcher', views.create_researcher, name='create_researcher'),
    path('download/<int:coversheet_id>/', views.download_cs, name='download'),
    path('edit/<int:coversheet_id>/', views.edit_form, name='edit_cs'),
    path('search', views.search, name='search'),
    path('panel/<int:coversheet_id>/', views.panel, name='panel_cs'),
    path('approve_or_disapprove_coversheet/<int:coversheet_id>/', views.approve_or_disapprove_coversheet, name='approve_or_disapprove_cs'),
]
