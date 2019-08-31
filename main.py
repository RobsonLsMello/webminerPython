import requests 
from bs4 import BeautifulSoup

response = requests.get('http://pt.stackoverflow.com')

def mostrarPagina(r, pagina, tipo = 0):
  if tipo == 0:
    print(r.text)
  elif tipo == 1:
    #print(response.content)
    soup = BeautifulSoup(r.content,'html.parser')
    #print(soup.prettify())
    #print(soup.title.string,'\n')
    array = soup.find_all('div',class_ = "question-summary")
    return captarInformacoes(array, pagina)

def captarInformacoes(array, pagina):
  perguntas = []
  for pergunta in array:
    questao_a = pergunta.find("a", class_ = "question-hyperlink")
    questao = {
      'titulo' : questao_a.string,
      'url' : questao_a['href'],
      'pagina' : pagina
    }
    perguntas.append(questao)
  
  return perguntas


def verificarPagina(r, pagina = 1):
  informacoes = []
  if r.status_code == 200:
    print('conectado')
    informacoes = mostrarPagina(r, pagina, 1)
  else:
    print('Erro - Código: {0}'.format(r.status_code))
  return informacoes


def fazerPesquisa(tag = ''):
  pagina_limite = 6
  resultado = []
  for pagina in range(1, pagina_limite):
    r2 = requests.get('http://pt.stackoverflow.com/questions', params = {'page':str(pagina), 'tab': 'newest'})
    resultado.append(verificarPagina(r2, pagina))
  print(resultado)
