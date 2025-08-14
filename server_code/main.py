import anvil.secrets
import anvil.server
from anvil.tables import app_tables
from db_utils import run_select_query
from file_utils import match_file_id, get_file_params, get_import_params, map_and_order_values
from csv_parser import parse_csv_file, transform_to_table_rows

@anvil.server.callable
def parse_csv(file, currency=None, account_name=None):
  
  file_id = match_file_id(file.name)
  print(f"file_id={file_id}")
  if not file_id:
    return {"error": "file_id: No matching file ID found in filename."}

  file_params = get_file_params(file_id)
  print(f"file_params={file_params}")
  if not file_params:
    return {"error": "file_params: No file parameters found for this file ID."}
  
  import_params = get_import_params(file_params['AccountID'])
  print(f"import_params={import_params}")
  if not import_params:
    return {"error": "import_params: no import parameters found for this file ID."}
  
  df = parse_csv_file(file, file_params, import_params)
  value = transform_to_table_rows(df)
  print(map_and_order_values(value, import_columns))

@anvil.server.callable
def query_db(query, params=None):
  return run_query(query, params, fetch=True)

