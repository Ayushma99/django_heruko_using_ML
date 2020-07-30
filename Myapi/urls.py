
from django.urls import path,include
from . import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register("approval", views.viewapprove)

urlpatterns = [

    # path("api/",include(router.urls)),
    path("",views.cform,name="form"),

]
