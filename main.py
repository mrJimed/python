def my_sum_count(lst: list[int]) -> dict[str, int]:
    result = [item for item in lst if item > 0 and item % 2 == 0]
    return {
        'count': len(result),
        'sum': sum(result)
    }

# flake 8
# git actions
#
