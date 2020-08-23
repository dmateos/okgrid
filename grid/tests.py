import pytest
from django.contrib.auth.models import User
from django.test import Client
from rest_framework.test import APIClient
from .models import Grid


def test_index_load():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_goto_grids_on_auth():
    User.objects.create_user(username="test", password="p455w0rd123")
    client = Client()
    client.login(username="test", password="p455w0rd123")

    response = client.get("/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_grid_create():
    User.objects.create_user(username="test", password="p455w0rd123")
    client = APIClient()
    client.login(username="test", password="p455w0rd123")

    response = client.post("/api/grids/", {"name": "testgrid"}, format="json")
    assert response.status_code == 201


def test_grid_create_unauthenticated():
    client = APIClient()
    response = client.post("/api/grids/", {"name": "testgrid"}, format="json")
    assert response.status_code == 403


@pytest.mark.django_db
def test_grid_get():
    User.objects.create_user(username="test", password="p455w0rd123")

    client = APIClient()
    client.login(username="test", password="p455w0rd123")

    response = client.get("/api/grids/1/")
    assert response.status_code == 404

    Grid.objects.create(name="TestGrid")
    response = client.get("/api/grids/1/")
    assert response.status_code == 200
