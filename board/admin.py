from django.contrib import admin
from django import forms
from .models import Post
# Register your models here.

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'req_date': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}),
            'sendmail_date': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}),
        }

@admin.register(Post)  # ✅ 모델 등록
class PostAdmin(admin.ModelAdmin):
    list_display = ( "vul_ok", "srv_name", "req_date", "adm_buseo", "adm_buseo", "srv_loc", "bigo", "created_date")  # 관리자 목록에 표시할 필드
    search_fields = ("srv_name","adm_buseo", "adm_buseo",)  # 검색 가능 필드
    list_filter = ("created_date", "vul_ok")  # 필터 추가
    form = PostAdminForm