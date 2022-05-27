import pytest


# @pytest.mark.parametrize("inp, out",[(2,4),(3,28),(4,256)])
# def test_param01(inp,out):
#     assert (inp**inp) == out

#parameterizing the fixtures : 

@pytest.fixture(params = [(3,4),[3,5]])
def fixture01(request):
    print('calling function '+ str(request.scope))
    return request.param


def test_fix_params01(fixture01):
    assert (type(fixture01)) in [tuple,list]