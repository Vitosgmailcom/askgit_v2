
from src.Helper.helperDB import HelperDB
from src.SQL_statements.SQL import SQLStatements

import pytest

class BaseTest:
    get_from_DB: HelperDB
    SQL: SQLStatements

    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.get_from_DB = HelperDB()
        request.cls.SQL = SQLStatements()


