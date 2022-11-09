from transformers import AutoTokenizer, AutoModelForSequenceClassification
#import torch
from archivo import readFile
from leer import lee
from casos import respuesta, traduce
from googletrans import Translator

def main():
  translator = Translator()
  model_name = "bert-base-cased-finetuned-mrpc"
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name)
  dicc = readFile("input.txt")
  ress = readFile("respuesta.txt")
  col = 0
  e=0
  
  texto = "prueba , 1"
  while(e==0):
    texto = input()
    if(texto !="exit"):
          col, palabra, src = respuesta(texto,col,dicc,translator,tokenizer,model)
          print(traduce(translator,ress[palabra],src))
          lee(palabra,src)
    else:
      e = 1  

main()