import holoviews as hv
from holoviews import opts, dim
hv.extension('bokeh')
import panel


def build_map():
    sankey = hv.Sankey([
        ['A', 'X', 5],
        ['A', 'Y', 7],
        ['A', 'Z', 6],
        ['B', 'X', 2],
        ['B', 'Y', 9],
        ['B', 'Z', 4]]
    )
    map = sankey.opts(width=600, height=400)

    chart = panel.panel(map, widget_location='bottom')
    #chart.embed()
    chart.save("dashboard.html", embed=True)

build_map()