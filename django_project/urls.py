from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('articles/new/', core_views.create_article, name='create_article'),
    path('articles/', core_views.article_list, name='article_list'),
    path('articles/<int:pk>/', core_views.article_detail, name='article_detail'),
    path('articles/<int:pk>/', core_views.article_detail, name='article_detail'),

    path('doctors/', core_views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', core_views.doctor_detail, name='doctor_detail'),


    path('profile/', core_views.profile, name='profile'),
    path('profile/edit/', core_views.edit_profile, name='edit_profile'),
    path('feedback/', core_views.submit_feedback, name='submit_feedback'),
    path('signup/', core_views.signup, name='signup'),  
    path('login/', core_views.login_view, name='login'),
    path('logout/', core_views.logout_view, name='logout'),
    path('health_facts/', core_views.health_facts, name='health_facts'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)