import anvil.secrets
# ---------------- server_module/file_utils.py ----------------
from db_utils import run_select_query

FILE_IDS = ['1698855-40-2', '1698855-40-3', '1698855-41-3', '45054060', 'Transactions']

def match_file_id(file_name):
  return next((fid for fid in FILE_IDS if fid in file_name), None)

def get_file_params(acc_no):
  rows = run_select_query("SELECT * FROM tblAccounts WHERE AccountNumber = %s", (acc_no,))
  return rows[0] if rows else None

@anvil.server.callable
def get_import_columns():
  rows = run_select_query("Show Tables,")
  return rows[0] if rows else None
