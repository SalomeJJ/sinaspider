# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from api.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/109-35","79985","d5d82a6f920c4b57b2149cec2c338e33" )
r.addBodyPara("channelId", "5572a108b3cdc86cf39001cd")
r.addBodyPara("channelName", "国内焦点")
r.addBodyPara("title", "")
r.addBodyPara("page", "1")
r.addBodyPara("needContent", "1")
r.addBodyPara("needHtml", "0")
r.addBodyPara("needAllList", "0")
r.addBodyPara("maxResult", "100")
r.addBodyPara("id", "")
# r.addFilePara("img", r"C:\Users\showa\Desktop\使用过的\4.png") #文件上传时设置
res = r.post()
#print(res.text) # 返回信息
f=open('res.txt','a',encoding='utf-8')
f.write(res.text)
f.close()