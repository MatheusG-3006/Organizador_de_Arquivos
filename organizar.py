import os 
import shutil

pasta = input("Digite o Nome da Pasta a ser Organizada: ")

categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".tiff", ".tif"], 
    "Docs": [".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlxs", ".ods", ".ppt", ".pptx"], 
    "Áudios": [".mp3", ".wav", ".aac", ".wma", ".ogg"], 
    "Vídeos": [".mp4", ".avi", ".mov", ".wmv"], 
    "Outros": [".zip", ".rar", ".exe", ".html", ".htm", ".css", ".js", ".7z"]
}

def encontrarextensoes(extensao):
    for categoria, extensoes in categorias.items(): 
        if extensao in extensoes:
            return categoria
    return "Outros" 
    
if not os.path.exists(pasta): 
    print("Arquivos Não Encontrados")
    exit()

for arquiv in os.listdir(pasta):
    caminho = os.path.join(pasta, arquiv)

    if os.path.isfile(caminho): 
        _, extensao = os.path.splitext(arquiv)
        categoria = encontrarextensoes(extensao.lower())
        print(f"Arquivo: {arquiv}, Extensão: {extensao}, Categoria: {categoria}, Tipo: {type(categoria)}")
        alvo = os.path.join(pasta, categoria)

        if not os.path.exists(alvo):
            os.mkdir(alvo)
        shutil.move(caminho, os.path.join(alvo, arquiv))

print("Organizado com Sucesso!!")