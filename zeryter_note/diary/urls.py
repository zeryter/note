from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zeryter_note.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'diary.webpage.homepage', name='homepage'),
    url(r'^diary/(?P<pk>[0-9]+)/$','diary.webpage.diary_views'),
    url(r'^diary/new/$', 'diary.webpage.diary_new', name='diary_new'),
    url(r"^post/(?P<pk>[0-9]+)/edit/$", 'diary.webpage.diary_edit', name='diary_edit'),
    url(r'^draft/', 'diary.webpage.diary_draft', name='diary_draft'),
    url(r'^publish/(?P<pk>[0-9]+)/$', 'diary.webpage.diary_publish', name='diary_publish'),





    url(r'^test/', 'diary.test.test_web.home'),
)

