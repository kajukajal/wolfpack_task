from django.contrib import admin

from my.models import user_data


class userAdmin(admin.ModelAdmin):
    list_display=["name","age","image"]


admin.site.register(user_data,userAdmin)
