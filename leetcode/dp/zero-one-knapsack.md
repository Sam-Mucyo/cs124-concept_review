### 0/1 Knapsack Pattern in Dynamic Programming

The **0/1 Knapsack Problem** is another classic DP problem, where the goal is to maximize the total value of items in a knapsack with a given weight capacity. Here's how to approach it:

---

#### **1. Decision Tree Approach**

- **Problem Statement**:
  - Given $n$ items with weights $w[i]$ and values $v[i]$, and a knapsack of capacity $W$, determine the maximum value you can achieve without exceeding $W$.
- **Recursive Decision**:

  - For each item $i$, you have two choices:

    1. **Include the item** $i$ (if its weight $w[i]$ is ≤ remaining capacity).
    2. **Exclude the item** $i$.

  - Recursive formula:
    \[
    \text{max_value}(i, W) =
    \begin{cases}
    0 & \text{if } i = 0 \text{ or } W = 0, \\
    \text{max}(\text{max_value}(i-1, W), v[i-1] + \text{max_value}(i-1, W-w[i-1])) & \text{otherwise.}
    \end{cases}
    \]

---

#### **2. Time and Space Complexity**

- **Time Complexity**:
  - Exponential: $O(2^n)$, as there are $2^n$ combinations of items to consider.
- **Space Complexity**:
  - $O(n)$, due to the recursion stack depth of $n$.

---

#### **3. Observations for Optimization**

- **Overlapping Subproblems**:
  - The same subproblem (e.g., solving for a specific $i, W$) is recomputed multiple times.
- **Optimal Substructure**:
  - The optimal solution to $i$ items and $W$ weight depends only on the solution for smaller subproblems.

---

#### **4. Translating to Efficient Solutions**

**Optimization Techniques**:

1. **Memoization (Top-Down Approach)**:

   - Store results for each $i, W$ in a 2D table to avoid recomputation.
   - Complexity: $O(n \cdot W)$ time and space.

2. **Bottom-Up DP (Tabulation)**:
   - Solve iteratively using a 2D DP table or optimize further using a 1D DP array.
   - Complexity:
     - Time: $O(n \cdot W)$, as each subproblem is solved once.
     - Space:
       - $O(n \cdot W)$: for a 2D table.
       - $O(W)$: for a 1D array (space-optimized).

---

#### **5. Efficient 1-D Bottom-Up Solution**

```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)  # Create a 1D array for DP

    for i in range(n):
        # Traverse from right to left to prevent overwriting previous states
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]  # The maximum value for the given capacity
```

**Explanation**:

1. Use a 1D array `dp[w]` where `dp[w]` represents the maximum value achievable with weight $w$.
2. Iterate over items, and for each item, update the DP array **backwards** to ensure previous states are not overwritten.
3. Return `dp[capacity]` as the result.

---

### Decision Tree vs. Optimized Solution

| **Aspect**           | **Decision Tree**       | **Optimized DP Solution**    |
| -------------------- | ----------------------- | ---------------------------- |
| **Time Complexity**  | $O(2^n)$                | $O(n \cdot W)                |
| **Space Complexity** | $O(n)$ (stack)          | $O(W)$ (1D array)            |
| **Approach**         | Recursive, redundant    | Iterative, avoids redundancy |
| **Key Observation**  | Overlapping subproblems | Use a DP array for reuse     |

The 1D bottom-up solution is ideal for coding interviews due to its efficiency in both time and space.

### **Practice Problems**

1. **Partition Equal Subset Sum**  
   [Problem #416](https://leetcode.com/problems/partition-equal-subset-sum/)

   - Determine if the array can be partitioned into two subsets with equal sums.

2. **Last Stone Weight II**  
   [Problem #1049](https://leetcode.com/problems/last-stone-weight-ii/)

   - Minimize the difference between two groups of stone weights.

3. **Target Sum**  
   [Problem #494](https://leetcode.com/problems/target-sum/)

   - Assign $+$ or $-$ to each number to achieve a target sum.

4. **Subset Sum**  
   [Problem](https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1) (GeeksforGeeks)

   - Determine if there’s a subset with a sum equal to a given value.

5. **Knapsack Problem**  
   [Problem](https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1) (GeeksforGeeks)

   - Classic knapsack problem to maximize value within weight capacity.

6. **Coin Change II**  
   [Problem #518](https://leetcode.com/problems/coin-change-ii/)

   - Count combinations of coins to make up a given amount.

7. **Ones and Zeroes**  
   [Problem #474](https://leetcode.com/problems/ones-and-zeroes/)

   - Find the maximum subset with given constraints on 0s and 1s.

8. **Maximum Profit in Job Scheduling**  
   [Problem #1235](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
   - Schedule jobs to maximize profit while avoiding overlap.

---

These problems cover the key variations of the **Fibonacci** and **0/1 Knapsack patterns**, and practicing them will solidify your understanding of DP concepts. Let me know if you'd like explanations or solutions for any of these!
