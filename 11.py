# -*- coding:utf-8 -*-
import requests

burp0_url = "http://bugzero.cn:80/a/login"
burp0_cookies = {"jeesite.session.id": "c74fe9b853d442ae800eab58449b115b", "rememberMe": "deleteMe", "Hm_lvt_cf49a60363f5b0477076111dbd3a4b90": "1600862681", "Hm_lpvt_cf49a60363f5b0477076111dbd3a4b90": "1602965724", "JSESSIONID": "D2A6565D8D8ADFB6BDC96639FDA26F3A"}
burp0_headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://bugzero.cn", "Referer": "http://bugzero.cn/index/login.html", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
