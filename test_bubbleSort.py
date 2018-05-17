import bubbleSort


def test_bubblesort_5470_58():
    """should return 58, 5470"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [5470, 58]
    assert bubble_sort.given(a_list) == [58, 5470]


def test_bubblesort_5470_58_19():
    """should return 58, 19, 5470"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [5470, 58, 19]
    assert bubble_sort.given(a_list) == [58, 19, 5470]


def test_bubblesort_misc_tests_for_first_iteration():
    """should return 1, 2, 3"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [1, 2, 3]
    assert bubble_sort.given(a_list) == [1, 2, 3]

    """should return 1, 3, 2"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [1, 3, 2]
    assert bubble_sort.given(a_list) == [1, 2, 3]

    """should return 58, 19, 60, 5470"""
    bubble_sort = bubbleSort.BubbleSort()
    a_list = [5470, 58, 19, 60]
    assert bubble_sort.given(a_list) == [58, 19, 60, 5470]


