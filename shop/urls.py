"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product.views import CategoryListView, ProductViewSet, CommentViewSet, RatingViewSet, FavoriteViewSet

from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
# from cart.views import CartApiView


"""=============Swagger docs============="""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        default_version='v1',
        description="auth API"
    ),
    public=True
)
"""======================================"""

router=DefaultRouter()
router.register('products',ProductViewSet )
router.register('comments', CommentViewSet)
# router.register('likes', LikeViewSet)
router.register('rating', RatingViewSet)
router.register('favorite', FavoriteViewSet)
# router.register('carts',CartViewSet )
# router.register('orders',OrderViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('docs/', swagger_view.with_ui('swagger', cache_timeout=0)),

    path('accounts/', include('allauth.urls')),
    path('', include('product.urls')),
    path('api/account/', include('rest_framework.urls')),
    # path('v1/api/', include('product.urls')),
    path('v1/api/categories/', CategoryListView.as_view()),
    path('v1/api/user/', include('users.urls')),
    path('v1/api/',include(router.urls)),
    # path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),
    path('', include('orders.urls')),
    # path('api/v1/cart/', CartApiView.as_view()),
    # path('api/v1/orders/', include('order.urls')),
    # path('basket/', include('basket.urls')),
    # path('v1/api/cart/', include('cart.urls')),
    # path('v1/api/orders/', include('order.urls'))
]
