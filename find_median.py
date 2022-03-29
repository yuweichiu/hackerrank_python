def findMedian(arr):
    # Write your code here
    # sorted = False
    # while sorted == False:
    #     non_sorted_cnt = 0
    #     for i in range(len(arr)-1):
    #         if arr[i] > arr[i+1]:
    #             tmp = arr[i+1]
    #             arr[i+1] = arr[i]
    #             arr[i] = tmp
    #             non_sorted_cnt += 1
    #     if non_sorted_cnt != 0:
    #         sorted = False
    #     else:
    #         sorted = True
    arr.sort()        
    median_id = int((len(arr)-1)/2)
    
    return arr[median_id]

findMedian(arr=[5, 3, 1, 4, 2])