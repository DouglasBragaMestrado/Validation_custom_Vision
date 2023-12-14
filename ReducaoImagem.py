from PIL import Image
import os

diretorio = '_data'
novo_diretorio = '_data'

for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.jpg') or arquivo.endswith('.png') or arquivo.endswith('.bmp'):
        imagem = Image.open(os.path.join(diretorio, arquivo))
        largura, altura = imagem.size
        #nova_largura, nova_altura = int(largura * 0.5), int(altura * 0.5)
        nova_largura, nova_altura = int(256), int(256)
        imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.LANCZOS)
        imagem_redimensionada.save(os.path.join(novo_diretorio, arquivo))
