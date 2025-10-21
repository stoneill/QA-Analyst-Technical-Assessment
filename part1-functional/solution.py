# Removes duplicates from a list
def remove_duplicates(seq):
    seen = set()
    return list(filter(lambda x: x not in seen and not seen.add(x), seq))

# Test cases
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))  # [1, 2, 3, 4, 5]
    print(remove_duplicates([1, 1, 1]))              # [1]
    print(remove_duplicates([]))                    # []
