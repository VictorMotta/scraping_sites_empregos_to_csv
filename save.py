import csv

#funcao para salva no csv
def save_to_csv(jobs):
  #seleciona arquivo
  file = open('jobs.csv', 'w', encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(['title','company', 'location', 'how old', 'link'])
  
  #para cada job da lista recebida escreve 1 linha
  for job in jobs:
    writer.writerow(list(job.values()))
  
  file.close()


    
