from django.urls import path
from rest_framework_nested import routers
#from rest_framework.routers import DefaultRouter
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')


#router.register('products', views.ProductViewSet)
#router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls + products_router.urls
