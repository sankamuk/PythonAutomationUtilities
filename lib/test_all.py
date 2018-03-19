from mysql_lib import get_select_data, insert_data
from win_remote import run_command, run_to_copy, run_from_copy
from file_comm import text_compare

#==============================================================================================
# Mysql Test
#data = (4, "/trans/dochome/4")
#query_str = "INSERT INTO TaskProof VALUES (%s, %s)"
#insert_data(query_str, data)
#data = get_select_data("select * from TaskProof")
#for row in data:
#    print(row[0])
#    print(row[1])
#==============================================================================================

#==============================================================================================
# Windows Admin Test
#run_to_delete("xsnw50f525a.pharma.aventis.com", "C:\\Users\\x002909a\\Desktop\\MFT\\test.txt")
#run_to_copy("xsnw50f525a.pharma.aventis.com", "/usr/local/share/python_workspace/cft_devops/app.py", "C:\\Users\\x002909a\\Desktop\\MFT\\app.py")
#op, err, stat = run_command("xsnw50f525a.pharma.aventis.com", "powershell get-filehash -algorithm md5 C:\\Users\\x002909a\\Desktop\\MFT\\app.py")
#print(op.decode('utf-8'))
#run_from_copy("xsnw50f525a.pharma.aventis.com", "/usr/local/share/python_workspace/cft_devops/lib/app.py", "C:\\Users\\x002909a\\Desktop\\MFT\\app.py")
#==============================================================================================

#==============================================================================================
# File compare Test
#stat, outpt = text_compare('/usr/local/share/python_workspace/cft_devops/lib/F1', '/usr/local/share/python_workspace/cft_devops/lib/F2')
#print("Status {}\n".format(str(stat)))
#print(outpt)
#==============================================================================================
