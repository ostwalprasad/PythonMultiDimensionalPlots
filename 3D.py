
import pandas as pd



#Read cars data from csv
data = pd.read_csv("cars.csv")


#Make Plotly figure
import plotly
import plotly.graph_objs as go

fig1 = go.Scatter3d(x=data['curb-weight'],
                    y=data['horsepower'],
                    z=data['price'],
                    marker=dict(opacity=0.9,
                                reversescale=True,
                                colorscale='Blues',
                                size=5),
                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="curb-weight"),
                                yaxis=dict( title="horsepower"),
                                zaxis=dict(title="price")),)

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("3DPlot.html"))





