import os
import random
import shutil
import pandas as pd

def selecionar_e_salvar_imagens(pasta_origem, pasta_destino, arquivo_csv, nome_coluna, percentual):
    # Criar a nova pasta se ela não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Listar todas as imagens na pasta original
    imagens = [f for f in os.listdir(pasta_origem) if f.endswith('.jpg')]

    # Selecionar aleatoriamente 10% das imagens
    num_imagens = len(imagens)
    num_selecionadas = max(1, int(percentual * num_imagens / 100))
    imagens_selecionadas = random.sample(imagens, num_selecionadas)

    # Copiar as imagens selecionadas para a nova pasta
    for imagem in imagens_selecionadas:
        shutil.copy(os.path.join(pasta_origem, imagem), os.path.join(pasta_destino, imagem))

    # Ler o arquivo CSV
    df = pd.read_csv(os.path.join(pasta_origem, arquivo_csv))

    # Filtrar linhas correspondentes às imagens selecionadas
    linhas_selecionadas = df[df[nome_coluna].isin(imagens_selecionadas)]

    # Salvar as linhas selecionadas em um novo arquivo CSV na nova pasta
    arquivo_csv_selecionado = os.path.join(pasta_destino, '_annotations.csv')
    linhas_selecionadas.to_csv(arquivo_csv_selecionado, index=False)


tipo = 'valid'
pasta_origem = tipo
pasta_destino = tipo + '10'
arquivo_csv = '_annotations.csv'
nome_coluna = 'filename'
percentual = 10

selecionar_e_salvar_imagens(pasta_origem, pasta_destino, arquivo_csv, nome_coluna, percentual)