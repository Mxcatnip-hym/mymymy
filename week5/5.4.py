def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2
#希尔排序的时间复杂度取决于选取的步长序列。对于最坏情况的时间复杂度为O(n^2)，但在实际应用中，希尔排序通常表现得比其它O(n^2)的排序算法更快，因为它在一开始就通过步长的设置使得数组的大部分元素有序。希尔排序的平均时间复杂度依赖于步长序列的选择。一些步长序列的平均时间复杂度可以达到O(n log^2 n)。空间复杂度是O(1)，因为希尔排序是一种原地排序算法，它只需要常数级别的额外空间来存储临时变量。
