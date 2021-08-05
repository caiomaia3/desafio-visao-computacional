# Desafio de Visão Computacional
repo-name: **desafio-visao-computacional**

## Objetivo

Este repositório tem o objetivo de armazenar a solução do desafio de visão computacional proposto no Centro de Competência em Robótica do SENAI CIMATEC.

## Desafio

O desafio consiste em realizar transformações em determinada imagem, de modo que as cartas presentes nesta imagem sejam apresentadas na forma retangular e sem oclusão.

![Imagem de Cartas](img/cards.jpg)


## Material de Apoio

- [Link do Minicurso do RoSA](https://github.com/Brazilian-Institute-of-Robotics/bir-mini-robotic-vision/tree/presentation)
- [Google Coolab do Mini-curso](https://colab.research.google.com/drive/1ozEWpFhsqHC6vI3QS-IxH6HThysonxKq)


## Preparação

Antes de trabalhar na solução é importante preparar um ambiente virtual, pois isto permite que a instalação de bibliotecas necessárias para aplicação não sejam instaladas no âmbito global do sistema.
O pacote escolhido para esta função é o [Venv](https://docs.python.org/3/library/venv.html) e sua instalação segue os seguintes passos:

### Instalação do Pip

Utilizarei o **Ubuntu 20.04** para este trabalho, que possui o Python 3 já pré-instalado. Deste modo só precisarei instalar o **pip**, que é um instalador de pacotes para o Python. A instalação ocorre ao executar os seguintes comandos no terminal:

```console
sudo apt update
sudo apt -y upgrade
sudo apt-get install python3-pip
```
### Instalação do Virtualenv e Criação do Ambiente

Utilizando o **pip** podemos instalar o venv como seguinte comando no terminal:

```console
pip3 install virtualenv
apt install python3.8-venv
```
No Unbuntu 20.04 o pacote do venv esta associado ao Python3.8, mas a versão pode ser diferente em outras distribuições.

Dentro da pasta que deseja criar o ambiente virtual execute o seguinte comando de terminal:
```console
python3 -m venv .venv
```
Dara ativar o ambiente basta utilizar o  seguinte comando:
```console
source .venv/bin/activate
```
Se tudo ocorreu bem, deverá aparecer o nome do ambiente, (.venv) antes do nome do usuário.

![prompt-venv](img/readme/prompt.png)

Para finalizar o processo instalarei uma extensão do VS Code que ativa automaticamente o ambiente no ambiente de desenvolvimento. Esta extensão é [Python Auto Venv](https://marketplace.visualstudio.com/items?itemName=whinarn.python-auto-venv) após instalar e reiniciar o VS Code o ambiente virtual será ativado automaticamente. Na interface do VS Code aparecerá versão do python e o nome do ambiente no canto inferior esquerdo.

![vscode-inter](img/readme/vscode-interface.png)


## Instalação de Pacotes no Ambiente

Antes de utilizar funções básicas do OpenCV será necessário instalar alguns pacotes no ambiente virtual. Estes são: [numpy](https://numpy.org/), uma biblioteca numérica, [scikit-image](https://scikit-image.org/), para utilizar imagens da internet, e [opencv](https://opencv.org/). Nesta instalação será utilizada novamente o pip, mas agora no **ambiente virtual**. Portanto execute:

```console
python -m pip install -U pip
python -m pip install -U numpy
python -m pip install -U opencv-contrib-python
python -m pip install -U scikit-image
```

O flag -m aponta que sera utilizado um módulo de python. Já o flag -U faz com que o pacote seja atualizado, caso já tenha sido instalado.

Para testar a configuração do ambiente rode o seguinte script:
```console
python src/open-cv-first-touch.py
```
e a seguinte imagem deverá aparecer na tela. É possível que o script demore um pouco.

![lenna](img/readme/lenna.png)


## Correção de Perspectiva


A principal funcionalidade para  desafio é a correção de perspectiva, portanto, o primeiro passo do nosso processo de solução será esta correção.
Para realizar esta tarefa utilizaremos o script ``perspective_transform.py``, que possui o seguinte código:

```python
#  Autor: Caio Maia - caiomaia3@gmail.com
#  Este script tem o objetivo de experimentar as funções básicas do open-cv
import cv2
import numpy as np
from skimage import io
import card_transformation as ct

imported_image = io.imread("./img/cards.jpg")
imported_image = cv2.cvtColor(imported_image,cv2.COLOR_BGR2RGB)

source_points = np.float32([[111,217],
        [289,184],
	[154,483],
	[355,439]])

cv2.imshow('myImage2',ct.perspective(imported_image,source_points))
cv2.waitKey(0) 
cv2.destroyAllWindows()
```

Na primeira secção do código são realizadas importações das bibliotecas: OpenCV, Numpy, scikit-image. A OpenCV é a biblioteca que mais iremos utilizar, para realizar transformações nas imagens de interesse. A Numpy é um biblioteca numérica para o Python e em nosso contexto oferece uma base para o trabalho no OpenCV, pois oferece a estrutura de dado que permite a representação das imagens em forma de array. Já a scikit-image é utilizada para realizar importação de imagens ``.jpg`` no formato de array do Numpy.

O pacote ``card_transformation.py`` é de autoria própria e abarca as funções que utilizaremos.

A variável source_points` contém um array com os pontos, pares ordenados com a localização do pixel, que definem a região em que será realizada a transformação.

```python
source_points = np.float32([[111,217],
        [289,184],
	[154,483],
	[355,439]])
```
Se marcarmos este pontos na imagem original teremos a seguinte imagem:

![ROI-da-carta](/img/ROI.png)
 Vale ressaltar a importância da sequência dos pontos no array, que possuem a seguinte disposição na imagem.

```python
# 1 ---- 2
# |      |
# |      |
# |      |
# 3 ---- 4
```
Entretanto, a alteração da imagem ocorre no método ``ct.perspective(imported_image,source_points)``, que possui o seguinte código:

```python
def perspective(input_image,source_points):
	## Define card size and position
	card_height = 350
	card_width  = 250

	start_point = [0,0]
	end_point   =[card_width,card_height]

	destination_points = np.float32([start_point,
				[card_width,0],
				[0,card_height],
				end_point])

	transformation_matrix = cv2.getPerspectiveTransform(source_points,destination_points)
	output_image = cv2.warpPerspective(input_image,transformation_matrix,(card_width,card_height))
	return output_image
```

No início deste método são definidos a proporcionalidade da imagem no final da correção e os pontos que definirão esta nova imagem. Em seguida é calculada a matriz de transformação entre as duas regiões e que mapeia os pixels presentes na imagem fonte e os reposiciona na nova imagem. Lembrando que estas regiões são definidas pelos arrays de pontos de localização dos pixels.

Finalmente é aplicada a matriz de transformação na ``input_imagem``, por meio do método ``.warpPerspective()`` e retorna ``output_image``, a imagem transformada.

Ao executar o script ``perspective_transform.py`` a seguinte imagem do Rei de Espadas é mostrada na tela, sendo tirada e corrigida a partir da foto original ``./img/cards.jpg``:

![k-espadas](img/k-espadas.png)



## Correção da Oclusão


