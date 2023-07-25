
import configparser
import logging

import pytest
import requests

# from Utilities import CustomLogger
# from Utilities.readproperties import ReadConfig

config = configparser.RawConfigParser()
config.read('/home/ramesh/PycharmProjects/pytest_demo1/config.ini')
from pages.api_page import ExampleAPIPage


@pytest.fixture
def api_page():
    base_url = "https://cqube-qa-new.tibilprojects.com"
    return ExampleAPIPage(base_url)


class TestAPI:
    # logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/Test_login.log",
    #                                    level=logging.DEBUG)

    def test_jwt_token(self):
        #self.logger.info("********TC1 testing of jwt token Started***********")
        response = requests.get(config.get('config', 'base_url') + "/api/ingestion/generatejwt")
        assert response.status_code == 200

    def test_schedule_api(self):
        request_body = {"processor_group_name": "Run Latest Code aws", "scheduled_at": "0 49 16 * * ?"}
        response = requests.post(config.get('config', 'base_url') + "/api/spec/schedule", json=request_body)
        assert response.status_code == 202

    def test_adapters(self):
        #self.logger.info("********TC testing Ended***********")
        request_body = {"processor_group_name": "Run_adapters", "scheduled_at": '0 39 16 * * ?'}
        response = requests.post(config.get('config', 'base_url') + "/api/spec/schedule", json=request_body)
        assert response.status_code == 200
