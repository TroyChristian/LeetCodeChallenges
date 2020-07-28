


class ListNode:
   def __init__(self, val=0, next_node=None):
       self.val = val
       self.next = next_node

   def add_Node(self, new_node_val, new_node):
        if self.next == None:
            self.next = new_node

   def link_nodes(self, listNode):
      self.next = listNode

   # FirstList = ListNode(2,ListNode(4, ListNode(3,None)))



class Solution:
   def traverseLinkedList(self, ListNode, array):
      tailFound = False
      tail = 0
      while not tailFound:
         array.append(ListNode.val)
         if ListNode.next != None:
            ListNode = ListNode.next
         if ListNode.next == None:
            tailFound = True
            tail = ListNode.val
            array.append(tail)
            
         
   
      
   def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      FirstListNumbers = []
      SecondListNumbers = []

      
      self.traverseLinkedList(l1, FirstListNumbers)
      

      self.traverseLinkedList(l2, SecondListNumbers)
      

      FirstListNumbers = [i for i in reversed(FirstListNumbers)]
      SecondListNumbers = [i for i in reversed(SecondListNumbers)]
     

      firstListLetterString = ""
      secondListLetterString = ""
      for i in FirstListNumbers:
         firstListLetterString += str(i)

      FirstListNumberInteger = int(firstListLetterString)# number representing the nodes of the l1, reversed and has one number. 

      for i in SecondListNumbers:
         secondListLetterString += str(i) 

      SecondListNumberInteger = int(secondListLetterString) # number representing the nodes of the l2, reversed and has one number.

      sumOfNodes = FirstListNumberInteger + SecondListNumberInteger
      print(sumOfNodes)

      stringSumOfNodes = str(sumOfNodes) #cast to string so I can iterate over it.
      ListSumOfNodes = []
      for i in stringSumOfNodes:
         ListSumOfNodes.append(int(i))
      ListSumOfNodes = [i for i in reversed(ListSumOfNodes)]

      print(ListSumOfNodes)

      # Put  stringSumOfNodes elements into an array as int into ListSumOfNodes
      # Create ListOfNewNodes array
      # Turn elements of ListSumOfNodes into ListNodes
      #append those ListNodes to ListOfNewNodes Array

      # link the nodes inside listOfNewNodes together up to the penultimate value using linkNode function
      # append the tail ListOfNewNodes[-2].link_node(tail) # Make the tail the next value of the penultimate node.

      listOfNewNodes = []
      for i in ListSumOfNodes:
        newNode =  ListNode(i,None)
        listOfNewNodes.append(newNode)

      

      tail = listOfNewNodes[-1]
      
                            
       
   
      n= 0
      for i in listOfNewNodes[0:2]: #ListNode(8:None), ListNode(0,None), ListNode(7:None) 
            
            
            i.link_nodes(listOfNewNodes[n + 1]) # might make appending tail redundant
            if n == 0:
               ResultListNode = ListNode(i.val, i.next)
            if n > 0:
               ResultListNode.add_Node(i.val, i.next)
            
            
           
            n += 1
      print(ResultListNode.val, ResultListNode.next.val, ResultListNode.next.next.val)
    
      
      return ResultListNode

      
            
           

      
      


         

      
      

      
         
        
# Iterate over the linked list, and store each value found in an array.
# Reverse the arrays 
# Convert them into integer values
#add them together
# For the resulting x digit number, each digit will become the value of a ListNode
# We will iterate backwords over the array and assign each digit as a value in a listNode until it is empty

#Return that ListNode

FirstList = ListNode(2,ListNode(4, ListNode(3,None)))
SecondList = ListNode(5,ListNode(6, ListNode(4,None)))

mySolution = Solution()
mySolution.addTwoNumbers(FirstList, SecondList)

