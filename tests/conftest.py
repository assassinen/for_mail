import pytest

@pytest.yield_fixture
def entry_point(request):
    entry_points = {'docker': {'host': 'web', 'port': 5000},
                    'local': {'host': '127.0.0.1', 'port': 5000}}
    entry_point_name = request.config.getoption('--entry_point')
    yield entry_points.get(entry_point_name)

def pytest_addoption(parser):
    parser.addoption('--entry_point', action='store', default='docker')
