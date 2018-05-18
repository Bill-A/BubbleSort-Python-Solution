import bubbleSort


def test_bubblesort_5470_58():
    """should return 58, 5470"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [5470, 58]
    assert bubble_sort.given(a_list) == [58, 5470]


def test_bubblesort_for_5470_58_19_60():
    """should return 19, 58, 60, 5470"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [5470, 58, 19, 60]
    assert bubble_sort.given(a_list) == [19, 58, 60, 5470]


def test_bubblesort_5470_58_19_60_1998_1960_1957():
    """should return 19, 58, 60, 1957, 1960, 1998, 5470"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [5470, 58, 19, 60, 1998, 1960, 1957]
    assert bubble_sort.given(a_list) == [19, 58, 60, 1957, 1960, 1998, 5470]



