def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 1
    max_length = 1
    length = 1
    prev = 0
    
    i = 0
    while i < len(A):
        if i == 0:
            prev = A[i]
            i += 1
            continue
        if (prev < A[i]):
            length += 1
            if length > max_length:
                max_length = length
                count = 1
            elif length == max_length:
                count += 1
        else:
            length = 1
        prev = A[i]
        i += 1
            
    return count
