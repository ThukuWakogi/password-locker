import pyperclip

class User():
  '''
  blueprint for user data
  '''

  def __init__(self, username, password):
    '''
    constructor for instantiating an empty object

    Args:
      username: users' username, must be unique
      password: users' passord
    '''

    self.username = username
    self.password = (self.generatePassword(), password)[password.trim() == '' or password.trim == None]

  def generatePassword(self):
    '''
    generate random password
    '''

    import random, string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    