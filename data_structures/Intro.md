# Intro to Data Structures.

#### A Data Structure is a way to store and organize data in a computer, so that it can be used efficiently.
_Abstract data Types/Mathematical models_<br>
_Implementation._
  
### List (ADT)
 - Store a given number of elements of given data-type.(or mixed)
   - Add 0(n)
 - Write/Modify element at a position.
   - Insert O(n)
   - Remove O(n)
 - Read element at a position.
   - Access O(1)
   
### Array V/s Linked List   
 |--|Array|Linked List|
 |-----|----|-----|
 | Cost of Accessing an Element| Constant time O(1)|Linear time O(n)| 
 | Memory Requirements| - Fixed Size(if not Dynamic)<br> - Memory may not be available as one large block| - No unused memory/ extra memory for pointer variables<br> - Memory may be available as multiple small blocks|
 |Cost of Inserting an element|1) At Beginning - O(n) <br> 2) At End - O(1) 'if array is not full' <br> 3) At ith Position - O(n) |O(1) <br> O(n) <br> O(n)|
 |Ease of Use| Yeah| A bit Messy|
 
 
