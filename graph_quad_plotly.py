# Import dependencies
import plotly
import plotly.graph_objs as go
import numpy as np

data_quad = np.genfromtxt('data_quad.csv', delimiter=',')
x, y, z = data_quad.T

# Configure Plotly to be rendered inline in the notebook.
plotly.offline.init_notebook_mode()

# Configure the trace.
trace = go.Scatter3d(
    x = x, # h
    y = y, # a
    z = z, # T
    mode='markers',
    marker={
        'size': 5,
        'opacity': 0.5,
    }
)

# Configure the layout.
layout = go.Layout(
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0}
)

data = [trace]

plot_figure = go.Figure(data=data, layout=layout)

# Render the plot.
plotly.offline.iplot(plot_figure)