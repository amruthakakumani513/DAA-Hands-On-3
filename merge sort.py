def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    return result
def MergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    return merge(left, right)
array = list(map(int,input().split(' ')))#[5, 9, 4, 7, 4, 2, 3, 6]
sorted_array = MergeSort(array)
print("Sorted array: ", sorted_array)
