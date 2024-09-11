widgets = int(input("Number of widgets: ")) # Asks user for input and converts into an integer
gizmos = int(input("Number of gizmos: ")) # Asks user for input and converts into an integer
widgets_total = widgets * 75 # Calculate total widget weight with the input widgets from line 1
gizmos_total = gizmos * 112 # Calculate total gizmo with the input from line 2
print("The Total Weight of the Order:", gizmos_total + widgets_total) # Prints the total amount of weight by adding the widget total and gizmo total