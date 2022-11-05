import matplotlib.pyplot as plt

def midpointCircleDrawing(x_center, y_center, radius):
  x = radius
  y = 0

  #Initial point
  print("(", x + x_center, ", ", y + y_center, ")", sep = "", end = "")

  # When radius is zero only a single
  # point be printed
  if(radius > 0):

    #second quad
    print("(", x + x_center, ", ", -y + y_center, ")", sep = "", end = "")

    #third quad
    print("(", y + x_center, ",", x + y_center, ")", sep = "", end = "")

    #fourth quad
    print("(", -y + x_center, ",", x + y_center, ")", sep = "", end = "")

    #initializing p
    P = 1 - radius

    while(x > y):
      y += 1

      #Midpoint inside or on the perimeter
      if (P <= 0):
        P = P + 2 * y + 1

      #Midpoint outside the perimeter
      else:
        x =- 1
        P = P + 2 * y - 2 * x + 1

      if(x < y):
        break

      print("\n(", x + x_center, ", ", y + y_center,")", sep = "", end = "")
      print("(", -x + x_center, ", ", y + y_center,")", sep = "", end = "")
      print("(", x + x_center, ", ", -y + y_center,")", sep = "", end = "")
      print("(", -x + x_center, ", ", -y + y_center,")", sep = "", end = "")

      if(x != y):
            print("\n(", y + x_center, ", ", x + y_center,")", sep = "", end = "")
            print("(", -y + x_center, ", ", x + y_center,")", sep = "", end = "")
            print("(", y + x_center, ", ", -x + y_center, ")", sep = "", end = "")
            print("(", -y + x_center, ", ", -x + y_center, ")", sep = "", end = "")
  
if __name__=="__main__":
    midpointCircleDrawing(0, 0, 10)

