# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]

#         return quicksort(less) + [pivot] + quicksort(greater)
    
# print(quicksort([10, 5, 2, 3]))

# worst time complexity: O(n sqrt)
# average time complexity: O(n log n)


def partition(arr, low, high):
    pivot = arr[high]  # 选择最后一个元素作为枢轴
    i = low - 1       # 初始化 i 为 low - 1
    
    for j in range(low, high - 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素，将小于或等于枢轴的元素移到左侧
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 将枢轴放到正确的位置
    return i + 1  # 返回枢轴的最终位置

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # 找到枢轴位置
        quick_sort(arr, low, pi - 1)    # 递归排序左子数组
        quick_sort(arr, pi + 1, high)   # 递归排序右子数组

# 示例使用
arr = [7, 4, 9, 10, 1, 2, 1, 5, 5, 200]
quick_sort(arr, 0, len(arr) - 1)
print("排序后的数组:", arr)
