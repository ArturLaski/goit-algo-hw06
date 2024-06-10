import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Create a min-heap from the cable lengths
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Continue until there is only one cable left
    while len(cable_lengths) > 1:
        # Extract the two shortest cables
        first_min = heapq.heappop(cable_lengths)
        second_min = heapq.heappop(cable_lengths)
        
        # The cost to connect them
        cost = first_min + second_min
        total_cost += cost
        
        # Push the resulting cable back into the heap
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Example usage and test cases
test_cases = [
    [4, 3, 2, 6],
    [1, 2, 5, 10, 35, 89],
    [2, 2, 3, 3],
    [5, 5, 4, 4, 7],
    [10, 20, 30, 40, 50]
]

for i, cables in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    print(f"Cable lengths: {cables}")
    print(f"Minimum cost to connect cables: {min_cost_to_connect_cables(cables)}")
    print()
