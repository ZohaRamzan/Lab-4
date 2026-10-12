def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
# Main program
arr=[10,20,30,40,50,60,70]
target=int(input("Enter the element to search: "))
result=binary_search(arr, target)

if result==-1:
    print("Element not found")
else:
    print("Element found at index:",result)