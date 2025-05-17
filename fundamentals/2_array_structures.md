# Array Structures
Array structures involve <mark style="background-color:#E5CCFF80">different ways of organising an array of data</mark> to achieve a goal, typically searches.

The methods include:
- stacks: first in, last out,
- queues: first in, first out,
- heaps: tree with ordered subtrees.

### Stack
The idea is to <mark style="background-color:#CCE5FF80">access the most recent resource first</mark>. (Reverse order).

It is primarily implemented with initialise, push and pop.

### Queue
The idea is to <mark style="background-color:#CCE5FF80">access the oldest resource first</mark>. (Preserve order).

It is primarily implemented with initialise, enqueue, dequeue.

### Heap
The idea is to <mark style="background-color:#CCE5FF80">always access the highest or lowest priority item efficiently</mark>, i.e. in logarithmic time. (Partial ordering).

It is primarily implemented with initialise, insert (push), and extract (pop).

<mark style="background-color:#f9e79f80">Use</mark>:

```C++
// C++

    vector<int> vc{ 40, 10, 20, 50, 30 };

    // making heap
    make_heap(vc.begin(), vc.end());

    // adding
    vc.push_back(60);
    push_heap(vc.begin(), vc.end());

    // using pop_heap() function to move the largest element
    // to the end
    pop_heap(vc.begin(), vc.end());

    // actually removing the element from the heap using
    // pop_back()
    vc.pop_back();
```
```python
# Python
    import heapq
    heapq = []
    
    # Add elements
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 8)

    # Access smallest element (always at index 0)
    print(heap[0])  # Output: 2

    # Remove and return the smallest element
    smallest = heapq.heappop(heap)
    print(smallest)  # Output: 2

    # Resulting heap: [5, 8]

```