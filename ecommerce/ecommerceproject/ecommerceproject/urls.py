
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include("shop.urls")),
    path('search/', include("search_app.urls")),
    path('cart/', include("cart.urls")),
]

