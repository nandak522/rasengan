from django.conf.urls import patterns, url

urlpatterns = patterns('versions.views',
    url(r'^$', 'view_enter_versions', {'enter_versions_template':'enter_versions.html'}, 'enter_versions'),
    url(r'^validate/$', 'view_validate_versions', {'validate_versions_template':'validate_versions.html', 'enter_versions_template':'enter_versions.html'}, 'validate_versions'),
    url(r'^generate_file/$', 'view_generate_file', {'generate_versions_file_template':'generate_file.html'}, 'generate_file'),
)
