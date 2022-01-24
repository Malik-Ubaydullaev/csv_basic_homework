def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   first_row = []
   row = data.split('\n')
   first_row = row[1].split(',')
   return first_row
   
   

# Read the csv file
data = open('data.csv').read()
print(get_first_row(data))