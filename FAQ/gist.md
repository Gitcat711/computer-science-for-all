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
 
 
