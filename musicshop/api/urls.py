from django.urls import path
from .views import BlogList, BookList, InstrumentList, StoreList, BlogDetail, BookDetail, InstrumentDetail, StoreDetail

urlpatterns = [
    path("blog/", BlogList.as_view(), name="blog"),
    path("blog/<int:pk>/", BlogDetail.as_view(), name="blog"),
    path("books/", BookList.as_view(), name="book"),
    path("books/<int:pk>", BookDetail.as_view(), name="book"),
    path("instruments/", InstrumentList.as_view(), name="instrument"),
    path("instruments/<int:pk>", InstrumentDetail.as_view(), name="instrument"),
    path("store/", StoreList.as_view(), name="store"),
    path("store/<int:pk>", StoreDetail.as_view(), name="store")
]