
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="iskahome"),
    path('signup/',views.user_signup,name="iskasignup"),
    path('login/',views.user_login,name="iskalogin"),
    path('addadver/',views.post,name="iskaadd"),
    path('logout/',views.user_logout,name="iskalogout"),
    path('contact/',views.contact,name="iskacontact"),
    path('youradvertisment/',views.yourad,name="iskaad"),
    path('search/',views.searchk,name="iskasearch"),
    path('about/',views.about,name="iskaabout"),
    path('showselectedhouse/',views.showselecthouse,name="iskashowselecthouse"),
    path('showselectedapartment/',views.showselectapartment,name="iskashowselectapartment"),
    path('showselectedbanglow/',views.showselectbanglow,name="iskashowselectbanglow"),
    path('recent/<check>/',views.recent,name="iskarecent"),
    path('oldest/<check>/',views.oldest,name="iskaoldest"),
    path('shuffle/<check>/',views.shuffle,name="iskashuffle"),
    path('delete_post/<check>/',views.delete_post,name="iskadelete"),
    path('update_post/<check>/',views.update_post,name="iskaupdate"),
    path('information/<check>',views.information,name="iskainformation"),
    path('delete_confirm/<check>',views.delete_confirm,name="iskadeleteconfirm"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
