from winrm.protocol import Protocol
import base64
import os
import sys
import time
"""
  Library to execute operation on remote Windows host. Note module connect via domain user using Kerberos based authentication.
  Requirement: https://github.com/diyan/pywinrm
  Dependency: 
"""

def run_command(server_name, command_line) :
  """
      Execute remote command and return the output.
      Remark: No handing of any kind of exeception. Kerberos ticket should be intiated.
      Args:
        server_name(string): Name of the host to connect.
        command_line(string): Command to execute.
      Returns:
        Standard output, Standard error, Status
  """
  host_name = "http://"+ server_name +":5985/wsman"
  win_connect = Protocol(endpoint=host_name, transport='kerberos')
  shell_id = win_connect.open_shell()
  command_id = win_connect.run_command(shell_id, command_line)
  return win_connect.get_command_output(shell_id, command_id)

def run_to_copy(server_name, local_path, remote_path) :
  """
      Transfer text file to remote Windows host.
      Remark: No handing of any kind of exeception. Kerberos ticket should be intiated.
      Args:
        server_name(string): Name of the host to connect.
        local_path(string): Absolute path to local file.
        remote_path(string): Absolute path to remote file.
      Returns:
        
  """
  host_name = "http://"+ server_name +":5985/wsman"
  conn = Protocol(endpoint=host_name, transport='kerberos')
  shell_id = conn.open_shell()

  file = open(local_path, 'r')
  text_file = file.read()
  file.close()
 
  remote_path_str = '"'+ remote_path +'"'
  part_1 = """$stream = [System.IO.StreamWriter] """+ remote_path_str +"""
$s = @"
"""

  part_2 = """
"@ | %{ $_.Replace("`n","`r`n") }
$stream.WriteLine($s)
$stream.close()"""

  script = part_1 + text_file + part_2
  encoded_script = base64.b64encode(script.encode('utf_16_le')).decode('ascii')
  command_id = conn.run_command(shell_id, "powershell -encodedcommand %s" % (encoded_script))
  stdout, stderr, return_code = conn.get_command_output(shell_id, command_id)
  conn.cleanup_command(shell_id, command_id)
  conn.close_shell(shell_id)

def run_from_copy(server_name, local_path, remote_path) :
  """
      Transfer text file from remote Windows host to local Unix host.
      Remark: No handing of any kind of exeception. Kerberos ticket should be intiated.
      Args:
        server_name(string): Name of the host to connect.
        local_path(string): Absolute path to local file.
        remote_path(string): Absolute path to remote file.
      Returns:
        
  """
  host_name = "http://"+ server_name +":5985/wsman"
  conn = Protocol(endpoint=host_name, transport='kerberos')
  shell_id = conn.open_shell()

  command_id = conn.run_command(shell_id, "type "+ remote_path)
  stdout, stderr, return_code = conn.get_command_output(shell_id, command_id)
  conn.cleanup_command(shell_id, command_id)
  file = open(local_path, 'w')
  file.write(stdout.decode('ascii'))
  file.close()
  conn.close_shell(shell_id)


def run_to_delete(server_name, remote_path) :
  """
      Delete file from remote Windows host.
      Remark: No handing of any kind of exeception. Kerberos ticket should be intiated.
      Args:
        server_name(string): Name of the host to connect.
        remote_path(string): Absolute path to remote file.
      Returns:
  """
  host_name = "http://"+ server_name +":5985/wsman"
  conn = Protocol(endpoint=host_name, transport='kerberos')
  shell_id = conn.open_shell()

  command_id = conn.run_command(shell_id, "del "+ remote_path)
  stdout, stderr, return_code = conn.get_command_output(shell_id, command_id)
  conn.cleanup_command(shell_id, command_id)
  conn.close_shell(shell_id)


