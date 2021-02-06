import os

import pytest

import ShiftSchedulerApi


@pytest.fixture
def client():
    config = {
        "SCHEDULER_CONFIG": {
            "PRODUCTION_DATABASE": {
                "TYPE": "mysql",
                "NAME": "test_scheduler",
                "HOST": "localhost",
                "PORT": 3306,
                "USER": "scheduleruser",
                "PASSWORD": "bM1stkriG"
            },
            "ADMIN_DATABASE": {
                "TYPE": "mysql",
                "NAME": "test_dbpanel",
                "HOST": "localhost",
                "PORT": 3306,
                "USER": "scheduleruser",
                "PASSWORD": "bM1stkriG"
            }
        }}
    with ShiftSchedulerApi.create_app(config) as app:
        with app.test_client() as client:
            yield client


def test_get_runs(client):
    rv = client.get("/scheduler/getRuns")
    assert 'asd' in rv
