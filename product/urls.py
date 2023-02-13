from django.urls import include, path
import product.views as views

urlpatterns = [
    path("", views.ProductAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailView.as_view()),
]
