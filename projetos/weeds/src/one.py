import os
import shutil
import pandas as pd

def selecionar_e_salvar_imagens_unicas(pasta_origem, pasta_destino, arquivo_csv, nome_coluna):
    # Criar a nova pasta se ela não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Listar todas as imagens na pasta original
    imagens = [f for f in os.listdir(pasta_origem) if f.endswith('.jpg')]

    # Ler o arquivo CSV
    df = pd.read_csv(os.path.join(pasta_origem, arquivo_csv))

    # Contar as ocorrências de cada imagem no CSV
    ocorrencias = df[nome_coluna].value_counts()

    # Selecionar imagens que aparecem apenas uma vez no CSV
    imagens_unicas = ocorrencias[ocorrencias == 1].index.tolist()

    # Copiar as imagens únicas para a nova pasta
    for imagem in imagens_unicas:
        if imagem in imagens:
            shutil.copy(os.path.join(pasta_origem, imagem), os.path.join(pasta_destino, imagem))

    # Filtrar linhas correspondentes às imagens únicas
    linhas_selecionadas = df[df[nome_coluna].isin(imagens_unicas)]

    # Salvar as linhas selecionadas em um novo arquivo CSV na nova pasta
    arquivo_csv_selecionado = os.path.join(pasta_destino, 'linhas_selecionadas.csv')
    linhas_selecionadas.to_csv(arquivo_csv_selecionado, index=False)

# Exemplo de uso
tipo = 'train'
pasta_origem = tipo
pasta_destino = tipo + '-single'
arquivo_csv = '_annotations.csv'
nome_coluna = 'filename'

selecionar_e_salvar_imagens_unicas(pasta_origem, pasta_destino, arquivo_csv, nome_coluna)
