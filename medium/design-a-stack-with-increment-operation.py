"""
1381. Design a Stack With Increment Operation
Design a stack which supports the following operations.
Implement the CustomStack class:
	• CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
	• void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
	• int pop() Pops and returns the top of stack or -1 if the stack is empty.
	• void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
"""

"""
Constraints:
	• 1 <= maxSize <= 1000
	• 1 <= x <= 1000
	• 1 <= k <= 1000
	• 0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.
"""

""" 
Example 1:
Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.

"""
import sys
import logging

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """        
        self.size = 0        
        self.stack = []
        self.maxSize = maxSize        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.size < self.maxSize:
        	self.stack.append(x)        	        	
        	self.size = self.size + 1

				return None
				        	        
    def pop(self):
        """
        :rtype: int
        """
        if not self.size:
        	return -1
        else:
        	self.size = self.size - 1
        	return self.stack.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """        
        if k < self.size:
            idx_list = self.findIdx(lambda e: e < self.stack[k])
        else:
        	idx_list = [i for i in range(self.size)]
            
        for idx in idx_list:
            self.stack[idx] = self.stack[idx] + val
		        	
        return None	
        
    def findIdx(self, cond):
    	"""
    	:type: lambda
    	:rtype: List[int]    	
    	"""
    	return [i for i, elem in enumerate(self.stack) if cond(elem)]
    	
        
        
def main():
		pass

if __name__ == "__main__":
    loggerTest = logging.getLogger("test")
    loggerTest.setLevel(logging.INFO) # DEBUG < INFO < WARNING < ERROR < CRITICAL  
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamHander = logging.StreamHandler()
    #streamHander.setFormatter(formatter)
    loggerTest.addHandler(streamHander)

    main()    
  