# import pytest
# from pages.api_page import ExampleAPIPage
#
#
# @pytest.fixture
# def api_page():
#     base_url = "https://reqres.in/api/users?page=2"
#     return ExampleAPIPage(base_url)
#
#
# def test_get_example_data(api_page):
#     response = api_page.get_data()
#     assert response.status_code == 200
#     assert "data" in response.json()
#     response_data = response.json()
#
#     email_to_find = 'michael.lawson@reqres.in'
#     assert any(entry['email'] == email_to_find for entry in response_data['data'])
#
#     print(response_data)
#     print(email_to_find)
#
#
# def test_post_example_data(api_page):
#     data = {"key": "value"}
#     # headers = {"Authorization": "Bearer QpwL5tke4Pnpja7X4"}
#     #
#     # response = api_page.post_data(data, headers)
#     #
#     # assert response.status_code == 201
#     # assert response.json()["success"] is True


import configparser
import pytest
import requests

config = configparser.RawConfigParser()
config.read('/home/ramesh/PycharmProjects/pytest_demo1/config.ini')
from pages.api_page import ExampleAPIPage


@pytest.fixture
def api_page():
    base_url = "https://cqube-qa-new.tibilprojects.com"
    return ExampleAPIPage(base_url)


def test_jwt_token(api_page):
    response = requests.get(config.get('config', 'base_url') + "/api/ingestion/generatejwt")
    assert response.status_code == 200


def test_dimension_api():
    response = requests.get(config.get('config', 'base_url') + "/api/new_programs")

    # response = api_page.get_data()
    # assert response.status_code == 200
    # assert "data" in response.json()
    # response_data = response.json()
    #
    # email_to_find = 'michael.lawson@reqres.in'
    # assert any(entry['email'] == email_to_find for entry in response_data['data'])
    #
    # print(response_data)
    # print(email_to_find)
