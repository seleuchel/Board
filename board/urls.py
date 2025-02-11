from django.urls import path
from .views import index, post_update

urlpatterns = [
    path("", index, name="index"),  # 메인 페이지
    path("post/update/", post_update, name="post_update"),
]
