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

def main():
  print_welcome_text()

if __name__ == '__main__':
  main()
