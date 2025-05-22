# Dynamic Programming
DP is about solving problems by breaking them <mark style="background-color:#E5CCFF80">down into overlapping subproblems</mark> and using the results of those subproblems to build up solutions efficiently.

### Ingredients of a DP Problem
1. <b>Choice</b> – At each step, what options do I have?

2. <b>State</b> – What defines the current situation?

3. <b>Transition</b> – How does the state change when I make a choice?

4. <b>Base Case</b> – What's the simplest version of this problem I already know the answer to?

5. <b>Goal</b> – What state/result do I ultimately want?

- subproblem: can i solve a smaller version of this problem (like a trivial one)? is it any easier?
- recurrence: how can i solve a larger version using only what i know about the smaller version?
- base case: until i cannot use any smaller version

### Common DP Patterns
| Pattern           | Description                                | Example Problems         |
| ----------------- | ------------------------------------------ | ------------------------ |
| **1D DP**         | Solve using a 1D array or recursion + memo | Climbing Stairs, Fib     |
| **2D DP**         | Usually for grid/substring problems        | Unique Paths, Edit Dist. |
| **Knapsack**      | Choose items to maximize/minimize a value  | 0/1 Knapsack, Subset Sum |
| **DP on Strings** | Compare or build strings with operations   | LCS, Edit Distance       |
| **DP on Trees**   | Bottom-up + memo at each node              | House Robber III         |
| **DP on Subsets** | Iterate over subsets or partitions         | Partition Equal Subset   |

### Example
Climbing Stairs. Each time, you can climb 1 or 2 steps. How many distinct ways to reach step n?

```python
def climbStairs(n):
    if n <= 2:  # base case
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # choice and transition

    return dp[n] # goal
```