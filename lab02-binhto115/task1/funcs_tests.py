import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      self.assertEqual(funcs.f(1.0), 9.0)
      self.assertEqual(funcs.f(2.0), 32.0)

   def test_f_2(self):
      self.assertEqual(funcs.g(2.0, 2.0), 8.0)
      self.assertEqual(funcs.g(3.0, 3.0), 18.0)

   #self.fail("Test not implemented")

   def test_f_3(self):
      self.assertEqual(funcs.hypotenuse(0, 0), 0.0)
      self.assertEqual(funcs.hypotenuse(1, 1), 1.4142135623730951)

   def test_f_4(self):
      self.assertTrue(funcs.is_positive(2.0))
      self.assertFalse(funcs.is_positive(-1.0))
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
