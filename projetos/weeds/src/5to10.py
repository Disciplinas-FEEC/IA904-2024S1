import os
import shutil
import pandas as pd

def selecionar_e_salvar_imagens_5a10(pasta_origem, pasta_destino, arquivo_csv, nome_coluna):
    # Criar a nova pasta se ela não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Listar todas as imagens na pasta original
    imagens = [f for f in os.listdir(pasta_origem) if f.endswith('.jpg')]

    # Ler o arquivo CSV
    df = pd.read_csv(os.path.join(pasta_origem, arquivo_csv))

    # Contar as ocorrências de cada imagem no CSV
    ocorrencias = df[nome_coluna].value_counts()

    # Selecionar imagens que aparecem de 5 a 10 vezes no CSV
    imagens_5a10 = ocorrencias[(ocorrencias >= 5) & (ocorrencias <= 10)].index.tolist()

    # Copiar as imagens selecionadas para a nova pasta
    for imagem in imagens_5a10:
        if imagem in imagens:
            shutil.copy(os.path.join(pasta_origem, imagem), os.path.join(pasta_destino, imagem))

    # Filtrar linhas correspondentes às imagens selecionadas
    linhas_selecionadas = df[df[nome_coluna].isin(imagens_5a10)]

    # Salvar as linhas selecionadas em um novo arquivo CSV na nova pasta
    arquivo_csv_selecionado = os.path.join(pasta_destino, '_annotations.csv')
    linhas_selecionadas.to_csv(arquivo_csv_selecionado, index=False)

# Exemplo de uso
tipo = 'processadas/train'
pasta_origem = tipo
pasta_destino = tipo + '-5to10'
arquivo_csv = '_annotations.csv'
nome_coluna = 'filename'

selecionar_e_salvar_imagens_5a10(pasta_origem, pasta_destino, arquivo_csv, nome_coluna)