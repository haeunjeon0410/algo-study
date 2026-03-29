import sys

data = sys.stdin.read().splitlines()

if data:
    tree_dict = {}
    total_count = 0
    
    for name in data:
        if name in tree_dict:
            tree_dict[name] += 1
        else:
            tree_dict[name] = 1
        total_count += 1
    
    sorted_trees = sorted(tree_dict.keys())
    
    for tree in sorted_trees:
        ratio = (tree_dict[tree] / total_count) * 100
        print(f"{tree} {ratio:.4f}")