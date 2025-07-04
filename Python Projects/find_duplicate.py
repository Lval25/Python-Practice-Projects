# Find the duplicate in a list

class findDupe:
    def __init__(self, list):
        self.nums = list

    def finddupe(self):
        seen = set()
        for i in self.nums:
            if i in seen:
                return True
            seen.add(i)
            print(seen)
        return False


dupe = findDupe([1,2,3,3,4,5,6,7,7])
print(dupe.finddupe())
#print(dupe([1,2,3,3,4,5,6,7,7]))
