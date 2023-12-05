# BIBLIOTECAS/IMPORTS
from datetime import time, datetime
import random
import numpy as np
import pandas as pd

# LISTAS/DICIONÁRIOS
alunos = []
treino = []
questionario = []
perfil_nutricional = []
avaliacao_periodica = []
produtos = []
lista_desejos = []
historico_compras = []
estoque = []

# MENU
def menu():
  print()
  print(' ..:: BEM VINDO(A) A ACADEMIA VITALFIT ::.. ')
  print()
  print('''Escolha uma opção:
  [ 1 ] - Cadastro e Acompanhamento Individual
  [ 2 ] - Moda Fitness VitalFit
  [ 3 ] - Central de Treinamento Individual
  [ 4 ] - Avaliação Nutricional
  [ 5 ] - ENCERRAR PROGRAMA''')

# MÓDULO 1 - VALMIR
def menu_mod1():
  print('''Escolha uma opção:
  1 - Cadastrar de Alunos
  2 - Realizar Avaliação
  3 - Exibir Alunos
  4 - Exibir Avaliações de um Aluno
  5 - Enviar Mensagem
  6 - Exibir Mensagens de um Aluno
  7 - Gerar Relatório de Progresso
  8 - Personalizar Treino Automatizado
  9 - Exibir Histórico de Acompanhamento
  10 - Sair''')

class Academia:
  def __init__(self):
    self.alunos = {}

  def cadastrar_aluno(self):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    peso = float(input("Digite o peso do aluno (kg): "))
    altura = float(input("Digite a altura do aluno (m): "))
    condicao_medica = input("Informe alguma condição médica relevante (ou deixe em branco): ")

    metas = {}
    metas['perda_peso'] = float(input("Meta de perda de peso (kg): "))
    metas['ganho_massa'] = float(input("Meta de ganho de massa muscular (kg): "))
    metas['melhoria_resistencia'] = float(input("Meta de melhoria da resistência: "))

    aluno = {
      'nome': nome,
      'idade': idade,
      'peso': peso,
      'altura': altura,
      'condicao_medica': condicao_medica,
      'metas': metas,
      'avaliacoes': [],
      'mensagens': [],
      'treino': []
    }

    self.alunos[nome] = aluno
    print(f"Aluno {nome} cadastrado com sucesso!\n")

  def realizar_avaliacao(self, aluno_nome):
    if aluno_nome in self.alunos:
      data_avaliacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

      avaliacao = {
          'data': data_avaliacao,
          'teste_fisico': input("Resultado do teste físico: "),
          'medicao_peso': float(input("Medição de peso (kg): ")),
          'desempenho_exercicio': input("Análise de desempenho em exercícios específicos: ")
      }

      self.alunos[aluno_nome]['avaliacoes'].append(avaliacao)
      print(f"Avaliação para {aluno_nome} realizada com sucesso!\n")
    else:
      print(f"Aluno {aluno_nome} não encontrado.\n")

  def exibir_alunos(self):
    print("\nLista de Alunos:")
    for nome, aluno in self.alunos.items():
      print(f"\nNome: {aluno['nome']}")
      print(f"Idade: {aluno['idade']}")
      print(f"Peso: {aluno['peso']} kg")
      print(f"Altura: {aluno['altura']} m")
      print(f"Condição Médica: {aluno['condicao_medica']}")
      print("Metas:")
      for meta, valor in aluno['metas'].items():
        print(f"  {meta.capitalize()}: {valor}")
      print("\n")

  def exibir_avaliacoes(self, aluno_nome):
    if aluno_nome in self.alunos:
      print(f"\nAvaliações de {aluno_nome}:")
      for avaliacao in self.alunos[aluno_nome]['avaliacoes']:
        print(f"\nData: {avaliacao['data']}")
        print(f"Teste Físico: {avaliacao['teste_fisico']}")
        print(f"Medição de Peso: {avaliacao['medicao_peso']} kg")
        print(f"Desempenho em Exercícios: {avaliacao['desempenho_exercicio']}")
        print("\n")
    else:
        print(f"Aluno {aluno_nome} não encontrado.\n")

  def enviar_mensagem(self, remetente, destinatario, mensagem):
    if destinatario in self.alunos:
      data_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      mensagem = {
          'remetente': remetente,
          'data_envio': data_envio,
          'mensagem': mensagem
      }
      self.alunos[destinatario]['mensagens'].append(mensagem)
      print(f"Mensagem enviada para {destinatario}.\n")
    else:
        print(f"Destinatário {destinatario} não encontrado.\n")

  def exibir_mensagens(self, aluno_nome):
    if aluno_nome in self.alunos:
      print(f"\nMensagens para {aluno_nome}:")
      for mensagem in self.alunos[aluno_nome]['mensagens']:
          print(f"\nRemetente: {mensagem['remetente']}")
          print(f"Data de Envio: {mensagem['data_envio']}")
          print(f"Mensagem: {mensagem['mensagem']}")
          print("\n")
    else:
        print(f"Aluno {aluno_nome} não encontrado.\n")

  def gerar_relatorio_progresso(self, aluno_nome):
    if aluno_nome in self.alunos:
      aluno = self.alunos[aluno_nome]
      ultima_avaliacao = aluno['avaliacoes'][-1] if aluno['avaliacoes'] else None
      metas = aluno['metas']

      relatorio = f"Relatório de Progresso para {aluno_nome}:\n"

      if ultima_avaliacao:
          relatorio += f"\nÚltima Avaliação (Data: {ultima_avaliacao['data']}):\n"
          relatorio += f"  - Teste Físico: {ultima_avaliacao['teste_fisico']}\n"
          relatorio += f"  - Medição de Peso: {ultima_avaliacao['medicao_peso']} kg\n"
          relatorio += f"  - Desempenho em Exercícios: {ultima_avaliacao['desempenho_exercicio']}\n"
      else:
          relatorio += "\nNenhuma avaliação realizada ainda.\n"

      relatorio += "\nMetas:\n"
      for meta, valor in metas.items():
          relatorio += f"  - {meta.capitalize()}: {valor}\n"

      print(relatorio)
    else:
        print(f"Aluno {aluno_nome} não encontrado.\n")

  def personalizar_treino_automatizado(self, aluno_nome):
    if aluno_nome in self.alunos:
      aluno = self.alunos[aluno_nome]
      ultima_avaliacao = aluno['avaliacoes'][-1] if aluno['avaliacoes'] else None
      metas = aluno['metas']

      if ultima_avaliacao:
        novo_treino = f"Treino Personalizado para {aluno_nome} (Sugestão Automática):\n"
        novo_treino += "Ajustes sugeridos com base na última avaliação e metas:\n"

        if ultima_avaliacao['desempenho_exercicio'] == 'Melhorou':
          novo_treino += "Aumentar a intensidade dos exercícios.\n"

        aluno['treino'].append(novo_treino)
        print("Treino personalizado sugerido automaticamente e armazenado.\n")
      else:
          print("Não é possível personalizar o treino automaticamente. Nenhuma avaliação disponível.\n")
    else:
        print(f"Aluno {aluno_nome} não encontrado.\n")

  def exibir_historico_acompanhamento(self, aluno_nome):
    if aluno_nome in self.alunos:
      aluno = self.alunos[aluno_nome]

      print(f"Histórico de Acompanhamento para {aluno_nome}:\n")
      for avaliacao in aluno['avaliacoes']:
        print(f"Data: {avaliacao['data']}")
        print(f"Teste Físico: {avaliacao['teste_fisico']}")
        print(f"Medição de Peso: {avaliacao['medicao_peso']} kg")
        print(f"Desempenho em Exercícios: {avaliacao['desempenho_exercicio']}")
        print("\n")

      for treino in aluno['treino']:
        print(treino)

      print("\n")
    else:
        print(f"Aluno {aluno_nome} não encontrado.\n")


if __name__ == "__main__":
  academia = Academia()
  academia.menu_mod1()

# MÓDULO 2 - SAMYRA
def menu_mod2():
  print('''Escolha uma opção:
  1 - Cadastrar Produto
  2 - Perfil de Compra do Aluno
  3 - Promoções Personalizadas
  4 - Lista de Desejos
  5 - Avisos de Novos Produtos
  6 - Sistema de Pagamento
  7 - Acompanhamento de Entregas
  8 - Programa de Fidelidade
  9 - Avaliação de Produtos
  10 - Gestão de Estoque
  11 - SAIR/VOLTAR''')

def cadastro_produto(): # roupas e acessórios
  tamanhos_dispiniveis = ['PP', 'P', 'M', 'G', 'GG', 'XG', 'XGG', 'UNICO']
  produto = input('Produto: ')
  id_produto = int(input('ID: '))
  tamanho = input('Tamanho: ').upper()
  while tamanho != tamanhos_dispiniveis:
    tamanho = input('TAMANHO INVÁLIDO! Digite novamente: ').upper()
    if tamanho == tamanhos_dispiniveis:
      continue
  descricao = input('Descrição: ')
  preco = float(input('Preço: '))
  quantidade = int(input('Quantidade: '))
  imagem = input('Digite o caminho da imagem: ')
  # ARQUVO
  with open('produtos.txt', 'a') as arquivo:
    arquivo.write(f'{produto}, {id_produto}, {tamanho}, {descricao}, {preco}, {quantidade}, {imagem}')
    print(arquivo)
  try:
    with open('produtos.txt', 'r') as arquivo:
      arquivo.read()
      print(arquivo)
  except FileNotFoundError as erro:
    print(f'ERRO: {erro}! Arquivo não encontrado.')
  # GRAVANDO NA LISTA/DICIONÁRIO - GRAVANDO NO PRODUTO?
  produtos.append({'Produto': produto, 'ID': id_produto, 'Tamanho': tamanho, 'Descrição': descricao, 'Preço': preco, 'Quantidade': quantidade, 'Imagem': imagem})
  print(produtos)
  # GRAVANDO NO ESTOQUE
  estoque.append({'Produto': produto, 'ID': id_produto, 'Tamanho': tamanho, 'Quantidade': quantidade, 'Imagem': imagem})

def perfil_compra():
  print(' ..:: Bem vindo(a) ao seu portal de preferências! ::..')
  for historico in historico_compras:
    print(historico)
  cliente = input('Cliente: ')
  pref_estilo = input('Sua preferência de estilo? ')
  pref_tamanho = input('Sua preferência de tamanho: ').upper().split()
  pref_cor = input('Sua preferência de cor: ')
  historico_compras.append({'Cliente': cliente, 'Preferência de estilo': pref_estilo, 'Preferência de tamanho': pref_tamanho, 'Preferência de cor': pref_cor})


def promocoes():
  # se um produto aparecer mais de uma vez no historico de compra ou na preferencia, realizar uma promoção
  promocoes = []
  print(' ..:: CANAL EXCLUSIVO DE PROMOÇÕES ::.. ')
  for prod in historico_compras:
    if historico_compras.count(prod) > 1:
      print(f'Promoção para o produto {prod}! Aproveite!')
      promocoes.append(prod)
  promocao = input('Deseja comprar o produto da promoção? ')
  while promocao == 'Ss' or promocao == 'SIM' or promocao == 'Sim' or promocao == 'sim':
    print(f'Produto adicionado ao carrinho! Siga os próximos passos para realizar a compra.')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade: '))
    if produto and id_produto in promocoes:
      print(f'COMPRA REALIZADA COM SUCESSO!')
    historico_compras.append({'Produto': produto, 'ID': id_produto, 'Preço': preco, 'Quantidade': quantidade})
    if promocao == 'Nn' or promocao == 'NAO' or promocao == 'Nao' or promocao == 'nao':
      print('O produto foi adicionado a sua lista de desejos.')
      lista_desejos.append(produto)
      break


def lista_desejo():
  print(' ..:: Bem vindo(a) a sua lista de desejos! ::.. ')
  print()
  desejo = input('Deseja adicionar algum produto na sua lista de desejos? ')
  if desejo == 'Ss' or desejo == 'SIM' or desejo == 'Sim' or desejo == 'sim':
    id_produto = int(input('Digite o ID do produto: '))
    if id_produto in produtos:
      print(produtos[id_produto])
      lista_desejos.append({'ID': id_produto})
      print('PRODUTO ADICONADO À LISTA DE DESEJOS!')
  for p in historico_compras: 
    id_produto = p
    if historico_compras.count(p) > 1:
      print('Verifique o CANAL EXCLUSIVO DE PROMOÇÕES! Seu produto pode está em promoção!')


def novos_produtos():
  for novo_p in historico_compras:
    pref_estilo = novo_p
    print(novo_p)
    print('Existem produtos semelhantes a sua preferencia de estilo! Vem conferir!')
  # perguntar se quer receber avisos por email ou pelo aplicativo
  print('''Por onde deseja receber avisos de novos produtos/coleções?
  1. Email
  2. Aplicativo''')
  op = int(input('Opção: '))
  if op == 1:
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    end_email = input('Digite o endereço de email: ')
    dias = input('Quais os dias que deseja receber avisos sobre os produtos? ')
    if dias in dias_semana:
      print('Dias registrado com sucesso!')
    print(f'Você receberá os avisos por email no endereço {end_email} nos dias {dias}!')
    # pedir endereço de email e perguntar os dias que deseja receber avisos
  elif op == 2:
    notificacao = input('Deseja ativar as notificações para receber avisos sobre os produtos? ')
    while notificacao == 'Ss' or notificacao == 'SIM' or notificacao == 'Sim' or notificacao == 'sim':
      print('Notificações ativadas com sucesso!')
      if notificacao == 'Nn':
        break
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')

def sistema_pagamento():
  status_pagamento = ['Pendente', 'Aguardando pagamento', 'Concluido']
  print('''Qual forma de pagamento deseja utilizar?
  1. Dinheiro/Boleto
  2. Cartão''')
  opc = int(input('Opção: '))
  if opc == 1:
    print('Método escolhido: Boleto')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Preço do produto: '))
    status_pagamento == 'Aguardando pagamento'
    print('Seu boleto foi gerado! Estaremos aguadando seu pagamento.')
    ponto_fidelidade = 15
    historico_compras.append({'Produto': produto, 'ID': id_produto, 'Ponto de Fidelidade': ponto_fidelidade})
  elif opc == 2:
    print('Método escolhido: Cartão')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Preço do produto: '))
    titular_cartao = input('Titular do cartão: ')
    numero_cartao = int(input('Número do cartão: '))
    banco = input('Seu banco: ')
    print('CARTÃO REGISTRADO! Estamos processando seu pagamento. Só um momento')
    time.sleep(1.5)
    status_pagamento == 'Concluido'
    print('Sua compra foi aprovada! Pagamento processado com sucesso!')
    ponto_fidelidade = 30
    historico_compras.append({'Produto': produto, 'ID': id_produto, 'Ponto de Fidelidade': ponto_fidelidade})
  else:
    print('MÉTODO DE PAGAMENTO INVÁLIDO! Tente novamente mais tarde.')

def acompanhamento_entregas():
  possiveis_status = ["Em processamento", "Em trânsito", "Entregue"]
  codigo_rastreio = int(input('Digite o código de rastreio da sua entrega: '))
  print('Só um momento...')
  novo_status = random.choice(possiveis_status)
  status_atual = novo_status
  # informações em tempo real do status da entrega, podendo acompanhar o progresso da entrega
  while status_atual != "Entregue":
    time.sleep(2) 
    print(f'O status atual da sua entrega é {status_atual}')
    if status_atual == 'Entregue':
      print('Produto entregue com sucesso!')
      break

def programa_fidelidade():
  pontos = []
  print('''Escolha uma opção:
  1 - Realizar compra
  2 - Consultar pontos
  3 - Trocar pontos''')
  opc_pontos = int(input('Opção: '))
  if opc_pontos == 1:
    cliente = input('Cliente: ')
    produto = input('Produto: ')
    id_produto = int(input('ID: '))
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade: '))
    pontos_ganhos = int(preco / 10) # Exemplo: 1 ponto para cada R$10 gastos
    pontos.append({'Cliente': cliente, 'Produto': produto, 'ID': id_produto, 'Preço': preco, 'Quantidade': quantidade, 'Pontos ganhos': pontos_ganhos})
    if cliente in pontos:
        pontos[cliente] += pontos_ganhos
    else:
        pontos[cliente] = pontos_ganhos
    print(f'Compra realizada por {cliente}. Pontos acumulados: {pontos_ganhos}.')
    print()
  elif opc_pontos == 2:
    if cliente in pontos:
      return pontos[cliente]
    else:
      return 0
  elif opc_pontos == 3:
    if cliente in pontos and pontos[cliente] >= pontos_ganhos:
      pontos[cliente] -= pontos_ganhos
      print(f'{cliente} trocou {pontos_ganhos} pontos por um desconto ou brinde exclusivo.')
    else:
      print(f'{cliente} não possui pontos suficientes para realizar a troca.')
      print()
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')

def avalia_produto():
  avaliacao = input('Qual produto deseja avaliar? ')
  nota = int(input('Atribua uma nota para esse produto: '))
  comentario = input('Dê sua opnião sobre o produto: ')
  melhoria = input('O que você acha que pode ser melhorado? ')
  print(f'Produto avaliado: {avaliacao}, Nota: {nota}, Comentário: {comentario}, Melhoria: {melhoria}')
  print('Agradecemos o seu feedback! Sua opinião é de suma importância para a melhora da nossa rede.')

def gestao_estoque():
  quantidade_inicial = 1
  print('''Escolha uma opção:
  1 - Adicionar produto
  2 - Atualizar o estoque
  3 - Realizar venda
  4 - Monitorar o estoque''')
  opc_estoque = int(input('Opção: '))
  if opc_estoque == 1:
    produto = input('Produto: ')
    quantidade = int(input('Quantidade: '))
    estoque.append({'Produto': produto, 'Quantidade': quantidade})
    if produto not in estoque:
      estoque[produto] = quantidade_inicial
      print(f'Produto {produto} adicionado ao estoque com quantidade inicial de {quantidade_inicial}.')
    else:
      print(f"Produto '{produto}' já existe no estoque.")
    print()
  elif opc_estoque == 2:
    produto = input('Produto: ')
    quantidade = int(input('Quantidade: '))
    if produto in estoque:
      estoque[produto] += quantidade
      print(f'Estoque de {produto} atualizado para {estoque[produto]} unidades.')
    else:
      print(f'Produto {produto} não encontrado no estoque.')
      print()
  elif opc_estoque == 3:
    produto = input('Produto: ')
    quantidade = int(input('Quantidade: '))
    if produto in estoque and estoque[produto] >= quantidade:
      estoque[produto] -= quantidade
      print(f'Venda de {quantidade} unidades de {produto} realizada com sucesso. Estoque atual: {estoque[produto]} unidades.')
    else:
      print(f'Venda de {quantidade} unidades de {produto} não pode ser realizada. Estoque insuficiente.')
    print()
  elif opc_estoque == 4:
    for e in estoque:
      print(' ..:: MONITORAMENTO DO ESTOQUE ::..')
      produto, quantidade = e.items()
      print(f'Produto: {produto} - Quantidade: {quantidade}')
      print(e)
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')


# MÓDULO 3
def menu_mod3():
  print('''Escolha uma opção:
  1 - Montar Treino Personalizado
  2 - Acesso a Biblioteca de Vídeos de Exercícios
  3 - Rotinas de Treino Personalizadas
  4 - Acompanhamento de desempenho
  5 - Alerta de Treino
  6 - Comunicação com o Professor
  7 - Premiassões e Reconhecimentos
  8 - SAIR/VOLTAR''')


# MÓDULO 4 - VITÓRIA
class Aluno:
  def __init__(self, nome):
    self.nome = nome
    self.perfil_nutricional = {
        'habitos_alimentares': '',
        'restricoes_alimentares': '',
        'objetivos_peso': '',
        'preferencias_alimentares': ''
    }
    self.questionario_preenchido = False

  def preencher_questionario(self):
    print(f"\nQuestionário Inicial para {self.nome}:")
    self.perfil_nutricional['habitos_alimentares'] = input("Hábitos alimentares: ")
    self.perfil_nutricional['restricoes_alimentares'] = input("Restrições alimentares: ")
    self.perfil_nutricional['objetivos_peso'] = input("Objetivos de peso: ")
    self.perfil_nutricional['preferencias_alimentares'] = input("Preferências alimentares: ")
    self.questionario_preenchido = True

  def atualizar_perfil(self, habitos, restricoes, objetivos, preferencias):
    self.perfil_nutricional['habitos_alimentares'] = habitos
    self.perfil_nutricional['restricoes_alimentares'] = restricoes
    self.perfil_nutricional['objetivos_peso'] = objetivos
    self.perfil_nutricional['preferencias_alimentares'] = preferencias

  def exibir_perfil(self):
    print(f"\nPerfil Nutricional de {self.nome}:")
    for chave, valor in self.perfil_nutricional.items():
      print(f"{chave.capitalize()}: {valor}")

  def registrar_dieta_diaria(self):
    if not self.questionario_preenchido:
      print("Preencha o questionário inicial antes de registrar a dieta.")
      return

    print(f"\nRegistrando a Dieta Diária para {self.nome}:")
    entrada_alimentar = input("Descreva sua ingestão alimentar diária: ")
    print(f"Dieta registrada para {self.nome}: {entrada_alimentar}")

  def receber_orientacoes_nutricionais(self):
    if not self.questionario_preenchido:
      print("Preencha o questionário inicial antes de receber orientações.")
      return

    print(f"\nOrientações Nutricionais Personalizadas para {self.nome}:")
    # Lógica para gerar orientações com base nas informações do aluno
    if 'Perder peso' in self.perfil_nutricional['objetivos_peso']:
      print("Sugestão: Ajuste a dieta para reduzir a ingestão calórica e inclua exercícios regulares.")
    else:
        print("Sugestão: Mantenha uma dieta equilibrada e ajuste as porções conforme necessário.")

class PerfilNutricional:
  def __init__(self):
    self.habitos_alimentares = ''
    self.restricoes_alimentares = ''
    self.objetivos_peso = ''
    self.preferencias_alimentares = ''

  def preencher_perfil(self, habitos, restricoes, objetivos, preferencias):
    self.habitos_alimentares = habitos
    self.restricoes_alimentares = restricoes
    self.objetivos_peso = objetivos
    self.preferencias_alimentares = preferencias

  def exibir_perfil(self):
    print("\nPerfil Nutricional:")
    print(f"Hábitos Alimentares: {self.habitos_alimentares}")
    print(f"Restrições Alimentares: {self.restricoes_alimentares}")
    print(f"Objetivos de Peso: {self.objetivos_peso}")
    print(f"Preferências Alimentares: {self.preferencias_alimentares}")

class RegistroDiario:
  def __init__(self):
    self.registros = []

  def adicionar_registro(self, entrada):
    self.registros.append(entrada)

  def exibir_registros(self):
    print("\nRegistros Diários:")
    for i, entrada in enumerate(self.registros, start=1):
      print(f"{i}. {entrada}")

  def analisar_dieta(self):
    if not self.registros:
      print("Nenhum registro diário encontrado.")
      return

    dados_alimentares = np.array([entrada.split(",") for entrada in self.registros])
    df = pd.DataFrame(dados_alimentares, columns=["Refeição", "Lanche", "Quantidade"])
    total_calorias = df['Quantidade'].astype(float).sum()

    print(f"\nAnálise Nutricional:")
    print(f"Total de Calorias Consumidas: {total_calorias} calorias")

class OrientacoesNutricionais:
  def __init__(self, perfil, registro_diario):
    self.perfil = perfil
    self.registro_diario = registro_diario

  def gerar_orientacoes(self):
    if not self.perfil.habitos_alimentares or not self.registro_diario.registros:
      print("Preencha o perfil e registre a dieta para gerar orientações.")
      return

    print("\nOrientações Nutricionais Personalizadas:")
    # Lógica para gerar orientações com base nas informações do perfil e análise nutricional
    if 'Perder peso' in self.perfil.objetivos_peso:
      print("Sugestão: Ajuste a dieta para reduzir a ingestão calórica e inclua exercícios regulares.")
    else:
        print("Sugestão: Mantenha uma dieta equilibrada e ajuste as porções conforme necessário.")

class SistemaAcompanhamento:
  def __init__(self, meta_agua, meta_proteina):
    self.registros_agua = {}
    self.registros_suplementos = {}
    self.meta_agua = meta_agua
    self.meta_proteina = meta_proteina

  def registrar_agua(self, aluno, quantidade):
    if aluno not in self.registros_agua:
      self.registros_agua[aluno] = []
    data_atual = datetime.date.today()
    self.registros_agua[aluno].append({"data": data_atual, "quantidade": quantidade})

  def registrar_suplemento(self, aluno, suplemento):
    if aluno not in self.registros_suplementos:
      self.registros_suplementos[aluno] = []
    data_atual = datetime.date.today()
    self.registros_suplementos[aluno].append({"data": data_atual, "suplemento": suplemento})

  def verificar_hidratacao(self, aluno):
    total_agua = sum(registro["quantidade"] for registro in self.registros_agua.get(aluno, []))
    if total_agua < self.meta_agua:
      return f"{aluno}, beba mais água! Apenas {total_agua} ml hoje."

  def verificar_metas_nutricionais(self, aluno):
    total_proteina = sum(1 for registro in self.registros_suplementos.get(aluno, []) if registro["suplemento"] == "proteina")
    if total_proteina < self.meta_proteina:
      return f"{aluno}, você precisa de mais proteína. Apenas {total_proteina} suplementos de proteína registrados."

class IntegracaoApp:
  def __init__(self):
    self.dados_app = None

  def sincronizar_dados(self, dados):
    # Lógica de sincronização com aplicativos de rastreamento alimentar
    self.dados_app = dados

  def exibir_dados_sincronizados(self):
    print("\nDados Sincronizados com Aplicativos:")
    print(self.dados_app)

class ComunicacaoNutricionista:
  def __init__(self, nome_nutricionista):
    self.nome_nutricionista = nome_nutricionista
    self.mensagens = []

  def enviar_mensagem(self, mensagem):
    self.mensagens.append(f"{self.nome_nutricionista}: {mensagem}")

  def exibir_mensagens(self):
    print("\nMensagens do Nutricionista:")
    for mensagem in self.mensagens:
      print(mensagem)

class SistemaNutricao:
  def __init__(self, perfil, registro_diario, integracao_app, comunicacao_nutricionista):
    self.perfil = perfil
    self.registro_diario = registro_diario
    self.integracao_app = integracao_app
    self.comunicacao_nutricionista = comunicacao_nutricionista

  def integrar_app_rastreamento(self, dados_app):
    self.integracao_app.sincronizar_dados(dados_app)
    self.integracao_app.exibir_dados_sincronizados()

  def fornecer_feedback(self, mensagem):
    self.comunicacao_nutricionista.enviar_mensagem(mensagem)

  def exibir_feedback_nutricionista(self):
    self.comunicacao_nutricionista.exibir_mensagens()


# CHAMADA DAS FUNÇÕES
while True:
  menu()
  opcao = int(input('Opção: '))
  if opcao == 1:
    menu_mod1()
    escolha = int(input('Opção: '))
    if escolha == 1:
      self.cadastrar_aluno()
    elif escolha == 2:
      aluno_nome = input("Digite o nome do aluno para a avaliação: ")
      self.realizar_avaliacao(aluno_nome)
    elif escolha == 3:
      self.exibir_alunos()
    elif escolha == 4:
      aluno_nome = input("Digite o nome do aluno para exibir as avaliações: ")
      self.exibir_avaliacoes(aluno_nome)
    elif escolha == 5:
      remetente = input("Digite o seu nome: ")
      destinatario = input("Digite o nome do destinatário: ")
      mensagem = input("Digite a mensagem: ")
      self.enviar_mensagem(remetente, destinatario, mensagem)
    elif escolha == 6:
      aluno_nome = input("Digite o nome do aluno para exibir as mensagens: ")
      self.exibir_mensagens(aluno_nome)
    elif escolha == 7:
      aluno_nome = input("Digite o nome do aluno para gerar o relatório de progresso: ")
      self.gerar_relatorio_progresso(aluno_nome)
    elif escolha == 8:
      aluno_nome = input("Digite o nome do aluno para personalizar o treino automaticamente: ")
      self.personalizar_treino_automatizado(aluno_nome)
    elif escolha == 9:
      aluno_nome = input("Digite o nome do aluno para exibir o histórico de acompanhamento: ")
      self.exibir_historico_acompanhamento(aluno_nome)
    elif escolha == 10:
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
  elif opcao == 2:
    menu_mod2()
    opc_mod2 = int(input('Opção: '))
    if opc_mod2 == 1:
      cadastro_produto()
    elif opc_mod2 == 2:
      perfil_compra()
    elif opc_mod2 == 3:
      promocoes()
    elif opc_mod2 == 4:
      lista_desejo()
    elif opc_mod2 == 5:
      novos_produtos()
    elif opc_mod2 == 6:
      sistema_pagamento()
    elif opc_mod2 == 7:
      acompanhamento_entregas()
    elif opc_mod2 == 8:
      programa_fidelidade()
    elif opc_mod2 == 9:
      avalia_produto()
    elif opc_mod2 == 10:
      gestao_estoque()
    elif opc_mod2 == 11:
      print('ENCERRANDO...')
      break
    else:
      print('Opção Inválida! Tente novamente mais tarde.')
  elif opcao == 3:
    print()
  elif opcao == 4:
    aluno1 = Aluno("João")
    aluno1.preencher_questionario()
    aluno1.exibir_perfil()
    aluno1.registrar_dieta_diaria()
    aluno1.receber_orientacoes_nutricionais()

    perfil_aluno = PerfilNutricional()
    perfil_aluno.preencher_perfil("Saudáveis", "Nenhuma", "Perder peso", "Vegetariana")

    registro_aluno = RegistroDiario()
    registro_aluno.adicionar_registro("Café da Manhã, Frutas, 200g")
    registro_aluno.adicionar_registro("Almoço, Frango grelhado, 300g")
    registro_aluno.adicionar_registro("Lanche, Barrinha de cereal, 1 unidade")

    perfil_aluno.exibir_perfil()
    registro_aluno.exibir_registros()

    registro_aluno.analisar_dieta()

    orientacoes_aluno = OrientacoesNutricionais(perfil_aluno, registro_aluno)
    orientacoes_aluno.gerar_orientacoes()

    sistema = SistemaAcompanhamento(meta_agua=2000, meta_proteina=3)
    sistema.registrar_agua("Aluno1", 1500)
    sistema.registrar_suplemento("Aluno1", "proteina")

    print(sistema.verificar_hidratacao("Aluno1"))
    print(sistema.verificar_metas_nutricionais("Aluno1"))

    integracao_app = IntegracaoApp()
    comunicacao_nutricionista = ComunicacaoNutricionista("Nutricionista1")

    sistema_nutricao = SistemaNutricao(perfil_aluno, registro_aluno, integracao_app, comunicacao_nutricionista)
    dados_app_rastreamento = {"alimento": "Maçã", "calorias": 50}
    sistema_nutricao.integrar_app_rastreamento(dados_app_rastreamento)
    sistema_nutricao.fornecer_feedback("Preciso de mais orientações sobre minha dieta.")
    sistema_nutricao.exibir_feedback_nutricionista()
  elif opcao == 5:
    print('Encerrando o programa...')
    break
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')
