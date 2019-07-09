from src.optimal_rod_cutter import OptimalRodCutter
from test.rod_cutter_test import (RodCutterTest, prices, RodCutter)
from timeit import Timer
import unittest
                                              
class OptimalRodCutterTest(RodCutterTest):
  
  def create_rod_cutter(self):
    self.rod_cutter = OptimalRodCutter()
    
  def compute_time(self, rod_class):
    rod_cutter = rod_class
    times = Timer(lambda: rod_cutter.cut_rod(15, prices))
    
    return times.timeit(number  = 1)

  def test_timing_of_both_algorithm_ensure_optimal_is_better_for_length_of_15(self):

    self.assertGreater(self.compute_time(RodCutter()), self.compute_time(OptimalRodCutter()) * 10)


if __name__ == '__main__':
  unittest.main()

