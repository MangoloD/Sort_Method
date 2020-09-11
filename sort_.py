arr_list = [5, 1, 4, 9, 23, 18, 56]


def bubble_sort(arr):
    """冒泡排序"""
    # 第一层表示循环层数
    for i in range(len(arr) - 1):
        # 第二层表示具体比较那两个元素
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # 如果前面的大于后面的，则交换位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort(arr_list))


def selection_sort(arr):
    """选择排序"""
    # 第一层表示循环的次数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小值
        min_index = i
        # 第二层表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 如果当前元素比最小值小，则把当前元素下标设置为最小值下标
                min_index = j
        # 查找一遍后，将最小值与初始元素交换位置
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(selection_sort(arr_list))


def insertion_sort(arr):
    """插入排序"""
    # 第一层表示循环插入的次数
    for i in range(1, len(arr)):
        # 设置当前需要插入的元素
        element = arr[i]
        # 与当前元素进行比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > element:
            # 当比较元素大于当前元素，交换位置，后移比较元素
            arr[pre_index + 1] = arr[pre_index]
            # 向前选择下一个比较元素
            pre_index -= 1
        # 当比较元素小于当前元素，则将当前元素插在其后面
        arr[pre_index + 1] = element
    return arr


print(insertion_sort(arr_list))


def shell_sort(arr):
    """希尔排序"""
    # 取整计算增量（间隔）值
    gap = len(arr) // 2
    while gap > 0:
        # 从增量值开始遍历比较
        for i in range(gap, len(arr)):
            j = i
            element = arr[i]
            # 元素与其他同列的前面每个元素比较，如果比前面小则互换
            while j - gap > 0 and element < arr[j - gap]:
                arr[j] = arr[j - gap]
                arr[j - gap] = element
            #     j -= gap
            # arr[j] = element
        # 缩小增量（间隔）值
        gap //= 2
    return arr


print(shell_sort(arr_list))


def merge_sort(arr):
    """归并排序"""
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分为两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算
    return marge(merge_sort(left), merge_sort(right))


def marge(left, right):
    """排序合并两个数列"""
    result = []
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    return result


new_arr_list = [100, 6, 7, 50]
x = marge(arr_list, new_arr_list)
print(merge_sort(x))


def quick_sort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    # 选取基准，任意挑选，这里选择中间的数
    mid = arr[len(arr) // 2]
    # 定义基准左右两侧数列
    left, right = [], []
    # 从原始数据中移除基准数值
    arr.remove(mid)
    for element in arr:
        # 大于等于基准值放右边，小于放左边
        if element >= mid:
            right.append(element)
        else:
            left.append(element)
    # 采用迭代的方式进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


arr_list = [5, 1, 4, 9, 23, 18, 56]
print(quick_sort(arr_list))

# # 一行代码实现快排
# quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
#     [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
#     [item for item in array[1:] if item > array[0]])
#
# print(quick_sort(arr_list))
