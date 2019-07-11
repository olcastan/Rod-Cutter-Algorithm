from src.rod_cutter import RodCutter
import unittest

prices = {1: 1, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 5, 8: 9, 9: 9, 10: 10}


class RodCutterTest(unittest.TestCase):
  
  def create_rod_cutter(self):
    self.rod_cutter = RodCutter()

  def setUp(self):
    self.create_rod_cutter()

  def test_canary_test(self):
    self.assertTrue(True)

  def test_rod_of_length_0(self):

    self.assertEqual((0, []), self.rod_cutter.cut_rod(0, prices))

  def test_rod_of_length_1(self):

    self.assertEqual((1, [1]), self.rod_cutter.cut_rod(1, prices))

  def test_rod_of_length_2(self):

    self.assertEqual((2, [1, 1]), self.rod_cutter.cut_rod(2, prices))

  def test_rod_of_length_3(self):

    self.assertEqual((3, [1, 1, 1]), self.rod_cutter.cut_rod(3, prices))

  def test_rod_of_length_5(self):

    self.assertEqual((5, [1, 1, 1, 1, 1]), self.rod_cutter.cut_rod(5, prices))

  def test_rod_of_length_10(self):

    self.assertEqual((11, [1, 1, 8]), self.rod_cutter.cut_rod(10, prices))

  def test_rod_of_length_11(self):

    self.assertEqual((12, [1, 1, 1, 8]), self.rod_cutter.cut_rod(11, prices))

  def test_rod_of_length_14(self):

    self.assertEqual((15, [1, 1, 1, 1, 1, 1, 8]), self.rod_cutter.cut_rod(14, prices))
    
if __name__ == '__main__':
  unittest.main()


