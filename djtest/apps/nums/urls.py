from django.urls import path

from . import views

urlpatterns = (
    path('', views.list_view, name='nums_list'),
    path('create/<int:number>', views.create_view, name='nums_create'),
    path('update/<int:number_id>/<int:value>', views.update_view, name='nums_update'),
    path('delete/<int:number_id>', views.delete_view, name='nums_delete'),
)
