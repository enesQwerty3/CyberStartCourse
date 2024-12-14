import math

def euclideanDistance(point1,  point2):
    if(type(point1) == tuple  and type(point2) == tuple):
        diffX  = abs(point1[0] - point2[0]) #x
        diffY = abs(point1[1] - point2[1]) #y
        return math.sqrt(diffX*diffX + diffY*diffY)

    else:
        return -1

points = []
points.append((4, 15))
points.append((6, 9))
points.append((1, 7))
points.append((7, 2))
points.append((10, 25))
points.append((0, 8))
print("points: ", points)
minDistance = 999999
distances = []
for i in range(len(points)):
    #print("i", i)
    for j in range(len(points) - i):
        if(j == i and i == 0):
            continue
        elif(j + i != len(points) and j + i != i):        
            #print("j+i", j+i)
            print(points[i])
            print(points[j + i], "\n**************")
            distance = euclideanDistance(points[i], points[i + j])
            print("distance", distance)
            distances.append(distance)
            if(distance < minDistance):
                minDistance = distance      #listeyi oluştururken minimumu bulursak tekrar for ile listeyi dönmeye gerek kalmaz
        
print("result: ", minDistance)