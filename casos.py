from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from googletrans import Translator
import random

mm = [[10001,	2002,	1003,	1005,	1005,	3009,	1007,	1008,	1030,	1010,	1005,	1005,	1031,	1026,	4029,	1026,	5023,	1026,	1027,	1026,	1031,	1021,	5, 1023, 1021, 1005], 
      [10001,	2002,	3,	5,	5,	3009,	7,	8,	30,	10,	5,	5,	31,	26,	4029,	22,	5023,	26,	27,	26,	31,	21,	5, 1023, 1021, 1005],
      [10001,	15,	1003,	6004,	7006,	3009,	1007,	1008,	1030,	1010,	1005,	1005,	1031,	1026,	4029,	1026,	5023,	1026,	1027,	1026,	1031,	1021,	5, 1023, 1021, 1005],
      [10001,	2002,	1003,	1005,	1005,	3009,	1007,	1008,	3009,	1010,	1018,	1003,	1031,	26,	4029,	1026,	5023, 1026,	1027,	1026,	1031,	1021,	5, 1023, 1021, 1005],
      [32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	32,	1033,	32,	32, 32, 32, 32],
      [10001,	2002,	3,	5,	5,	3009,	7,	8,	30,	10,	5,	5,	31,	26,	4029,	26,	5034,	26,	27,	26,	31,	21,	5, 1023, 21, 1005],
      [10001,	8002,	3,	5,	5,	3009,	7,	8,	30,	10,	5,	5,	31,	26,	4029,	26,	5023,	26,	27,	26,	31,	21,	5, 1023, 21, 1005],
      [10001,	9002,	3,	5,	5,	3009,	7,	8,	30,	10,	5,	5,	31,	26,	4029,	26,	5023,	26,	27,	26,	31,	21,	5, 1023, 21, 1005],
      [10001,	8002,	3,	6031,	7016,	3009,	7,	8,	30,	10,	5,	5,	31,	26,	4029,	26,	5023,	26,	27,	26,	31,	21,	5, 1023, 21,5],
      [10001,	9002,	3,	6017,	7019,	3009,	7,	8,	30,	10,	5,	5,	31,	26,	4029,	26,	5023,	26,	27,	26,	31,	21,	5, 1023, 21, 5],
      [10001, 2002,	3,	5,	5,	3009,	7,	8,	30,	10,	5,	5,	31,	26,	4029,	22,	5023,	26,	27,	26,	31,	21,	3009, 1023, 21, 5]]

jokes = [9,11,12,13,14,19,24,25,26]

def caso(texto, dicc,tokenizer,model):
  clave = "Probablementenuncaseinserteesto"
  i = 0
  salir = 0
  cantidad = len(dicc)
  while(i < cantidad and salir != 1):
    clave = dicc[i]
    tokens = tokenizer.encode_plus(texto, clave, return_tensors="pt")
    classification_logits = model(**tokens)[0]
    results = torch.softmax(classification_logits, dim=1).tolist()[0]

    if (round(results[1] * 100)<75):
      i += 1
    else:
      salir = 1

  return i

def matrizcasos(col, ren):
  valor = mm[col][ren]
  if (valor >= 1000):
    col = int((valor-valor % 1000)/1000)
    valor = int(valor - col*1000)
  if(valor == 9):
    valor = random.choice (jokes)

  return valor, col

def respuesta(texto,col,dicc,translator,tokenizer,model):
  textos = translator.translate(texto)
  #print(textos.text)
  ren = caso(textos.text,dicc,tokenizer,model)
  if (ren < len(dicc)):
    valor, col = matrizcasos(col,ren)
  else:
    valor = 20
  return col, valor-1, textos.src

def traduce(translator, palabra, src):
  if (src != "en"):
    ingles = translator.translate(palabra,src = "en", dest=src)
    palabra = ingles.text
  return palabra