from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    temp = anvil.server.call('db_check')
    print(temp)
    exit()
      
    result = anvil.server.call('parse_csv', file)
    #result = anvil.server.call('get_import_columns',2)
    #rows = anvil.server.call('testing_db')
    print(f"result is type {type(result)} and length {len(result)}")
    #self.print_table(rows)
    
    print(result)
    alert("CSV data saved to the data table!")


  def print_table(self, rows):
    if not rows:
      print("No data")
      return
  
      # Safe: get headers from the first row (which is a dict)
    headers = rows[0].keys()
  
    # Print header row
    print(" | ".join(headers))
    print("-" * (len(headers) * 15))
  
    # Print each row
    for i, row in enumerate(rows):
      print(f"Row {i}: {row} (type: {type(row)})")
      print(" | ".join(str(row[h]) for h in headers))
  

