import asyncio
import os

import requests, random

a = ['socks4', 'socks5', 'http']


async def parse():
     for i in range(4):
        try:
            type = random.choice(a)
            a.remove(type)
        except IndexError:
            print('success!')
        responce = requests.get(f'https://openproxylist.xyz/{type}.txt').text
        responce2 =  requests.get(
            f'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-{type}.txt').text
        responce3 = requests.get(f'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/{type}.txt').text
        responce4 =  requests.get(f'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/{type}.txt').text
        responce5 =  requests.get(
            f'https://raw.githubusercontent.com/IshanSingla/ProxyLists/main/proxys/{type}.txt').text
        responce6 = requests.get(
            f'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/{type}.txt').text
        # временно не работает responce7 = requests.get(f'https://neversquad.xyz/v2/api?request=getproxy&hwid=FREE&proxy_type={type}').text
        responce8 = requests.get(f'https://proxyspace.pro/{type}.txt').text
        responce9 = requests.get(f'http://89.107.10.34/{type}').text.replace('u', '0').replace('l', '1').replace('o', '2').replace('d', '3').replace('v', '4').replace('z', '5').replace('j', '6').replace('q', '7').replace('w', '8').replace('e', '9'))
        f = open(f'proxys/{type}.txt', 'w')
        f.write(responce)
        f.write(responce2)
        f.write(responce3)
        f.write(responce4)
        f.write(responce5)
        f.write(responce6)
        #f.write(responce7)
        f.write(responce8)
        f.write(responce9)
        f.close()


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(parse())
]
ioloop.run_until_complete(asyncio.wait(tasks))
