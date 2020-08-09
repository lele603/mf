import pytest
import yaml

from code.calc import Calcu

with open("./datas/cal.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    adddata = datas['add']['adddata']
    addid = datas['add']['addid']
    subdata = datas['sub']['subdata']
    subid = datas['sub']['subid']
    muldata = datas['mul']['muldata']
    mulid = datas['mul']['mulid']
    divdata = datas['div']['divdata']
    divid = datas['div']['divid']


@pytest.fixture(scope="module")
def start():
    print("开始计算")
    calc = Calcu()
    yield calc
    print("结束计算")


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
