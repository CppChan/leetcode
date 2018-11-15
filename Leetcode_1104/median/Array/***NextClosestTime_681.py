# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.


class Solution(object):
  def nextClosestTime(self, T):
    Digit, T = list(set(T[:2] + T[3:])), list(T) 
    for i, lim in ((4, '9'), (3, '5'), (1, ['9', '3'][T[0] == '2']), (0, '2')): # limit for each position
        try:    T[i] = min(d for d in Digit if T[i] < d <= lim); break # success for one of the four position
        except: T[i] = min(Digit)# not succeed, substitue with a smallest digit.
    return ''.join(T)