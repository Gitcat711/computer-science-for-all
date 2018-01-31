## Various programming terminologies and methods that cannot be overlooked.

#### 1. Memoization
- **Memoization** ensures that a function doesn't run for the same inputs more than once by keeping a record of the results for the given inputs (usually in a _dictionary/key-value-pair_).
- Memoization is a common strategy for **dynamic programming** problems, which are problems where the solution is composed of solutions to the same problem with smaller inputs

---------------------------
#### 2. Garbage Collection.
- A **Garbage Collector** automatically frees up memory that a program isn't using anymore. Let's try with example

```python
def get_min(nums):
  # NOTEs: this is NOT the fastest way to get the min!

  nums_sorted = sorted(nums)
  return nums_sorted[0]

my_nums = [5, 3, 1, 4, 6]
print get_min(my_nums)
```
- Look at ` nums_sorted ` in `get_min()`. We allocate that whole list inside our function, and once the function returns we don't need the list anymore. In fact, once the function returns we don't have any references to it anymore! What happens to that list in memory? The Python garbage collector will notice we don't need it anymore and free up that space.
- How does the Garbage Collector know when something can be freed?
  -  One option is to start by figuring out what we can't free. For example, we definitely can't free local variables that we're going to need later on. And, if we have a list, then we also shouldn't free any of the list's elements.

  - This is the main intuition behind one garbage collector strategy:
      - Carefully figure out what things in memory we might still be using or need later on.
      - Free everything else.

  - This strategy is often called tracing garbage collection, since we usually implement the first step by tracing references from one object (say, the list) to the next (an element within the list).

 - A different option is to have each object keep track of the number of things that reference it—like a variable holding the location of an array or multiple edges pointing to the same node in a graph. We'll call this number an object's reference count.

 - In this case, a garbage collector can free anything with a reference count of zero.

 - This strategy is called reference counting, since we are counting the number of times each object is referenced.

 -----------

####  3. What is `in-place` Algorithm?
 - An **in-place** algorithm operates directly on its input and changes it, instead of creating and returning a new object. This is sometimes called _destructive_, since the original input is "destroyed" when it's edited to create the new output.
 - **Caution**: `"In-place"` does _not mean "without creating any additional variables!"_ Rather, it means "_without creating a new copy of the input._" In general, an in-place function will only create additional variables that are O(1) space.
 - Below is nice example.

```python
def sq_list_in(arr_int_list):
  # using enumerate() lets us get the index and element
    for index, element in enumerate(arr_int_list):
        arr_int_list[index] *= element
  # We can directly make this function return,
  #because we are modifying arr_int_list in-place
    return arr_int_list

def sq_list_out(arr_int_list):
  # We define new list or allocate a new list with the lenght # of input list.
  sq_list = [None] * len(arr_int_list)

  for index, element in enumerate(arr_int_list):
    sq_list[index] =  element ** 2

  return squared_list

 ```

 -----
#### 4. What is Brute-force algorithm?
-  A brute force algorithm simply tries all possible answers to a question and checks them for correctness.

- It's rarely the most efficient approach, but it can be helpful to consider the time cost of the brute force approach when building an optimised solution. If your solution isn't faster than the brute force approach, it may not be optimal. 
