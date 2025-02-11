from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title", "vul_ok", "srv_name", "req_date", "sendmail_date",
            "adm_buseo", "srv_loc", "bigo", "created_date"
        ]  # ✅ 모든 필드를 포함
        widgets = {
            "req_date": forms.DateInput(attrs={"type": "date"}),  # 날짜 필드용 위젯
            "sendmail_date": forms.DateInput(attrs={"type": "date"}),
            "created_date": forms.DateInput(attrs={"type": "date"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "vul_ok": forms.CheckboxInput(attrs={"class": "form-check-input"}),  # ✅ True/False 체크박스
            "bigo": forms.Textarea(attrs={"class": "form-control", "rows": 3}),  # 메모용 필드
        }
