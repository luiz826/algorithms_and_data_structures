def selection_sort(l:list) -> list:
    """ Selection sort algorithm
        
        Args:
            l (list): list of integers
        
        Return:
            list: the sorted list
        
        Time Complexity:
            O(n²)
    """
    for i in range(len(l)):
        minor = l[i]
        id_m = i
        for j in range(i, len(l)):
            if l[j] < minor:
                minor = l[j]
                id_m = j
        
        l[i], l[id_m] = l[id_m], l[i]
        
    return l
