from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zeryter_note.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', 'diary.webpage.homepage'),
)

