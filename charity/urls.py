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
    path('member/<int:id>', views.view_member, name='view-member')
]
