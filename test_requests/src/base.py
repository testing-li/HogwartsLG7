import requests


class Base:
    # 类变量是指，多个实例、类可以共用这个变量
    token = None

    def __init__(self):
        if self.token is None:
            self.token = self.get_token()

    @staticmethod
    def get_token():
        corpid = 'wwe653983e4c732493'
        corpsecret = 'T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        # requests.get 代表发送 get 请求
        r = requests.get(url)
        # r.text 代表取原生返回值
        # print(r.text)
        # 　r.json 代表将原生格式转换为 json 格式
        access_token = r.json()["access_token"]
        return access_token

