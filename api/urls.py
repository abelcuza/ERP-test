from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.btre import views as btre_views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register(r'realtor', btre_views.RealtorViewSet)
router.register(r'listing', btre_views.ListingViewSet)
router.register(r'contact', btre_views.ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

