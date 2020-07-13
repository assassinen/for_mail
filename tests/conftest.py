import pytest

@pytest.yield_fixture
def entry_point(request):
    entry_points = {'local': {'host': '127.0.0.1', 'port': 80},
                    'nginx': {'host': 'web', 'port': 80}}
    entry_point_name = request.config.getoption('--entry_point')
    yield entry_points.get(entry_point_name)

def pytest_addoption(parser):
    parser.addoption('--entry_point', action='store', default='docker')
