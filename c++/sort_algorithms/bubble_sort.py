def bubble_sort(l:list[int]) -> list:
    """ Blubble sort algorithm

        Args:
            l (list): list of integers
        
        Return:
            list: the sorted list

        Time Complexity:;
            O(n²)
    """
    for i in range(len(l)):
        bigger = 0
        id_b = 0
        for j in range(len(l)-i):
            if l[j] >= bigger:
                bigger = l[j] 
                id_b = j
    
        l[j], l[id_b] = l[id_b], l[j]            
        
    return l
