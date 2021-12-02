class Point():
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    ##For printing the object
    def __repr__(self):
        return "({}, {})".format(self.x,self.y)
    ##distance from origin
    def distance(self):
        return (self.x**2+self.y**2)**0.5
    ##Change the co-ordinate of the point based on the input
    def shift(self,val_x,val_y):
        self.x+=val_x
        self.y+=val_y
    ##Mirror the point
    def mirror(self):
        self.x=-(self.x)
        self.y=-(self.y)
    
if __name__=='__main__':
    p=Point(x=5.0,y=6.5)
    print("The point is: ",p)
    print(p.distance())
    p.shift(5.5,-3.5)
    print("The new point is: ",p)
    p.mirror()
    print("The point after mirroring: ",p)