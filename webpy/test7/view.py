import web
import config
import db
import os  

root = os.path.dirname(__file__)   #是我的电脑编译器的原因还是。。
path= root +"/templates/" #保险起见最好都加上绝对路径

datastr=''
t_globals =dict(
                datastr=web.datestr,
                )

render = web.template.render(path,cache=config.cache,globals = t_globals)
render._keywords["globals"]["render"]=render#这句话是不是定义不定义都一样

def listing(**k):
    l=db.listing(**k)
    return render.listing(l)
