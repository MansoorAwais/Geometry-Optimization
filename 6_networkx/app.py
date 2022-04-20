from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    # "/createGraphy",
    "/Graph_network_gh",
    name = "Create Graph",
    inputs=[
        hs.HopsInteger("Count X", "X", "Number of node in X", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Count Y", "Y", "Number of node in Y", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0),
        hs.HopsNumber("radius", "R", "Radius of sphere", hs.HopsParamAccess.ITEM, default= 0.08),






    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST),
       hs.HopsBrep("Sphere Start","SS","1st Sphere in all nodes", hs.HopsParamAccess.ITEM),
       hs.HopsBrep("Sphere End","SE","Last Sphere in all nodes", hs.HopsParamAccess.ITEM),
    #    hs.HopsString("Quantity","NN","Number of Nodes", hs.HopsParamAccess.ITEM),
    #    hs.HopsString("Quantity","NE","Number of Edges ", hs.HopsParamAccess.ITEM),
    

    ]
)
def createGraph(X, Y, layout,R):

    G = geo.createGridGraph(X, Y)
    GW = geo.addRandomWeigrhs(G)

    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout) 


    sphere_start = rg.Sphere(nodes[0],R) 
    sphere_end = rg.Sphere(nodes[-1],R)
    sphere_start = rg.Sphere.ToBrep(sphere_start)
    sphere_end = rg.Sphere.ToBrep(sphere_end)
    # NN = len(nodes)
    # NN = str(NN)
    # NE = len(edges)
    # NE = str(NE)

    return nodes, edges , sphere_start ,sphere_end 





if __name__== "__main__":
    app.run(debug=True)