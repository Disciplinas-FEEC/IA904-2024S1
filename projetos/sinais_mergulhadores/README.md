# Leitor de Sinais de Mão de Mergulhadores
# Diver Hand Signal Reader

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome, RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em duplas ou trios.
> 
> | Nome                        | RA      | Curso                          |
> |-----------------------------|---------|--------------------------------|
> | Raphael Melloni Trombini    | 271322  | Aluno Especial                 |
> | Ícaro Dias dos Santos       | 245542  | Mestrado em Engenharia Mecânica|
> | José Alfredo Zapana García  | 272291  | Mestrado em Engenharia Elétrica|

## Descrição do Projeto

O objetivo deste projeto é desenvolver um sistema capaz de identificar e interpretar sinais de mão de mergulhadores, utilizando técnicas de visão computacional, para facilitar a comunicação subaquática e melhorar a segurança durante mergulhos. Este trabalho se inspira e busca contribuir para os objetivos do projeto CADDY, um projeto da União Europeia focado no desenvolvimento de tecnologias para entender e interagir com mergulhadores em ambientes subaquáticos. Os principais objetivos do CADDY incluem a compreensão do comportamento do mergulhador através da interpretação de gestos manuais simbólicos e outros indicadores não verbais, além do desenvolvimento de sistemas cognitivos de (re)planejamento de missões com base nessas interações. O projeto também explora a integração com o 'Caddian corpus', um conjunto extenso de comandos sintaticamente e semanticamente corretos dentro da linguagem hierárquica multi-AUV denominada Caddian, que foi especialmente desenvolvida para o projeto CADDY. Este corpus serve como base para o entendimento e a interpretação das interações subaquáticas, contendo desde comandos simples até sequências mais complexas de gestos.

## Metodologia

O desenvolvimento do sistema de detecção e classificação de gestos subaquáticos foi conduzido através de duas abordagens principais: (1) uma abordagem baseada na detecção de mãos seguida pela classificação dos gestos a partir das regiões de interesse (ROI) detectadas e (2) uma abordagem que explora o uso de modelos de detecção e classificação integrados, especificamente o YOLOv8. Ambas as abordagens utilizaram o mesmo dataset de teste para garantir uma comparação justa dos resultados obtidos.

### Detecção de Mãos e Classificação de Gestos

**Descrição**: Nesta abordagem, inicialmente as mãos dos mergulhadores foram detectadas nas imagens utilizando uma arquitetura Shallow U-Net. As regiões de interesse (ROIs) contendo as mãos foram então extraídas e alimentadas em uma rede neural convolucional (CNN) para a classificação dos gestos.

**Justificativa Teórica**: Esta abordagem foi escolhida com base na hipótese de que a detecção de uma única classe (mão) poderia ser mais robusta do que a detecção direta de múltiplas classes de gestos. Uma vez que as mãos são detectadas com precisão, a classificação dos gestos a partir das ROIs se torna um problema mais localizado e específico, potencialmente melhorando a precisão geral do sistema. A U-Net, conhecida por sua eficiência em segmentação de imagens, foi utilizada para garantir a detecção precisa das mãos, enquanto a CNN foi empregada para aproveitar sua eficácia em tarefas de classificação de imagens.

**Viabilidade**: Utilizamos um dataset contendo imagens estéreo de mergulhadores realizando diversos gestos. A preparação do dataset envolveu a combinação de arquivos CSV de verdadeiros positivos e negativos, filtragem de imagens duplicadas e criação de arquivos de anotação para cada imagem. O dataset foi dividido em conjuntos de treino, validação e teste. A Shallow U-Net foi treinada para segmentar as mãos nas imagens, e a CNN foi treinada para classificar os gestos a partir das ROIs extraídas.

**Ferramentas e Técnicas Utilizadas**:

- **Shallow U-Net**: Utilizada para a segmentação das mãos.
- **CNN**: Utilizada para a classificação das ROIs em gestos específicos.
- **Frameworks**: Pytorch foi utilizado para implementar e treinar os modelos.
- **Pré-processamento de Imagens**: Técnicas de aumento de dados como rotação, espelhamento e ajuste de contraste foram aplicadas para melhorar a robustez do modelo.

### Modelo Integrado de Detecção e Classificação (YOLOv8)

**Descrição**: Utilizamos o modelo YOLOv8, um modelo de detecção de objetos que realiza simultaneamente a detecção e a classificação dos gestos subaquáticos em uma única etapa. O YOLOv8 nano foi escolhido devido ao seu tamanho reduzido e eficiência computacional, adequados para aplicações embarcadas.

**Justificativa Teórica**: O YOLO (You Only Look Once) é uma família de modelos de detecção de objetos conhecida por sua capacidade de realizar detecção e classificação em tempo real com alta precisão. A versão YOLOv8 nano foi escolhida por equilibrar desempenho e eficiência computacional, sendo especialmente útil para aplicações onde os recursos de hardware são limitados, como em robôs subaquáticos.

**Viabilidade**: O dataset foi convertido para um formato compatível com YOLO, o que incluiu a normalização das coordenadas de ROI e a criação de arquivos de anotação no formato YOLO. O modelo YOLOv8 nano foi então treinado utilizando este dataset, e sua performance foi avaliada em termos de precisão, recall e mAP (mean Average Precision).

**Ferramentas e Técnicas Utilizadas**:

- **YOLOv8 nano**: Utilizado para a detecção e classificação integrada de gestos.
- **Frameworks**: PyTorch e a biblioteca Ultralytics YOLO foram utilizados para implementar e treinar o modelo.
- **Conversão do Dataset**: Scripts personalizados foram desenvolvidos para converter o dataset original para o formato necessário pelo YOLOv8.
- **Treinamento e Validação**: O modelo foi treinado utilizando GPUs para acelerar o processo, com avaliação contínua em um conjunto de validação para ajustar hiperparâmetros e prevenir overfitting.

### Utilização do Mesmo Dataset de Teste

Ambas as abordagens, Shallow U-Net + CNN e YOLOv8 nano, utilizaram o mesmo dataset de teste para garantir uma comparação justa e direta dos resultados obtidos. Este procedimento permitiu avaliar as performances relativas das duas abordagens em condições idênticas, facilitando a análise comparativa e a interpretação dos resultados.


## Bases de Dados e Evolução

| Base de Dados                    | Endereço na Web                                                                     | Resumo Descritivo                                                                                                                                                                                                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CADDY Underwater Gestures Dataset| [CADDY Dataset Homepage](http://www.caddian.eu//CADDY-Underwater-Gestures-Dataset.html)| Conjunto de dados composto por aproximadamente 10.000 pares de imagens estéreo coletadas em 8 cenários diferentes para interação subaquática humano-robô e contem imagens para 16 gestos da linguagem Caddian. As imagens foram capturadas durante experimentos que simulam diversas condições e tarefas subaquáticas, com o objetivo de desenvolver e testar sistemas de reconhecimento de gestos que facilitam a comunicação entre mergulhadores e veículos autônomos subaquáticos (AUVs). Cada cenário reflete um contexto específico de mergulho, variando desde ambientes com visibilidade reduzida até situações com iluminação artificial, projetados para desafiar e aprimorar a capacidade dos sistemas robóticos em entender e reagir a comandos humanos no ambiente subaquático. |

A distribuição do conjunto de dados é a seguinte:

### De acordo à presença de gestos

| Classe   | Total fotos estéreo |
|----------|---------------------|
| Positiva | 9239                |
| Negativa | 7190                |

### De acordo ao gesto realizado

| Comando        | ID de classe | Total fotos estéreo |
|----------------|--------------|---------------------|
| Start_comm     | 0            | 1820                |
| End_comm       | 1            | 1318                |
| Up             | 2            | 352                 |
| Down           | 3            | 462                 |
| Photo          | 4            | 925                 |
| Backwards      | 5            | 561                 |
| Carry          | 6            | 717                 |
| Boat           | 7            | 369                 |
| Here           | 8            | 261                 |
| Mosaic         | 9            | 226                 |
| Num_delimiter  | 10           | 992                 |
| One            | 11           | 161                 |
| Two            | 12           | 404                 |
| Three          | 13           | 388                 |
| Four           | 14           | 235                 |
| Five           | 15           | 48                  |

<details>
<summary title="Click to Expand/Collapse">Exemplos de gestos</summary>

| Comando        | Exemplo                                                        | Comando         | Exemplo                                                        |
|----------------|----------------------------------------------------------------|-----------------|----------------------------------------------------------------|
| Start_comm     | ![start_com](https://github.com/RTrombini/IA904-2024S1/assets/114251488/15a2e9fe-3323-4f69-8f85-c768e96263e2) | Up              | ![up](https://github.com/RTrombini/IA904-2024S1/assets/114251488/569e165b-c0de-491f-9ee8-b877e10c0654) |
| Down           | ![down](https://github.com/RTrombini/IA904-2024S1/assets/114251488/45c43049-c052-40b2-aade-cc9c31cc8e6c) | Photo           | ![photo](https://github.com/RTrombini/IA904-2024S1/assets/114251488/a3c7c7b7-aec2-45b2-b7c1-4239dd83ab94) |
| Backwards      | ![backwards](https://github.com/RTrombini/IA904-2024S1/assets/114251488/ec93ee23-5fba-4591-90c5-45f90677df42) | Carry           | ![carry](https://github.com/RTrombini/IA904-2024S1/assets/114251488/5f2909c4-3150-4526-b201-d604d96ab4ad) |
| Boat           | ![boat](https://github.com/RTrombini/IA904-2024S1/assets/114251488/1de76e5d-877a-4d83-9d5c-3427b06b5227) | Here            | ![here](https://github.com/RTrombini/IA904-2024S1/assets/114251488/f34a67ee-be11-48d3-a672-32984a6fc3e5) |
| Num_delimiter  | ![num_delimiter](https://github.com/RTrombini/IA904-2024S1/assets/114251488/378f3cb7-80c8-4f83-8bc1-7afc6fc6a60a) | One             | ![one](https://github.com/RTrombini/IA904-2024S1/assets/114251488/39d3c371-6d82-4080-a5a1-4a38187641c7) |
| Two            | ![two](https://github.com/RTrombini/IA904-2024S1/assets/114251488/9e38bcfe-a82e-4d9a-bd7e-2aad0fcb830c) | Three           | ![three](https://github.com/RTrombini/IA904-2024S1/assets/114251488/e986f257-9feb-41fa-b2fe-b3ff8580a946) |
| Four           | ![four](https://github.com/RTrombini/IA904-2024S1/assets/114251488/3fbfa2ac-60ff-4d21-9881-79f594d8df5a) | Five            | ![five](https://github.com/RTrombini/IA904-2024S1/assets/114251488/bb105794-46b7-481b-9589-55af5a0e77e0) |
| End_comm       | ![end_com](https://github.com/RTrombini/IA904-2024S1/assets/114251488/da66fa64-eaf6-41ce-81a0-6f9022384fce) |                 |                                                                |


</details>


## Ambiente computacional

### Ambiente

Python foi escolhido como linguagem de programação para treinar e avaliar os modelos, se utilizaram principalmente Jupyter Notebooks para permitir uma leitura fácil e reproducibilidade dos modelos.

#### Ambiente para treinamento do modelo SUN-CNN
A versão utilizada para o treinamento do modelo SUN-CNN foi Python 3.12.2.

#### Ambiente para treinamento do modelo YOLO-v8
A versão utilizada para o treinamento do modelo YOLO-v8 foi Python 3.11.9.

### Bibliotecas
 
- Bibliotecas para pré-processamento de imagens: OpenCV, Pillow (PIL), Numpy
- Bibliotecas para aumento de imagens: Torchvision
- Bibliotecas para Deep Learning: PyTorch, YOLOv8
- Biblioteca para manipulação de dados: Pandas
- Bibliotecas para obtenção de métricas: Pytorch e Sklearn
- Bibliotecas para visualização de dados: Matplotlib e Seaborn

#### Versões das bibliotecas usadas para o treinamento do modelo SUN-CNN
- OpenCV 4.9.0
- Pillow (PIL) 10.3.0
- Numpy 1.26.4
- Torchvision 0.17.1+cu118
- CUDA toolkit 11.8
- PyTorch 2.2.1+cu118
- Pandas 2.2.1
- Sklearn 1.4.1.post1
- Matplotlib 3.8.3 
- Seaborn 0.13.2

#### Versões das bibliotecas usadas para o treinamento do modelo YOLO-v8
- OpenCV 4.9.0.80
- Pillow 10.3.0
- Numpy 1.26.4
- Torchvision 0.18.0+cu121
- Pandas 2.0.1
- Sklearn 1.5.0
- Matplotlib 3.9.0
- Seaborn 0.13.2
- CUDA toolkit 11.8
- PyTorch 2.2.1+cu118

### Recursos computacionais

#### Treinamento do modelo SUN-CNN
O treinamento foi realizado numa máquina local com uma gpu NVIDIA 2060 de 6 GB de VRAM em um computador com um processador Ryzen 9 4900HS octacore e 16 GB de RAM para o sistema.

#### Treinamento do modelo YOLO-v8
O treinamento foi realizado numa máquina local com uma gpu NVIDIA 4070 de 12 GB de VRAM em um computador com um processador Ryzen 5 5600 hexacore e 32 GB de RAM para o sistema. 

### Discussão e Dicas para implementação

## Workflow


A continuação se apressenta o workflow seguido pelo grupo, onde primeiro foi feita uma exploração dos dados divulgados pelo grupo CADDY, a partir dos quais foram obtidos insights sobre as abordagens que se poderiam ser tomadas para resolver o problema, decidindo fazer uma comparação entre dois modelos de Deep Learning. Finalmente, depois de iterações e refinamentos dos modelos se realizou uma avaliação com um conjunto de teste específico para os dois modelos.

![workflow](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/workflow.png)


### Detecção com YOLO

#### 1. Preparação do Dataset

##### Dataset Inicial:

O dataset inicial consistia em imagens estéreo (esquerda e direita) de mergulhadores realizando diversos gestos. As imagens foram divididas em duas categorias principais:
- **True Positives**: Contendo gestos a serem reconhecidos.
- **True Negatives**: Sem gestos.

Cada imagem no dataset era acompanhada por um arquivo CSV com as seguintes informações:
- `index`: Índice da imagem.
- `scenario`: Cenário da imagem.
- `stereo left`: Caminho para a imagem estéreo esquerda.
- `stereo right`: Caminho para a imagem estéreo direita.
- `label name`: Nome da classe do gesto.
- `label id`: ID da classe do gesto.
- `roi left`: Região de interesse na imagem esquerda.
- `roi right`: Região de interesse na imagem direita.

##### Conversão do Dataset:

Para utilizar o YOLOv8, o dataset precisava ser convertido para um formato compatível. Este processo incluiu várias etapas e foi realizado no notebook `dataset_converter.ipynb`:

###### Combinação dos CSVs True Positives e True Negatives:
- **Ação:** Os CSVs de true positives e true negatives foram combinados em um único CSV.
- **Motivo:** Facilitar o processamento unificado das anotações e garantir que todas as classes estejam representadas no mesmo arquivo.

###### Filtragem de Imagens:
- **Ação:** Apenas imagens com anotações válidas foram mantidas.
- **Motivo:** Garantir que o dataset final contenha apenas imagens relevantes para o treinamento e evitar dados ruidosos.
- **Ação:** Imagens duplicadas (esquerda e direita) foram removidas para evitar overfitting. Apenas imagens da direita foram mantidas.
- **Motivo:** Reduzir a redundância e o volume de dados, mantendo a diversidade necessária para um treinamento eficaz.

###### Criação de Arquivos de Anotação YOLO:
- **Ação:** Convertendo as coordenadas de ROI para o formato YOLO.
  - Formato YOLO: `<class_id> <x_center> <y_center> <width> <height>`
  - Coordenadas foram normalizadas para estar entre 0 e 1.
- **Motivo:** Adaptar as anotações ao formato esperado pelo modelo YOLO.
- **Ação:** Salvando as anotações em arquivos `.txt` no formato YOLO.
- **Motivo:** Compatibilizar o formato das anotações com os requisitos do YOLO.

###### Divisão em Conjuntos de Treino, Validação e Teste:
- **Ação:**  Esse dataset foi dividido em 76.5% para treino, 10% para validação e 13.5% para teste.
- **Motivo:** Garantir que o modelo seja treinado, validado e testado de maneira adequada, permitindo a avaliação de sua performance em dados não vistos durante o treinamento.
- **Ação:** As imagens e anotações correspondentes foram movidas para diretórios específicos (`train`, `val`, `test`).
- **Motivo:** Organizar o dataset de acordo com as convenções do YOLO para facilitar o treinamento e a inferência.

#### 2. Estrutura do Dataset Final

##### Estrutura de Diretórios:

```text
Dataset/
│
├── images/
│   ├── train/
│   ├── val/
│   └── test/
│
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
│
└── dataset.yaml
```


###### Formato dos Arquivos de Anotação:

Cada arquivo `.txt` de anotação segue o formato YOLO:

```
<class_id> <x_center> <y_center> <width> <height>
```


### 3. Treinamento da YOLOv8 Nano

#### Configuração do Treinamento:

Utilizou-se o modelo pré-treinado YOLOv8 nano (`yolov8n.pt`).

**Parâmetros de treinamento:**
- **Épocas:** 100
- **Tamanho das imagens:** 640x640 pixels
- **Batch size:** 16
- **Learning rate:** 0.01
- **Otimização:** SGD com momentum de 0.9

O treinamento foi realizado no notebook `yolo_training.ipynb`.

### 4. Realizar Inferência com o Modelo Treinado

A inferência foi realizada no notebook `yolo_inference.ipynb`, onde as imagens de teste foram processadas pelo modelo treinado para avaliar a performance em condições não vistas durante o treinamento.



## Avaliação

### Problem Fingerprinting

**Objetivo:**
Mapear o problema para uma categoria específica, capturando todas as propriedades relevantes que influenciam a seleção de métricas.

**Domínio de Aplicação:**
Análise de imagens subaquáticas para detecção e classificação de gestos de mão.

**Tipo de Tarefa:**
Detecção de objetos e classificação.

**Variabilidade das Condições:**
- **Iluminação:** As condições de iluminação subaquática podem variar significativamente, afetando a qualidade da imagem.
- **Visibilidade:** A clareza da água e a presença de partículas podem impactar a visibilidade.

**Desbalanceamento de Classes:**
Algumas classes de gestos são mais frequentes que outras, o que pode levar a um desbalanceamento no conjunto de dados.

**Requisitos de Precisão e Recall:**
- **Alta Precisão:** Necessário para minimizar falsos positivos, onde um gesto é detectado erroneamente.
- **Alto Recall:** Necessário para minimizar falsos negativos, onde um gesto presente na imagem não é detectado.

### Metric Selection

**Objetivo:**
Determinar um conjunto de métricas pertinentes ao problema/categoria.

**Métricas Selecionadas:**
- **Precisão (Precision):** Mede a proporção de detecções corretas entre todas as detecções realizadas pelo modelo.
- **Revocação (Recall):** Mede a proporção de detecções corretas entre todas as instâncias reais dos gestos nas imagens.
- **mAP50 (Mean Average Precision at IoU=0.50):** Média da precisão média para cada classe, considerando um limiar de IoU de 0.50.
- **mAP50-95 (Mean Average Precision at IoU=0.50:0.95):** Média da precisão média para cada classe, considerando múltiplos limiares de IoU, de 0.50 a 0.95.
- **F1 Score:** Combina precisão e recall em uma única métrica, útil para medir o equilíbrio entre ambos.
- **IoU (Intersection over Union):** Mede a sobreposição entre as caixas delimitadoras previstas e as reais, usada para avaliar a qualidade da detecção.

### Metric Application

**Objetivo:**
Recomendações relacionadas à implementação e interpretação das métricas.

**Implementação:**
- **Ferramentas:** Utilização do framework YOLOv8, que já possui implementações integradas para calcular as métricas de detecção.
- **Validação Cruzada:** Dividir o conjunto de dados em treinamento, validação e teste para garantir que o modelo generalize bem.
- **Ajuste de Hiperparâmetros:** Ajustar hiperparâmetros do modelo, como a taxa de aprendizado, para otimizar as métricas selecionadas.

**Interpretação:**
- **Precisão e Recall:** Analisar a precisão e recall para identificar possíveis trade-offs e ajustar o modelo conforme necessário.
- **mAP50 e mAP50-95:** Utilizar estas métricas para obter uma visão geral da performance do modelo em diferentes classes e limiares de IoU.
- **Análise de Falsos Positivos/Negativos:** Examinar casos de falsos positivos e negativos para identificar padrões e ajustar a estratégia de treinamento ou coleta de dados.



## Experimentos e Resultados

### Experimento com YOLOv8

Realizamos um experimento com o modelo YOLOv8 para avaliar a dificuldade de detectar as mãos dos mergulhadores nas imagens subaquáticas. Para nossa surpresa, a detecção de mãos foi muito bem-sucedida, mesmo nas imagens mais turvas e com baixa visibilidade. Motivados por esses resultados positivos, prosseguimos com o treinamento do modelo para a detecção de gestos específicos, separados em 17 classes (16 classes de gestos e uma classe sem gestos).

#### Preparação do Dataset:

- Utilizamos as classes e Regiões de Interesse (ROIs) disponíveis no arquivo CSV do dataset original.
- Para evitar overfitting, optamos por usar apenas metade das imagens, especificamente as imagens right. Como tínhamos imagens left e right devido ao uso de câmeras estéreo, essa escolha manteve a diversidade do dataset sem repetir dados.
- Não aplicamos nenhum pré-processamento nas imagens neste teste, para observar os resultados da maneira mais crua possível.


##### Treinamento da YOLOv8 Nano

###### Divisão em Conjuntos de Treino, Validação e Teste:
- Esse dataset foi dividido em 72% para treino, 10% para validação e 18% para teste.
- O dataset foi preparado mantendo apenas as imagens da direita, eliminando duplicações das imagens estéreo.

###### Aumento dos Dados
As seguintes transformações foram aplicadas aos dados de treinamento utilizando as configurações padrão do YOLOv8:

1. **Scale**: Redimensionamento aleatório das imagens.
2. **Translation**: Translação das imagens.
3. **Rotation**: Rotação aleatória das imagens.
4. **Shear**: Aplicação de deformação nas imagens.
5. **Horizontal Flip**: Inversão horizontal das imagens.

###### Hiperparâmetros

**Hiperparâmetros:**
- **Batch size**: 16
- **Tamanho das imagens**: 640x640 pixels
- **Número de classes**: 17
- **Épocas**: 100
- **Learning rate inicial**: 0.01

#### Resultados:

- A detecção de gestos foi aceitável, com o modelo conseguindo identificar os diferentes gestos subaquáticos.
- Resultados detalhados, incluindo tabelas de verdade e curvas ROC, serão adicionados posteriormente para explicar os resultados em detalhes.

##### Curvas de perdas

![loss para detecção](https://github.com/RTrombini/IA904-2024S1/assets/114251488/e1811cc0-ac4d-4caf-83f3-3ef053fdc03e)

![loss para classificação](https://github.com/RTrombini/IA904-2024S1/assets/114251488/faf5dfa8-cdf0-4b94-b0d8-94b1374ee919)



##### Matriz de confusão:

- Segue abaixo a matriz de confusão  normalizada da detecção no dataset de testes:



![matriz_confusao](https://github.com/RTrombini/IA904-2024S1/assets/114251488/ff2a9f1f-528c-48ae-9c4b-1bb658bdfc6c)

##### Classes Corretamente Classificadas

| Classe          | Percentual de Acertos | Observação                                                          |
|-----------------|-----------------------|---------------------------------------------------------------------|
| start_comm      | 100%                  | Todas as instâncias foram corretamente classificadas como start_comm. |
| end_comm        | 100%                  | Todas as instâncias foram corretamente classificadas como end_comm.   |
| up              | 98%                  | 2% das instâncias foram erroneamente classificadas.        |
| down            | 100%                   | Todas as instâncias foram corretamente classificadas como down.                 |
| photo           | 100%                   | Todas as instâncias foram corretamente classificadas como photo.      |
| backwards       | 98%                   | 2% das instâncias foram erroneamente classificadas.                  |
| carry           | 99%                  | 1% das instâncias foram erroneamente classificadas.      |
| boat            | 97%                   | 3% das instâncias foram erroneamente classificadas.       |
| here            | 98%                   | 2% das instâncias foram erroneamente classificadas.                  |
| mosaic          | 100%                    | Todas as instâncias foram corretamente classificadas como mosaic.                  |
| num_delimiter   | 100%                   | Todas as instâncias foram corretamente classificadas como num_delimiter.                  |
| one             | 95%                   | 5% das instâncias foram erroneamente classificadas.                  |
| two             | 100%                  | Todas as instâncias foram corretamente classificadas como two.        |
| three           | 100%                   | Todas as instâncias foram corretamente classificadas como three.                 |
| four            | 100%                   | Todas as instâncias foram corretamente classificadas como four.                 |
| five            | 100%                  | Todas as instâncias foram corretamente classificadas como five.       |
| negative        | 0%                    | As instâncias não  foram classificadas como negative.   |
| background      | 100%                  | Todas as instâncias negative foram  classificadas como background. |


### Erros de Classificação

| Classe    | Percentual de Erro | Observação                                            |
|-----------|---------------------|-------------------------------------------------------|
| up        | 2%                  | 2% das instâncias de up foram erroneamente classificadas.         |
| backwards | 2%                  | 2% das instâncias de backwards foram erroneamente classificadas.|
| carry     | 1%                  | 1% das instâncias de carry foram erroneamente classificadas.      |
| boat      | 3%                  | 3% das instâncias de boat foram erroneamente classificadas.       |
| one       | 5%                  | 5% das instâncias de one foram erroneamente classificadas.        |


<details>
<summary title="Click to Expand/Collapse">Exemplos de gestos</summary>

| Comando        | Exemplo                                                        | Comando         | Exemplo                                                        |
|----------------|----------------------------------------------------------------|-----------------|----------------------------------------------------------------|
| Start_comm     | ![start_com](https://github.com/RTrombini/IA904-2024S1/assets/114251488/15a2e9fe-3323-4f69-8f85-c768e96263e2) | Up              | ![up](https://github.com/RTrombini/IA904-2024S1/assets/114251488/569e165b-c0de-491f-9ee8-b877e10c0654) |
| Down           | ![down](https://github.com/RTrombini/IA904-2024S1/assets/114251488/45c43049-c052-40b2-aade-cc9c31cc8e6c) | Photo           | ![photo](https://github.com/RTrombini/IA904-2024S1/assets/114251488/a3c7c7b7-aec2-45b2-b7c1-4239dd83ab94) |
| Backwards      | ![backwards](https://github.com/RTrombini/IA904-2024S1/assets/114251488/ec93ee23-5fba-4591-90c5-45f90677df42) | Carry           | ![carry](https://github.com/RTrombini/IA904-2024S1/assets/114251488/5f2909c4-3150-4526-b201-d604d96ab4ad) |
| Boat           | ![boat](https://github.com/RTrombini/IA904-2024S1/assets/114251488/1de76e5d-877a-4d83-9d5c-3427b06b5227) | Here            | ![here](https://github.com/RTrombini/IA904-2024S1/assets/114251488/f34a67ee-be11-48d3-a672-32984a6fc3e5) |
| Num_delimiter  | ![num_delimiter](https://github.com/RTrombini/IA904-2024S1/assets/114251488/378f3cb7-80c8-4f83-8bc1-7afc6fc6a60a) | One             | ![one](https://github.com/RTrombini/IA904-2024S1/assets/114251488/39d3c371-6d82-4080-a5a1-4a38187641c7) |
| Two            | ![two](https://github.com/RTrombini/IA904-2024S1/assets/114251488/9e38bcfe-a82e-4d9a-bd7e-2aad0fcb830c) | Three           | ![three](https://github.com/RTrombini/IA904-2024S1/assets/114251488/e986f257-9feb-41fa-b2fe-b3ff8580a946) |
| Four           | ![four](https://github.com/RTrombini/IA904-2024S1/assets/114251488/3fbfa2ac-60ff-4d21-9881-79f594d8df5a) | Five            | ![five](https://github.com/RTrombini/IA904-2024S1/assets/114251488/bb105794-46b7-481b-9589-55af5a0e77e0) |
| End_comm       | ![end_com](https://github.com/RTrombini/IA904-2024S1/assets/114251488/da66fa64-eaf6-41ce-81a0-6f9022384fce) |                 |                                                                |


</details>

##### Métricas de Detecção

**Resultados Obtidos:**
- **Precisão (Precision):** 0.913
- **Sensibilidade:** 0.928
- **mAP50 (Mean Average Precision at IoU=0.50):** 0.932
- **mAP50-95 (Mean Average Precision at IoU=0.50:0.95):** 0.693

**Discussão:**
Os resultados obtidos indicam um bom desempenho do modelo YOLOv8 na detecção e classificação de gestos de mão em imagens subaquáticas. A alta precisão e recall demonstram a eficácia do modelo em minimizar tanto falsos positivos quanto falsos negativos. As métricas mAP50 e mAP50-95 fornecem uma visão abrangente da performance do modelo em diferentes limiares de IoU, mostrando que o modelo é robusto para várias condições de detecção.

### Modelo SUN-CNN

#### Experimentos

Apartir dos resultados obtidos com a YOLO-v8 nano, apareceu a pergunta de se era possível obter resultados no mesmo nível com menos parâmetros treináveis, pegando en conta que a ideia do projeto é que o modelo seja embarcável num robô subaquático. Nesse sentido, o uso de uma rede de segmentação mais uma rede de classificação deveria realizar de maneira satisfátoria essa tarefa. Nós escolhimos uma variação da U-net original, chamada Shallow U-net, pois tem menos camadas de profundidade para o encoder-decoder, assim mesmo tem menos camadas de filtros, reduzindo o número de parâmetros desde o início. No caso da rede CNN, se armou uma estrutura com 4 camadas convolucionais com batch normalization e função de ativação ReLU para fazer a extracção de características das imagens filtradas pela Shallow U-net e umas camadas Fully connected com regularização Dropout para aumentar a sua generalização e fazer a classificação do gesto feito pelo mergulhador.

##### Arquitetura da Shallow U-Net

| Layer (type)         | Output Shape             | Param #  |
|----------------------|--------------------------|----------|
| Conv2d-1             | [-1, 32, 160, 212]       | 896      |
| Conv2d-2             | [-1, 32, 160, 212]       | 9,248    |
| MaxPool2d-3          | [-1, 32, 80, 106]        | 0        |
| DownConv-4           | [[-1, 32, 80, 106], [-1, 32, 160, 212]] | 18,496   |
| Conv2d-5             | [-1, 64, 80, 106]        | 8,496    |
| Conv2d-6             | [-1, 64, 80, 106]        | 36,928   |
| MaxPool2d-7          | [-1, 64, 40, 53]         | 0        |
| DownConv-8           | [[-1, 64, 40, 53], [-1, 64, 80, 106]] | 73,856   |
| Conv2d-9             | [-1, 128, 40, 53]        | 18,496   |
| Conv2d-10            | [-1, 128, 40, 53]        | 147,584  |
| DownConv-11          | [[-1, 128, 40, 53], [-1, 128, 40, 53]] | 147,584  |
| ConvTranspose2d-12   | [-1, 64, 80, 106]        | 32,832   |
| Conv2d-13            | [-1, 64, 80, 106]        | 73,792   |
| Conv2d-14            | [-1, 64, 80, 106]        | 36,928   |
| UpConv-15            | [-1, 64, 80, 106]        | 0        |
| ConvTranspose2d-16   | [-1, 32, 160, 212]       | 8,224    |
| Conv2d-17            | [-1, 32, 160, 212]       | 18,464   |
| Conv2d-18            | [-1, 32, 160, 212]       | 9,248    |
| UpConv-19            | [-1, 32, 160, 212]       | 0        |
| Conv2d-20            | [-1, 2, 160, 212]        | 66       |

**Total params**: 466,562
**Trainable params**: 466,562
**Non-trainable params**: 0

##### Arquitetura da CNN

| Layer (type)         | Output Shape             | Param #  |
|----------------------|--------------------------|----------|
| Conv2d-1             | [-1, 32, 160, 212]       | 896      |
| BatchNorm2d-2        | [-1, 32, 160, 212]       | 64       |
| MaxPool2d-3          | [-1, 32, 80, 106]        | 0        |
| Conv2d-4             | [-1, 32, 80, 106]        | 9,248    |
| BatchNorm2d-5        | [-1, 32, 80, 106]        | 64       |
| MaxPool2d-6          | [-1, 32, 40, 53]         | 0        |
| Conv2d-7             | [-1, 32, 40, 53]         | 9,248    |
| BatchNorm2d-8        | [-1, 32, 40, 53]         | 64       |
| MaxPool2d-9          | [-1, 32, 20, 26]         | 0        |
| Conv2d-10            | [-1, 32, 20, 26]         | 9,248    |
| BatchNorm2d-11       | [-1, 32, 20, 26]         | 64       |
| Conv2d-12            | [-1, 32, 20, 26]         | 25,632   |
| BatchNorm2d-13       | [-1, 32, 20, 26]         | 64       |
| MaxPool2d-14         | [-1, 32, 10, 13]         | 0        |
| Linear-15            | [-1, 128]                | 532,608  |
| Dropout1d-16         | [-1, 128]                | 0        |
| Linear-17            | [-1, 64]                 | 8,256    |
| Dropout1d-18         | [-1, 64]                 | 0        |
| Linear-19            | [-1, 17]                 | 1,105    |

**Total params**: 596,561

**Trainable params**: 596,561

**Non-trainable params**: 0




##### Treinamento da Shallow U-net

###### Divisão em Conjuntos de Treino, Validação e Teste:
- Se selecionou 75% do dataset original para gerar um dataset reduzido.
- Se utilizou um seed 42 para fazer todo split (dataset não usado, train-test-val split).
- Esse dataset reduzido foi dividido em 72% para treino, 10% para validação e 18% para teste.
- Se escolheu só usar as imagens da esquerda.

###### Aumento dos Dados
As seguintes transformações foram aplicadas aos dados de treinamento usando `transforms.Compose`:

1. **RandomZoomOut**: Aplica um zoom out aleatório na imagem com uma probabilidade de 20%.
2. **RandomRotation**: Rotaciona a imagem aleatoriamente dentro do intervalo de 0 a 20 graus.
3. **RandomHorizontalFlip**: Inverte a imagem horizontalmente com uma probabilidade de 50%.
4. **GaussianBlur**: Aplica um desfoque gaussiano com um tamanho de kernel de 3x3.
5. **RandomAdjustSharpness**: Ajusta a nitidez da imagem com um fator de nitidez de 1.25.
6. **Resize**: Finalmente todas as imagens foram reajustadas para ter o mesmo tamanho depois das transformações.

###### Hiperparâmetros

- Batch size: 32
- Tamanho das imagens: (162,212,3)
- Número de classes: 2
- Profundidade da Unet: 3
- Filtros inicíais: 32
- Modo: Concatenação
- Épocas: 188
- Learning rate: 0.00005

##### Treinamento do modelo integrado SUN-CNN

###### Divisão em Conjuntos de Treino, Validação e Teste:
- Se utilizou todo o dataset.
- Se utilizou um seed 42 para fazer todos os splits (train-test-val split).
- Esse dataset foi dividido em 76.5% para treino, 10% para validação e 13.5% para teste.
- Se escolheu só usar as imagens da esquerda.

###### Aumento dos Dados
As seguintes transformações foram aplicadas aos dados de treinamento usando `transforms.Compose`:

1. **RandomZoomOut**: Aplica um zoom out aleatório na imagem com uma probabilidade de 20%.
2. **RandomRotation**: Rotaciona a imagem aleatoriamente dentro do intervalo de 0 a 20 graus.
3. **RandomHorizontalFlip**: Inverte a imagem horizontalmente com uma probabilidade de 50%.
4. **GaussianBlur**: Aplica um desfoque gaussiano com um tamanho de kernel de 3x3.
5. **RandomAdjustSharpness**: Ajusta a nitidez da imagem com um fator de nitidez de 1.25.
6. **Resize**: Finalmente todas as imagens foram reajustadas para ter o mesmo tamanho depois das transformações.

###### Hiperparâmetros de treinamento

- Batch size: 32
- Tamanho das imagens: (162,212,3)
- Número de classes: 17
- Épocas: 150
- Learning rate inícial: 0.0005
- Learning rate decay: 0.98, cada 5 épocas

#### Resultados

##### Curvas de perdas e precisão

Como o treinamento da rede Shallow U-net + CNN teve duas etapas, se obtiveram duas curvas de perdas

![Curva de Perda UNet](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/curva_perda_unet.png)

![Curves Classification Gestures](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/curves_classification_gestures.png)

##### Matriz de confusão

![Confusion Matrix](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/conf_matrix.png)

##### Relátorio de classificação

![Classification Report](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/classification_report.png)

##### Métricas de segmentação

- Intersection over Union (IoU): 0.90
- Pixel accuracy: 0.82

<details>
<summary title="Click to Expand/Collapse">Exemplos de gestos segmentados</summary>

| Comando            | Exemplo                                                        | Comando            | Exemplo                                                        |
|--------------------|-----------------------------------------------------------------|--------------------|----------------------------------------------------------------|
| Start_comm         | ![Image 1](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class1.png) | End_comm           | ![Image 2](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class2.png) |
| Up                 | ![Image 3](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class3.png) | Down               | ![Image 4](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class4.png) |
| Photo              | ![Image 5](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class5.png) | Backwards          | ![Image 6](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class6.png) |
| Carry              | ![Image 7](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class7.png) | Boat               | ![Image 8](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class8.png) |
| Here               | ![Image 9](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class9.png) | Mosaicc      | ![Image 10](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class10.png) |
| Num_delimiter                | ![Image 11](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class11.png) | One                | ![Image 12](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class12.png) |
| Two              | ![Image 13](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class13.png) | Three               | ![Image 14](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class14.png) |
| Four               | ![Image 15](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class15.png) | Five           | ![Image 16](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class16.png) |
| Negative | ![Image 17](https://raw.githubusercontent.com/RTrombini/IA904-2024S1/main/projetos/sinais_mergulhadores/assets/exampleResults_class0.png)   |  | |
</details>

##### Métricas de classificação

- Precisão: 0.95
- Sensibilidade: 0.91
- F1 score: 0.92 
- Cohen Kappa score: 0.94
- Matthews Correlation Coefficient: 0.94

##### Número de parâmetros treináveis

- Shallow U-net: 466,562
- CNN: 596,561
- Total: 1,063,123

## Discussão

A motivação central deste projeto é desenvolver um sistema eficaz para identificar e interpretar sinais de mão de mergulhadores, com o objetivo de melhorar a comunicação subaquática e a segurança durante mergulhos. Este sistema se inspira no projeto CADDY, que visa entender o comportamento dos mergulhadores através da interpretação de gestos manuais simbólicos e indicadores não verbais. Para atingir este objetivo, foram exploradas duas abordagens principais: a detecção e classificação de gestos utilizando a YOLOv8 e a combinação de segmentação com a Shallow U-Net seguida por uma classificação com uma CNN.

O treinamento do modelo YOLOv8 nano envolveu a preparação do dataset, incluindo a conversão das coordenadas de ROI para o formato YOLO. Utilizamos 100 épocas com imagens de 640x640 pixels. Os resultados obtidos foram:

- **Precisão (Precision)**: 0.913
- **Revocação (Recall)**: 0.928
- **mAP50 (Mean Average Precision at IoU=0.50)**: 0.932
- **mAP50-95 (Mean Average Precision at IoU=0.50:0.95)**: 0.693

Por outro lado, a abordagem utilizando a Shallow U-Net para segmentação seguida por uma CNN para classificação apresentou resultados competitivos. Com um menor número de parâmetros, essa abordagem demonstrou ser menos custosa computacionalmente e ainda assim eficaz para a tarefa de detecção de gestos subaquáticos.

Os resultados indicam que ambos os métodos são viáveis para a detecção e classificação de gestos subaquáticos. No entanto, ao comparar os dois métodos, observamos que os resultados foram muito próximos. Dado que o método Shallow U-Net + CNN possui um menor custo computacional e um número significativamente menor de parâmetros, ele se mostra mais performático e relevante para aplicações práticas.

Em termos de métricas, tanto a precisão quanto o recall são cruciais. A precisão é importante para minimizar falsos positivos, enquanto o recall é essencial para garantir que os gestos sejam detectados sempre que presentes. No contexto de segurança subaquática, um alto recall pode ser ligeiramente mais crítico, pois garantir que todos os gestos sejam detectados pode prevenir acidentes e melhorar a comunicação.

Comparando os dois métodos, o método Shallow U-Net + CNN, devido ao seu menor custo computacional e alta performance, parece ser mais adequado para futuras aplicações. Este método não só alcança resultados comparáveis aos da YOLOv8, mas também é mais eficiente, tornando-se uma escolha preferível para a implementação em sistemas de comunicação subaquática.

Esta análise destaca a importância de considerar não apenas a performance bruta, mas também a eficiência e a aplicabilidade prática ao escolher e desenvolver modelos de Machine Learning para detecção de gestos subaquáticos.


## Conclusão

O desenvolvimento deste projeto nos permitiu alcançar dois sistemas eficazes para a detecção e classificação de gestos de mão de mergulhadores. Utilizando duas abordagens distintas – YOLOv8 e Shallow U-Net seguida de CNN – conseguimos validar a viabilidade de ambas as técnicas, cada uma com seus pontos fortes específicos.

### Principais Conclusões

1. **Viabilidade de Modelos de Detecção e Classificação**: Tanto o YOLOv8 quanto a combinação de Shallow U-Net com CNN demonstraram ser eficazes na tarefa de detecção de gestos subaquáticos. Cada abordagem apresentou alta precisão e recall, com resultados muito próximos.

2. **Eficiência Computacional**: O método Shallow U-Net + CNN, devido ao seu menor número de parâmetros e custo computacional reduzido, mostrou-se mais eficiente, tornando-se uma alternativa preferível para aplicações práticas onde recursos computacionais são limitados.

3. **Importância das Métricas de Avaliação**: A precisão e o recall se mostraram métricas essenciais para avaliar a performance dos modelos, garantindo que os gestos sejam corretamente detectados e minimizando falsos positivos e negativos.

### Principais Desafios

1. **Preparação e Conversão do Dataset**: Converter o dataset para um formato compatível com os modelos de detecção foi um desafio significativo, além da necessidade de balancear as classes de gestos para evitar vieses nos resultados.

2. **Pré-processamento das Imagens**: Lidar com as variáveis condições subaquáticas durante o pré-processamento das imagens foi crítico para melhorar a performance dos modelos.

### Lições Aprendidas

1. **Importância da Reprodutibilidade**: Garantir que nossos métodos e resultados sejam reprodutíveis é crucial para a validade científica. A criação de pipelines claros e detalhados, juntamente com a documentação rigorosa dos passos, permite que outros pesquisadores possam replicar e validar nossos achados.

2. **Uso de Métricas Adequadas**: Selecionar as métricas corretas para avaliar a performance dos modelos é fundamental. Precisão, recall, mAP e outras métricas foram essenciais para compreender a eficácia dos modelos desenvolvidos.

3. **Comparação entre Abordagens**: Comparar diferentes abordagens de visão computacional nos permitiu identificar não apenas qual modelo performa melhor, mas também qual é mais eficiente e prático para implementações reais. Esse entendimento é vital para a aplicação de soluções em ambientes operacionais.

4. **Adaptação a Condições Variáveis**: O pré-processamento das imagens e a adaptação dos modelos para lidar com as variáveis condições subaquáticas foram desafios que nos ensinaram a importância da flexibilidade e robustez nos métodos de visão computacional.


Este projeto não apenas avançou na área de detecção de gestos subaquáticos, mas também solidificou nosso entendimento sobre a importância da reprodutibilidade, avaliação de métricas e comparação entre diferentes abordagens em projetos de visão computacional.


## Trabalhos futuros

Com mais tempo e recursos, há várias áreas que poderiam ser exploradas e melhoradas para fortalecer ainda mais os resultados obtidos neste projeto.

### Ajuste Fino de Hiperparâmetros

1. **Exploração de Hiperparâmetros**: Realizar uma busca mais aprofundada por hiperparâmetros poderia otimizar ainda mais o desempenho dos modelos. Isso inclui ajustar taxas de aprendizado, tamanhos de batch e parâmetros específicos dos modelos YOLOv8 e Shallow U-Net.

2. **Validação Cruzada**: Implementar técnicas de validação cruzada para garantir que o modelo generalize bem em diferentes subconjuntos dos dados.

### Testes em um Sistema em Tempo Real

1. **Implementação em Tempo Real**: Implementar e testar os modelos em um sistema de comunicação subaquática em tempo real para validar sua eficácia operacional e identificar possíveis melhorias.

2. **Desenvolvimento de Interface**: Criar uma interface de usuário amigável que permita aos mergulhadores e operadores interagir com o sistema de reconhecimento de gestos de maneira intuitiva.

### Exploração de Modelos Alternativos

1. **Arquiteturas de Modelos Diferentes**: Explorar outras arquiteturas de modelos de deep learning, como Transformers, que têm se mostrado promissoras em várias tarefas de visão computacional.

2. **Modelos Híbridos**: Investigar combinações de diferentes tipos de modelos (e.g., combinação de CNNs com RNNs para considerar a sequência temporal dos gestos).

3. **Modelos YOLO Maiores**: Considerando que utilizamos apenas a YOLOv8n (nano), seria interessante explorar como os modelos maiores da mesma família (YOLOv8s, YOLOv8m, YOLOv8x) poderiam melhorar a performance.

### Pré-processamento Avançado de Imagens

1. **Filtros e Técnicas de Realce de Imagem**: Desenvolver e aplicar técnicas mais avançadas de pré-processamento de imagens para melhorar a qualidade das imagens subaquáticas, como filtros adaptativos e métodos de realce de contraste.

2. **Redução de Ruído**: Implementar algoritmos mais sofisticados para a redução de ruído nas imagens, o que poderia melhorar a precisão da detecção e classificação dos gestos.

Ao abordar essas áreas, poderíamos não apenas melhorar o desempenho dos modelos desenvolvidos, mas também garantir sua aplicabilidade prática em uma variedade maior de condições e cenários, contribuindo para a comunicação subaquática de maneira mais eficiente e segura.


## Referências

- Gomez Chavez, A.; Ranieri, A.; Chiarella, D.; et al. CADDY Underwater Stereo-Vision Dataset for Human–Robot Interaction (HRI) in the Context of Diver Activities. J. Mar. Sci. Eng. 2019, 7, 16.
- Chiarella, D. Towards Multi-AUV Collaboration and Coordination: A Gesture-Based Multi-AUV Hierarchical Language and a Language Framework Comparison System. J. Mar. Sci. Eng. 2023, 11, 1208.
- Ultralytics. YOLOv8 Documentation. Available at: [https://docs.ultralytics.com/](https://docs.ultralytics.com/)
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
- Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980.
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778).
- Lin, T. Y., Goyal, P., Girshick, R., He, K., & Dollar, P. (2020). Focal Loss for Dense Object Detection. IEEE Transactions on Pattern Analysis and Machine Intelligence, 42(2), 318-327.
- Paszke, A., et al. (2019). PyTorch: An Imperative Style, High-Performance Deep Learning Library. In Advances in Neural Information Processing Systems (NeurIPS).
- Redmon, J., & Farhadi, A. (2018). YOLOv3: An incremental improvement. arXiv preprint arXiv:1804.02767.
- Ronneberger, O., Fischer, P., & Brox, T. (2015). U-Net: Convolutional Networks for Biomedical Image Segmentation. In International Conference on Medical image computing and computer-assisted intervention (pp. 234-241). Springer, Cham.
- Metrics Reloaded. Platform for selecting and evaluating performance metrics for machine learning models. Available at: [https://metrics-reloaded.io/](https://metrics-reloaded.io/)
- Simonyan, K., & Zisserman, A. (2014). Very Deep Convolutional Networks for Large-Scale Image Recognition. arXiv preprint arXiv:1409.1556.

