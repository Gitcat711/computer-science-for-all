#### A binary search algorithm finds an item in a sorted list in O(lgn) time.

 - A brute force search would walk through the whole list, taking O(n) time in the worst case.

Let's say we have a sorted list of numbers. To find a number with a binary search, we:

    Start with the middle number: is it bigger or smaller than our target number? Since the list is sorted, this tells us if the target would be in the left half or the right half of our list.
    We've effectively divided the problem in half. We can "rule out" the whole half of the list that we know doesn't contain the target number.
    Repeat the same approach (of starting in the middle) on the new half-size problem. Then do it again and again, until we either find the number or "rule out" the whole set.
