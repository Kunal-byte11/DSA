class Solution :
    def quicksort(self,arr,low,high):
        if low < high :
            p_index = self.partition(arr, low ,high)

            self.quicksort(arr,low,p_index-1)
            self.quicksort(arr,p_index+1,high)

    def partition(self , arr, low, high):
        pivot = arr[low]
        i = low
        j = high


        while i < j:
            while i <= high - 1 and arr[i] <=pivot:
                i+=1

            while j >=low+1 and arr[j] > pivot:
                j-=1

            if i < j :
                arr[i] , arr[j] = arr[j] , arr[i]

        arr[low] , arr[j] = arr[j] , arr[low]

        return j