class Credential:
  '''
  blueprint for how credentials should be stored
  '''

  def __init__(self, *, category=None, username=None, password=None):
    self.credentialCategory = category
    self.credentialUsername = username
    self.credentialPassword = (password, self.generatePassword())[password.strip() == '' or password.strip == None]

    # if username.strip() == '' or username == None:
    #   self.username = username
    #   self.password = password
    # else:
    #   self.username = username
    #   self.password = (password, self.generatePassword())[password.strip() == '' or password.strip == None]

  def generatePassword(self):
    '''
    generate random password
    '''

    import random, string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
