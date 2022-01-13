from django.urls import path
from snippets import views
# urlpatterns = [
#     path('snippets/<int:pk>/', views.snippet_detail),
#     path('snippets/', views.snippet_list),
# ]

urlpatterns = [
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/', views.SnippetList.as_view())
]