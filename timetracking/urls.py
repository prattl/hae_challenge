from django.conf.urls import patterns, include, url
from timetracking.views import HomeView, JobsView, JobsDetailView, TimeEntriesView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^jobs/$', JobsView.as_view(), name='jobs'),
    url(r'^jobs/(?P<pk>\d+)/$', JobsDetailView.as_view(), name='jobs_details'),
    url(r'^time-entries/$', TimeEntriesView.as_view(), name='time_entries'),
)
