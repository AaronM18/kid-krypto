"""
 Criptografía FI, UNAM
 Aarón Mejia Ortiz
 30.3.2020
 """

DEBUG = False
DEBUG_TEST = False

def getInput(lines = []):
  """ 
    Gets input from file input. Returns list of lines from input file
  """
  import fileinput
  return [ line.strip('\n') for line in fileinput.input() ]

class KidKrypto:

  def __init__(self):
    self.public = (0,0)
    self.private = 0

  def initNumbers(self):
    import random
    return [ random.randint(1,10)  for i in range(4) ]

  def setup(self, random: bool, a=0, b=0, A=0, B=0) -> None:
    if random:
      a, b, A, B = self.initNumbers()

    m = a * b - 1
    e = A * m + a
    d = B * m + b
    n = (e * d - 1) // m
    DEBUG and print('m', m,'e', e,'d', d,'n', n)
    self.public = (n, e)
    self.private = d

    return 

  def encrypt(self, x: int) -> int:
    y = (x * self.public[1]) % self.public[0]
    return y

  def decrypt(self, y: int) -> int:
    x = (y * self.private) % self.public[0]
    return x

  def getKeys(self) -> None:
    print('Public', self.public)
    print('Private', self.private)

def test():
  test_vectors = [
    (3, 4, 5, 6, 200, 161),
    (3, 4, 5, 6, 650, 62),
    (9, 11, 5, 8, 1028, 572),
    (9, 11, 5, 8, 54, 2546),
    (47, 22, 11, 5, 12223, 13268),
    (47, 22, 11, 5, 4356, 28929),
  ] # a,b A, B, plan, cipher
  kk = KidKrypto()

  
  for index, vector in enumerate(test_vectors):
    a, b, A, B, plainText, cipherText = vector
    
    print('='*20)
    print( str(index) + '. ', a, b, A, B, plainText, cipherText)
    
    kk.setup(False, a=a, b=b, A=A, B=B)
    
    DEBUG_TEST and kk.getKeys()
    
    en_res = kk.encrypt(plainText)
    de_res = kk.decrypt(cipherText)

    print('Encript: ', 'sucess' if en_res == cipherText else 'failed', '<'+str(en_res)+'>')
    print('Encript: ', 'sucess' if de_res == plainText else 'failed', '<'+str(de_res)+'>')

def main():
  lines = getInput()
  op, a, b, A, B, message = lines

  kk = KidKrypto()
  kk.setup(False, a=int(a), b=int(b), A=int(A), B=int(B))

  if op == 'E':
    print(kk.encrypt(int(message)))
  if op == 'D':
    print(kk.decrypt(int(message)))

main() if __name__ == "__main__" else None
