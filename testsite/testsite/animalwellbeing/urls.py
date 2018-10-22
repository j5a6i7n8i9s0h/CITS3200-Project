from django.urls import path
from . import views
app_name = 'awb'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login', views.login_view, name='login'),
    path('accounts/logout',views.logout_view, name='logout'),
    path('createcoversheet',views.form_creation, name='createcoversheet'),
    path('accounts/createresearcher', views.create_researcher, name='create_researcher'),
    path('download/<int:coversheet_id>/', views.download_cs, name='download'),
    path('download_rs/<int:coversheet_id>/', views.download_rs, name='download_rs'),
    path('edit/<int:coversheet_id>/', views.edit_form, name='edit_cs'),
    path('search', views.search, name='search'),
    path('user_activation', views.user_activation, name='user_activation'),
    path('activate/<str:username>', views.activate, name='activate'),
    path('profile', views.view_profile, name='view_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('get_username', views.get_username, name='get_username'),
    path('validate_question', views.validate_question, name='validate_question'),
    path('panel/<int:coversheet_id>/', views.panel, name='panel_cs'),
    path('approve_or_disapprove_coversheet/<int:coversheet_id>/', views.approve_or_disapprove_coversheet, name='approve_or_disapprove_cs'),
    path('request_approval/<int:coversheet_id>/', views.request_approval, name='request_approval'),
    path('cs_requests/',views.requests_approval_admin, name='cs_requests'),
    path('cancel_request/<int:coversheet_id>/', views.cancel_request, name='cancel_request'),
    path('activate_detail/<str:username>/', views.activate_detail, name='activate_detail'),
    path('decline_user/<str:username>/',views.decline_user,name='decline_user'),
    path('criteria', views.criteria, name='criteria')
]
