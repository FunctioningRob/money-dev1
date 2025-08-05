import anvil.secrets
import anvil.server
from anvil.tables import app_tables
from db_utils import run_query
from file_utils import match_file_id, get_file_params
from csv_parser import parse_csv_file, transform_to_table_rows

@anvil.server.callable
def parse_csv(file, currency=None, account_name=None):
  file_id = match_file_id(file.name)
  if not file_id:
    return {"error": "No matching file ID found in filename."}

  file_params = get_file_params(file_id)
  if not file_params:
    return {"error": "No parameters found for this file ID."}

  df = parse_csv_file(file, file_params)
  rows = transform_to_table_rows(df)

  app_tables.tmp_stage_transactions.delete_all_rows()
  for row in rows:
    app_tables.tmp_stage_transactions.add_row(**row)

  return {"status": "success", "row_count": len(rows)}

@anvil.server.callable
def query_db(query, params=None):
  return run_query(query, params, fetch=True)