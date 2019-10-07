import sys
sys.path.append('.')

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

def cli(logged_in_user):
  '''
  acts as the main part of the program
  '''
  while (logged_in_user != None):
    authentication()
  else:
    print('you are in!')
    input()
    logged_in_user = None

def authentication():
  '''
  login or signup user
  '''
  
  # while True:
  #   print('Type in \'l\' to login')
  #   print('Type in \'s\' to signup')
  #   authenticate_decision = input().lower()

  #   if authenticate_decision == 'l':
  #     print('Enter your username and password')
  #     username = input('username:')
  #     password = input('password:')
  #     print('bravo')
  #     break
  #   elif authenticate_decision == 's':
  #     print('Enter your username and password')
  #     username = input('username:')
  #     password = input('password:')
  #     confirm_password = input('confirm password:')
  #     print('you in')
  #     break
  #   else:
  #     print('Not clear, please try again and enter the given options.')

  #   break

def main():
  print_welcome_text()
  cli(logged_in_user)
    
if __name__ == '__main__':
  main()
