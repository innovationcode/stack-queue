Stack and Queue both are Linear data structures.
- In the linear data structure, the data is organized in a linear order in which elements are linked one after the other.
- The traversing of data in the linear data structure is easy as it can make all the data elements to be traversed in one go, but at a time only one element is directly reachable.<br>

## Stack
- A stack is a linear data structure in which elements can be inserted and deleted only from one side of the list, called the top. A stack follows the LIFO (Last In First Out) principle, i.e., the element inserted at the last is the first element to come out.

### The Stack operations are
- ```Stack()``` creates a new stack that is empty. It needs no parameters and returns an empty stack.
- ```push(item)``` adds a new item to the top of the stack. It needs the item and returns nothing.
- ```pop()``` removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
- ```peek()``` returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
- ```isEmpty()``` tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
- ```size()``` returns the number of items on the stack. It needs no parameters and returns an integer.


## Queue
- A queue is a linear data structure in which elements can be inserted only from one side of the list called rear, and the elements can be deleted only from the other side called the front. The queue data structure follows the FIFO (First In First Out) principle, i.e. the element inserted at first in the list, is the first element to be removed from the list. 