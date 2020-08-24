import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Grid


def create_user(client=None):
    User.objects.create_user(username="test", password="p455w0rd123")
    if client:
        client.login(username="test", password="p455w0rd123")


#
# VIEW TESTS
#

def test_index_load():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_goto_grids_on_auth():
    client = Client()
    create_user(client)

    response = client.get(reverse("index"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_grids_list_shows_list():
    client = Client()
    create_user(client)

    Grid.objects.create(name="TestGrid1234")
    Grid.objects.create(name="GridTastic3000")

    response = client.get(reverse("grids"))

    assert response.status_code == 200
    assert "TestGrid1234" in str(response.content)
    assert "GridTastic3000" in str(response.content)


def test_grids_list_redirect_on_noauth():
    client = Client()

    response = client.get(reverse("grids"), follow=True)
    assert response.status_code == 404


@pytest.mark.django_db
def test_grids_detail_view():
    client = Client()
    create_user(client)

    response = client.get(reverse("griddetails", args=(1,)))
    assert response.status_code == 404

    grid = Grid.objects.create(name="TestGrid1234")
    response = client.get(reverse("griddetails", args=(grid.id,)))
    assert response.status_code == 200
    assert "TestGrid1234" in str(response.content)


#
# API TESTS
#

@pytest.mark.django_db
def test_grid_api_create():
    client = APIClient()
    create_user(client)

    response = client.post("/api/grids/", {"name": "testgrid"}, format="json")
    assert response.status_code == 201


def test_grid_api_create_unauthenticated():
    client = APIClient()
    response = client.post("/api/grids/", {"name": "testgrid"}, format="json")
    assert response.status_code == 403


@pytest.mark.django_db
def test_grid_api_get_grid():
    client = APIClient()
    create_user(client)

    response = client.get("/api/grids/1/")
    assert response.status_code == 404

    Grid.objects.create(name="TestGrid")
    response = client.get("/api/grids/1/")
    assert response.status_code == 200


def test_grid_elements_api_create():
    pass


def test_grid_elements_api_get():
    pass
