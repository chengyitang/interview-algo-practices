from collections import defaultdict
import sys

def find_levels_between(inputs):

    request = inputs[0].split('/')

    adj = defaultdict(list)

    for pair in inputs[1:]:
        employee, manager = pair.split('/')
        adj[employee].append(manager)

    #print(adj)

    visited = set()
    def dfs(node, target, level):
        if node == target:
            return level
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                result = dfs(neighbor, target, level + 1)
                if result != 0:
                    return result
        visited.remove(node)
        return 0
    
    return dfs(request[0], request[1], 0)

def main():
    # Read inputs
    inputs = []
    try:
        while True:
            n = sys.stdin.readline().strip('\n')
            if not n:
                break
            inputs.append(n)
    except:
        pass
    
    print(find_levels_between(inputs))

if __name__ == "__main__":
    main()