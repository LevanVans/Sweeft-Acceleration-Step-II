import unittest


def bigger_is_greater(w: str):
    
    # Change w type to list , because str object does not support item assigment 
    w = list(w)
    last_index = len(w) - 1
    
    # First find where order becames asc
    first = last_index

    while first > 0 and w[first] <= w[first-1]:
        first -= 1
        
    
    # if order is fully desc , 'first' will get equal to 0 , that means we cant arrange anaything
    
    if first == 0:
        return "no answer"

    """
     If return statement not completed , we found 2 indexes where order becames asc
     Now lets find bigger than w[first-1]'s index , still startig from the end 
     In  w[first:]  we have desc order  so the first found one will be smallest 
    """
    
    second = last_index 
    
    while second > 0 and w[second] <= w[first-1]:
        second -= 1 
        

    #Now swap places , after what we still get desc order in w[first:]  
    w[first-1], w[second] = w[second],w[first-1]
    
    # Now replace w[first:] with reversed w[first:] , which will be aranged asc , so will be smaller one 
    
    w[first:] = list(reversed(w[first:]))
    
    return "".join(w)
    

class TestBiggerIsGreater(unittest.TestCase):

    def test_word(self):
        T = int(input("T: "))
        output = str(T) + " "
        for i in range(T):
            w = input("w: ")
            output += bigger_is_greater(w) + " "
    
        print(output)
            
if __name__ == "__main__":
    
    unittest.main()