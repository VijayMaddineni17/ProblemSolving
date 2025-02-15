'''
Given an array of integers greater than zero, determine if it is possible to
split it in two sub-arrays (without reordering the elements of the original array), 
such that the sum of the values in each of the two resulting sub-arrays is the same. 
Return true if possible, otherwise return false.
In: can_partition ( [5, 2, 31)
(151, (2, 31)
Out [1]: - True
In: can_partition((1, 1, 3])
Out [3]: • False
'''


class compareSubArraySum:
    def __init__(self,arr:list):
        self.arr=arr
        self.total_sum=sum(arr)
        
    
    def validate(self):
        if self.total_sum%2!=0:
            return False
        target=self.total_sum//2
        prefix_sum=0
        for num in self.arr:
            prefix_sum+=num
            
            if prefix_sum==target:
                return True
        
        return False


class TestSubArraySum:
    def test_cases(self):
        arr1 = [5, 2, 31]
        test1 = compareSubArraySum(arr1)
        assert test1.validate() == False, f"Test failed for {arr1}"

        arr2 = [1, 1, 3]
        test2 = compareSubArraySum(arr2)
        assert test2.validate() == False, f"Test failed for {arr2}"

      
        arr3 = [1, 2, 3, 4, 5, 5]
        test3 = compareSubArraySum(arr3)
        assert test3.validate() == True, f"Test failed for {arr3}"

        
        arr4 = [10]
        test4 = compareSubArraySum(arr4)
        assert test4.validate() == False, f"Test failed for {arr4}"

        arr5=[]
        test5 = compareSubArraySum(arr5)
        assert test5.validate() == False, f"Test failed for {arr5}"

        print("All tests passed!")


test = TestSubArraySum()
test.test_cases()
        
            
            
    