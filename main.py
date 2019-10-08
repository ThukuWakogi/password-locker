import json
from models.user.user import User
from models.credential.credential import Credential

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
  global logged_in_user
  print('What would you like to do with your credentials? =D')

  while True:
    print('enter (v) to view credentials')
    print('enter (a) to add credentials')
    print('enter (e) to edit credentials')
    print('enter (d) to delete credentials')
    print('enter (x) to go back')
    credential_action = input()

    if credential_action == 'v':
      if len(logged_in_user.credentials) > 0:
        for credential in logged_in_user.credentials:
          print(f'{credential.credentialCategory} {credential.credentialUsername} {credential.credentialPassword}')
          print('that\'s all :)')
      else:
        print('lol, you don\'t have any credentials.')
    elif credential_action == 'a':
      print('this are the social platforms available')

      for index, social_platform in data['credentialCategory']:
        print(f'{index}: {social_platform}')
      
      category_choice = input().strip().lower()
    elif credential_action == 'e':
      print('you will edit credentials. soon enough :)')
    elif credential_action == 'd':
      print('you will delete credentials. you will')
      print('you will')
      print('soon')
      print(':)')
    elif credential_action == 'x':
      print('cool... logging you out')
      break
    else:
      print('You input doesn\'t look right. please try again :)')

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
            logged_in_user = User(username=user['username'], password=user['password'], credentials=user['credentials'])
            print('You are in!')
            print(logged_in_user)
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
              'password': f'{_password}',
              'credentials': []
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
