from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'iln.website.views.home', name='home'),
    url(r'^home/$', 'iln.website.views.home_a', name='home_a'),
    url(r'^premios/(?P<slug>.*)$', 'iln.website.views.premios', name='premios'),
    url(r'^tarefas/$', 'iln.website.views.tarefas', name='tarefas'),
    url(r'^saldo/$', 'iln.website.views.saldo', name='saldo'),
    url(r'^pedidos/$', 'iln.website.views.pedidos', name='pedidos'),
    url(r'^regulamento/$', 'iln.website.views.regulamento', name='regulamento'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
)
