import bubbleSort


def test_bubble_sort_list_of_2_1():
    """should return 1, 2"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [2, 1]
    assert bubble_sort.given(a_list) == [1, 2]

