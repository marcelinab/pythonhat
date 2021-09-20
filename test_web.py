from urllib.request import urlopen
from datetime import date

import requests


def test_display():
    link = "http://127.0.0.1:5000/"
    f = urlopen(link)
    myfile = f.read()
    content = myfile.decode("utf-8")
    current_date = str(date.today())
    assert current_date in content

def test_comment():
    comment = "test"
    link = "http://127.0.0.1:5000/"
    myobj = {'comment': comment}
    requests.post(link+"/add-comment", data=myobj)
    f = urlopen(link)
    myfile = f.read()
    content = myfile.decode("utf-8")
    assert comment in content
