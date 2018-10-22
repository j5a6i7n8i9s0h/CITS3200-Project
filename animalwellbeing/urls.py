from django.urls import path
from . import views
app_name = 'awb'
urlpatterns = [
    path('', views.index, name='index'),
    path('awb/', views.index, name='index'),
    path('awb/accounts/login', views.login_view, name='login'),
    path('awb/accounts/logout',views.logout_view, name='logout'),
    path('awb/createcoversheet',views.form_creation, name='createcoversheet'),
    path('awb/accounts/createresearcher', views.create_researcher, name='create_researcher'),
    path('awb/download/<int:coversheet_id>/', views.download_cs, name='download'),
    path('awb/edit/<int:coversheet_id>/', views.edit_form, name='edit_cs'),
    path('awb/search', views.search, name='search'),
    path('awb/user_activation', views.user_activation, name='user_activation'),
    path('awb/activate/<str:username>', views.activate, name='activate'),
    path('awb/profile', views.view_profile, name='view_profile'),
    path('awb/edit_profile', views.edit_profile, name='edit_profile'),
    path('awb/change_password', views.change_password, name='change_password'),
    path('awb/get_username', views.get_username, name='get_username'),
    path('awb/validate_question', views.validate_question, name='validate_question'),
    path('awb/panel/<int:coversheet_id>/', views.panel, name='panel_cs'),
    path('awb/approve_or_disapprove_coversheet/<int:coversheet_id>/', views.approve_or_disapprove_coversheet, name='approve_or_disapprove_cs'),
    path('awb/request_approval/<int:coversheet_id>/', views.request_approval, name='request_approval'),
    path('awb/cs_requests/',views.requests_approval_admin, name='cs_requests'),
    path('awb/cancel_request/<int:coversheet_id>/', views.cancel_request, name='cancel_request'),
    path('awb/activate_detail/<str:username>/', views.activate_detail, name='activate_detail'),
    path('awb/decline_user/<str:username>/',views.decline_user,name='decline_user'),
    path('awb/criteria', views.criteria, name='criteria')
]
