import paramiko
"""
  Library to perform remote Unix host actions.
  Requirement: http://www.paramiko.org/ 
"""

def run_command(server_name, user_id, user_password, command_line) :
  """ 
      Execute remote command and return the output. 
      Remark: No handing of any kind of exeception.
      Args:
        server_name(string): Name of the host to connect.
        user_id(string): User to connect with.
        user_password(string): User password.
        command_line(string): Command to execute.
      Returns:
        Standard input, Standard output, Standard error
  """
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(server_name, username=user_id, password=user_password)
  stdin, stdout, stderr = ssh.exec_command(command_line)
  return stdin, stdout, stderr

def run_to_copy(server_name, user_id, user_password, local_file, remote_file) :
  """
      Copy file from local to remote.
      Remark: No handing of any kind of exeception.
      Args:
        server_name(string): Name of the host to connect.
        user_id(string): User to connect with.
        user_password(string): User password.
        local_file(string): Absolute path of file in local.
        remote_file(string): Absolute path of file in remote.
      Returns:
        
  """
  sf = paramiko.Transport((server_name,22))
  sf.connect(username = user_id, password = user_password)
  sftp = paramiko.SFTPClient.from_transport(sf)
  return sftp.put(local_file,remote_file)

def run_from_copy(server_name, user_id, user_password, local_file, remote_file) :
  """
      Copy file from remote to local.
      Remark: No handing of any kind of exeception.
      Args:
        server_name(string): Name of the host to connect.
        user_id(string): User to connect with.
        user_password(string): User password.
        local_file(string): Absolute path of file in local.
        remote_file(string): Absolute path of file in remote.
      Returns:

  """
  sf = paramiko.Transport((server_name,22))
  sf.connect(username = user_id, password = user_password)
  sftp = paramiko.SFTPClient.from_transport(sf)
  return sftp.get(remote_file,local_file )

