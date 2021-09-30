import unittest
from main import read_file, validate_data

class TestMain(unittest.TestCase):
    
    def test_read_file(self):
        ''' Testa a leitura do arquivo '''
        self.assertEqual(type(read_file()), list)

    def test_validate_data(self):
        ''' Testa o parse dos dados '''
        self.assertEqual(validate_data(), True)
    

unittest.main()