import pymysql
from property_loader import mysql_property_extractor
"""
  Library to execute query on remote/local mysql database.
  Requirement: https://github.com/PyMySQL/PyMySQL
  Dependency: property_loader library in current project.
"""

def get_select_data(sql_query):
  """
      Execute select query and return result.
      Remark: No handing of any kind of exeception.
      Args:
      Returns:
        Query result cursor(list of column dictonary)
  """
  db_detail = mysql_property_extractor()
  db = pymysql.connect(db_detail[0], db_detail[1], db_detail[2], db_detail[3])
  cursor = db.cursor()
  cursor.execute(sql_query)
  return cursor
  db.close()

def insert_data(sql_query, data):
  """
      Execute insert query and insert data.
      Remark: No handing of any kind of exeception.
      Args:
        sql_query(string): insert query.
        data(touple): data to insert.
      Returns:
  """
  db_detail = mysql_property_extractor()
  db = pymysql.connect(db_detail[0], db_detail[1], db_detail[2], db_detail[3])
  cursor = db.cursor()
  cursor.execute(sql_query, data)
  db.commit()
  db.close()
