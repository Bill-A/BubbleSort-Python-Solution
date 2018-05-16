import bubbleSort


def test_bubble_sort_list_of_5470_58():
    """should return 58, 5470"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [5470, 58]
    assert bubble_sort.given(a_list) == [58, 5470]

