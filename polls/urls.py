from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    #/polls/<question_id>/
    path('<int:question_id>/', views.detail, name='detail'),
    # the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]