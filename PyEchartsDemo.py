from pyecharts import options as opts
from pyecharts.charts import Bar,Pie,Funnel
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
import random

bar=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
    .add_xaxis(['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'])
    .add_yaxis('商家A',[5,30,23,45,25,40])
    .add_yaxis('商家B',[10,20,40,22,29,50])
    .add_yaxis('商家C',[100,26,29,89,59,200])
    .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'))
)
bar.render('./echarts/render.html')


bar1=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
    .add_xaxis(['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'])
    .add_yaxis('商家D',[random.randint(10,100) for _ in range(6)])
    .add_yaxis('商家E',[random.randint(10,100) for _ in range(6)])
    .add_yaxis('商家F',[random.randint(10,100) for _ in range(6)])
    .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'))
)
bar1.render('./echarts/renderC.html')


c = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("./echarts/pie_base.html")
)

d=(
    Funnel()
    .add('商品',[list(z) for z in zip(Faker.choose(),Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))
    .render("./echarts/funnel_base.html")
)
