# coding=utf-8

from CCPRestSDK import REST
# import ConfigParser

# 主帐号
accountSid = '8a216da86f17653b016f3c27a7be1a76'

# 主帐号Token
accountToken = '3dbe86c146f9419eb239fd277b856f6c'

# 应用Id
appId = '8a216da86f17653b016f3c27a8321a7d'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'


# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id


class CCP(object):
    """自己封装的发送短信的辅助类"""
    # 用来保存对象的类属性
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance

    def send_Template_sms(self, to, datas, temp_Id):
        # 初始化REST SDK
        result = self.rest.sendTemplateSMS(to, datas, temp_Id)
        # for k, v in result.items():
        #
        #     if k == 'templateSMS':
        #         for k, s in v.items():
        #             print('%s:%s' % (k, s))
        #     else:
        #         print('%s:%s' % (k, v))
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示短信发送成功
            return 0
        else:
            # 表示短信发送失败
            return -1

            # sendTemplateSMS(手机号码,内容数据,模板Id)


if __name__ == "__main__":
    ccp = CCP()
    # 1代表模板ID，下载SDK的官网api文档有说明
    # 这里填测试号码 免费发送短信  填的不是测试号码收短信费用
    ret = ccp.send_Template_sms("18512548414", ["520wyl", "zak"], 1)
    print(ret)
