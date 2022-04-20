from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
# import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/Point_Cylinder",
    name = "Create Random Points",
    inputs=[
        # hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("R radius", "R", "radius of cylinder", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("H height", "H", "height of cylinder", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsPoint("Random Points","RP","List of generated random points ", hs.HopsParamAccess.ITEM),
       hs.HopsBrep("Random Cylinder","RC","List of generated random cylinder ", hs.HopsParamAccess.ITEM)
       
    ]
)
def createRandomPoints(x,y,z,radius,height):

    
    #create a point with rhino3dm
    random_pt = rg.Point3d(x, y, z)
    random_circle = rg.Circle(random_pt,radius)
    random_cylinder = rg.Cylinder(random_circle,height) 
    
    
    random_cylinder = rg.Cylinder.ToBrep(random_cylinder,True,True)

    return random_pt,random_cylinder







if __name__== "__main__":
    app.run(debug=True)