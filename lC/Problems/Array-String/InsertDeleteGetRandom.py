

class RandomizedSet:

    #need self in every class method

    def __init__(self):
        self.vals = []
        self.vals_to_indices = {}

        
    def insert(self, val: int) -> bool:
        if val in self.vals_to_indices:
            return False
        self.vals_to_indices[val] = len(self.vals)
        self.vals.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.vals_to_indices:
            return False
        index = self.vals_to_indices[val]
        last_val = self.vals[-1]
        self.vals_to_indices[last_val] = index
        self.vals[index] = last_val
        self.vals.pop()
        del self.vals_to_indices[val]
        return True