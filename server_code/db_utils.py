import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# ---------------- server_module/db_utils.py ----------------
import pymysql
import anvil.secrets
import decimal

def connect():
  return pymysql.connect(
    host='bbelbnkbjyewmxmblwdi-mysql.services.clever-cloud.com',
    port=3306,
    user='urmzj2jtlkndes2g',
    password=anvil.secrets.get_secret("db_password"),
    database='bbelbnkbjyewmxmblwdi',
    cursorclass=pymysql.cursors.DictCursor
  )

def run_select_query(query, params=None, fetch=True):
  conn = connect()
  with conn.cursor() as cursor:
    cursor.execute(query, params or ())
    if fetch:
      rows = cursor.fetchall()
      return [_convert_decimal(row) for row in rows]
    else:
      conn.commit()
      return {"status": "success"}

def _convert_decimal(row):
  return {k: float(v) if isinstance(v, decimal.Decimal) else v for k, v in row.items()}

  