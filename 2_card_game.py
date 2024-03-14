def calculate_unique_quantity(first_collection: list[int],
                              second_collection: list[int],
                              modifications: list[list[str]]) -> list[int]:
    """Calculate unique card quantity."""
    unique_quantity = list()
    for action, player, card in modifications:
        collection = first_collection if player == 'A' else second_collection
        if action == '1':
            collection.append(int(card))
        elif action == '-1':
            collection.remove(int(card))
        common_cards = len(set(first_collection) & set(second_collection))
        unique_quantity.append(len(first_collection) + len(second_collection) - 2 * common_cards)
    return unique_quantity


def read_input() -> tuple:
    """Read input data."""
    _, _, num = map(int, input().split())
    first_collection = list(map(int, input().split()))
    second_collection = list(map(int, input().split()))
    modifications = [input().split() for _ in range(num)]
    return first_collection, second_collection, modifications


if __name__ == "__main__":
    first_collection, second_collection, modifications = read_input()
    result = calculate_unique_quantity(first_collection, second_collection, modifications)
    print(' '.join(map(str, result)))
