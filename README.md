# Projeto de Detecção de Acordes de Violão com YOLOv11

Este projeto implementa um sistema de detecção de acordes de violão utilizando o modelo YOLOv11m da biblioteca Ultralytics. O objetivo principal é treinar um modelo customizado capaz de identificar e mapear acordes específicos em imagens e vídeos de violão.

## Visão Geral do Projeto

O projeto consiste nas seguintes etapas:

1.  **Coleta e Anotação de Dados:** Criação de um dataset customizado de fotos de acordes de violão.
2.  **Preparação do Dataset:** Geração de arquivos de configuração (YAML) para treinamento e validação.
3.  **Treinamento do Modelo:** Treinamento de um modelo YOLOv11m customizado utilizando PyTorch e CUDA.
4.  **Predição e Testes:** Utilização do modelo treinado para fazer predições em novas imagens e vídeos.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Ultralytics:** Biblioteca para utilização do modelo YOLOv11.
* **PyTorch:** Framework de aprendizado de máquina para o treinamento do modelo.
* **CUDA:** Tecnologia da NVIDIA para aceleração do treinamento na GPU.
* **labelImg:** Ferramenta de anotação gráfica de imagens para criação dos labels do dataset.
* **Conda:** Gerenciador de pacotes e ambientes para configuração do ambiente de desenvolvimento.

## Especificações do Modelo YOLOv11m

| Modelo    | Tamanho (pixels) | mAPval 50-95 | Velocidade CPU ONNX (ms) | Velocidade T4 TensorRT10 (ms) | Parâmetros (M) | FLOPs (B) |
| :-------- | :--------------- | :----------- | :----------------------- | :---------------------------- | :------------- | :-------- |
| YOLOv11m | 640              | 51.5         | 183.2 ± 2.0              | 4.7 ± 0.1                     | 20.1           | 68.0      |

## Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:

MYDATAG2/
├── runs/                   # Diretório para logs de treinamento e resultados.

├── train/                  # Imagens e labels para treinamento.

├── val/                    # Imagens e labels para validação.

├── 16.jpeg                 # Exemplo de imagem no dataset.

├── classes.txt             # Arquivo com os nomes das classes (acordes).

├── data_custom.yaml        # Arquivo de configuração do dataset.

├── foto_resultado.jpg      # Exemplo de imagem com predição.

├── mymodel.pt              # Modelo treinado customizado.

├── prediction.py           # Script para realizar predições.

├── train.py                # Script para treinar o modelo.

├── video_resultado.avi     # Exemplo de vídeo com predição.

├── video4.mp4              # Exemplo de vídeo de entrada.

└── yolov11m.pt             # Modelo YOLOv11m pré-treinado (ou baixado).

## Processo de Implementação

### 1. Coleta e Anotação do Dataset Customizado

Foram coletadas mais de 50 fotos de acordes feitos no violão. Para cada foto, os acordes foram manualmente rotulados (label) utilizando a ferramenta `labelImg`.

**Instalação do labelImg:**

```bash
pip install labelImg
```

### 2. Preparação dos Arquivos de Configuração

Após a anotação, foram criados os arquivos `.yaml` necessários para o treinamento. O arquivo `data_custom.yaml` contém as informações sobre os caminhos para as imagens de treinamento (/train) e validação (/val), além da lista de classes (classes).

### 3. Treinamento do Modelo

O treinamento do modelo foi realizado utilizando o script `train.py` da biblioteca Ultralytics. O processo envolveu 100 epochs (iterações completas sobre o dataset de treinamento) e aproveitou a aceleração da GPU através do CUDA e PyTorch para um treinamento mais eficiente.

```bash
yolo task=detect mode=train model=yolov11m.pt data=data_custom.yaml epochs=100 name=yolov11m_custom_train device=0 
```

### 4. Predição e Testes

O modelo mymodel.pt foi então utilizado para realizar predições em novas imagens e vídeos, demonstrando sua capacidade de detectar os acordes treinados.

```bash
yolo task=detect mode=predict model=mymodel.pt source=16.jpeg show=True
```

ℹ️
**Para vídeo muda apenas a source.**


```bash
yolo task=detect mode=predict model=mymodel.pt source=video4.mp4 show=True
```

## Como Replicar o Projeto
Para utilizar o meu modelo, basta seguir os passos abaixo: 

- Crie uma pasta e faça as ações dentro dela.
- Configure o Ambiente: Instale Python, Conda, PyTorch (com suporte a CUDA) e Ultralytics.
- Configurar GPU: Através do prompt anaconda realize o comando abaixo:
- Crie uma pasta: Nela adicione o modelo mymodel.pt e a imagem e video disponibilizados no projeto, então rode o comando abaixo (estando com o prompt nessa pasta):

```bash
yolo task=detect mode=predict model=mymodel.pt source=video4.mp4 show=True
```


