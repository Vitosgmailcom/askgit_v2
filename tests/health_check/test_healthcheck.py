
import pytest
import allure
import logging as log

@pytest.mark.healthcheck
def test_healthcheck():
    log.info("Running healthcheck")



