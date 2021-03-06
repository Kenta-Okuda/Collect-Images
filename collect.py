# -*- coding:utf-8 -*-
import json
import os
import urllib2
from google_keys import key_dict

key_dict = key_dict

def url_search(keyword, count):
    # 画像urlを取得
    img_urls = []
    base_url = "https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&searchType=image&q={2}&num=10&start={3}"
    # 1回で10個までしか取得できない
    for i in range(count):
        start_index = i*10+1
        url = base_url.format(key_dict["api_key"], key_dict["engine_id"], keyword, start_index)
        res = urllib2.urlopen(url)
        data = json.load(res)
        img_urls += [result["link"] for result in data["items"]]

    return img_urls


def url_download(urls, dl_path):
    #urlから画像をフォルダにダウンロード
    print("Start downloading.")
    possible_exts = [".png", ".jpg", ".jpeg"]
    img_index = 0
    opener = urllib2.build_opener()
    if os.path.exists(dl_path) == False:
	os.mkdir(dl_path)
    for url in set(urls):
        try:
	    print(str(img_index)+": "+url)
            file_name, ext = os.path.splitext(url)
            if ext not in possible_exts:
                continue
            req = urllib2.Request(url, headers={"User-Agent": "Magic Browser"})
            img_file = open("./"+dl_path+"/"+str(img_index)+ext, "wb")
            img_file.write(opener.open(req).read())
            img_file.close()
            img_index += 1

        except:
            continue


def main():
    print("本当に実行しますか？ y/n")
    if raw_input().strip() != "y":
        sys.exit()
    keyword = "KEYWORD"
    count = 1
    dl_path = "images"
    urls = url_search(keyword, count)
    url_download(urls, dl_path)
    print("Done.")

if __name__ == '__main__':
    main()
