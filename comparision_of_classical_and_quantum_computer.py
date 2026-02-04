import math
def classical_search(arr, target):
    steps = 0
    for x in arr:
        steps += 1
        if x == target:
            return steps
    return steps
def grover_steps(N):
    return round((math.pi / 4) * math.sqrt(N))
def compare(N, target):
    data = list(range(N))
    c_steps = classical_search(data, target)
    q_steps = grover_steps(N)
    print(f"N = {N}")
    print(f"Classical steps : {c_steps}")
    print(f"Quantum steps   : {q_steps}")
    print("-" * 25)
compare(16, 11)
compare(64, 42)
compare(256, 200)
compare(1024, 700)
