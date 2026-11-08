from codes.bubble_sort_23 import bubble_sort

def test_unsorted_list(): assert bubble_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]

def test_already_sorted_list(): assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse_sorted_list(): assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_empty_list(): assert bubble_sort([]) == []

def test_duplicates(): assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]

def test_original_list_unchanged(): 
    numbers = [4, 2, 1] 
    bubble_sort(numbers) 
    assert numbers == [4, 2, 1]