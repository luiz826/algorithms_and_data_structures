def linear_search(l:list[int], x:int) -> bool:
    """ Linear search algorithm
    
        Args:
            l (list): list of numbers
            x (int): number to be found
        
        Return:
            bool: If the number was found or not

        Time Complexity:
            O(n)
    """
    for i in range(len(list)):
        if l[i] == x:
            return True
    
    return False