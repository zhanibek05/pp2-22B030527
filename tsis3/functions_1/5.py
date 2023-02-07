import itertools

def print_permutations(s):
    permutations = list(itertools.permutations(s))
    for permutation in permutations:
        print("".join(permutation))

s = input()
print_permutations(s)
    