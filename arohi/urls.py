from django.urls import path
from . import views

app_name = 'arohi'

urlpatterns = [
    # path('', views.order),

    path('', views.home, name='home_page',),

    path('contact', views.contact, name='contact_page'),

    path('feed/consumer/', views.consumer_feed, name='consumer_feed',),
    path('feed/investor/', views.investor_feed, name='investor_feed',),

    path('auth/login', views.login, name='login'),
    path('auth/signup', views.sign_up, name='signup'),

    path('dashboard/consumer', views.dashboard_consumer, name='consumer_dashboard'),
    path('dashboard/investor', views.dashboard_investor, name='investor_dashboard'),
    path('dashboard/entrepreneur', views.dashboard_entrepreneur, name='entrepreneur_dashboard'),

    path('product/add', views.add_product, name='add_product'),
    path('product/buy', views.buy_product, name='buy_product'),

    path('profiles/consumer', views.profile_consumer, name='profile_consumer'),
    path('profiles/entrepreneur', views.profile_entrepreneur, name='profile_entrepreneur'),
    path('profiles/investor', views.profile_investor, name='profile_investor'),
]
