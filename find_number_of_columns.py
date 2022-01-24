def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    txt = data.split('\n')
    column = txt[0].split(',')
    return len(column)

# Read the csv file
data = open('data.csv').read()
print(find_number_of_columns(data))
