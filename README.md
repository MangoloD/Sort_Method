# Sort_Method

本章节实现的算法功能主要借鉴于 微信公众号：`裸睡的猪`，微信号：`IT--Pig`

首先用一张图了解下各排序方法的时间复杂度、空间复杂度及其稳定性：
![Image Text](https://github.com/MangoloD/Sort_Method/blob/master/images/all_sort.jpg?raw=true)

## 一、冒泡排序
冒泡排序（Bubble Sort）的原理是通过依次比较两个相邻的元素，将较大的值向后移动，最终完成排序。
### 1. 过程图解
![](https://github.com/MangoloD/Sort_Method/blob/master/images/bubble_sort.gif?raw=true)
### 2. 算法思想
1. 首先第一个元素和第二个元素开始比较，如果第一个元素比第二个大，则交换位置，以此类推...  
2. 经过一轮比较，最大的元素将排在最后一个位置，重复1中的操作，第二大的元素会排在倒数第二的位置，第三大的元素则会排在倒数第三个位置  
以此类推，我们只要重复n-1同样的操作即可完成排序。

## 二、选择排序
选择排序（Selection sort）的原理是每一次从需要排序的数据中选出最小或最大的元素，并将它放在序列的第一个位置。
### 1. 过程图解
![](https://github.com/MangoloD/Sort_Method/blob/master/images/selection_sort.gif?raw=true)
### 2. 算法思想
1. 首先我们将第一个元素设置为需要比较的元素，然后依次将后面的元素与它进行比较，如果比较的所有元素有比它小的元素，则交换位置。
2. 重复1中的操作，第二位置应该放第二小的元素，我们找到第二小的元素与第二个位置的元素进行位置交换，以此类推，找出每个位置的最小元素，完成排序。

## 三、插入排序
插入排序（Insertion-Sort）原理是构建有序序列，对于未排序的序列，在已排好的序列中从后向前扫描，找到相应位置并插入，以此完成排序。
### 1. 过程图解
![](https://github.com/MangoloD/Sort_Method/blob/master/images/insertion_sort.gif?raw=true)
### 2. 算法思想
1. 从所要比较的第二个元素开始和前面的元素进行比较，如果前面的元素比它大，则当前元素前移，直至找到比它小或等于它的元素停止前移
2. 依次选择到最后一个元素，完成所有排序

## 四、希尔排序
希尔排序(Shell’s Sort)是插入排序的一种，是直接插入排序算法的一种更高效的改进版本，它与插入排序的不同之处在于，它会优先比较距离较远的元素。
### 1. 过程图解
![](https://github.com/MangoloD/Sort_Method/blob/master/images/shell_sort.jpg?raw=true)
### 2. 算法思想
1. 设置一个增量（间隔）值
2. 对元素进行和增量元素（这两个元素在一个纵列）作比较，例如增量值为7，那么就对0,7,14...位置上的元素进行比较排序
3. 当第一组比较完后，比较第二组，即1,8,15...
4. 所有元素排完序后，缩小增量（间隔）值（缩小为原增量值的一半），重复上述操作
5. 当增量值为1时，数列基本排好序，最后一遍普通插入即可

已知的最增量式是由 Sedgewick 提出的 (1, 5, 19, 41, 109,…)，该步长的项来自 `9 4^i - 9 2^i + 1 和 4^i - 3 2^i + 1` 这两个算式。这项研究也表明 “比较在`希尔排序`中是最主要的操作，而不是交换。 用这样增量式的`希尔排序`比`插入排序`和`堆排序`都要快，甚至在小数组中比`快速排序`还快，但是在涉及大量数据时`希尔排序`还是比`快速排序`慢。

## 五、归并排序
归并排序（MERGE-SORT）主要采用分治法（Divide and Conquer），归并排序适用于子序列有序的数据排序。
### 1. 过程图解
![](https://github.com/MangoloD/Sort_Method/blob/master/images/merge_sort.jpg?raw=true)
### 2. 算法思想
分治法（Divide-and-Conquer）：将原问题划分成 n 个规模较小而结构与原问题相似的子问题；递归地解决这些问题，然后再合并其结果，就得到原问题的解。  
1. 使用递归将原数列采用二分法分成多个子数列
2. 将两个子序列合并并返回
3. 将所有子序列按2步骤合并并完成排序

## 六、快速排序
快排的实现方式多种多样，最简单易懂的是`分治+迭代`
## 1. 过程图解
![](https://github.com/MangoloD/Sort_Method/blob/master/images/quick_sort.jpg?raw=true)

一行代码实现快排：
```
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
```
## 2. 算法思想
1. 在数列之中，选择一个元素作为”基准”（pivot），或者叫比较值。
2. 数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右边
3. 以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。  

举个例子，假设我现在有一个数列需要使用快排来排序：{3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48}，我们来看看使用快排的详细步骤：  
1. 选取中间的26作为基准值（基准值可以随便选）  
2. 数列从第一个元素3开始和基准值26进行比较，小于基准值，那么将它放入左边的分区中，第二个元素44比基准值26大，把它放入右边的分区中，依次类推就得到下图中的第二列。  
3. 然后依次对左右两个分区进行再分区，得到下图中的第三列，依次往下，直到最后只有一个元素  
4. 分解完成再一层一层返回，返回规则是：左边分区+基准值+右边分区

## 七、 排序性能测试
### 1. 实验算法
冒泡排序、选择排序、插入排序、希尔排序、归并排序、快速排序
### 2. 数据集规模
随机生成一个数据集，可从小到大（10->100->1000...）
### 3.比较方法
比较每个排序算法所用时长，采用`随机数`、`基本有序`数据集进行排序
