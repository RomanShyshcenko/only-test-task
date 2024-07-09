from django.urls import path

from only_fans_stat import views

urlpatterns = [
    path('accounts-detail/', views.ListAccountDetailView.as_view(), name='accounts-detail'),
    path('links/', views.ListLinksView.as_view(), name='links'),
    path('links/create/', views.CreateLinksView.as_view(), name='create_links'),
]
