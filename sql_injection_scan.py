#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import requests
import re

url = 'http://testphp.acunetix.com/artists.php?artist=2'

padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)

injecao = padrao.groups()[0] + '\''

print injecao

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

req = requests.get(injecao, headers=header)

html = req.text

if 'mysql_fetch_array()' in html:
    print 'Vulneravel'
else:
    print 'NAO vulneravel'