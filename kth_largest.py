def kth_largest(a, k):
    k = len(a) - k
    
    def quick_select(left, right):
        pivot, p = a[right], left
        for i in range(left, right):
            if a[i] <= pivot:
                a[i], a[p] = a[p], a[i]
                p += 1
        a[p], a[right] = a[right], a[p]
        
        if p > k: return quick_select(left, p - 1)
        elif p < k: return quick_select(p + 1, right)
        else: return a[p]
        
    return quick_select(0, len(a) - 1)