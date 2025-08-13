from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    
    #result = anvil.server.call('parse_csv', file)
    result = anvil.server.call('get_import_columns')

    print(result)

    alert("CSV data saved to the data table!")
