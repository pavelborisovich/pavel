#sudo pip3 install requests
import requests
#sudo pip3 install BeautifulSoup4
#sudo pip3 install bs4
from bs4 import BeautifulSoup as BS
import os
s = requests.Session()

auth_html = s.get('http://tgym.ru/users/login/')
auth_bs = BS(auth_html.content, 'html.parser')
csrf = auth_bs.select('input[name=authenticity_token]')[0]['value']

payload = {
    'utf8': '"✓"',
    'authenticity_token': csrf,
    'user[login]': 'your_login', # input('Введите пожалуйста логин ): 
    'user[password]': 'your_password', #input('Введите пожалуйста пароль: )'
    'user[remember_me]': "1",
    'commit': "Вход"
}

answ = s.post('http://tgym.ru/users/login/', data = payload)
anw_bs = BS(answ.content, 'html.parser')

a = anw_bs.find('div', class_ = 'login_anchor')
b = a.find('a').text

# print(b)

test = s.get('http://tgym.ru/skeds')
test_ = BS(test.content, 'html.parser')

text = open('text.txt', 'w')
text.write(str(test_))
text.close()
lala = test_.find_all('a', class_ = 'button btn btn-sm btn-outline-danger')
href = lala[-1].get('href')
url = ['http://tgym.ru' + href]
def get_file(url):
    response = requests.get(url, stream=True)
    return response
def save_data(name, file_data):
    file = open(name, 'bw')
    for chunk in file_data.iter_content(4096): 
        file.write(chunk)

from urllib.parse import unquote
name1 = unquote(url[0])
def get_name(url):
    name = name1.split('/')[-1]
    name = name.split('?')[0]
    return name
for name in url:
    save_data(get_name(name), get_file(name))

