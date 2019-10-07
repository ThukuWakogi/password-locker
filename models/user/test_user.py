import unittest
from user import User

class TestUser(unittest.TestCase):
  '''
  tests if all user functionality works
  '''

  def setUp(self):
    '''
    set up method to run before each use case
    '''

    self.user = User(username='wayne', password='rockfeller')

  def test_init(self):
    '''
    tests if the object initializes
    '''
    
    self.assertEqual(self.user.username, 'wayne')
    self.assertEqual(self.user.password, 'rockfeller')

if __name__ == '__main__':
  unittest.main()
