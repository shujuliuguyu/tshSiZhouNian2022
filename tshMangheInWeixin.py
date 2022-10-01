import requests
import time
import re

urlRaw='http://app.akb48-china.com/mysterybox/mysterybox/index/'
# i=1
sum = 0
for i in range(1,49):
    res=requests.get(urlRaw+str(i),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63070517)','Cookie':'akb48_session=e9c148db109be1156d4fa208712d579dc189d4d8; wx_userinfo=12a8bcc6a7b09d793a9a3a559d60a48193cb3e5ab15c6e78f4cdb6f5e99e499dfe66c0a651488ad357564981a6548ecb156f0e6a49241696f036275f85d78b05H8TiwZMDJVWffXtIrjieT%2BpQ7BykdzV%2FUxt6lCnjfUV8oWzQnRS6YQqsmTGl9zGolC5IFLYct7W3Oy9nJDrR7Q5Kgo1S5mPCDty3KxtMD8TN8iDjMFNOPRr30jDX9n5%2BXwRCZvWuFSVmrhqqe6OVNx0cbNwras8onOpd6t9WqR9u4EnWz95I3sHgjAII8mhyyRFGzrx3KsfFpOTRGoQVPrHLHpENExdQusGcY7ahVU3FXuv6jFHo1Ahe%2FYWVHRdNvLPyqJhvkF%2BSphRYakXITCyKLOWnDdYcP%2BYkCuvSEX8MFrBUykHudRnemd%2BGcWrw1tiGZXpsRMGe%2BPLlLMZD5RT3qttiB0gm%2B8f9QLuFgAi3RCqUhG0BDUYsO19mCyW7NplzhHnezc5p9T7HODD5WufYTJ0Cp3U2GbZdQ4p5bHsZBgx4xOsrHRCY5j8ZvE%2FVSZUWHAe%2Bl%2BJXWwhOPac7Aw%3D%3D; Hm_lvt_8b11cd3c1c69771937bd932a040aeb2c=1664529658; Hm_lpvt_8b11cd3c1c69771937bd932a040aeb2c=1664529907'})
    # print(res.text)
    name=re.findall('<div>《Four你心中的歌》盲盒 - (.+?) 版本</div>', res.text)
    muqiandijixiang=re.findall('目前是第(.+?)箱', res.text)
    benxiangshengyujifen=re.findall('本箱剩余(.+?)份', res.text)
    maichuduoshao=100*int(muqiandijixiang[0])-int(benxiangshengyujifen[0])
    # print(name[0]+" "+muqiandijixiang[0]+" "+benxiangshengyujifen[0]+" "+str(maichuduoshao))
    print(name[0]+" "+str(maichuduoshao))
    sum+=48*int(maichuduoshao)
print("盲盒总共卖出多少钱："+str(sum))
print("制表时间："+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
