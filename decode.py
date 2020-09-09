import hashlib


def NameGen(valor):
    name = [f'tqc{valor}-{i}' for i in range(1, 201)]
    #for i in range(1, 11):
     #   name = f'tqc{valor}-{i}'
    return name

def Md5(text):
    hash_ = hashlib.md5(f'{text}'.encode()).hexdigest()
    return hash_

#img = '3ddbc989e59b3f2ab6100986adda4475'

def Decode(img, valor):

    hashs = [Md5(x) for x in NameGen(valor)]

    for i in hashs:
        if img == i:
            return True



#Decode(img, 200)