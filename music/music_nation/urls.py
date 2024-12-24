from django.urls import path, include, re_path,reverse
from . import views as music_nation_views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib import admin

app_name = 'music_nation'
urlpatterns = [
    #home /
    path('admin/', admin.site.urls),
    path('',music_nation_views.signup,name='signup'),
    path('login/',music_nation_views.loginpage,name='login'),
    path('home/', music_nation_views.home, name='home'),

    #profile_detail /@username/
    path('@<str:username>/', music_nation_views.profile_detail, name='profile_detail'),

    #add new album /@username/add
    path('@<str:username>/add/', music_nation_views.add_album, name='add_album'),

    #album's detail page /@username/album/album_name
    path('@<str:username>/album/<str:album>/', music_nation_views.album_detail, name='album_detail'),

    # login the user /login/
    

    # signUp new user /signup/
   
    path('about/', music_nation_views.about, name='about'),
    path('feedback/', music_nation_views.feedback, name='feedback'),

    #delete album /@username/album/album_name/delete
    path('@<str:username>/album/<str:album>/delete/', music_nation_views.delete_album, name='delete_album'),

    #add songs to the albums
    path('@<str:username>/album/<str:album>/add/', music_nation_views.add_song, name='add_song'),

    #logout the current user
    path('logout/',music_nation_views.logout,name="logout"),
]
#path('link', view, name='', kwargs={})
#re_path(r'regex', view, name='', kwargs={})
