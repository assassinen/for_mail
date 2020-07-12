import requests
import pytest


cases = [
    (1, 'odd'),
    (2, 'even')
]
@pytest.mark.parametrize('value, result', cases,
                         ids=[f' test_value: {i[0]}  - result: {i[1]}' for i in cases])
def test_smoke_positive(entry_point, value, result):
    host = entry_point.get('host')
    port = entry_point.get('port')
    response = requests.get(f'http://{host}:{port}/{value}')
    assert response.status_code == 200
    assert result == response.text


cases = [
    ('s', 404),
    ('rm -f', 404),
    ('!@#$%^&*', 404),
]
@pytest.mark.parametrize('value, result', cases,
                         ids=[f' test_value: {i[0]}  - result: {i[1]}' for i in cases])
def test_smoke_negative(entry_point, value, result):
    host = entry_point.get('host')
    port = entry_point.get('port')
    response = requests.get(f'http://{host}:{port}/{value}')
    assert response.status_code == result
