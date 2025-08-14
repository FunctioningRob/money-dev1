import anvil.secrets
# ---------------- server_module/file_utils.py ----------------
from db_utils import run_select_query

FILE_IDS = ['1698855-40-2', '1698855-40-3'',' '1698855-41-3', '40003658065': '45054060', 'Transactions']



def match_file_id(file_name):
  return next((fid for fid in FILE_IDS if fid in file_name), None)

def get_file_params(acc_no):
  print(f"acc_no: {acc_no}")
  rows = run_select_query("SELECT * FROM tblAccounts WHERE AccountID = %s", (acc_no))
  return rows if rows else None

def get_import_params(acc_ID):
  rows = run_select_query("SELECT * FROM tblImportParameters WHERE AccountID = %s", (acc_ID,))
  return  rows[0]

def get_import_columns(acc_no):
  rows = run_select_query("SELECT * FROM tblImportParameters WHERE AccountID = %s", (acc_no,))
  return rows[0] if rows else None

def map_and_order_values(row, import_columns):
  # import_columns keys are target DB columns in order you want,
  # values are keys in your input row dictionary.
  ordered_values = []
  for db_col in import_columns:
    import_col = import_columns[db_col]
    ordered_values.append(row.get(import_col))
    return ordered_values


@anvil.server.callable
def testing_db():
  rows = run_select_query("SHOW TABLES")
  return rows if rows else None