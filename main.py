from models.user.user import User

logged_in_user = None

def check_datafile_exists():
  '''
  checks if data file exists

  returns:
    True: if data file exists
    False: if data file doesn't exist
  '''
  try:
    open('data.txt').close()
    return True
  except FileNotFoundError:
    return False

def print_welcome_text():
  '''
  prints welcome text
  '''
  print('-' * 100)
  print('\t' * 5)
  print(' ' * 42 + 'PASSWORD LOCKER')
  print('\t' * 3)
  print(' ' * 20 + 'Manage your passwords across multiple social media platforms')
  print('\t' * 5)
  print('-' * 100)

def cli():
  '''
  acts as the main part of the program
  '''

  global logged_in_user

  while logged_in_user == None:
    authentication()
  else:
    print('you are in!')
    input()

def authentication():
  '''
  login or signup user
  '''
  
  global logged_in_user
  
  while True:
    print('Type in \'l\' to login')
    print('Type in \'s\' to signup')
    authenticate_decision = input().lower()

    if authenticate_decision == 'l':
      print('Enter your username and password')
      _username = input('username: ')
      print(type(_username) == 'str')
      _password = input('password: ')

      
      logged_in_user == User(username=_username, password=_password)
      print('bravo')
      break
    elif authenticate_decision == 's':
      while True:
        print('Enter your username and password')
        _username = input('username: ')
        _password = input('password: ')
        confirm_password = input('confirm password: ')

        if confirm_password == _password:
          logged_in_user = User(username=_username, password=_password)
          print('you are in! :D')
          break
        else:
          print('passwords don\'t much, try again')
    else:
      print('Not clear, please try again and enter the given options.')

def main():
  print_welcome_text()
  cli()
    
if __name__ == '__main__':
  main()
