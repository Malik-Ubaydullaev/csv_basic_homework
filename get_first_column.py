def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    first_column = []
    row = data.split('\n')
    first_column = row[1].split(',')
    return first_column
    
# Read the csv file
data = open('data.csv').read()
print(get_first_column(data))