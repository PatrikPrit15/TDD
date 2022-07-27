import pytest, random
# from faker import Faker



def fn(x):
    return x*2


@pytest.mark.parametrize("i",[(2,4),(4,8),(54,108)])
def test1(i):
    assert fn(i[0])==i[1]

def testr():
    for i in range(10000):
        assert fn(i)==i*2