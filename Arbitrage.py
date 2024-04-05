from collections import defaultdict

# Provided liquidity dictionary
liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

# Function to calculate the amount received after a swap
def swap(from_token, to_token, amount):
    # 0.3% swap fee
    rate = liquidity.get((from_token, to_token))
    if not rate:
        r_b, r_a = liquidity.get((to_token, from_token))
    else:
        r_a, r_b = rate
    
    return (997 * amount * r_b) / (1000 * r_a + 997 * amount)


# Function to explore all paths and select the one that maximizes tokenB amount
def find_max_path(current_token, amount, path, visited=set(), depth=0, max_depth=5):
    # Base cases
    if depth > max_depth:  # Limiting the depth to prevent infinite recursion
        return path, amount
    if current_token == "tokenB" and len(path) > 1 and amount > 20:  # Target achieved
        return path, amount

    max_amount = 0
    max_path = path
    next_tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
    next_tokens.remove(current_token)  # Avoid going back to the same token
    for next_token in next_tokens:
        if next_token not in visited:  # Avoid cycles
            next_amount = swap(current_token, next_token, amount)
            if next_amount > max_amount:  # Choose the swap that gives the maximum amount
                next_path, final_amount = find_max_path(next_token, next_amount, path + [next_token], visited | {next_token}, depth + 1, max_depth)
                if final_amount > max_amount:
                    max_amount = final_amount
                    max_path = next_path

    return max_path, max_amount

# Start the search with 5 units of tokenB
max_profitable_path, max_final_amount = find_max_path("tokenB", 5, ["tokenB"])

if max_profitable_path:
    print(f"Path: {'->'.join(max_profitable_path)}, tokenB balance={max_final_amount}")
else:
    print("No profitable path found.")


# # test B-->A-->D-->B
# a0 = swap("tokenB", "tokenA", 5)
# a1 = swap("tokenA", "tokenD", a0)
# a2 = swap("tokenD", "tokenB", a1)
# print(a2)  # 20.0
