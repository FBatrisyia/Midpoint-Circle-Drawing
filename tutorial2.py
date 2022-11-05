import matplotlib.pyplot as plt
import streamlit as st

def midpointCircleDrawing(x_center, y_center, radius):
  x = radius
  y = 0
  
  st.header("Midpoint Drawing Circle Algorithm")
  st.write("x = 0, y = 0, radius = 10)
  
  #Initial point
  st.write("(", x + x_center, ", ", y + y_center, ")", sep = "", end = "")

  # When radius is zero only a single
  # point be printed
  if(radius > 0):

    st.write("(", x + x_center, ", ", -y + y_center, ")", "(", y + x_center, ",", x + y_center, ")", "(", -y + x_center, ",", x + y_center, ")")

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

      st.write("(", x + x_center, ", ", y + y_center,")", "(", -x + x_center, ", ", y + y_center,")", 
               "(", x + x_center, ", ", -y + y_center,")", "(", -x + x_center, ", ", -y + y_center,")")

      if(x != y):
            st.write("(", y + x_center, ", ", x + y_center,")", "(", -y + x_center, ", ", x + y_center,")", 
                     "(", y + x_center, ", ", -x + y_center, ")", "(", -y + x_center, ", ", -x + y_center, ")")
  
if __name__=="__main__":
    midpointCircleDrawing(0, 0, 10)

