# `Detecção de ervas daninhas usando visão computacional`
# `Weed detection using computer vision`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Dra. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Curso|
> |--|--|--|
> | Erick Aparecido Escagion | 249095  | Aluno de mestrado em Engenharia Elétrica na área de Engenharia de Computação|
> | Víctor Manuel Villegas Salabarria  | 272594  | Aluno de mestrado em Engenharia Mecânica|

## Descrição do Projeto

As ervas daninhas são uma das pragas agrícolas mais prejudiciais que tem um grande impacto sobre as plantações. As ervas daninhas são responsáveis pelo aumento dos custos de produção devido ao desperdício de culturas, o que tem um impacto significativo na economia agrícola global [1]. Neste sentido, o objetivo geral deste projeto é detectar ervas daninhas em lavouras utilizando imagens de campos de cultivo para auxiliar o engenheiro-agrônomo a tomar decisões quanto à aplicação adequada de herbicidas, eliminando a necessidade de pulverização em massa, prática predominante na agricultura de grande escala, bem como reduzindo custos e tornando os produtos mais atrativos para os consumidores.

## Métodos

O método utilizado neste trabalho é composto por: aquisição de dados, pré-processamento, experimentação de modelos e avaliação. Esse método foi cíclico, para que, a cada avaliação de um modelo, sejam identificadas novas técnicas visando obter melhores resultados. Além disso, foi criada uma linha de base, que é um modelo de aprendizado de máquina simples para a criação de previsões rápidas para o conjunto de dados em questão. Somado a isso, durante a fase de experimentação, utilizou-se alguns métodos recentes de aprendizado profundo que têm demonstrado um bom desempenho na deteccção de objetos, sendo eles: a família de métodos R-CNN - *Regions with CNN Features*; [2]. Após uma primeira análise dos dados, alguns pré-processamentos foram testados, como a eliminação de ruídos sal e pimenta. Por fim, na etapa de avaliação, para determinar se um objeto foi localizado corretamente, foi usada a métrica quantitativa IoU (Intersection over Union) como medida de similaridade, essa medida é calculada pela área de sobreposição, dividida pelo tamanho da união das duas caixas delimitadoras. Foi utilizado tambem a AP (Average Precision), metrica essa que reflete tanto a precisão quanto a abrangência da recuperação ou classificação de itens relevantes, sendo uma ferramenta valiosa para avaliar e comparar os modelos [3].

## Bases de Dados

> |Base de Dados | Endereço na Web | Resumo descritivo
> |----- | ----- | -----
> *Weeds Computer Vision Project* | https://universe.roboflow.com/augmented-startups/weeds-nxe1w | Um conjunto de imagens de plantações com ervas daninhas que pode facilmente confundir os modelos de detecção de objetos devido à semelhança das ervas daninhas em relação aos seus arredores [4]. Esse conjunto contém 3664 imagens de treinamento (87%), 359 de validação (9%) e 180 imagens de teste (4%). As imagens estão disponíveis em formato JPEG, coloridas e com resolução de 416x416 píxeis.
> *Pessoal* | <span style="color:red">(projetos/weeds/data/guys)</span>. | Um conjunto de 20 imagens de vegetação distintas em formato JPEG coloridas, tiradas a partir de um Samsung A71 e de um Iphone 11 em varios terrenos.

Os dados do Weeds Computer Vision Project estão disponiveis no link da própria tabela, devido ao tamanho do dataset nao ser suportado pelo GitHub, para chegar na sua versão processada basta usa o script disponibilizado em <span style="color:red">(projetos/weeds/src/process.py)</span> um exemplo desse processamento pode ser visto em <span style="color:red">(projetos/weeds/notebooks/removing_noise_from_images.ipynb)</span>.

## Ambiente Computacional

O Google Colab foi escolhido como ambiente de desenvolvimento por ser uma plataforma online gratuita que facilita a interação da equipe, oferece acesso a GPUs e TPUs de maneira limitada(na sua versão gratuita), a configuração é simples, baseada no Jupyter Notebook, com bibliotecas populares pré-instaladas e a sua integração com o Google Drive permite fácil armazenamento e organização de dados e projetos [5].

Varias bibliotecas foram utilizadas no decorrer do projeto, entre elas as principais foram:

- OS: Utilizada para interagir com o sistema operacional, permitindo operações como navegação entre diretórios, manipulação de arquivos e execução de comandos do sistema.
- Glob: Usada para encontrar todos os caminhos correspondentes a um padrão específico, facilitando a localização de arquivos em diretórios.
- Matplotlib: Uma biblioteca de visualização de dados que permite a criação de gráficos e figuras, essencial para análise e apresentação de dados.
- Pillow: Uma biblioteca de processamento de imagens que permite abrir, manipular e salvar diversos formatos de imagem.
- Collections: Oferece tipos de dados especializados, como defaultdict, e Counter, que são úteis para estruturas de dados como estruturas de dados.
- Numpy: Fundamental para a computação numérica em Python, fornece suporte para arrays e matrizes multidimensionais, além de funções matemáticas de alto nível.
- csv: Utilizada para ler e escrever arquivos CSV (Comma Separated Values), facilitando a manipulação de dados tabulares.
- Random: Fornece funções para geração de números aleatórios e para realizar operações aleatórias, como a seleção aleatória de elementos.
- OpenCV: Biblioteca de visão computacional que permite o processamento e análise de imagens e vídeos, suportando diversas operações de transformação e reconhecimento.
- Datetime: Utilizada para manipulação de datas e horas, permitindo operações como cálculos de tempo e formatação de datas.
- Torch: Biblioteca para machine learning e deep learning, essencial para a criação e treinamento de modelos de aprendizado profundo.
- TorchVision: Conjunto de ferramentas para visão computacional com - PyTorch, incluindo transformações de imagem e datasets prontos para uso em modelos de visão computacional.
- Sklearn: Biblioteca de aprendizado de máquina que oferece uma vasta gama de algoritmos e ferramentas para análise e modelagem de dados.
- Tqdm: Biblioteca para exibição de barras de progresso, facilitando o acompanhamento da execução de loops e tarefas longas.
- Pickle: Utilizada para serialização e desserialização de objetos Python, permitindo salvar e carregar objetos de forma eficiente.
- Pandas: Biblioteca para manipulação e análise de dados que oferece estruturas de dados como DataFrames, facilitando o trabalho com dados tabulares.

Vale o destaque que o uso do Google colab na versao gratuita nao atendeu o projeto de maneira eficiente, pois causou gargalo devido as limitacoes do uso GPU por dia.

## Workflow

![Workflow](https://github.com/mapovoa/IA904-2024S1/blob/main/projetos/weeds/assets/wf.png)

## Avaliação

Neste projeto, o problema pode ser enquadrado como uma tarefa de detecção de objetos, onde o objetivo é detectar plantas daninhas em imagens, baseando-se nas coordenas do boundBox, as imagens de entrada são imagens RGB, tambem foram testadas com as mesmas imagens porem convetidas em escala de Cinza.

O modelo de aprendizado de máquina deve prever a classe (planta daninha ou não) e a localização (caixa delimitadora) de cada objeto na imagem.
Portanto, o "problem fingerprint" deste projeto é uma tarefa de detecção de objetos em imagens.
Tendo definido a categoria do problema, o próximo passo é selecionar as métricas de avaliação recomendadas para essa categoria.
Algumas das metricas escolhidas são:
Average Precision (AP): Mede a precisão média do modelo em diferentes limiares de confiança. É uma métrica abrangente que leva em conta tanto a precisão quanto a revocação.
Intersection over Union (IoU): Mede a sobreposição entre as caixas delimitadoras previstas e as caixas de referência. É importante para avaliar a qualidade da localização dos objetos.
Portanto, neste projeto, utilizaremos as seguintes métricas:
Average Precision with IoU 0.5 (AP@0.5): Calcula a precisão média considerando apenas as previsões com IoU acima de 0.5 como verdadeiros positivos. Essa métrica avalia tanto a classificação quanto a localização dos objetos.

A escolha dessa métrica se justifica por:
Ela é amplamente utilizada e recomendada para tarefas de detecção de objetos, conforme indicado no artigo "Metrics Reloaded".
Ao considerar um limiar de IoU de 0.5, a métrica avalia não apenas a classificação correta dos objetos, mas também a qualidade da localização, evitando o "pitfall" de métricas que não consideram a precisão espacial.
É uma métrica abrangente que resume o desempenho do modelo em um único valor, facilitando a comparação entre diferentes modelos.
Foi escolhido além disso, uma análise quantitativa dos modelos em quanto ao seu desempenho considerando istos parâmetros para dos escenarios diferentes o primeiro com 1 erva somente, o segundo teste com ervas entre 5 e 10 ervas e o final com todas as imagens. 
Sobre a interpretação das metricas, calcularemos a AP@0.5 para cada imagem de teste e, em seguida, reportaremos a média desses valores como o resultado final. Essa abordagem de agregação por imagem é recomendada para evitar distorções causadas por diferentes números de objetos por imagem. A AP@0.5 varia de 0 a 1, sendo 1 o valor ideal. Quanto maior o valor, melhor o desempenho do modelo na tarefa de detecção de objetos, considerando tanto a classificação quanto a localização. Valores abaixo de 0.5 indicam um desempenho insatisfatório. 

## Experimentos e Resultados

Foram realizados 16 experimentos no total, variando o uso de pré-processamento para reduzir o ruído sal e pimenta tanto em imagens RGB quanto em imagens em escala de cinza durante o treinamento. Também foram treinados modelos com as imagens originais. Para cada caso, foram considerados os seguintes cenários de treinamento:

- Dados com uma planta daninha por imagem
- Dados com 5-10 plantas daninhas por imagem
- Dados com 10% das imagens selecionadas aleatoriamente
- Dados com 30% das imagens selecionadas aleatoriamente

Para o primeiro caso com 50 imagens de teste de entre 5 e 10 ervas daninhas o melhor modelo resulto sendo o teste treinado com imagems desse mesmo tipo RGB com preprocessamento incluido com um AP de 0.84 Como visto na Figura abaixo.

![FirstTest](https://github.com/mapovoa/IA904-2024S1/blob/main/projetos/weeds/assets/first-test.jpeg)

Para este primeiro caso os resultados com todas imagens preprocessadas tanto em RGB como escala de cinza são mostradas na Tabela abaixo.

|Imagens com pre-processamento  | RGB | Escala de cinza |
|--|--|--|
| 1 Erva daninha | 0.05 | 0.03 |
| 5 - 10 Ervas daninhas | 0.84 | 0.36 |
| 10% dos dados | 0.41 | 0.18 |
| 30% dos dados | 0.39 | 0.25 |

Para o segundo cenario com 50 imagens de teste de entre 1 e 16 ervas daninhas o melhor modelo resulto sendo o teste treinado com imagems também de entre 5 e 10 ervas daninhas tipo RGB com preprocessamento incluido com um AP de 0.76.

![SecondTest](https://github.com/mapovoa/IA904-2024S1/blob/main/projetos/weeds/assets/second-test.jpeg)

Para este segundo caso os resultados com todas imagens preprocessadas tanto em RGB como escala de cinza são mostradas na Tabela abaixo.

|Imagens com pre-processamento  | RGB | Escala de cinza |
|--|--|--|
| 1 Erva daninha | 0.32 | 0.20 |
| 5 - 10 Ervas daninhas | 0.76 | 0.53 |
| 10% dos dados | 0.61 | 0.44 |
| 30% dos dados | 0.59 | 0.44 |


## Discussão
Os resultados mostram que o uso de pré-processamento das imagens RGB teve um impacto positivo no desempenho dos modelos de detecção de plantas daninhas. Os modelos treinados com imagens RGB pré-processadas para reduzir o ruído sal e pimenta apresentaram os melhores resultados em termos de Average Precision com IoU 0.5 (AP@0.5).
Isso indica que o pré-processamento foi eficaz em melhorar a qualidade das imagens de entrada, facilitando o aprendizado do modelo e, consequentemente, sua capacidade de detectar corretamente as plantas daninhas.

Outro aspecto relevante observado foi o impacto da quantidade de dados de treinamento. Os melhores resultados foram obtidos nos cenários com 5-10 plantas daninhas por imagem, tanto para o primeiro quanto para o segundo conjunto de experimentos. Isso sugere que uma quantidade intermediária de plantas daninhas por imagem (entre 5-10) fornece um conjunto de treinamento mais equilibrado e representativo, permitindo que o modelo aprenda de forma mais eficaz as características das plantas daninhas. Por outro lado, os cenários com apenas 1 planta daninha por imagem ou com apenas 10% e 30% dos dados de treinamento apresentaram desempenho inferior. Isso indica que esses conjuntos de treinamento podem não ter sido suficientemente representativos para que o modelo aprendesse as características relevantes.

Um resultado interessante foi que os modelos treinados com imagens em escala de cinza não conseguiram superar 40% de AP@0.5 em nenhum dos cenários. Isso sugere que a estratégia de utilizar imagens em escala de cinza não foi eficaz para a tarefa de detecção de plantas daninhas neste projeto. Provavelmente, as informações de cor presentes nas imagens RGB são importantes para que o modelo aprenda a distinguir as plantas daninhas de forma mais precisa. A perda dessas informações na conversão para escala de cinza pode ter prejudicado o desempenho dos modelos.

## Conclusão
Com base nos experimentos realizados, ficou evidente que o pré-processamento das imagens RGB, aplicando técnicas para reduzir o ruído sal e pimenta, resultou nos melhores desempenhos na detecção de plantas daninhas, indicando que essa abordagem foi eficaz em melhorar a qualidade das imagens de entrada e facilitar o aprendizado do modelo.

Além disso, os melhores resultados foram obtidos nos cenários com 5-10 plantas daninhas por imagem de treinamento, sugerindo que uma quantidade intermediária fornece um conjunto de treinamento mais equilibrado e representativo, permitindo que o modelo aprenda as características relevantes de forma mais eficaz. Por outro lado, os modelos treinados com imagens em escala de cinza não conseguiram superar 40% de AP@0.5 em nenhum dos cenários, indicando que a estratégia de utilizar apenas informações em escala de cinza não foi adequada para essa tarefa, provavelmente devido à perda de informações de cor importantes.

É importante ressaltar que o uso do Google Colab na sua versão gratuita foi uma limitação nos testes realizados, pois a GPU acabava rapidamente. Isso restringiu a capacidade de treinar e salvar mais modelos, o que poderia ter fornecido insights adicionais. Portanto, o acesso a uma maior capacidade computacional, incluindo memória e GPU, seria relevante para expandir a pesquisa e obter resultados ainda mais robustos.

## Trabalhos Futuros
Com base nesses resultados, algumas direções interessantes para estudos futuros incluem:

- Explorar outras técnicas de pré-processamento: Investigar se outras abordagens de pré-processamento, como aumento de dados, podem trazer ainda mais benefícios ao desempenho dos modelos.
- Avaliar arquiteturas de modelos diferentes: Testar diferentes arquiteturas de redes neurais convolucionais (CNNs) para a tarefa de detecção de plantas daninhas, a fim de identificar modelos mais adequados.
- Investigar o uso de informações adicionais: Avaliar se a incorporação de outras informações, como dados de sensoriamento remoto ou características agronômicas, pode melhorar ainda mais a capacidade de detecção dos modelos.
- Realizar testes em cenários reais: Aplicar os modelos treinados em situações reais de campo, avaliando seu desempenho em condições mais próximas da aplicação final.

Essas direções de pesquisa podem ajudar a aprimorar ainda mais a capacidade de detecção de plantas daninhas utilizando imagens digitais, contribuindo para o avanço dessa importante área de aplicação.

## Referências

> 1. De Morais Martins, Jean Marcos, and Roberto Andreani Junior. "Impactos das plantas daninhas nas culturas agrícolas e seus métodos de controle." Revista VIDA: Exatas e Ciências da Terra (VIECIT) 1.2 (2023): 34-54.
> 2. Wang, Aichen, Wen Zhang, and Xinhua Wei. "A review on weed detection using ground-based machine vision and image processing techniques." Computers and electronics in agriculture 158 (2019): 226-240.
> 3. Yan, Jiangqiao, et al. "IoU-adaptive deformable R-CNN: Make full use of IoU for multi-class object detection in remote sensing imagery." Remote Sensing 11.3 (2019): 286.
> 4. Startups, A. Weeds Dataset. [S.l.]: Roboflow, nov. 2021. https://universe.roboflow.com/augmented-startups/weeds-nxe1w. visited on 2024-05-05 Disponível em: <https://universe.roboflow.com/augmented-startups/weeds-nxe1w> 
> 5. Carneiro, Tiago, et al. "Performance analysis of google colaboratory as a tool for accelerating deep learning applications." Ieee Access 6 (2018): 61677-61685.
