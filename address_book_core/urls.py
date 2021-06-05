# Set the url configurations of the core project address_book_core
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),                                                   # Add urls of admin site
    path('', include('address_book.urls',namespace='address_book')),                   # Include urls of the address_book app
    path('api/', include('address_book_api.urls',namespace='address_book_api')),       # Include urls of the address_book_api app
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),     # Activate user login url for the APIview
]
