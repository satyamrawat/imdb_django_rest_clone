from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformVS, ReviewList,ReviewDetail, ReviewCreate,UserReview,WatchListGV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename="streamplatform")


urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name = 'movie-detail'),
    path('new-list/', WatchListGV.as_view(), name = 'new-movie-list'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name = 'stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name = 'stream-detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name = 'review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name = 'review-list'),    
    path('review/<int:pk>/', ReviewDetail.as_view(), name = 'review-detail'),
    path('reviews/', UserReview.as_view(), name = 'user-review-detail'),

]