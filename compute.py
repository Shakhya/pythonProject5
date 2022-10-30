class Figure:                                            #creating a new class.
    def __init__(self, count, name, area):               #used __int__ function.
        self.count = count
        self.name = name                                 #self parameters to access count, name and area.
        self.area = area
        print(count, '-', name, 'with area size', area)  #printing count , name and area.

data = [
    {"type": "Square", "area": 150.5},
    {"type": "Rectangle", "area": 80},
    {"type": "Rectangle", "area": 660},                  #using given list and assigning to variables.
    {"type": "Circle", "area": 68.2},
    {"type": "Triangle", "area": 20}
]

count=1                                                 #intialising count to 1.
for i in data:
    Figure(str(count), i["type"], i["area"])
    count += 1                                          #for loop to iterate data.

    


