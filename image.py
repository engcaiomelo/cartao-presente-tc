from PIL import Image
import png

def Cartao(valor):
    cartao_nome = f'cartao_{valor}.png'
    cartao = Image.open(cartao_nome)
    area_cartao = (197, 237, 443, 483)
    qrcodes = [f'tqc{valor}-{i}.png' for i in range(1,101)]
    imgs = [Image.open(j) for j in qrcodes]
    for x in range(0,100):
        cartao.paste(imgs[x], area_cartao)
        cartao.save(f'cartao_{qrcodes[x]}', quality=100)



