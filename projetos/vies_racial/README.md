# `Desvendando Viés: Uma Análise dos Algoritmos de Imagem e Detecção Facial`
# `Unraveling Bias: An Analysis of Image and Facial Detection Algorithms`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, 
oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

Segue tabela com as informações dos alunos do projeto:

|Nome  | RA | Curso|
|--|--|--|
| Leonardo Vilela de Abreu Silva Pereira | 220198 | Aluno Especial |
| Sílvia Claudino Martins Gomes | 271629 | Aluna Especial |

## Descrição do Projeto
O viés racial em modelos de detecção e reconhecimento facial é a tendência de desempenho desigual com base na raça das pessoas, devido a desequilíbrios nos dados de treinamento e padrões discriminatórios nos algoritmos. Identificar o viés envolve avaliar o desempenho em diferentes grupos raciais, analisar os conjuntos de dados e investigar os algoritmos utilizados.

O projeto visa compreender o viés racial em modelos amplamente reconhecidos na literatura. Para este estudo, será utilizada uma base de dados de imagens de rostos de pessoas de diversas etnias, denominada FairFace. Serão aplicados modelos de visão computacional populares na comunidade de processamento de imagens para serem comparados. Espera-se, ao final do projeto, compreender quais modelos apresentam melhor desempenho em relação ao viés racial.

Para alcançar este objetivo de detecção de viés iremos primeiramente analisar os embeddings das imagens utilizando ferramentas de redução de dimensionalidade como t-SNE (*t-distributed Stochastic Neighbor Embedding*) ou UMAP (*Uniform Manifold Approximation and Projection*) e, neste espaço reduzido, verificar como a rede separa diversas etnias. 

Realizamos, também, uma análise na literatura de métricas de viés, como paridade demográfica, igualdade de oportunidades,etc... Estas métricas são essenciais para compreender melhor como o desempenho dos modelos varia entre diferentes grupos raciais e para identificar potenciais áreas de discriminação.

Para a análise dessas métricas, selecionamos alguns modelos populares de detecção facial (MTNCC, Blaze Face e Retina Face), utilizando o dataset mencionado na seção de dataset. O MTNCC (Multi-Task Cascaded Convolutional Networks) é conhecido por sua eficácia em detecção facial multitarefa. Blaze Face é um modelo leve e rápido, frequentemente usado em aplicações móveis, enquanto Retina Face é aclamado por sua precisão em reconhecimento facial robusto. Esses modelos serão avaliados para identificar disparidades de desempenho entre diferentes grupos étnicos, proporcionando uma visão abrangente das limitações e potencialidades dos modelos em termos de equidade racial.

## Metodologia
Nesta seção, será delineada a metodologia adotada para investigar o viés na distribuição dos embeddings das redes de imagens em relação à raça, utilizando técnicas de redução de dimensionalidade como t-Distributed Stochastic Neighbor Embedding (t-SNE) ou Uniform Manifold Approximation and Projection (UMAP). 

No que diz respeito ao pré-processamento, prevemos realizar poucas ou nenhuma modificação nos dados, uma vez que nosso objetivo é analisar o comportamento dos modelos e identificar quais hiperparâmetros precisam ser ajustados para mitigar o viés racial em cada um deles. Também planejamos aumentar o conjunto de dados utilizando diversas técnicas de aumento de dados, garantindo o equilíbrio das etnias representadas no conjunto. 

Esse enfoque permitirá a avaliação dos melhores modelos e ajustes de hiperparâmetros que possam mitigar o viés racial nos modelos. Por fim, pretendemos aplicar técnicas de interpretabilidade, como atribuição de saliência e mapas de ativação, para compreender quais características da imagem os modelos estão priorizando em suas decisões.

## Bases de Dados e Evolução
A base de dados que será utilizada será a [FairFace](https://github.com/joojs/fairface). Um conjunto de dados de atributos faciais para raças, gêneros e idades equilibrados. Durante este projeto, só serão utilizados os rótulos de raça. [1] Serão apresentados três exemplos de imagens presentes entre os dados e os respectivos rótulos:

<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="text-align: center;">
    <img src="./data/raw/train/40864.jpg" alt="Imagem 1" width="30%" />
    <p>Idade: 50-59 <br>Gênero: Male <br>Raça: Middle Eastern</p>
  </div>
  <div style="text-align: center;">
    <img src="./data/raw/train/86722.jpg" alt="Imagem 2" width="30%" />
    <p>Idade: 0-2<br>Gênero: Male<br>Raça: Black</p>
  </div>
  <div style="text-align: center;">
    <img src="./data/raw/train/17.jpg" alt="Imagem 3" width="30%" />
    <p>Idade: 20-29<br>Gênero: Female<br>Raça: Southeast Asian</p>
  </div>
</div>

O conjunto é conhecido por realizar um bom balanceamento entre as diversas etnias presentes no conjunto como é possível visualizar na imagem a seguir:

![Gráfico](./assets/grafico_dados.jpg)

A base de dados possui dois conjuntos separados, um composto para o treino, com 86744 imagens, e o outro composto para a validação, com 10954 imagens. Além do gráfico, podemos analisar os dados de balanceamento através da tabela a seguir, com a quantidade de imagens para cada etnia no conjunto de treino e validação.

|Etnia  | Treino | Validação |
|--|--|--|
| White | 16527 | 2085 |
| Latino Hispanic | 13367 | 1623 |
| Indian | 12319 | 1556 |
| East Asian | 12287 | 1550 |
| Black | 12233 | 1516 |
| Southeast Asian | 10795 | 1415 |
| Middle Eastern | 9216 | 1209 |

A seguir, será apresentado um resumo em forma de tabela com as principais informações da base de dados.

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
FairFace | https://github.com/dchen236/FairFace | Um conjunto de dados de atributos faciais para raças, gêneros e idades equilibrados. [1]

## Ferramentas

Serão apresentadas a seguir as ferramentas e bibliotecas a serem utilizadas durante o projeto.

Biblioteca principal:
- PyTorch

Data-augmentation:
- Random Rotation
- Random Horizontal Flip
- Random Vertical Flip
- Random Resized Crop

Modelos utilizados para geração dos embeddings:
- FaceNet
- VGGFace

Redução de dimensionalidade:
- t-Distributed Stochastic Neighbor Embedding (t-SNE) 
- Uniform Manifold Approximation and Projection (UMAP)

Avaliação de modelos:
- Weights & Biases

Cálculo de métricas:
- TorchEval

Explicabilidade:
- Grad-cam
- Saliency Vanilla_gradient

## Principais desafios
Durante o desenvolvimento do projeto, antecipamos a presença de desafios significativos relacionados a questões éticas. Conscientes da diversidade de perspectivas e debates valiosos, reconhecemos a necessidade de um estudo cuidadoso. O reconhecimento facial, tarefa que sucede a detecção facial, objeto de estudo nesta pesquisa, frequentemente é encarado como uma prática intrusiva que pode expor indivíduos pertencentes a minorias em certos contextos nacionais. Esses grupos correm o risco de serem erroneamente identificados ou percebidos como ameaças à segurança por modelos de reconhecimento facial. No entanto, a compreensão das injustiças e preconceitos presentes nessas situações é uma empreitada complexa. Além disso, enfrentaremos o desafio de compreender o conceito de etnia, especialmente em uma sociedade tão diversa e miscigenada como a nossa.

## Cronograma
Nesta seção será apresentado o cronograma do projeto.

|Semana | Data | Atividade |
|--|--|--|
| Semana 1 | 28/04 à 04/05 | Definição do projeto |
| Semana 2 | 05/05 à 11/05 | Documentação e planejamento do projeto |
| Semana 3 | 12/05 à 18/05 | Análise dos dados |
| Semana 4 | 19/05 à 25/05 | Aplicação da técnica t-SNE |
| Semana 5 | 26/05 à 01/06 | Aplicação da técnica UMAP |
| Semana 6 | 02/06 à 08/06 | Comparação entre modelos e visualização de explicabilidade |
| Semana 7 | 09/06 à 15/06 | Documentação e escrita das conclusões do projeto |
| Semana 8 | 16/06 à 22/06 | Revisão e preparação da apresentação |

## Referências

[1] FairFace. 2021. "FairFace: Face Attribute Dataset for Balanced Race, Gender, and Age". https://github.com/joojs/fairface

[2] Kärkkäinen, K., & Joo, J. (2019). FairFace: Face Attribute Dataset for Balanced Race, Gender, and Age. Recuperado de https://doi.org/10.48550/arXiv.1908.04913

[3] Cavazos, J. G., Phillips, P. J., Castillo, C. D., & O’Toole, A. J. (2021). Accuracy Comparison Across Face Recognition Algorithms: Where Are We on Measuring Race Bias? IEEE Transactions on Biometrics, Behavior, and Identity Science, 3(1), 101–111. DOI: 10.1109/TBIOM.2020.3027269
 
