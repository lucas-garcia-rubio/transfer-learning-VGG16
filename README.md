O dataset precisa estar separado da seguinte maneira:

data/
data/train/
data/train/classe1
data/train/classe2
...
data/test/
data/test/classe1
data/test/classe2
...
data/validation/
data/validation/classe1
data/validation/classe2
...


separar_arquivos.py deve estar em uma pasta contendo:
data/
original_dataset/

Sendo que original_dataset deve estar dividido assim:
original_dataset/classe1
original_dataset/classe2
...


separar_arquivos.py além de dividir o dataset, faz também um recorte ao centro, retirando 20% das bordas de todos os lados.
