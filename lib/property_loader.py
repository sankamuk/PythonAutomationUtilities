import configparser
"""
  Library to read property file Yaml and return property list of property for a section.
  Requirement: https://docs.python.org/2/library/configparser.html
  Dependency: 
"""


def mysql_property_extractor():
  """
      Extract property from Configuration file(yaml) named config.properties in same property and extract property for section MYSQL_DB.
      Remark: No handing of any kind of exeception.
      Args:

      Returns:
        Property list
  """
  config = configparser.RawConfigParser()
  config.read('config.properties')
  prop = (config.get('MYSQL_DB', 'db.host'), config.get('MYSQL_DB', 'db.user'), config.get('MYSQL_DB', 'db.passwd'), config.get('MYSQL_DB', 'db.schema'))
  return prop
