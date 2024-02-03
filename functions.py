from pytube import YouTube
from flask import render_template
from googlesearch import search 
from bs4 import BeautifulSoup
import requests
import os
import time
from pathlib import Path

def play(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download("static/audio/")
    
def download(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    path=str(Path.home() / "Downloads/")
    out_file = video.download(path)
    
def query(q):  
        user_query=q        
        URL="https://www.google.com/search?q=play song" + user_query+ "on youtube"
        headers = {
            'User-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        }
        page=requests.get(URL,headers=headers)
        soup=BeautifulSoup(page.content,'html.parser')
        result=soup.find_all('a')
        links={}
        for i in result:
            href=str(i.get('href'))
            if href.startswith("https://www.youtube.com/watch?v="):
                yt = YouTube(href)
                title=yt.title
                image=yt.thumbnail_url
                links[title]=(href,image)
        return links

def filterdownload(file):
    list1=[i for i in file if i.endswith(".mp3") or i.endswith(".mp4")]
    return list1


      