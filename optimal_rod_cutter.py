from src.rod_cutter import RodCutter

class OptimalRodCutter(RodCutter):
  def __init__(self):
    super().__init__()
    self.rod_cutter_cache = {}
    
  def cut_rod(self, length, prices):
    if length not in self.rod_cutter_cache:
      self.rod_cutter_cache[length] = super().cut_rod(length, prices)
  
    return self.rod_cutter_cache[length]

