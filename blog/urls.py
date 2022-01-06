from django.contrib import admin
from django.urls import path
from blog_app.views import about,blog,home,maqola,maqola1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('blog/', blog),
    path('about/', about),
    path('maqola/', maqola),
    path('maqola/<int:son>', maqola1,name="maqola1"),

]
