# conftest.py

import pytest
from desafio_testesAutomatizados_Hipólito import app as flask_app 

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()