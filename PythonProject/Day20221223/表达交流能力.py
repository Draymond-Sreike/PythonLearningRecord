from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
line = Line()

line.add_xaxis(["明显提升", "有提升", "无提升"])
line.add_yaxis("", [0.523, 0.385, 0.092])

line.set_global_opts(
    title_opts=TitleOpts(title="表达交流能力", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render()