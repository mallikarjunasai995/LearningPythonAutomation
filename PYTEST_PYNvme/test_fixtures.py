import pytest
def test_checkrequest(example01):
    #https://pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html
    assert 1 == 1
# #fixtures are nothing but functions to prepare input data, functions
# @pytest.fixture()
# def setup_list():
#     print('in fixtures \n')
#     city = ['nellore','ongole']
#     return city

# def main_func(setup_list):
#     print('just took the input of setup list fixure in this function')


#usefixture - won't use the fixture at all

# weekday1 = ['mon','tue','wed']
# weekday2 = ['sun','fri','sat']

# @pytest.fixture()
# def setup01():
#     weekday1.append('thu')
#     yield weekday1  #return the object to the function 
#     print(weekday1)
#     weekday1.pop('thu')  #teardown method - where we added the thursday and removed in this step

# def test_extendlist(setup01):
#     setup01.extend(weekday2)
#     assert setup01 == ['mon','tue','wed','thu','sun','fri','sat']

