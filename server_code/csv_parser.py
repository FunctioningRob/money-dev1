#see I'm new

import anvil.secrets
import pandas as pd
import io
from datetime import datetime

def parse_csv_file(file, file_params, import_params):
  #file_params = anvil.server.call['get_import_params(file)',file]
  csv_text = file.get_bytes().decode('latin1')
  df = pd.read_csv(io.StringIO(csv_text), header=import_params['header_row'])
  
  #remove the last row (totals)
  if df.tail(1).isnull().all(axis=1).any():
    df = df.iloc[:-1]

  df['Currency'] = file_params['Currency']
  if 'Booking Date' in df.columns:
    df = df.drop(columns=['Booking Date'])

  df = df.fillna("")
  return df

def transform_to_table_rows(df):
  column_map = {
    'Value Date': 'TransactionDate',
    'Text': 'PaidTo',
    'Currency': 'Currency',
    'Debit': 'Debit',
    'Credit': 'Credit',
    'Balance': 'Balance'
  }
 
  filtered_cols = [col for col in df.columns if col in column_map]
  renamed_cols = [column_map[col] for col in filtered_cols]

  rows = []
  for _, row in df.iterrows():
        converted = {}
        for col, new_col in zip(filtered_cols, renamed_cols):
            val = row[col]
            if new_col in ['Debit', 'Credit', 'Balance']:
                val = float(val) if val != '' else 0.0
            elif new_col == 'TransactionDate':
                val = parse_date(val)
            elif new_col == 'Currency':
                val = str(val)
            converted[new_col] = val
        rows.append(converted)
        return rows

def parse_date(date_str):
    if not date_str or str(date_str).strip() == "":
        return None
    try:
        return datetime.strptime(str(date_str).strip(), "%d.%m.%Y").date()
    except Exception:
        return None
