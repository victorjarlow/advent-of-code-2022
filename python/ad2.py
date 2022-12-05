## Input handling
input=[]
with open('input2.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        input.append(line.split())

## Constants
WIN = 6
DRAW = 3
LOSE = 0

## Shape-Classes
class Rock():
    def beats(self, other):
        return isinstance(other, Scissors)
class Paper():
    def beats(self, other):
        return isinstance(other, Rock)
class Scissors():
    def beats(self, other):
        return isinstance(other, Paper)
    
shapeOf = {1: Rock(), 2: Paper(), 3: Scissors()} #helper

## Program logic
def points(opponent, me):
    opponent=ord(opponent)-64 #A = 1, B = 2, C = 3
    me=ord(me)-87 #X = 1, Y = 2, Z = 3
    if shapeOf[me].beats(shapeOf[opponent]) and not shapeOf[opponent].beats(shapeOf[me]):
        return WIN + me
    elif shapeOf[opponent].beats(shapeOf[me]) and not shapeOf[me].beats(shapeOf[opponent]):
        return LOSE + me
    else:
        return DRAW + me

def main():
    res = list(map(lambda x: points(x[0],x[1]), input))
    print(sum(res))
   
main()


#Extension: given a list of opponent shapes, find all ways to lose x rounds.