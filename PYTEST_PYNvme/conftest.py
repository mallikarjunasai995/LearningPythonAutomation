import pytest

@pytest.fixture()
def example01(request):
    print('hi am in setup04 fucntion')
    print('\n fixture scope :-' + str(request.scope))
    print('\n calling function'+ str(request.function.__name__))
    print('\n calling module'+ str(request.module.__name__))
    yield 52





