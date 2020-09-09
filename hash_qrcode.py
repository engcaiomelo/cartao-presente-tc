import pyqrcode as qr
import hashlib

def NameGen(valor):
    name = [f'tqc{valor}-{i}' for i in range(1, 101)]
    #for i in range(1, 11):
     #   name = f'tqc{valor}-{i}'
    return name


def QrCode(text):
    hash_ = hashlib.md5(f'{text}'.encode()).hexdigest()
    qrcode = qr.create(hash_)
    if tuple(text[:-4]) != '.png':
        name = text + '.png'
    qrcode.png(name, scale= 6)
    print(hash_)

def Generate(valor):
    names = [QrCode(i) for i in NameGen(valor)]



if __name__ == '__main__':

    #Generate(150)
