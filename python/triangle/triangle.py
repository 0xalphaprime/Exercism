

def equilateral(sides):
    for i in sides:
        if i == 0:
            return False
        elif i > sum(sides) - i:
            return False

    if sides[0] == sides[1] == sides[2]:
        return True
    else:
        return False    



def isosceles(sides):
    for i in sides:
        if i == 0:
            return False
        elif i > sum(sides) - i:
            return False

    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    else:
        return False


def scalene(sides):
    for i in sides:
        if i == 0:
            return False
        elif i > sum(sides) - i:
            return False
    
    if isosceles(sides) == False and equilateral(sides) == False:
        return True
    else:
        return False
        
