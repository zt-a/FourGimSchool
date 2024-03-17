from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
]


urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('main.urls', namespace='main')),
    path('news/', include('news.urls', namespace='news')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('archive/', include('archive.urls', namespace='archive')),
    path('personal/', include('personal.urls', namespace='personal')),
    path('books/', include('books.urls', namespace='books')),
    path('history/', include('history.urls', namespace='history')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('events/', include('event.urls', namespace='event')),
    path('blogs/', include('blog.urls', namespace='blog')),
    path('forum/', include('forum.urls', namespace='forum')),
    path('achievement/', include('achievement.urls', namespace='achievement')),
    path('contact_news/', include('contact_news.urls', namespace='contact_news')),
)


if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls"))),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
