from django.urls import path
from .views import index, post_update, download_csv

urlpatterns = [
    path("", index, name="index"),  # 메인 페이지
    path("post/update/", post_update, name="post_update"),
    path("download_csv/", download_csv, name="download_csv"),
    #path("upload-csv/", upload_csv, name="upload_csv"),
]
