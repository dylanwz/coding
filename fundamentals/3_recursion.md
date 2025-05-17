# Recursion
Recursive techniques involve <mark style="background-color:#E5CCFF80">solving a problem by breaking it down into smaller, identical instances</mark>.

Techniques include:
- recursive calls: re-call function,
- backtracking: try and undo.

### Recursive Calls
The idea is to <mark style="background-color:#CCE5FF80">re-call your function</mark>.

Recursive solutions are often of the following form:

```
function do_something():
    if base_case():     // (1)
        return
    
    continue ...        // (2)

    do_something()      // (3)

    finish ...          // (4)
```
(1) the base case is when the solution to the smaller subproblem has been found; (2) solve a subproblem; (3) move on to the next subproblem; and (4) use subproblem solutions to produce the final solution.

### Backtracking
The idea is to <mark style="background-color:#CCE5FF80">try, undo and repeat</mark>. It is smarter brute force, possible when there is a monotonic property to the solution space; if $X$ doesn't work, then any $Y > X$ will not either.

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

Backtracking, and recursion in general, lends itself to a stack structure because we want to access the last state.

```python
def backtrack(path, options):    
    stack = [(initial_path, initial_options)]

    while stack is not empty:
        
        # if something gets popped without anything having been pushed,
        # it means it wasn't a solution
        path, options = stack.pop()

        # found a temporary solution, save
        if base_case(path):
            result.append(copy_of(path))
            continue

        for option in options:
            if is_valid(option, path):
                # choose
                new_path = path + [option]           
                # advance   
                new_options = update(options, option)
                # explore
                stack.push((new_path, new_options))
```