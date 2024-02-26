from django.urls import path

from .views import (
    CreateCheckoutSessionView,
    CancelView,
    ProductLandingPageView,
    SuccessView,
)


urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<pk>/', ProductLandingPageView.as_view(), name='landing-page'),
    path('buy/<pk>/',
         CreateCheckoutSessionView.as_view(),
         name='create-checkout-session')
]
