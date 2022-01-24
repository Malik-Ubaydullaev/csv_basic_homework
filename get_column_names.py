#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    column_name = []
    row = data.split('\n')
    #row.pop()
          
    
    return row
    
# Read the csv file
data = open('data.csv').read()
print(get_column_names(data))