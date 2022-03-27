import pytest

@pytest.fixture()
def example01(request):
    print('hi am in setup04 fucntion')
    print('\n fixture scope :-' + str(request.scope))
    print('\n calling function'+ str(request.function.__name__))
    print('\n calling module'+ str(request.module.__name__))
    yield 52


# commandlineoptions

def pytest_addoption(parser):
    parser.addoption(
        "--pciaddr", action="store", default="", help="pci (BDF) address of the device under test, e.g.: 0000:01:00.0"
    )




