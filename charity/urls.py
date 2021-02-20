# Django
from django.urls import path

# local Django
from . import views

app_name = 'charity'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-member', views.add_member, name='add-member'),
    path('<int:category_id>', views.view_by_category, name='view-by-category'),
    path('members', views.view_all_members, name='view-all-members'),
    path('member/<str:id>', views.view_member, name='view-member'),
    path('update-member-info/<str:id>', views.update_member_personal_info, name='update-member-member-info'),
    path('update-requirements/<str:id>', views.update_member_requirements, name='update-member-requirements'),
    path('add-member-family/<str:id>', views.add_member_family, name='add-member-family'),
    path('family-member/<str:id>/<str:family_member_id>', views.family_member, name='family-member')
]
