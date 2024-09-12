def load_data_from_file_into_list(filename: str):
    data_table = []
    current_column = None
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('COLUMN'):
                current_column = line[7:]
            elif line == 'END':
                break
            else:
                data_table.append((current_column, line.split()))
    return data_table


def load_data_from_file_into_dictionary(filename: str):
    data_table = {}
    current_column = None
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('COLUMN'):
                current_column = line[7:]
                data_table[current_column] = []
            elif line == 'END':
                break
            else:
                data_table[current_column].extend(line.split())
    return data_table


def output_data_from_list(data_table: list):
    print("Displaying data from list...")
    for column_name, data in data_table:
        print(f"{'' * 20}\n{column_name}\n{'' * 20}")
        print("\n".join(data))


def output_data_from_dictionary(data_table: dict):
    print("Displaying data from dictionary...")
    for column_name, data in data_table.items():
        print(f"{'' * 20}\n{column_name}\n{'' * 20}")
        print("\n".join(data))


def output_total_mean_median(data_table, total_column_name: str):
    try:
        column_data = list(map(int, data_table[total_column_name]))
        total = sum(column_data)
        mean = total / len(column_data)
        median = sorted(column_data)[len(column_data) // 2]
        print(f"Displaying total from column {total_column_name} from ", end="")
        if isinstance(data_table, list):
            print("list...")
        elif isinstance(data_table, dict):
            print("dictionary...")
        print(f"Total from column {total_column_name} = {total}")
        print(f"The mean of column {total_column_name} = {mean}")
        print(f"The median of column {total_column_name} = {median}")
    except KeyError:
        print(f"Column: {total_column_name} could not be found")
    except (ValueError, TypeError):
        print(f"One or more values in {total_column_name} could not be converted into numerical values")




filename = "example.txt"
# Load data into the list
data_list = load_data_from_file_into_list(filename)
output_data_from_list(data_list)
# Load data into dictionary
data_dict = load_data_from_file_into_dictionary(filename)
output_data_from_dictionary(data_dict)
# Display total, mean, and median for "Credit" column
output_total_mean_median(data_dict, "Credit")