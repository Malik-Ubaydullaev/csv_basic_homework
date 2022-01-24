def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    columns = []
    row = data.split('\n')
    idx = 0
    while idx < len(row)-1:
        columns.append(row[idx].split(','))
        idx += 1
    first_column = []
    idx = 0
    while idx < len(columns):
        first_column.append(columns[idx][0])
        idx += 1
    return first_column
    
# Read the csv file
data = open('data.csv').read()
print(get_first_column(data))