import requests
import json

from six.moves import urllib


def get_pic_uri(uid):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid=107603{}&page={}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }
    page_num = 198
    print('==================当前是第' + str(page_num) + '页======================')
    while True:
        print('==================当前是第' + str(page_num) + '页======================')
        r = requests.get(url.format(uid, uid, page_num), headers=headers)
        data = json.loads(r.text)
        cards = data.get('data').get('cards')
        if len(cards) > 0:
            for card in cards:
                if card.get('card_type') == 9:
                    mblog = card.get('mblog')
                    if mblog:
                        retweeted_status = mblog.get('retweeted_status')
                        if retweeted_status:
                            pic_ids = retweeted_status.get('pic_ids')
                            print("------------------------" + str(
                                retweeted_status.get('created_at')) + "----------------------------")
                            if pic_ids:
                                for pic_id in pic_ids:
                                    picurl = 'https://wx2.sinaimg.cn/mw2000/' + pic_id + '.jpg'
                                    path = 'pic/' + str(page_num).zfill(5) + '_' + pic_id + '.jpg'
                                    print(picurl)
                                    re_down(picurl, path)
        else:
            break
        page_num += 1


def re_down(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
    except urllib.error.ContentTooShortError:
        print('Reloading...------------------------------------------------------------------')
        re_down(url, filename)


if __name__ == '__main__':
    get_pic_uri('2339808364')
