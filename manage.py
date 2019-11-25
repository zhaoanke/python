# coding:utf-8
from flask_session import Session
from flask_wtf import CSRFProtect

import redis
from ihome import create_app

# 创建flask 的应用对象
app = create_app("develop")



# 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 利用flask-session，将session数据保存到redis中
Session(app)

# 为flask补充csrf防护
CSRFProtect(app)


@app.route("/index")
def index():
    session[] =
    session.get()
    return "index page"

if __name__ == '__main__':
    app.run()