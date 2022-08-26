def insertion_sort(l:list) -> list:
    """Insertion sort algorithm
        
        Args:
            l (list): list of integers
        
        Return:
            list: the sorted list
        
        Time Complexity:
            O(n²)
    """
    n = len(l)
    for i in range(1, n):
        pivot = l[i]
        j = i - 1 
        while j >= 0 and l[j] > pivot:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = pivot
