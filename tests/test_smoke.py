import requests
import pytest

host = '0.0.0.0'
port = 5000

cases = [
    (1, 'нечетное'),
    (2, 'четное')
]
@pytest.mark.parametrize('value, result', cases,
                         ids=[f' test_value: {i[0]}' for i in cases])
def test_smoke_positive(value, result):
    response = requests.get(f'http://{host}:{port}/{value}')
    assert response.status_code == 200
    assert result == response.text


cases = [
    ('s', 404),
    ('rm -f', 404),
    ('!@#$%^&*', 404),
]
@pytest.mark.parametrize('value, result', cases,
                         ids=[f' test_value: {i[0]}' for i in cases])
def test_smoke_negativ(value, result):
    response = requests.get(f'http://{host}:{port}/{value}')
    assert response.status_code == result
