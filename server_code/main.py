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
    return {"error": "No matching file ID found in filename."}

  file_params = get_file_params(file_id)
  print(f"file_params={file_params}")
  if not file_params:
    return {"error": "No file parameters found for this file ID."}

  print(f"file_params={file_params['AccountID']}")
  
  import_params = get_import_params(file_params['AccountID'])
  print(f"import_params={import_params}")
  if not import_params:
    return {"error": "No import parameters found for this file ID."}
  
  df = parse_csv_file(file, file_params, import_params)
  value = transform_to_table_rows(df)
  print(map_and_order_values(value, import_columns))
        
        
"""
  remove = {'AccountId', 'header_row'}
  imported_sheet_columns = {k: v for k, v in import_params.items() if k not in remove}
  #imported_headers = list(imported_sheet_columns.values())
  database_columns = list(imported_sheet_columns.keys())
 

    
    
  
  #insert_statement = f"INSERT INTO tblStagedTransactions({', '.join(database_columns)})"
  # Build column string
  columns_str = ', '.join(database_columns)
  
# Create placeholders for parameterized query
  placeholders = ', '.join(['?'] * len(database_columns))
 
# Final SQL statement
  insert_statement = f"INSERT INTO tblStagedTransactions({columns_str}) VALUES ({placeholders})"

  print(insert_statement)

  #app_tables.tmp_stage_transactions.delete_all_rows()
  values_list=[]
  for row in rows:
    print(row)
    # Collect values for all columns for this row
    print("Col " .join(col for col in imported_sheet_columns))
    print("row " .join( [row[col] for col in imported_sheet_columns]))
    print(imported_sheet_columns)
    for col in imported_sheet_columns:    
     values = [row[col] for col in imported_sheet_columns]
     values_list.append(values)
    
   


      if key in import_params.value:
        sql_val = row[key]
        print(key + " --> " + key.value)
        
      SELECT `tblImportParameters`.`AccountId`,
    `tblImportParameters`.`TransactionDate`,
    `tblImportParameters`.`PaidTo`,
    `tblImportParameters`.`Currency`,
    `tblImportParameters`.`Debit`,
    `tblImportParameters`.`Credit`,
    `tblImportParameters`.`Balance`,
    `tblImportParameters`.`header_row`
FROM `bbelbnkbjyewmxmblwdi`.`tblImportParameters`;

       
        print(sql_val)
      # Add quotes if the value is a string
        if isinstance(sql_val, str):
          val = f"'{sql_val}'"
        value_parts.append(str(sql_val))
        values_list.append(f"({', '.join(value_parts)})")"""
  
    
    #app_tables.tmp_stage_transactions.add_row(**row)
    #return {"status": "success", "row_count": len(rows)}
"""
  column_map = {
    'Value Date': 'TransactionDate',
    'Text': 'PaidTo',
    'Currency': 'Currency',
    'Debit': 'Debit',
    'Credit': 'Credit',
    'Balance': 'Balance'
  }
"""

@anvil.server.callable
def query_db(query, params=None):
  return run_query(query, params, fetch=True)

