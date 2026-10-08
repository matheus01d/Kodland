dict = {"IDK" : "I don't know / Eu não sei","CRINGE": "Algo vergonhoso ou constrangedor","STALKEAR": "Investigar a vida de alguém online",'W' : 'Win / vitoria','L' : 'Lose / Perdeu'}

word = input("Digite uma palavra moderna que você não entende : ").upper()

if word in dict.keys():
    print(dict[word])
else:
  print('Palavra nao achada')
