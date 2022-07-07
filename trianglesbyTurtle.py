#Maya Anderson
#this program draws nested triangles


import turtle


def triangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)

        triangle(t, length/2)

def nestedTriangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length/2)


def main():
    n = int(input('Enter edge length: '))
    maya = turtle.Turtle()
    triangle(maya, n)

    carla = turtle.Turtle()
    nestedTriangle(carla, n)
                  
