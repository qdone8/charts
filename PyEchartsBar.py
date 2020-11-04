from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import random

list2=[
    {"value":12,"percent":12/(12+3)},
    {"value":23,"percent":23/(23+21)},
    {"value":33,"percent":33/(33+5)},
    {"value":3,"percent":3/(3+52)},
    {"value":33,"percent":33/(33+43)}
]

list3=[
    {"value":3,"percent":3/(12+3)},
    {"value":21,"percent":21/(23+21)},
    {"value":5,"percent":5/(33+5)},
    {"value":52,"percent":52/(33+52)},
    {"value":43,"percent":43/(33+43)}
]

bar1=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .add_xaxis([1,2,3,4,5])
    .add_yaxis("product1",list2,stack='stack1',category_gap='50%')
    .add_yaxis("product2",list3,stack='stack1',category_gap="50%")
    .render('./echarts/bar1.html')
)




