class frac:
    def __init__(self, num=1, den=1):
        self.num = num
        self.den = den

    def fracmul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den

        return self
    
    def fracdiv(self, a, b):
        self.num = a.num * b.den
        self.den = a.den * b.num

        return self
    
    def fracsub(self, a, b):
        self.num = (a.num * b.den) - (a.den * b.num)
        self.den = a.den * b.den
        return self
    

def gauss(a):
    
  from fractions import Fraction
  

  #augment
  dim = len(a[0])
  copythat = [0]*dim
  for i in range(len(a)):
      li = [frac(0, 1)]*dim
      li[i] = frac()
      copythat[i] = li

    

  #elimination
  for i in range(len(a)-1):
      for j in range(i+1, len(a)):
          
          if a[j][i].num != 0:
              e = frac()
              multiplier = e.fracdiv(a[j][i], a[i][i])
              
              for k in range(i, len(a)):
                  
                  c = frac()
                  d = frac()
              
                  a[j][k] = c.fracsub(a[j][k], d.fracmul(multiplier, a[i][k]))
                  reduced = Fraction(a[j][k].num, a[j][k].den)
                  a[j][k] = frac(reduced.numerator, reduced.denominator)
                  
          
              
              for k in range(0, len(a)):
                  #a[j][k] = frac()
                  c = frac()
                  d = frac()
                  
                  copythat[j][k] = c.fracsub(copythat[j][k], d.fracmul(multiplier, copythat[i][k])) 
                  
                  reduced = Fraction(copythat[j][k].num, copythat[j][k].den)
                  copythat[j][k] = frac(reduced.numerator, reduced.denominator)
  


  # Normalization
  normalizers = [0]*dim
  for i in range(len(a)):
      normalizers[i] = a[i][i]
      for j in range(len(a)):
          g = frac()
          copythat[i][j] = g.fracdiv(copythat[i][j], normalizers[i])

          reduced = Fraction(copythat[i][j].num, copythat[i][j].den)
          copythat[i][j] = frac(reduced.numerator, reduced.denominator)
          #a[i][j] = g.fracdiv(a[i][j], normalizers[i])
  for i in range(len(a)):
      #normalizers[i] = a[i][i]
      for j in range(i, len(a)):
          g = frac()
          a[i][j] = g.fracdiv(a[i][j], normalizers[i])

          reduced = Fraction(a[i][j].num, a[i][j].den)
          a[i][j] = frac(reduced.numerator, reduced.denominator)
  
  
 
  #backsubstitution
  for i in reversed(range(1, len(a))):
      for j in range(0, i):
          if a[j][i].num != 0:
              #e = frac()
              multiplier = a[j][i]
              #print (multiplier.num/multiplier.den)
              for k in range(i, len(a)):
                  #a[j][k] = frac()
                  c = frac()
                  d = frac()
              
                  a[j][k] = c.fracsub(a[j][k], d.fracmul(multiplier, a[i][k]))

                  reduced = Fraction(a[j][k].num, a[j][k].den)
                  a[i][j] = frac(reduced.numerator, reduced.denominator)
                  #print a[j][k].num, j, k, d.num, e.num
          
              if copythat[i][i].num != 4.8:
                  #e = frac()
                  #multiplier = e.fracdiv(copythat[j][i], copythat[i][i])
                  for k in range(0, len(a)):
                      #a[j][k] = frac()
                      c = frac()
                      d = frac()
                      e = frac()
                      copythat[j][k] = c.fracsub(copythat[j][k], d.fracmul(multiplier, copythat[i][k]))
                      #print (copythat[j][k].num/copythat[j][k].den, j, k, d.num, e.num)

                      reduced = Fraction(copythat[j][k].num, copythat[j][k].den)
                      copythat[j][k] = frac(reduced.numerator, reduced.denominator)
  
  
  return copythat
