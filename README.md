# Informações:
O dataset utilizado foi o da vida animal disponibilizado no link: https://www.kaggle.com/virtualdvid/oregon-wildlife

# Como utilizar o código

Crie uma pasta dataset com pastas vazias, cada uma referente a uma classe diferente.

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

# Resultados
As classes utilizadas foram:
* bald_eagle
* black_bear
* cougar
* gray_wolf
* raven
* red_fox
* sea_lions
* seals

### Para cada uma das classes, os seguintes resultados:
Classes | Precision | Recall
--------|-----------|-------
Bald Eagle | 1.00 | 0.93
Black Bear | 0.87 | 0.97
Cougar | 0.92 | 0.91
Gray Wolf | 0.97 | 0.91
Raven | 0.95 | 0.92
Red Fox | 0.99 | 0.94
Sea Lions | 0.80 | 0.90
Seals | 0.86 | 0.85

# Sugestões de melhoria
* Habilitar também as camadas iniciais para serem re-treinadas. Isso pode fazer com que elas capturem características mais importantes para um problema específico.
* Aumentar a quantidade de épocas.
* Testar custom_layers diferentes.

# Sugestões de uso
<p>É bem fácil de utilizar o código para outros propósitos. Basta alterar na linha 11 a quantidade de neurônios de saída. Utilizamos oito porque essa é a quantidade de classes que foi utilizada nesse código. Basta alterar para o número de classes desejadas.</p>
<p>Depois basta alterar os caminhos dos diretórios e o target_names para as classes desejadas.</p>
