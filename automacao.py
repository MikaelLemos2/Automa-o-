import os
import shutil

pasta_origem = "Downloads"
pasta_destino = "organizado"

tipos = {
    "PDFs": [".pdf"],
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".avi"],
    "Documentos": [".docx", ".txt", ".xlsx"]
}

if not os.path.exists(pasta_destino):
    os.mkdir(pasta_destino)

relatorio = {}

for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isfile(caminho_arquivo):
        movido = False

        for pasta, extensoes in tipos.items():
            for ext in extensoes:
                if arquivo.lower().endswith(ext):
                    pasta_final = os.path.join(pasta_destino, pasta)
                    
                    if not os.path.exists(pasta_final):
                        os.mkdir(pasta_final)

                    shutil.move(caminho_arquivo, pasta_final)
                    relatorio[pasta] = relatorio.get(pasta, 0) + 1
                    movido = True
                    break

        if not movido:
            pasta_outros = os.path.join(pasta_destino, "Outros")
            if not os.path.exists(pasta_outros):
                os.mkdir(pasta_outros)
            shutil.move(caminho_arquivo, pasta_outros)
            relatorio["Outros"] = relatorio.get("Outros", 0) + 1

# Gerar relatório
with open("relatorio.txt", "w") as f:
    for categoria, quantidade in relatorio.items():
        f.write(f"{categoria}: {quantidade} arquivos\n")

print("Organização concluída!")
