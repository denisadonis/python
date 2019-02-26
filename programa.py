class Vector():
  """Clase vector"""
  def __init__(self, valores=[]):    
    self.valores = valores

  def suma(self, vector2):
    v_temp = []

    if len(self) == len(vector2):
      for i in range(len(self)):
        v_temp.append(self.valores[i] + vector2.valores[i])

    return Vector(v_temp)

  def producto_punto(self, vector2):
    res = 0

    if len(self) == len(vector2):
      for i in range(len(self)):
        res += self.valores[i] * vector2.valores[i]

    return res
  
  def __len__(self):
    return len(self.valores)

  def __str__(self):
    return self.valores.__str__()


if __name__ == '__main__':
  v1 = Vector([1,2,3])
  v2 = Vector([4,5,6])
  v3 = v1.suma(v2)
  print(v3)
  print(type(v3))
  v4 = v1.producto_punto(v2)
  print(v4)
    
