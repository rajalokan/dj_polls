
from django.conf.urls import url

from polls.views import index, detail, result, vote


app_name = "polls"
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/result/$', result, name="result"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name="vote")
]
