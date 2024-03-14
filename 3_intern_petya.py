def calculate_line_sum(line_quantity: int, column_names: list[str],
                       table: list[list[int]], queries: list[list[str]]) -> int:
    """Calculate sum of matching rows."""
    required_lines = set()
    unnecessary_lines = set()
    for column_name, operand, value in queries:
        number_of_column = column_names.index(column_name)
        for line_number in range(line_quantity):
            if line_number in unnecessary_lines:
                continue
            if (operand == '<' and int(table[line_number][number_of_column]) < int(value)) or (
                    operand == '>' and int(table[line_number][number_of_column]) > int(value)):
                required_lines.add(line_number)
            else:
                unnecessary_lines.add(line_number)
                required_lines.discard(line_number)
    result_sum = sum(sum(table[line]) for line in required_lines)
    return result_sum


def read_input() -> tuple:
    """Read input data."""
    num, _, q = map(int, input().split())
    column_names = input().split()
    table = [list(map(int, input().split())) for _ in range(num)]
    queries = [input().split() for _ in range(q)]
    return num, column_names, table, queries


if __name__ == "__main__":
    num, column_names, table, queries = read_input()
    result = calculate_line_sum(num, column_names, table, queries)
    print(result)
