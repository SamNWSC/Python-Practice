# asks the user for pole lap and and their own laptime1
pole_lap= float(input("What was the pole lap in seconds"))
your_lap = float(input("What was your lap in seconds"))
# finds the difference 
difference = your_lap - pole_lap 
# prints difference 
print("{} seconds was the gap to pole".format(difference)) 