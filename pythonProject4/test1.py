def sum_numbers(a:int, b:int) -> int:
    return a+b

def test_sum_numbers():
    a= 2
    b=4

    result = sum_numbers(a, b)

    assert result == 6
