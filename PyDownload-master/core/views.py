from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from django.utils.encoding import smart_str
from pytube import YouTube
import os, shutil
from core.models import Video


# return the main search page
def search(request):
    return render(request, "search.html", {"query":""})


# display the result by fetching data from youtubeAPI
def result(request):
    if "query" not in request.POST:
        print("no query no action")
        return render(request, "result.html", {"query":"N/A", "data": []})
        
    query = request.POST["query"]

    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'q': query,
        'key': settings.YOUTUBE_API_KEY,
        'maxResults' : 10,
        'type': 'video'
    }
    all_data = []
    videos = []
    r = requests.get(search_url, params=search_params)
    results = r.json()['items']
    for result in results: 
        title  = result['snippet']['title']
        url = 'https://www.youtube.com/watch?v=' + result["id"]["videoId"]
        thumbnail = result['snippet']['thumbnails']['medium']['url']
        video = Video.objects.create(title=title, url = url, thumbnail = thumbnail)
        videos.append(video)
    if "download" in request.POST:
        print("download detected")
        empty_folder()
        print("server download folder emptied")
        url = request.POST["download"]
        return download(url, request)
        # return render(request, "result.html", {"query":"N/A", "data": []})
    return render(request, "result.html", {"query":query, "data": videos})


# helper method to download youtube video
def download(url, request):
    yt = YouTube(url)
    video = yt.streams.first()
    video.download("downloads")
    file_name = video.title + ".mp4"
    file_path = os.path.join("downloads", file_name)
    f = open(file_path, 'rb')
    response = HttpResponse(f.read(), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Accel-Redirect'] = smart_str('downloads')
    print("download finished")
    return response


def empty_folder():
    for root, dirs, files in os.walk("downloads"):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
