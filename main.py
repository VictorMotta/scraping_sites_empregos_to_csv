from indeed import search_ideed
from stackoverflow import search_so
from save import save_to_csv



#busca
print("Bem vindo ao App de Procura de empregos de desenvolvedores!")
search = input("Digite a linguagem desejada: ").lower()


#salva resultado do indeed
result_indeed = search_ideed(search)
#salva resultado do indeed
result_so = search_so(search)


all_resuts = result_indeed + result_so

#envia para salvar no csv
save_to_csv(all_resuts)