def interactive_binary_search(l:list[int], x:int) -> bool:
    """ The interactive implemetation of binary search

        Args:
            l (list): sorted list of integers
            x (int): number to be search
        
        Return: 
            bool: If the number was found or not

        Time complexity: 
            O(log n)
    """
    find = False
    while find == False and len(l) > 0:    
        if x == l[len(l)//2]:
            find = True
        elif x > l[len(l)//2]:
            l = l[len(l)//2: ]
        elif x < l[len(l)//2]:
            l = l[ :len(l)//2+1]

    return find

def recursive_binary_search(l:list[int], x:int, s:int, e:int) -> bool:
    """ The recursive implemetation of binary search

        Args:
            l (list): sorted list of integers
            x (int): number to be search
            s (int): the start index of the list
            e (int): the index that indicates the end of the list
        
        Return: 
            bool: If the number was found or not

        Time complexity: 
            O(log n)
    """
    if e >= s:
        mid = (s + e)//2
        if x == l[mid]:
            return True
        elif x > l[mid]:
            return recursive_binary_search(l, x, x+1, e)
        elif x < l[mid]:
            return recursive_binary_search(l, x, s, x-1)
    else:
        return False
