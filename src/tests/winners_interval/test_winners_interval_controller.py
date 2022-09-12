import importlib
import json
import os
import unittest
from pathlib import Path


class TestWinnersIntervalController(unittest.TestCase):

    def test_get_min_max_interval_when_min_max_len_is_correct(self):
        os.environ['CSV_FILE_PATH'] = str(Path("src/tests/resources/movielist.csv"))
        import app
        importlib.reload(app)

        response = app.flask_app.test_client().get(
            '/winnersinterval',
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert len(data['min']) == 1
        assert len(data['max']) == 1

    def test_get_min_max_interval_when_min_data_is_correct(self):
        os.environ['CSV_FILE_PATH'] = str(Path("src/tests/resources/movielist.csv"))
        import app
        importlib.reload(app)

        response = app.flask_app.test_client().get(
            '/winnersinterval',
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['min'][0]['followingWin'] == 1991
        assert data['min'][0]['previousWin'] == 1990
        assert data['min'][0]['interval'] == 1
        assert data['min'][0]['producer'] == 'Joel Silver'

    def test_get_min_max_interval_when_max_data_is_correct(self):
        os.environ['CSV_FILE_PATH'] = str(Path("src/tests/resources/movielist.csv"))
        import app
        importlib.reload(app)

        response = app.flask_app.test_client().get(
            '/winnersinterval',
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['max'][0]['followingWin'] == 2015
        assert data['max'][0]['previousWin'] == 2002
        assert data['max'][0]['interval'] == 13
        assert data['max'][0]['producer'] == 'Matthew Vaughn'

    def test_with_2_equals_max_intervals_of_same_producer(self):
        os.environ['CSV_FILE_PATH'] = str(
            Path("src/tests/resources/movielistwith2equalsmaxintervalofsameproducer.csv")
        )
        import app
        importlib.reload(app)

        response = app.flask_app.test_client().get(
            '/winnersinterval',
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert len(data['max']) == 2
        assert data['max'][0]['producer'] == 'Matthew Vaughn'
        assert data['max'][1]['producer'] == 'Matthew Vaughn'
