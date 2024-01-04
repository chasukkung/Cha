class Position:
   top = 0
   left = 0

   def __init__(self,x,y):
      self.left = x
      self.top = y
   def move(self, offset_x, offset_y):
       self.left += offset_x
       self.top += offset_y


dot1 = Position(100, 200)
print(f"Top={dot1.top},left={dot1.left}")
dot1.move(-10,30)
print(f"Top={dot1.top},left={dot1.left}")