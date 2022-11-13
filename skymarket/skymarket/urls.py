from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# TODO здесь необходимо подклюючит нужные нам urls к проекту

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/", include('users.urls')),
    path("api/", include('ads.urls')),
    path("api/token/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),

    path("api/shema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)