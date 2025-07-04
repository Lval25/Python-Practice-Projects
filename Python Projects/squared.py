class Square():
    def __init__(self):
        pass

    def square(self, square):
        new_square = []
        for i in range(len(square)):
            sqr = square[i] ** 2
            new_square.append(sqr)
        new_square.sort()
        return new_square

    def soreted_squared(self, array):
        n = len(array)
        i,j = 0 , n-1
        res = [0]*n

        for k in reversed(range(n)):
            if array[i]**2 > array[j]**2:
                res[k] = array[i]**2
                i+=1
            else:
                res[k] = array[j]**2
                j-=1
        return res






sqr = Square()
#print(sqr.square([0,1,4,9,15,-17,-18,-19]))
print(sqr.soreted_squared([-3,2,-2,4,-5,6]))
