from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name = 'index'),
    path('upload/project/', views.upload, name = "upload"),
    path('search/',views.search_project, name='search.post'),
    path("project/<int:project_id>/", views.project_details, name="project_details"),
    path('review//<int:id>/',views.review_project, name='review.project'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/',views.ProfileList.as_view()),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='profile'),
    path('add_profile/',views.add_profile,name = 'add_profile'),
     path('update_profile/<int:id>/',views.update_profile, name='update_profile'),
]