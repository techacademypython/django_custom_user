from django.shortcuts import render
from like_app.models import Post, Like
from django.http import JsonResponse

# Create your views here.


def main_index(request):
    context = {}
    context["post_list"] = Post.objects.all()
    if request.method == "POST" and request.is_ajax():
        post_id = request.POST.get("post_id")
        post = Post.objects.filter(id=post_id).last()
        if post:
            like = Like.objects.filter(post=post, user=request.user).last()
            if like:  # unlike
                post.like_count -= 1
                post.save()
                like.delete()
                return JsonResponse({
                    "message": f"{post.name} xeberi dislike etdiniz",
                    "like_count": post.like_count,
                    "status": True
                })
            else:  # like
                post.like_count += 1
                post.save()
                Like.objects.create(
                    user=request.user,
                    post=post
                )
                return JsonResponse({
                    "message": f"{post.name} xeberi like etdiniz",
                    "like_count": post.like_count,
                    "status": False
                })
    return render(request, "index.html", context)
