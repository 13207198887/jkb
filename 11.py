import requests

burp0_url = "http://www.bugzero.cn:80/a/login"
burp0_cookies = {"Hm_lvt_cf49a60363f5b0477076111dbd3a4b90": "1601541967,1602941023", "pageNo": "1", "pageSize": "12", "JSESSIONID": "2B82120BDF5AA392191B46DE5A8BD2B0", "jeesite.session.id": "f6b3e6c91b97439d93d56bb0a422b70e", "Hm_lpvt_cf49a60363f5b0477076111dbd3a4b90": "1602971883"}
burp0_headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Origin": "http://www.bugzero.cn", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36", "DNT": "1", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Referer": "http://www.bugzero.cn/index/login.html", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh,zh-CN;q=0.9", "Connection": "close"}
burp0_data = {"username": "17095936094", "password": "qq960201567", "validateCode": ''}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
