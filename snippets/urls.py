from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Function Based Views
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>', views.snippet_details),

    # Class Based Views
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),  
]

urlpatterns = format_suffix_patterns(urlpatterns)
