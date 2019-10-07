import pyperclip

class User():
  '''
  blueprint for user data
  '''

  def __init__(self, *, username=None, password=None):
    '''
    constructor for instantiating an empty object

    Args:
      username: users' username, must be unique
      password: users' passord
    '''

    if username.strip() == '' or username == None:
      self.username = username
      self.password = password
    else:
      self.username = username
      self.password = (self.generatePassword(), password)[password.strip() == '' or password.strip == None]

    

  def generatePassword(self):
    '''
    generate random password
    '''

    import random, string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
