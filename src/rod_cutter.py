class RodCutter:

  def cut_rod(self, length, prices):

    if length is 0:
      return 0, []

    max_price = prices.get(length, 0)
    max_cuts = [length]

    for rods in range(1, length):

      max_price_for_split_1, max_cuts_for_split_1 = self.cut_rod(rods, prices)
      max_price_for_split_2, max_cuts_for_split_2 = self.cut_rod(length - rods, prices)

      if max_price_for_split_1 + max_price_for_split_2 > max_price:
        max_price = max_price_for_split_1 + max_price_for_split_2
        max_cuts = max_cuts_for_split_1 + max_cuts_for_split_2

    return max_price, max_cuts
  
