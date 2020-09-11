# Sort_Method

本章节实现的算法功能主要借鉴于 微信公众号：`裸睡的猪`，微信号：`IT--Pig`

首先用一张图了解下各排序方法的时间复杂度、空间复杂度及其稳定性
![Image Text](https://github.com/MangoloD/Sort_Method/blob/master/images/all_sort.jpg?raw=true)
## 一、冒泡排序
冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。它主要通过依次比较两个相邻的元素，将较大的值向后移动。
### 1. 过程图解
![](https://github.com/MangoloD/Sort_Method/blob/master/images/bubble_sort.gif?raw=true)
### 2. 算法思想
1. 首先第一个元素和第二个元素开始比较，如果第一个元素比第二个大，则交换位置，以此类推...  
2. 经过一轮比较，最大的元素将排在最后一个位置，重复1中的操作，第二大的元素会排在倒数第二的位置，第三大的元素则会排在倒数第三个位置  
以此类推，我们只要重复n-1同样的操作即可完成排序。
### 3. 代码实现
![](https://github.com/MangoloD/Sort_Method/blob/master/sort_.py)

