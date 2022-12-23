from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
line = Line()

line.add_xaxis(["明显提升", "有提升", "无提升"])
line.add_yaxis("", [0.51, 0.401, 0.089])

line.set_global_opts(
    title_opts=TitleOpts(title="心理健康", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render()