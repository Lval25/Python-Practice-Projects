#Print the indices of the two numbers who sum equal
class Twosum:
    def __init__(self):
        self.nums = []
        self.target = 5

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        print(n)
        for i in range(n):
            for j in range(i, n):
                sum = i + j
                if sum == target:
                    return i, j
                

    
    def twoosumm(self, nums: list[int], target: int) -> list[int]:
        values = []
        for i , val in enumerate(nums):
            targ = target - val
            print(targ)
            # Check if the current value is in the new list
            if val not in values:
                values.append(val)
            # Check if the value in the list minus the current value equals the target
            elif targ in values:
                return val, targ[val]
        return values
        #print(values)

two = Twosum()
#print(two.twoSum([1,2,3,4,5,6,7,8,9], 10))
print(two.twoosumm([1,2,3,4,5,6,7], 10))
