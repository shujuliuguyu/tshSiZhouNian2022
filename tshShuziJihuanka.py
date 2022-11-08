import requests

urlRaw='https://api.bilibili.com/x/vas/nftcard/cardlist?act_id='

for i in range(6,14):
    res=requests.get(urlRaw+str(i))
    resData=res.json()
    for j in range(0,36):
        # print(resData['data']['round_list'][0]['card_list'][j]['card_name'])
        # print(resData['data']['round_list'][0]['card_list'][j]['card_img'])
        print(resData['data']['round_list'][0]['card_list'][j]['card_name'],resData['data']['round_list'][0]['card_list'][j]['card_img'])
    for k in range(0,6):
        # print(resData['data']['pre_list'][k]['card_name'])
        # print(resData['data']['pre_list'][k]['card_img'])
        print(resData['data']['pre_list'][k]['card_name'],resData['data']['pre_list'][k]['card_img'])