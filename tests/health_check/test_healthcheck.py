
import pytest
import allure
import logging as log

@allure.title("Health Check")
@pytest.mark.healthcheck
def test_healthcheck():
    log.info("Running healthcheck")



