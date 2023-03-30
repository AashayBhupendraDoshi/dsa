import heapq
def medianSlidingWindow(nums, k):
    '''
    This is a two heaps based solution, wherein we maintain two heaps,
    max_heap and min_heap such that:
    1) Any value in max_heap is larger then the largest value in min_heap
    2) max_heap is a min heap sorting data in ascending order and 
        min_heap is a max heap storing data in descending order

    Aim is to add and remove elements from the heap such that the root element
    in both or either constitute the middle element/s 
    Space Complexity: O(N)
    Time Complexity: O(NlogK)
    '''
    max_heap, min_heap = [], []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    # Add k elements to minheap
    for i,j in enumerate(nums[:k]):
        heapq.heappush(min_heap, (-j,i))
        
    # Shift k//2 elements from minheap to maxheap
    for i in range(k-k//2):
        m,n = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-m,n))
    
    
    get_median = lambda: max_heap[0][0] if k % 2 else (-min_heap[0][0] + max_heap[0][0]) / 2

    output = [get_median()]
    for i, j in enumerate(nums[k:]):
        # print(max_heap, '////', min_heap)

        # Add elements based on value
        if j >= max_heap[0][0]:
            heapq.heappush(max_heap, (j, i+k))
            if nums[i] <= max_heap[0][0]:
                m,n = heapq.heappop(max_heap)
                heapq.heappush(min_heap, (-m,n))
        else:
            heapq.heappush(min_heap, (-j, i+k))
            if nums[i] >= max_heap[0][0]: 
                m,n = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-m,n))
        # Remove non-window root elements
        while min_heap and min_heap[0][1] <= i: 
            heapq.heappop(min_heap)
        while max_heap and max_heap[0][1] <= i: 
            heapq.heappop(max_heap)
        # Calculate median
        # print(max_heap, '////', min_heap)
        output.append(get_median())
    return output