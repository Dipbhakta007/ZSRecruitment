# Register models in admin site
#
# (c) 2021 Dip Bhakta, Uttara, Dhaka
# email bhaktadip@gmail.com
# phone +8801725652782

from django.contrib import admin
from .models import Country,State,Address


admin.site.register(Country)
admin.site.register(State)
admin.site.register(Address)
