from django.shortcuts import render
from videos.models import Videos

def all_videos(request):
    all_videos = Videos.objects.order_by('created_date')
    return render(request,"videos/all_videos.html",{'all_videos':all_videos})
                
def watch_video(request, video_id=None):
    video = Videos.objects.get(id=video_id)
    return render(request,"videos/video_details.html",{'video':video})
