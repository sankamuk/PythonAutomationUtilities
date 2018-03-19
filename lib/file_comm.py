
"""
  Library to compare files.
  Requirement: 
  Dependency: 
"""

def text_compare(fname1, fname2):
  """
      Compare text file and print difference in text. Note compare Text Only.
      Remark: No handing of any kind of exeception.
      Args:
        fname1(string): Name of the first file.
        fname2(string): Name of the second file.
      Returns:
        Touple: Status (0 Success, 1 Failure), String output of comparison, note > symbolize first file < symbolize second file.
  """
  f1 = open(fname1)
  f2 = open(fname2)
  f1_line = f1.readline()
  f2_line = f2.readline()
  line_no = 1
  status = 0
  err_str = ""
  while f1_line != '' or f2_line != '':
    f1_line = f1_line.strip()
    f2_line = f2_line.strip()
    if f1_line != f2_line:
      if f2_line == '' and f1_line != '':
        #print(">+", "Line-%d" % line_no, f1_line)
        err_str = err_str + ">+" + "Line-{} {}\n".format(str(line_no), f1_line)
        status = 1
      elif f1_line != '':
        #print(">", "Line-%d" % line_no, f1_line)
        err_str = err_str + ">" + "Line-{} {}\n".format(str(line_no), f1_line)
        status = 1
      if f1_line == '' and f2_line != '':
        #print("<+", "Line-%d" % line_no, f2_line)
        err_str = err_str + "<+" + "Line-{} {}\n".format(str(line_no),f2_line)
        status = 1
      elif f2_line != '':
        #print("<", "Line-%d" %  line_no, f2_line)
        err_str = err_str + "<" + "Line-{} {}\n".format(str(line_no),f2_line)
        status = 1
      #print()
    f1_line = f1.readline()
    f2_line = f2.readline()
    line_no += 1
  f1.close()
  f2.close()
  return status, err_str
