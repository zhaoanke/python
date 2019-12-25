# coding:utf-8
from flask import Blueprint

# 创建蓝盘对象
api = Blueprint("api_1_0", __name__)

# 导入蓝图的视频
from . import index, verify_code
