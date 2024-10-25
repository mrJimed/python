from main import my_sum_count


def test_my_sum_count():
    lst = [1, 2, 3, 4, 5]
    my_sum = sum([item for item in lst if item > 0 and item % 2 == 0])
    my_count = len([item for item in lst if item > 0 and item % 2 == 0])
    result = my_sum_count(lst)
    assert result['count'] == my_count and result['sum'] == my_sum
