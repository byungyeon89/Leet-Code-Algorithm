

"""
1551. Minimum Operations To Make Array Equal

You Have An Array Arr Of Length N Where Arr[I] = (2 * I) + 1 For All Valid Values Of I (I.E. 0 <= I < N).
In One Operation, You Can Select Two Indices X And Y Where 0 <= X, Y < N And Subtract 1 From Arr[X] And Add 1 To Arr[Y] (I.E. Perform Arr[X] -=1 And Arr[Y] += 1). The Goal Is To Make All The Elements Of The Array Equal. It Is Guaranteed That All The Elements Of The Array Can Be Made Equal Using Some Operations.
Given An Integer N, The Length Of The Array. Return The Minimum Number Of Operations Needed To Make All The Elements Of Arr Equal.
"""

"""
Constraints:
1 <= N <= 10^4
"""

"""
Example 1:
Input: N = 3
Output: 2
Explanation: Arr = [1, 3, 5]
First Operation Choose X = 2 And Y = 0, This Leads Arr To Be [2, 3, 4]
In The Second Operation Choose X = 2 And Y = 0 Again, Thus Arr = [3, 3, 3].
Example 2:
Input: N = 6
Output: 9

"""
Import Sys
Import Logging

Class Solution(Object):
    Def Minoperations(Self, N):
        """
        :Type N: Int
        :Rtype: Int
        """              			
        	
        Arr =	[2*I+1 For I In Range(N)]        
        Arr = List(Map(Lambda X: Abs(X-N), Arr))
        	
        Return Int(Sum(Arr)/2)
        
        
Def Main():

    S = Solution()

    Test_Cases = [
        3,					# 1
        6,					# 2
        4,					# 3       
        ]	

    For I, Test In Enumerate(Test_Cases):
        Print("[%D]"% (I + 1))
        Print("Input: ", Test)
        Print("Output:", S.Minoperations(Test))
        Print('\N')

If __Name__ == "__Main__":
    Loggertest = Logging.Getlogger("Test")
    Loggertest.Setlevel(Logging.Info) # Debug < Info < Warning < Error < Critical  
    #Formatter = Logging.Formatter('%(Asctime)S - %(Name)S - %(Levelname)S - %(Message)S')

    Streamhander = Logging.Streamhandler()
    #Streamhander.Setformatter(Formatter)
    Loggertest.Addhandler(Streamhander)

    Main()    
  