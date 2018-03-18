# PythonAutomationUtilities

This is a set of utilities that can help you in any or every Python based automation project that you pick up. Please note this is not a single tool rather a set of utility function that should be good to have in your project library for various functionality.

Descriptions:

**win_remote**
  
  Library to execute operation on remote Windows host. Note module connect via domain user using Kerberos based authentication.
  
  Requirement: https://github.com/diyan/pywinrm
  
  Dependency:
  
**unix_remote**
  
  Library to perform remote Unix host actions.
  
  Requirement: http://www.paramiko.org/
  
**mysql_lib**
  
  Library to execute query on remote/local mysql database.
  
  Requirement: https://github.com/PyMySQL/PyMySQL
  
  Dependency: property_loader library in current project.
  
**property_loader**
 
  Library to read property file Yaml and return property list of property for a section.
  
  Requirement: https://docs.python.org/2/library/configparser.html
  
  Dependency:
  
### Requirement:
  Please note for the tool to connect to remote Windows host it uses Kerberos authentication mechanism. This is done to avoid issues in using Domain users which is in most of the case for Enterprise Windows server. Thus for remote Windows function to be used you should have a Kerberos TGT available in your Cache. PyWinRM module page has all details for the set and usage.
  
### Support and managebility

If you are reading this README file then you are probably about to use the my tools to help you in your Python project. Good choice. This tool is made for you. Moreover this tool is free and always will be thats my promise.

Now it is hard to believe that you will get 24/7 Support thats too much to ask for. But in case you face any issue and want my intervention and you cannot debug the hundreeds lines of Python Script your self, please do not hassitate to write to me. Its a guarentee you will get an answer but it is not a guarentee you will have it in a SLA.

Reach Me: sanmuk21@gmail.com

Best of luck. Happy Python coding.

