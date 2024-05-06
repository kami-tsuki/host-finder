import os
import requests
import itertools

main_domains = ['test', 'dev', 'change', 'this']
extensions = ['com', 'net', 'shop', 'de', 'io']

hosts = ['.'.join(item) for item in itertools.product(main_domains, extensions)]

for host in hosts:
    response = os.system("ping -c 1 " + host)
    if response == 0:
        print(host, 'is up!')
        try:
            r = requests.get('http://' + host)
            if r.status_code == 200:
                print('Successfully got status code 200 from', host)
            else:
                print('Did not get status code 200 from', host, ', got', r.status_code, 'instead.')
        except requests.exceptions.RequestException as e:
            print('Could not make a request to', host, ', error:', e)
    else:
        print(host, 'is down!')
