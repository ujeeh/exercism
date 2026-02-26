def equilateral(sides):
    is_equilateral = False
    if sides[0] and sides[1] and sides[2] > 0:
        if sides[0]== sides[1] and sides [1] == sides[2]:
            is_equilateral = True
    return is_equilateral


def isosceles(sides):
    is_isoceles = False
    if sides[0] + sides[1] > sides[2] and sides[2] + sides[1] > sides[0] and sides[0] + sides[2] > sides[1]:
        if sides[0] and sides[1] and sides[2] > 0:
            if sides[0] == sides[1] or sides[0] == sides [2]:
                is_isoceles = True
            elif sides[1] == sides[2]:
                is_isoceles = True
    return is_isoceles


def scalene(sides):
     is_scalene = False
     if sides[0] + sides[1] > sides[2] and sides[2] + sides[1] > sides[0] and sides[0] + sides[2] > sides[1]:
        if sides[0] and sides[1] and sides[2] > 0:
            if sides[0] != sides[1] and sides[0] != sides [2] and sides[1] != sides[2]:
                is_scalene = True
     return is_scalene

