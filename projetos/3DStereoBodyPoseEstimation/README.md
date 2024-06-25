# `Estimação Estéreo de Pose Corporal 3D`
# `3D Stereo Body Pose Estimation`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA904 - Projeto de Modelos em Computação Visual*, 
oferecida no primeiro semestre de 2024, na Unicamp, sob supervisão da Profa. Dra. Leticia Rittner e da Profa. Paula D. Paro Costa, ambas do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

Nome|RA|Curso
-|-|-
Elton Cardoso do Nascimento|233840|Mestrado em Engenharia Elétrica - Área de Concentração AE: Engenharia de Computação
Leonardo Rener de Oliveira|201270|Mestrado em Engenharia Elétrica - Área de Concentração AE: Engenharia de Computação

## Descrição do Projeto

Estimação de pose corporal é uma técnica amplamente utilizada em diversas indústrias como cinema e jogos, e se baseia na detecção de keypoints específicos no corpo de uma pessoa. Pode ser realizada desde utilizando equipamentos mais complexos e custosos como sistemas de mocap (motion capture), quanto por sensores mais simples como IMU (unidades de medição inercial), ou, utilizando IA (inteligência artificial), usando imagens de câmeras [1][2].

Mais especificamente, dentro do contexto universitário, é comum a necessidade de coletas simples de poses corporais, seja para testar e validar ideias em projetos de pesquisa, seja para realização de projetos de disciplina. Este tipo de demanda se beneficiaria de um método de coleta rápido e com pouca preparação, não necessitando de uma precisão tão grande quanto sistemas de mocap, como coleta a partir de imagens.

O objetivo deste projeto é então estimar a posição corporal no espaço 3D de uma pessoa, utilizando uma câmera estéreo (dipositivo com várias câmeras). Mais especificamente, este projeto utilizará uma "OAK-D", dipositivo desenvolvido para aplicações de visão computacional que possui três câmeras, duas laterais monocromáticas, global shutter e 720p; e uma central colorida, rolling shutter e 4K. A câmera se comunica com o computador através de um cabo USB-C, e também possui integrado processadores para execução de pipelines de processamento visual e IA [3].

## Métodos
Nossa proposta é utilizar um modelo detector de keypoints 2D pronto e utilizá-lo como um extrator de features, removendo as últimas camadas, executando-o uma vez em cada entrada e concatenado as features obtidas, que serão usadas de entrada para uma rede treinável que deverá estimar as posições dos pontos no espaço 3D. O treino será realizado de forma supervisionada. Serão exploradas arquiteturas densas e CNNs.

A avaliação será quantitativa com os dados sintéticos, comparando a solução obtida com o ground truth e a triangularização. A avaliação será no espaço métrico 3D, visto que desejamos estimar de fato a posição absoluta de cada junta, e utilizando como métrica a soma do erro quadrático médio (MSE) de cada keypoint. Entre aspectos não determinados, keypoints não disponíveis em nenhuma das 3 imagens poderão ser mascarado; e como métrica alternativa pensamos em explorar o erro absoluto médio (MAE), para diminuir problemas com outliers. Para comparação, utilizaremos uma triangularização não-linear.

Arquitetura proposta:

![Arquitetura](assets/Arquitetura.svg)

## Bases de Dados

Base de Dados | Endereço na Web | Resumo descritivo
-|-|-
OAK-D Synthetic Pose|[Zenodo OAK-D Synthetic Pose](https://zenodo.org/uploads/12212762?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjA1NDI1YjdkLTllNmUtNDFlMy04NWVmLTljMGE2ZDdmOGI0NyIsImRhdGEiOnt9LCJyYW5kb20iOiJiZTk1MWI5NTk4NTIzYjVkZDYwZGU3NGM5YTg0YTI5NiJ9.VhPRO2qFmZyNMXF9lh5pxEmGCO7KZzUy9x-5JwKdU2eN9skNTl3VM7C9eVNhimMWotTRtbYScAqRLdx4sgUwug)|Dataset de imagens sintéticas com avatares realizando diferentes poses. Sintetizado para simular a captura com uma OAK-D. Contém anotação de keypoints 2D e 3D.

Os dados serão sintetizados utilizando o motor de jogos Unity, que possui desenvolvido o pacote "Perception" para a geração de dados sintéticos [4]. Ela permitirá simular a configuração do dispositivo real e aplicando randomizações que julgarmos necessárias, tentando mitigar os efeitos da mudança do domínio virtual para real. Para a geração de "pessoas virtuais" utilizaremos o pacote "SyntheticHumans" [5].

São planejadas as randomizações: 
- Geração procedural de "pessoas virtuais"
- Pose da ‘pessoa virtual’
- Ruído aditivo na pose dos sensores
- Texturas de fundo
- Luz
- Parâmetros intrínsecos das câmeras
    - Foco
    - Tamanho do sensor

Cada entrada no conjunto de dados será composto de três imagens, uma para cada câmera, com apenas uma pessoa em cena e keypoints no espaço 2D e 3D anotados para cada câmera. Outros metadados para análise poderão ser obtidos. Poderemos gerar quantos dados forem necessários, mas iremos começar gerando um dataset de por volta de 6400 entradas. As imagens serão salvas em formato PNG, enquanto que outros dados serão em arquivo JSON. 

O dataset é divivido nos seguintes conjuntos:

Nome do conjunto | Nome explicativo | Tipo | Descrição
-|-|-|-
Scenario0|Fixed|Treino|Parâmetros da câmera fixos
Scenario1|WeakNormal|Treino|Parâmetros da câmera com randomização aditiva fraca e normalmente variada
Scenario2|StrongNormal|Treino|Parâmetros da câmera com randomização aditiva forte e normalmente variada
Scenario3|StrongUniform|Teste|Parâmetros da câmera com randomização aditiva fraca e uniformemente variada
Scenario4|Fixed-Test|Teste|Parâmetros da câmera fixos

Uma descrição mais detalhada do protocolo de geração pode ser obtido em [OAK-D Synthetic Pose Dataset Generation Protocol](https://github.com/EltonCN/IA904-2024S1/blob/7b13886703576c74ecca8f1b1dd751d36a8c1896/projetos/3DStereoBodyPoseEstimation/data/OAK-D%20Synthetic%20Pose%20Dataset%20Generation%20Protocol.pdf).

## Ambiente Computacional
> Descrever o ambiente/plataforma, bibliotecas e recursos computacionais utilizados, apresentando discussões, dicas e informações úteis para que outros possam utilizá-los.

## Workflow

- Geração de dados sintéticos
![Workflow de geração de dados](assets/Pipeline-Geração.svg)
- Treino do modelo
![Workflow de treinamento](assets/Pipeline-Treino.svg)
- Coleta de dados reais
![Workflow de coleta](assets/Pipeline-Coleta.svg)
- Avaliação
![Workflow de avaliação](assets/Pipeline-Avaliação.svg)

## Avaliação
> Definição das métricas de avaliação do projeto.
> Siga as três etapas sugeridas no artigo "Metrics Reloaded":
> 1. Problem fingerprinting - mapear o problema para uma categoria específica
> 2. Metric selection - identificar as métricas recomendadas para o problema/categoria, argumentar quais delas serão utilizadas e porque
> 4. Metric application - escolher e justificar as implementações que serão utilizadas, discutir como as métricas devem ser interpretadas
> 
> Apresente e discuta os resultados de cada etapa, deixando claras as decisões tomadas a partir desses resultados e o racional envolvido nessas decisões. Tente também relacionar as discussões e decisões com os "pitfalls" específicos apresentados no artigo (como suas escolhas evitam os "pitfalls"?).
> Você pode utilizar a plataforma [Metrics Reloaded](https://metrics-reloaded.dkfz.de/) para auxiliar neste processo. A plataforma gera um relatório que pode ser anexado a esta entrega, mas esse relatório **não** deve ser copiado e colado aqui, deve-se discutir as decisões tomadas a partir dele.
> Mais informações podem ser encontradas nos materiais de apoio no Classroom (Métricas para validação de análise de imagens).

## Experimentos e Resultados

Inicialmente, realizamos uma análise do dataset para avaliar possíveis vieses. Para isso, plotamos histogramas relevantes, que podem ser visualizados a seguir.

|  |  |
|----------|----------|
| ![Histograma de Altura](assets/dataset/histogram_height.png) | ![Histograma de Peso](assets/dataset/histogram_weight.png) |
| ![Histograma de Etnia](assets/dataset/histogram_ethnicity.png) | ![Histograma De Sexo](assets/dataset/histogram_sex.png) |
![Histograma de Idade](assets/dataset/histogram_age.png)

Observamos que o dataset apresenta um bom balanceamento em relação a características como altura, peso, etnia e sexo. Possuindo distribuições uniformes e abrangendo diferentes faixas de valores. No entanto, identificamos um desequilíbrio na distribuição por idade. A maioria dos dados está concentrada em faixas etárias adultas, o que pode afetar a generalização do modelo para outras faixas etárias.

> Descrição dos experimentos e resultados mais importantes.
> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, apresente o link para execução online, mas copie para esta parte a figura estática.

## Discussão
> Discussão dos resultados. Relacionar os resultados com as perguntas de pesquisa ou hipóteses avaliadas.
> A discussão dos resultados também pode ser feita opcionalmente na seção de Resultados, na medida em que os resultados são apresentados. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?

O maior problema a ser enfrentado será a transferência do modelo do domínio sintético para o real, o que poderá levar a necessidade iterativa de diversificação das imagens geradas.

## Conclusão
> Destacar as principais conclusões obtidas no desenvolvimento do projeto.
> Destacar os principais desafios enfrentados.
> Principais lições aprendidas.

## Trabalhos Futuros
Para futuras pesquisas e desenvolvimentos, há algumas áreas que podem ser exploradas. Primeiramente, a etapa de refinamento da pose estimada pode ser aprimorada. Isso envolve ajustar os keypoints estimados para melhor se alinharem com a anatomia real do corpo humano. Além disso, a triangularização não linear, que foi planejada mas não foi realizada devido ao prazo, pode ser implementada para melhorar a precisão da estimativa 3D.
Além das sugestões mencionadas anteriormente, existem outros pontos que podem ser explorados para aprimorar o estudo realizado. Primeiramente, testar diferentes arquiteturas de redes neurais pode ser interessante, visto que os resultados obtidos com a arquitetura utilizada não estão conforme o esperado. Além disso, considerar a coleta de dados além dos heatmaps, como informações de profundidade, pode enriquecer a estimativa 3D. Por fim, a realização da normalização dos dados, o que pode garantir uma maior consistência e precisão nas estimativas.

## Referências
[1] Zheng, Ce, et al. "Deep learning-based human pose estimation: A survey." ACM Computing Surveys 56.1 (2023): 1-37.

[2] Kumar, Pranjal, Siddhartha Chauhan, and Lalit Kumar Awasthi. "Human pose estimation using deep learning: review, methodologies, progress and future research directions." International Journal of Multimedia Information Retrieval 11.4 (2022): 489-521.

[3] “OAK-D — DepthAI Hardware Documentation 1.0.0 documentation.” Acesso em: 12 de maio de 2024. [Online]. Disponível em: https://docs.luxonis.com/projects/hardware/en/latest/pages/BW1098OAK/

[4] S. Borkman et al., “Unity Perception: Generate Synthetic Data for Computer Vision”. arXiv, 19 de julho de 2021. doi: 10.48550/arXiv.2107.04259.

[5] “Unity-Technologies/com.unity.cv.synthetichumans: A package for creating Unity Perception compatible synthetic people.” Acesso em: 12 de maio de 2024. [Online]. Disponível em: https://github.com/Unity-Technologies/com.unity.cv.synthetichumans