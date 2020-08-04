from django.shortcuts import render, redirect
from .models import melonlist
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    # return render(request,'index.html')
    Melonlist = melonlist.objects.all()
    return render(request,'index.html',{'Melonlist':Melonlist})

def melonCrolling():
    iamhuman={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

    url = "https://www.melon.com/chart/day/index.htm"
    req = requests.get(url, headers = iamhuman) #신분증 내고 빌리는 느낌 
    html = req.text

    soup = BeautifulSoup(html,'html.parser')

    songs = []
    song = soup.find_all('div',{"class":"ellipsis rank01"})
    for i in song:
        songs.append(i.find('a').text)

    singers = []
    singer = soup.find_all('div',{"class":"ellipsis rank02"})
    for i in singer:
        singers.append(i.find('a').text)

    ranks = []
    rank = soup.find_all('span',{"class":"rank"})
    for i in rank[1:]:
        ranks.append(i.text)

    albums = []
    album = soup.find_all('div',{"class":"ellipsis rank03"})
    for i in album:
        albums.append(i.find('a').text)

    # album_imgs = []
    # album_img = soup.find_all('a',{"class":"image_typeAll"})
    # for i in album_img:
    #     album_imgs.append(i.find('img').get("src"))

    album_imgs = []
    album_img = soup.select('td:nth-child(4) > div > a > img')
    for i in album_img:
        album_imgs.append(i.get("src"))

    sumlist = list(zip(songs,singers,ranks,album_imgs))
    return sumlist 

def crolling(request):
    Melon_data_list = melonCrolling()
    melonlist.objects.all().delete()
    for i in range(len(Melon_data_list)):
        melonlist(
            songName = Melon_data_list[i][0],
            singerName= Melon_data_list[i][1],
            rank = int(Melon_data_list[i][2]),
            imgSrc = Melon_data_list[i][3],
        ).save()
    return redirect('index')