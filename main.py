import json
from models.user.user import User

logged_in_user = None
quit_from_authenticate = False
data = []

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
  global data

  with open('data.json') as json_file:
    data = json.load(json_file)
    print(len(data['users']))

  print_welcome_text()
  print('would you like to log in or sign up')

  while True:
    print('to log in, enter (l)')
    print('to sign up, enter (s)')
    print('to exit, enter (e)')
    login_or_signup = input()

    if login_or_signup.strip().lower() == 'l':
      print('Welcome back! =D')
      print('Type in your username and email')
      _username = input('username: ').strip()
      _password = input('password: ').strip()

      for user in data['users']:
        if user['username'] == _username:
          if user['password'] == _password:
            logged_in_user = User(username=user['username'], password=user['password'])
            print('You are in!')
            manage_credentials()
            break
          else:
            print('Password inserted is wrong. :( Please try again')
          continue

      print('User doesn\'t exist. Kindly sign up')
    elif login_or_signup.strip().lower() == 's':
      print('We are excited to have you join us! :) we will need your username and email')
      print('Type in your username and email')
      _username = input('username: ').strip()
      _password = input('password: ').strip()
      confirm_password = input('confirm password: ').strip()
      user_exists = False

      if _username == '' or _password == '':
        print('we couldn\'t get some or all of the information. Try type in all the requirements')
        continue
      else:
        for user in data['users']:
          if user['username'] == _username:
            user_exists = user['username'] == _username
            print('username exists, try another username.')
          
        if user_exists == False:
          if _password == confirm_password:
            data['users'].append({
              'username': f'{_username}',
              'password': f'{_password}'
            })

            with open('data.json', 'w') as outfile:
              json.dump(data, outfile)
            
            logged_in_user = User(username=_username, password=_password)
            print('Congrats, you are now one of us! =D')
            manage_credentials()
            break
          else:
            print('passwords don\'t match, try again')
    elif login_or_signup.strip().lower() == 'e':
      logged_in_user = None
      print('bye, have a great time...')
      break

if __name__ == '__main__':
  main()
