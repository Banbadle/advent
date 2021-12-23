import json
with open("input.txt") as f:
    snailfish_list = [json.loads(line) for line in f]
       
    

class Pair():
    def __init__(self, parent=None, parent_index=None):
        self.parent = parent
        self.parent_index = parent_index # 0 left, 1 right
        self.level = (1 if parent == None else parent.level + 1)
        
    def set_vals(self, a,b):
        self.vals = [a,b]
        
    def explode(self):
        print(self.level)
        a,b = self.vals
        if type(a) == Pair: a.explode()
        if type(b) == Pair: b.explode()
        if self.level >= 4:
            print(a,b)
            self.explode_left(a)
            self.explode_right(b)
            self.parent.vals[self.parent_index] = 0
            
        return self
            
    def explode_left(self, a):          
        curr_node = self
        while curr_node.parent_index == 0:
            curr_node = curr_node.parent
            if curr_node == None:
                return                   #If head of tree, stop 
            
        if curr_node == None:
            return

        curr_node = curr_node.parent
        
        if curr_node == None:
            return
        
        if type(curr_node.vals[0]) != int:
            curr_node = curr_node.vals[0]
            while type(curr_node.vals[1]) != int:
                curr_node = curr_node.vals[1]
            curr_node.parent.vals[1] += a
        else:
            curr_node.vals[0] += a
    
    def explode_right(self,b):
        curr_node = self 
        while curr_node.parent_index == 1:
            curr_node = self.parent
 
        if curr_node == None:
            return                       #If head of tree, stop   
        curr_node = curr_node.parent
        
        if type(curr_node.vals[1]) != int:
            curr_node = curr_node.vals[1]
            while type(curr_node.vals[0]) != int:
                curr_node = curr_node.vals[0]
            curr_node.vals[0] += b
        else:
            curr_node.vals[1] += b
    
    def magnitude(self):
        a,b = self.vals
        if type(a) == Pair: a = a.magnitude()
        if type(b) == Pair: b = b.magnitude()
        
        return 3*a + 2*b
    
    def __str__(self):
        return f"[{self.vals[0]}, {self.vals[1]}]"

def tree_from_list(pair_list, parent=None, parent_index=None):
    new_pair = Pair(parent, parent_index)
    a,b = pair_list
    if type(a) == list: a = tree_from_list(a, new_pair, 0)
    if type(b) == list: b = tree_from_list(b, new_pair, 1)
    new_pair.set_vals(a,b)
    return new_pair
    
        
def get_split(n):
    return(int(n/2), int(n/2+0.5))

def explode(snailfish, level=0):
        
    a, a_add = snailfish[0], [0,0] if type(snailfish[0]) == int else explode(snailfish[0], level+1)
    b, b_add = snailfish[1], [0,0] if type(snailfish[1]) == int else explode(snailfish[1], level+1)
    
    snailfish[0] = a + b_add[0]
    snailfish[1] = b + a_add[1]
    
    if level >= 4: 
        return 0, snailfish
    else:
        return snailfish, [0,0]
    
tree = tree_from_list([[[[[9,8],1],2],3],4])
print(tree.explode())