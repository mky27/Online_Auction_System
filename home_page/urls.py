from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('register_pi/<str:username>/', views.register_pi, name='register_pi'),
    path('logout/', views.log_out, name='logout'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_auction/', views.create_auction, name='create_auction'),
    path('auction_details/<int:auction_id>/', views.auction_details, name='auction_details'),
    path('place_bid/<int:auction_id>/', views.place_bid, name='place_bid'),
    path('auto_update_auction/', views.auto_update_auction, name='auto_update_auction'),
    path('manual_update_auction/', views.manual_update_auction, name='manual_update_auction'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('add_to_watchlist/<int:auction_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:auction_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('withdraw_from_auction/<int:auction_id>/', views.withdraw_from_auction, name='withdraw_from_auction'),
    path('saved_auction/', views.saved_auction, name='saved_auction'),
    path('edit_auction/<int:auction_id>/', views.edit_auction, name='edit_auction'),
    path('completed_auction/', views.completed_auction, name='completed_auction'),
    path('completed_auction_details/<int:auction_id>/', views.completed_auction_details, name='completed_auction_details'),
    path('ongoing_auction/', views.ongoing_auction, name='ongoing_auction'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('cart/', views.cart, name='cart'),
    path('cart_auction_details/<int:auction_id>/', views.cart_auction_details, name='cart_auction_details'),
    path('checkout/<int:auction_winner_id>/', views.checkout, name='checkout'),
    path('remove_from_cart/<int:auction_winner_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('get_wallet_balance/', views.get_wallet_balance, name='get_wallet_balance'),
    path('wallet/', views.wallet, name='wallet'),
    path('reload_wallet/', views.reload_wallet, name='reload_wallet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)