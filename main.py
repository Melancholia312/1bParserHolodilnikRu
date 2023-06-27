import requests
from bs4 import BeautifulSoup
import csv

COOKIES = {
    'region_position_nn': '55',
    'example_ab_test': '2',
    'clean': '1',
    'new_reg': '2',
    'HRUSIDSHORT': '97abf19e0140f45554d59a0433f487a9',
    'HRUSID': '3df2b4b212e6b81a9c043471e4395187',
    'HRUSIDLONG': 'fe10d688f2ea1dd99f0bd995e2af53d9',
    'csrfnews': 'b88b281cb26a873b10554d3716b3bd3c',
    'ab_home': '28',
    '_utmx': '3df2b4b212e6b81a9c043471e4395187',
    '_ym_uid': '1687801889233907518',
    '_ym_d': '1687801889',
    '_ym_isad': '1',
    '_gid': 'GA1.2.1839076561.1687801889',
    'banners_rotations': '1247',
    '_utmz': '8867f09b01f4ddaa550fe0dcbb4c764a08014735834052674cbd51114a1310d1',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'tmr_lvid': '68f697ed3806e7f0ad8facb16efbb315',
    'tmr_lvidTS': '1687801889666',
    '_userGUID': '0:ljd5o11g:k5T1aawFrxgbyfyuOSuJtXsTrXVuV_PF',
    'flocktory-uuid': '8a87507c-c057-4251-88df-d9cedfbe6d1c-2',
    'advcake_track_id': '82431585-e57e-0839-a1b5-122539612299',
    'advcake_session_id': '681844a6-7975-c705-c4e6-e64afaa63166',
    '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"1000247C"}',
    'referer': 'saratov.holodilnik.ru',
    'prod_id': '0',
    '_rcmx_session': 'a635185f-f124-4f77-b1ae-527c4e7bb277',
    'wtb_sid': 'null',
    '_defnice': '1',
    'hidden_banners_ids': '',
    'PHPSESSID': '893ec02bd961cf80c1ab9d886eab3b8b',
    'new_reg_show': '1',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'HruEMH': 'f111b12574c8146d2b710e52625ceb39',
    '_ym_visorc': 'b',
    '_dvs': '0:ljdsl7dm:6I_52x6PWcIMJIWU6ecgTxCFFyfI8xdw',
    'OrderUserType': '1',
    '__utmg': 'fafdb4644121d834465fa28d7ee9a29e',
    '__utmkx': '0',
    'dSesn': '2029cce5-cfc4-0d43-b621-ab40628cae77',
    'path': 'climatic',
    'tmr_detect': '1%7C1687844935310',
    '_gp1000247C': '{"hits":63,"vc":1,"ac":1,"a6":1,"utm":"-10a9fd8e"}',
    'pageviewTimer': '723.0409999999999',
    'page_hits': '93',
    'qrator_jsid': '1687844656.552.PtHoalWX63sLqnso-pho7ol16fqmc5bdhu84ljllrd6quk5tq',
    '_gat': '1',
    'action_blocks': '8885,8793',
    '_ga': 'GA1.1.394750356.1687801889',
    '_ga_EHP29G0JCQ': 'GS1.1.1687840388.4.1.1687845335.0.0.0',
    'mindboxDeviceUUID': 'b6911ce7-ca90-41f8-a3e1-3877eaefce28',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22b6911ce7-ca90-41f8-a3e1-3877eaefce28%22%7D',
}

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'region_position_nn=55; example_ab_test=2; clean=1; new_reg=2; HRUSIDSHORT=97abf19e0140f45554d59a0433f487a9; HRUSID=3df2b4b212e6b81a9c043471e4395187; HRUSIDLONG=fe10d688f2ea1dd99f0bd995e2af53d9; csrfnews=b88b281cb26a873b10554d3716b3bd3c; ab_home=28; _utmx=3df2b4b212e6b81a9c043471e4395187; _ym_uid=1687801889233907518; _ym_d=1687801889; _ym_isad=1; _gid=GA1.2.1839076561.1687801889; banners_rotations=1247; _utmz=8867f09b01f4ddaa550fe0dcbb4c764a08014735834052674cbd51114a1310d1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_lvid=68f697ed3806e7f0ad8facb16efbb315; tmr_lvidTS=1687801889666; _userGUID=0:ljd5o11g:k5T1aawFrxgbyfyuOSuJtXsTrXVuV_PF; flocktory-uuid=8a87507c-c057-4251-88df-d9cedfbe6d1c-2; advcake_track_id=82431585-e57e-0839-a1b5-122539612299; advcake_session_id=681844a6-7975-c705-c4e6-e64afaa63166; _gpVisits={"isFirstVisitDomain":true,"idContainer":"1000247C"}; referer=saratov.holodilnik.ru; prod_id=0; _rcmx_session=a635185f-f124-4f77-b1ae-527c4e7bb277; wtb_sid=null; _defnice=1; hidden_banners_ids=; PHPSESSID=893ec02bd961cf80c1ab9d886eab3b8b; new_reg_show=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; HruEMH=f111b12574c8146d2b710e52625ceb39; _ym_visorc=b; _dvs=0:ljdsl7dm:6I_52x6PWcIMJIWU6ecgTxCFFyfI8xdw; OrderUserType=1; __utmg=fafdb4644121d834465fa28d7ee9a29e; __utmkx=0; dSesn=2029cce5-cfc4-0d43-b621-ab40628cae77; path=climatic; tmr_detect=1%7C1687844935310; _gp1000247C={"hits":63,"vc":1,"ac":1,"a6":1,"utm":"-10a9fd8e"}; pageviewTimer=723.0409999999999; page_hits=93; qrator_jsid=1687844656.552.PtHoalWX63sLqnso-pho7ol16fqmc5bdhu84ljllrd6quk5tq; _gat=1; action_blocks=8885,8793; _ga=GA1.1.394750356.1687801889; _ga_EHP29G0JCQ=GS1.1.1687840388.4.1.1687845335.0.0.0; mindboxDeviceUUID=b6911ce7-ca90-41f8-a3e1-3877eaefce28; directCrm-session=%7B%22deviceGuid%22%3A%22b6911ce7-ca90-41f8-a3e1-3877eaefce28%22%7D',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

CATEGORIES = {
    'Климат': '/climatic/',
    'Холодильники': '/refrigerator/',
    'Телевизоры': '/tv_all/tv/',
    'Стиральные Машины': '/washers/'
}

BASE_URL = 'https://saratov.holodilnik.ru'


def get_html(url):
    r = requests.get(url, cookies=COOKIES, headers=HEADERS)
    return r


def get_content(html):
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def parse(url):
    html = get_html(url)
    print('...')
    if html.status_code == 200:
        content = get_content(html)
        return content
    else:
        return 'ERROR'


def get_goods_from_page(url):
    goods_dict = {}
    content = parse(url)

    if content == 'ERROR':
        return goods_dict

    goods = content.find_all('div', class_='goods-tile preview-product')
    for good in goods:
        name = good.find('span', itemprop='name').text
        price = good.find('div', class_='price__value').text
        goods_dict[name] = price

    return goods_dict


def get_all_goods(url, page_count):
    all_goods = {}
    for page in range(1, page_count + 1):
        if page == 1:
            all_goods.update(get_goods_from_page(url))
            continue
        full_url = url + '?page=' + str(page)
        all_goods.update(get_goods_from_page(full_url))
    return all_goods


def write_to_csv(url, page_count):
    records = get_all_goods(url, page_count)

    with open('products.csv', 'w', encoding='UTF8') as f:
        w = csv.DictWriter(f, records.keys())
        w.writeheader()
        w.writerow(records)


def get_last_page_number(url):
    content = parse(url)

    if content == 'ERROR':
        return 0

    all_links = content.find_all('a', class_='page-link')
    if len(all_links) <= 3:
        return 1
    return all_links[-2].text


def ui():
    print('Категории: ' + ', '.join(CATEGORIES.keys()))
    user_category = input("Введите название категории: ").title()
    if user_category not in CATEGORIES.keys():
        print("Такой категории нет")
        return

    print("Идет подготовка вашего файла. Пожалуйста, подождите...")
    user_url = BASE_URL + CATEGORIES[user_category]
    write_to_csv(user_url, int(get_last_page_number(user_url)))
    print("Готово")


ui()

