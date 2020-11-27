# https://leetcode.com/contest/biweekly-contest-33/problems/thousand-separator
def thousandSeparator(self, n: int) -> str:
  res = []
  n = str(n)
  curr = ""
  for i in range(len(n)):
      curr += n[i]
      if ( len(n)- (i+1) ) % 3 == 0:
          res.append(curr)
          curr = ""
  return ".".join(res)
            
