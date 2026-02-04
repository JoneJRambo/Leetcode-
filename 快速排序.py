def quick_sort_basic(arr):
    """基础快速排序"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_basic(left) + middle + quick_sort_basic(right)


# 测试
arr = [64, 34, 25, 12, 22, 11, 90]
print("原数组:", arr)
print("排序后:", quick_sort_basic(arr.copy()))