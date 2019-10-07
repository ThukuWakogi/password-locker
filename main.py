from models.user.user import User

logged_in_user = None
quit_from_authenticate = False

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

def manage_credentials():
  while True:
    print('credentials are coming soon')
    input()
    break

def main():
  global logged_in_user
  global quit_from_authenticate
  print_welcome_text()

  while True:
    print('would you like to log in or sign up')
    print('to log in, enter (l)')
    print('to sign up, enter (s)')
    print('to exit, enter (e)')
    login_or_signup = input()

    if login_or_signup.strip().lower() == 'l':
      print('Welcome back! =D')
      print('Type in your username and email')
      _username = input('username: ').strip()
      _password = input('password: ').strip()

      if _username == 'user' or _password == 'user':
        print('you are in! =D')
        manage_credentials()
      else:
        print('oops! either the password or username is invalid. please try again')
        continue
    elif login_or_signup.strip().lower() == 's':
      print('We are excited to have you join us! :) we will need your username and email')
      print('Type in your username and email')
      _username = input().strip()
      _password = input().strip()
      if _username == 'user' or _password == 'user':
        print('we couldn\'t get some or all of the information. Try type in all the requirements')
        continue
      else:
        print('oops! either the password or username is invalid. please try again')
        continue
    elif login_or_signup.strip().lower() == 'e':
      print('bye, have a great time...')
      break

    
if __name__ == '__main__':
  main()
