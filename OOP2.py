from copy import copy
class Point():
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def __repr__(self):
        return '({}, {})'.format(self.x,self.y)
    
# class Rectangle():
#     def __init__(self,p1,p2):
#         self.point1=p1
#         self.point2=p2
#     def __repr__(self):
#         return '({}, {})'.format(self.point1,self.point2)
##In the above code there is a problem that a relation exists between rectangle and point classes. This is not desirable as we wouldn't want a rectangle with an upper left corner and a
##Lower right corner defined.
##So instead we can use a copy of the Point object to create the rectangle which will not alter the rectangle

class Rectangle():
    def __init__(self,p1,p2):
        self.point1=copy(p1)
        self.point2=copy(p2)
    def __repr__(self):
        return '({}, {})'.format(self.point1,self.point2)


if __name__=='__main__':
    p1=Point(3.5,5.5)
    p2=Point(4,7)
    print(p1,p2,sep='\n')
    r1=Rectangle(p1,p2)
    print(r1)
