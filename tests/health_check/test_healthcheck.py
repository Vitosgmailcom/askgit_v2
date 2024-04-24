
from tests.BaseTest import BaseTest

import pytest
import allure
import logging as log

@pytest.mark.healthcheck
class TestHealthCheck(BaseTest):

    @allure.title("Framework healthcheck")
    @pytest.mark.hc1
    def test_healthcheck(self):
        log.info("Running healthcheck")
        log.debug("Pass")

    @allure.title("DB connection healthcheck")
    @pytest.mark.hc2
    def test_db_connection_by_retriving_tandom_user(self):
        res_db = self.get_from_DB.get_random_user(self.SQL.get_random_user(), 1)
        assert res_db[0]['group'] == 'APG779'




