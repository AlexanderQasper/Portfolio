from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from .views import profile_view

from myproject.search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path('superadmin/', include('myproject.urls_django_admin')),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    
    path('accounts/', include('allauth.urls')),  # регистрация и логин allauth
    path('profile/', profile_view, name='profile'),  # личный кабинет пользователя
    
    path('', include(wagtail_urls)),  # остальные страницы через wagtail
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

