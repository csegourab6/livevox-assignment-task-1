import pytest
import os

@pytest.fixture()
def ASGName():
    try:
        TestASGName= os.environ['TestASGName']
        if(TestASGName==""):
            return None
        return TestASGName
    except Exception:
        return None
