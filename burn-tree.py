# #User function Template for python3

# class Depth:
#     def __init__(self, d: int):
#         self.d = d

# class Solution:
#     def minTime(self, root, target):
#         ans = -1
#         dp = Depth(-1)
#         self.burn(root, target, dp)
#         return ans
    
#     def burn(self, root, target, depth):
#         if root is None:
#             return 0
#         if root.data == target:
#             depth.d = 1
#             return 1
#         ld = Depth(-1)
#         rd = Depth(-1)
        
#         lh = self.burn(root.left, target, ld)
#         rh = self.burn(root.right, target, rd)
        
#         if ld.d != -1:
#             ans = max(ans, ld.d + 1 + rh)
#             depth.d = ld.d + 1
#         if rd.d != -1:
#             ans = max(ans, rd.d + 1 + lh)
#             depth.d = rd.d + 1
#         return max(lh, rh) + 1
            


# #{ 
# #  Driver Code Starts
# #Initial Template for Python 3

# from collections import deque

# # Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

# # Function to Build Tree   
# def buildTree(s):
#     #Corner Case
#     if(len(s)==0 or s[0]=="N"):           
#         return None
        
#     # Creating list of strings from input 
#     # string after spliting by space
#     ip=list(map(str,s.split()))
    
#     # Create the root of the tree
#     root=Node(int(ip[0]))                     
#     size=0
#     q=deque()
    
#     # Push the root to the queue
#     q.append(root)                            
#     size=size+1 
    
#     # Starting from the second element
#     i=1                                       
#     while(size>0 and i<len(ip)):
#         # Get and remove the front of the queue
#         currNode=q[0]
#         q.popleft()
#         size=size-1
        
#         # Get the current node's value from the string
#         currVal=ip[i]
        
#         # If the left child is not null
#         if(currVal!="N"):
            
#             # Create the left child for the current node
#             currNode.left=Node(int(currVal))
            
#             # Push it to the queue
#             q.append(currNode.left)
#             size=size+1
#         # For the right child
#         i=i+1
#         if(i>=len(ip)):
#             break
#         currVal=ip[i]
        
#         # If the right child is not null
#         if(currVal!="N"):
            
#             # Create the right child for the current node
#             currNode.right=Node(int(currVal))
            
#             # Push it to the queue
#             q.append(currNode.right)
#             size=size+1
#         i=i+1
#     return root

# if __name__=="__main__":
#     t=int(input())
#     for _ in range(t):
#         line=input()
#         target=int(input())
#         root=buildTree(line)
#         print(Solution().minTime(root,target))

# # } Driver Code Ends