from django.urls import path
from .views import *


urlpatterns = [
   # path('', index, name='index'),  # FBV 방식의 call
    path('', fileUpload, name='fileupload'),  # CBV 방식의 call

    #path('<int:pk>', views.single_post_page, name='post_detail'),
]

