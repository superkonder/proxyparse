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
        f = open(f'proxys/{type}.txt', 'w')
        f.write(responce)
        f.write(responce2)
        f.write(responce3)
        f.write(responce4)
        f.write(responce5)
        f.write(responce6)
        #f.write(responce7)
        f.close()


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(parse())
]
ioloop.run_until_complete(asyncio.wait(tasks))
