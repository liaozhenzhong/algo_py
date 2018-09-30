import pytest
from rod_cutting import *


@pytest.fixture
def price_list():
    price_list = [0] * 10
    price_list[1] = 1
    price_list[2] = 3
    price_list[4] = 7
    price_list[8] = 15
    return price_list


def test_bottom_up(price_list):
    bottom_up(price_list)
    print(price_list)


def test_top_down(price_list):
    print(top_down(9, price_list))
