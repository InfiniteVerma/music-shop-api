from django.contrib import admin
from .models import Blog, Instrument, Book, Store

admin.site.register(Blog)
admin.site.register(Instrument)
admin.site.register(Book)
admin.site.register(Store)