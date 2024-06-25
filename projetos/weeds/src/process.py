import os
import cv2

def processar_imagens(pasta_origem, pasta_destino):
    # Criar a nova pasta se ela não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Listar todas as imagens na pasta original
    imagens = [f for f in os.listdir(pasta_origem) if f.endswith('.jpg')]

    # Processar cada imagem
    for imagem in imagens:
        caminho_imagem = os.path.join(pasta_origem, imagem)
        # Ler a imagem
        img = cv2.imread(caminho_imagem)
        if img is None:
            print(f"Falha ao carregar a imagem: {caminho_imagem}")
            continue
        
        # Aplicar o filtro de mediana
        img_processada = cv2.medianBlur(img, 3)
        
        # Salvar a imagem processada na nova pasta
        caminho_imagem_nova = os.path.join(pasta_destino, imagem)
        cv2.imwrite(caminho_imagem_nova, img_processada)

# Exemplo de uso
tipo = 'valid30'
pasta_origem = tipo
pasta_destino = "processadas/" + tipo

processar_imagens(pasta_origem, pasta_destino)
