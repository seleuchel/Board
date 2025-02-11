from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import json
from datetime import datetime

def index(request):
    posts = Post.objects.all().order_by("-created_date")
    return render(request, "board/index.html", {"posts": posts})

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%b. %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return date_string  # 변환 실패 시 원본 그대로 반환


def post_update(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # JSON 데이터 읽기
            for post_data in data["posts"]:
                post_id = post_data.get("id")

                if post_id: # edit
                    post = Post.objects.get(id=post_data["id"])
                    post.vul_ok = post_data["vul_ok"]
                    post.srv_name = post_data["srv_name"]
                    post.req_date = parse_date(post_data["req_date"])
                    post.sendmail_date = parse_date(post_data["sendmail_date"])
                    post.adm_buseo = post_data["adm_buseo"]
                    post.adm_name = post_data["adm_name"]
                    post.srv_loc = post_data["srv_loc"]
                    post.bigo = post_data["bigo"]
                    post.save()
                    
                else: # new raw
                    Post.objects.create(
                        vul_ok=post_data.get("vul_ok", False),
                        srv_name=post_data.get("srv_name", ""),
                        req_date=post_data.get("req_date", None),
                        sendmail_date=post_data.get("sendmail_date", None),
                        adm_buseo=post_data.get("adm_buseo", ""),
                        adm_name=post_data.get("adm_name", ""),
                        srv_loc=post_data.get("srv_loc", ""),
                        bigo=post_data.get("bigo", ""),
                    )

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
