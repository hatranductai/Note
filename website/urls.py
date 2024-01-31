from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    re_path(r"^(?!api/|admin|static/).*", TemplateView.as_view(template_name="index.html")),
    
]

# for dir in settings.STATICFILES_DIRS:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[1])
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])