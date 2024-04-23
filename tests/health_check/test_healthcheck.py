
import pytest
import allure
import logging as log

@pytest.mark.health_check
def test_healthcheck():
    log.info("Running healthcheck")



