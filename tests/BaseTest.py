
from src.Helper.helperDB import HelperDB
from src.SQL_statements.SQL import SQLStatements
from src.Utility.requests import RequestsAPI
from src.Payloads.payloads import Payloads
from src.Endpoints.endpoints import Endpoints

import pytest

class BaseTest:
    get_from_DB: HelperDB
    SQL: SQLStatements
    API: RequestsAPI
    payloads: Payloads
    endpoint: Endpoints

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.get_from_DB = HelperDB()
        request.cls.SQL = SQLStatements()
        request.cls.API = RequestsAPI()
        request.cls.payloads = Payloads()
        request.cls.endpoints = Endpoints()


