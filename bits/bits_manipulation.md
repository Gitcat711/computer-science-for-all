### Binary
> There are 10 types of people, One who understand Binary and One who doesn't.

#### The Basics
- **Binary numbers** (or **base-2**) only use two values,0 and 1. So binary digit columns increase by 2 times (_1s, 2s, 4s_).

- Binary numbers are nice for computers because they can easily be expressed as series of bits, which only have two states (think of them as "on" or "off", "open" or "closed", or 000 or 111).  

- Here are the base-10 numbers 0 through 10 in _binary_.

|Binary|Decimal|
|---|--|---|
|0|0000|
|1|0001|        
|2|0010|
|3|0011|
|4|0100|
|5|0101|
|6|0110|
|7|0111|
|8|1000|
|9|1001|
|10|1010|

#### Negative numbers
 - TODO


#### Bitwise AND (&)
   **AND :** Only _True_ if both the inputs are `True(or 1)`

  |Input1|Input2|Result|
  |---|--|-------|
  |0|0| 0|
  |0|1| 0|
  |1|0| 0|
  |1|1| 0|

  ```
    10101110 - Input 1
  &  
    01100101 - Input 2
    ---------
    00100100 - Output
  ```
------------------------------------------------------------  
#### Bitwise OR(|)
**OR :** True if one of the inputs is `True(1)`

|Input1|Input2|Result|
|---|--|-------|
|0|0| 0|
|0|1| 1|
|1|0| 1|
|1|1| 1|

```
  10101110 - Input 1
|  
  01100101 - Input 2
  ---------
  11101111 - Output
```

----------------------------

#### Bitwise XOR(^)
**XOR ^:** True _if one and only one_ input bit is `True(1)`

|Input1|Input2|Result|
|---|--|-------|
|0|0| 0|
|0|1| 1|
|1|0| 1|
|1|1| 0|

```
  10101110 - Input 1
^  
  01100101 - Input 2
  ---------
  11101011 - Output
```
__________________________________
#### Bitwise NOT(~)
**NOT ~:** One's complement operator, Flips the input bit.

|Input1|Result|
|---|--|
|~0|1|
|~1|0|

```
~
  10101110 - Input 1
  ---------
  01010001 - Output
```
#### Left Shift(<<)
- Shift the binary digits by n, pad 0's on the right
- Each shift is a multiply by 2, (_unless there's overflow_)

```
  00010110
<<
  00000010
-----------
  01011000  
```

-----------------------------------
#### Right Shift(>>)
- Shift the binary digits by n, pad 0's on the left
- Each shift is a divide by 2 with round towards negative infinity.

```
   00010110
>>
   00000010
------------
   00000101
```
-----------------------------------

#### Bit Manipulation Basics

##### SET BIT

```python
def set_bit(x, position):
  mask = 1 << position
  return x | mask
#-----example
      x  00000110                 00000110   
position  00000101 (5)           | 00100000
    mask  00100000               -----------
                                   00100110
```
##### CLEAR BIT

```python
def clear_bit(x, position):
  mask = 1 << position
  return x & ~mask
#----example
       x 00000110                  00000110   x
position 00000010 (2)            & 11111011  ~mask
    mask 00000100                 ---------
  ~ mask 11111011                  00000010
```

##### FLIP BIT

```python
def flip_bit(x, position):
  mask = 1 << position
  return x ^ mask
#---- example
       x 01100110                 01100110 x
position 00000010               ^ 00000100 mask
    mask 00000100               ----------
                                  01100010 output
```
##### IS BIT SET
This checks if the bit at the certain position is set or not.
```python
def is_bit_set(x, position):
  shifted = x >> position
  return shifted & 1
#----example
       x 01100110                00000011  shifted   
position 00000101              & 00000001  1
 shifted 00000011              -----------
                                 00000001 output
```

##### MODIFY BIT
```python
def modify_bit(x, position, state):
  '''
  State = 1 --> set / State = 0 ---> clear
  '''
  mask = 1 << position
  return (x & ~mask) | (-state & mask)
#---- SET bit example
       x 00000110          ~mask  11011111            00000110  x & ~mask
position 00000101         -state  11111111          | 00100000  -state & mask
   state 00000001      x & ~mask  00000110           ----------
    mask 00100000   -state & mask 00100000            00100110

#---- CLEAR bit example
           x 00000110          ~mask  11011111        00000010  x & ~mask
    position 00000010         -state  00000000      | 00000000  -state & mask
       state 00000000      x & ~mask  00000010        ---------
        mask 00100000   -state & mask 0000000         00000010
```

#### BIT TRICKS

##### Is a number even or odd

```python
def check_even_odd(x):
  return ( x & 1 == 0)   #  ~(x & 1)
```
##### Check if Power of Two
```python
def pow_of_two(x):
  return (x & x-1) == 0
```
