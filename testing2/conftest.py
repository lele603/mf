import pytest
import yaml

from code.calc import Calcu

path = "./datas/caltest.yaml"


@pytest.fixture(scope="module")
def start():
    print("开始计算")
    calc = Calcu()
    yield calc
    print("结束计算")


@pytest.fixture(scope="module")
def setenv(cmdoption):
    print(cmdoption)
    global path
    if cmdoption == 'test':
        path = "./datas/caltest.yaml"
    elif cmdoption == 'dev':
        path = "./datas/caldev.yaml"
    elif cmdoption == 'st':
        path = "./datas/calst.yaml"
    return path


with open(path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    adddata = datas['add']['adddata']
    addid = datas['add']['addid']
    subdata = datas['sub']['subdata']
    subid = datas['sub']['subid']
    muldata = datas['mul']['muldata']
    mulid = datas['mul']['mulid']
    divdata = datas['div']['divdata']
    divid = datas['div']['divid']


@pytest.fixture(params=adddata, ids=addid)
def getadddata(request):
    data = request.param
    return data


@pytest.fixture(params=subdata, ids=subid)
def getsubdata(request):
    data = request.param
    return data


@pytest.fixture(params=muldata, ids=mulid)
def getmuldata(request):
    data = request.param
    return data


@pytest.fixture(params=divdata, ids=divid)
def getdivdata(request):
    data = request.param
    return data


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",
                      default="test",
                      dest="env",
                      help="set your run env")


@pytest.fixture(scope="session")
def cmdoption(request):
    return request.config.getoption("--env", default="test")
