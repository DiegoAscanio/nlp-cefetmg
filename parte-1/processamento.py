from nltk.probability import FreqDist
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

class Processamento:
    def _atribuir_texto(self, texto):
        # Atividade 1:
        # Realize a atribuição do texto
        self.texto = None

    def _construir_conjunto_stopwords(self, lingua):
        # Atividade 2:
        # Construa o conjunto_stopwords que consiste em um
        # conjunto (set) que concatena as stopwords da lingua
        # desejada (obtidas pelo método stopwords.words)
        # com uma lista construída a partir dos sinais de pontuação
        # (obtidas em from string import punctuation)

        # substitua None pelo função de stopwords do nltk que retorna
        # as stopwords da lingua desejada
        lista_stopwords = None

        # Substitua None pelo ojeto de pontuações punctuation importado
        # da biblioteca string
        lista_pontuacoes = None

        # Descomente a linha abaixo para criar o conjunto de stopwords
        #self.conjunto_stopwords = set(lista_stopwords + lista_pontuacoes)

    @property
    def tokens_sentencas(self):
        if self._sentencas_tokenizadas is None:
            # Atividade 3 - Substitua o None pelo comando do nltk que tokeniza
            # o texto em sentencas
            self._sentencas_tokenizadas = None
            # Fim Atividade 3
        return self._sentencas_tokenizadas

    @property
    def tokens_palavras(self):
        if self._palavras_tokenizadas is None:
            # Atvidade 4 - Substitua os Nones abaixo pelos comandos que
            # 4.1: Faz o objeto self.texto ficar em letras minusculas
            texto_minusculo = None
            # 4.2 Tokeniza o texto minusculo em palavras
            texto_minusculo_tokenizado = None
            # Fim Atividade 4
            self._palavras_tokenizadas = texto_minusculo_tokenizado
        return self._palavras_tokenizadas

    def remover_stopwords(self):
        # Atividade 5 - Implemente o método que realize a remoção de stopwords
        # do texto, armazenando no atributo self.texto_sem_stopwords as palavras 
        # do texto sem as stopwords
        #
        # Para implementar você pode percorrer a lista de palavras tokenizadas e 
        # adicionar a lista self.texto_sem_stopwords cada palavra da
        # lista de palavras tokenizadas que não esteja no conjunto de 
        # stopwords (representado pelo atributo self.conjunto_stopwords)
        # Disponível em: https://medium.com/@maelyalways/nltk-tutorial-8175e57fbfda 
        # Substitua o pass pelo(s) comando(s) necessários para adicionar 
        # palavras na lista self.texto_sem_stopwords que representa o 
        # texto sem as stopwords
        pass

    def calcular_frequencia_nao_stopwords(self):
        # Atividade 6:
        # O atributo `self.texto_sem_stopwords` da classe `Processamento`
        # contém a lista das palavras significantes do texto (que não 
        # são stopwords).
        #
        # Substituta o None pelo atributo adequado para calcular a
        # frequecia de palavras que não são stopwords no texto.
        self.frequencia_nao_stopwords = FreqDist(None)

    def palavras_mais_importantes(self, N):
        dicionario_frequencia = dict(self.frequencia_nao_stopwords)
        # Atividade 7:
        # 7.1 substitua o pass abaixo por um comando de importação
        # da classe Counter presente no pacote collections
        pass
        # 7.2 instancie um objeto counter da Classe counter que recebe 
        # no construtor dicionario_frequencia como parêmetro. Para isso
        # substitua o None pela instanciação correta
        counter = None
        # 7.3 retorne a lista de tuplas das N palavras mais importantes
        # do texto através do método most_common, substituindo
        # para tal o None pelo objeto counter e a chamada ao método
        # most_common
        return None

    def __init__(self, texto, lingua = 'english'):
        # 1. atribuicao do texto
        self._atribuir_texto(texto)
        # 2. criacao do conjunto de stopwords
        self._construir_conjunto_stopwords(lingua)
        # 3. instanciacao de outros atributos como None
        self._sentencas_tokenizadas = None
        self._palavras_tokenizadas = None
        self.texto_sem_stopwords = [] # lista vazia
