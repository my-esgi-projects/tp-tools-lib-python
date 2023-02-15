def user_verification(username):
     with open('/etc/passwd','r') as passwd_files:
         for line in passwd_files:
             if username == line.split(':')[0]:
                 return True
             return False