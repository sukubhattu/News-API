from django.urls import path
from django.urls.resolvers import URLPattern
from .views import NewsList, NewsDetail

app_name = "news"

urlpatterns = [
    path("", NewsList.as_view(), name="newsList"),
    path("<int:pk>", NewsDetail.as_view(), name="newsDetail"),
]
