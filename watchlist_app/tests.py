from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.stream = models.StreamPlatforms.objects.create(
            name="Netflix", about="Amazing Platform", website="http://www.netflix.com"
        )

    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "Amazing platform",
            "website": "http://netflix.com",
        }
        response = self.client.post(reverse("streamplatform-list"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse("streamplatform-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response = self.client.get(
            reverse("streamplatform-detail", args=(self.stream.id,))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.stream = models.StreamPlatforms.objects.create(
            name="Netflix", about="Amazing Platform", website="http://www.netflix.com"
        )
        self.watchlist = models.WatchList.objects.create(
            platform=self.stream,
            title="example movie",
            storyline="example stroyline",
            active=True,
        )

    def test_watchlist_create(self):
        data = {
            "platform": self.stream,
            "title": "example moview",
            "storyline": "example stroyline",
            "active": True,
        }

        response = self.client.post(reverse("movie-list"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse("movie-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_ind(self):
        response = self.client.get(reverse("movie-detail", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.stream = models.StreamPlatforms.objects.create(
            name="Netflix", about="Amazing Platform", website="http://www.netflix.com"
        )
        self.watchlist = models.WatchList.objects.create(
            platform=self.stream,
            title="example movie",
            storyline="example stroyline",
            active=True,
        )


    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating":4,
            "description": "ABCD",
            "watchlist":self.watchlist,
            'active':True
        }
        response = self.client.post(reverse("review-create", args =(self.watchlist.id,)), data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)



