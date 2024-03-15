def prefix_length(arrays: list[list[int]]) -> int:
    """Calculate length of common prefixes."""
    length_sum = 0
    for i, first_array in enumerate(arrays[:-1]):
        for second_array in arrays[i + 1:]:
            length_sum += sum(a == b for a, b in zip(first_array, second_array))
    return length_sum


def read_input() -> list[list[int]]:
    """Read input data."""
    num_arrays = int(input())
    arrays = []
    for i in range(num_arrays):
        int(input())
        array = list(map(int, input().split()))
        arrays.append(array)
    return arrays


if __name__ == "__main__":
    arrays = read_input()
    print(prefix_length(arrays))
