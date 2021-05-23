import unittest
import pdb

from nltk.probability import FreqDist
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from processamento import Processamento

class TestProcessamento(unittest.TestCase):
    def test_atribuir_texto(self, filename = 'the-sorrow-of-love-william-butler-yeats.txt'):
        # carregando o texto
        f = open(filename, 'r')
        texto = ''.join(f.readlines())
        f.close()
        # realizando assertion
        processamento = Processamento(texto = texto)
        self.assertEqual(
            texto, processamento.texto
        )

    def test_construir_conjunto_stopwords(self):
        # definindo o conjunto teste de stopwords
        conjunto_stopwords = {'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'ao', 'aos', 'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'até', 'com', 'como', 'da', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'depois', 'do', 'dos', 'e', 'ela', 'elas', 'ele', 'eles', 'em', 'entre', 'era', 'eram', 'essa', 'essas', 'esse', 'esses', 'esta', 'estamos', 'estas', 'estava', 'estavam', 'este', 'esteja', 'estejam', 'estejamos', 'estes', 'esteve', 'estive', 'estivemos', 'estiver', 'estivera', 'estiveram', 'estiverem', 'estivermos', 'estivesse', 'estivessem', 'estivéramos', 'estivéssemos', 'estou', 'está', 'estávamos', 'estão', 'eu', 'foi', 'fomos', 'for', 'fora', 'foram', 'forem', 'formos', 'fosse', 'fossem', 'fui', 'fôramos', 'fôssemos', 'haja', 'hajam', 'hajamos', 'havemos', 'hei', 'houve', 'houvemos', 'houver', 'houvera', 'houveram', 'houverei', 'houverem', 'houveremos', 'houveria', 'houveriam', 'houvermos', 'houverá', 'houverão', 'houveríamos', 'houvesse', 'houvessem', 'houvéramos', 'houvéssemos', 'há', 'hão', 'isso', 'isto', 'já', 'lhe', 'lhes', 'mais', 'mas', 'me', 'mesmo', 'meu', 'meus', 'minha', 'minhas', 'muito', 'na', 'nas', 'nem', 'no', 'nos', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'não', 'nós', 'o', 'os', 'ou', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'por', 'qual', 'quando', 'que', 'quem', 'se', 'seja', 'sejam', 'sejamos', 'sem', 'serei', 'seremos', 'seria', 'seriam', 'será', 'serão', 'seríamos', 'seu', 'seus', 'somos', 'sou', 'sua', 'suas', 'são', 'só', 'também', 'te', 'tem', 'temos', 'tenha', 'tenham', 'tenhamos', 'tenho', 'terei', 'teremos', 'teria', 'teriam', 'terá', 'terão', 'teríamos', 'teu', 'teus', 'teve', 'tinha', 'tinham', 'tive', 'tivemos', 'tiver', 'tivera', 'tiveram', 'tiverem', 'tivermos', 'tivesse', 'tivessem', 'tivéramos', 'tivéssemos', 'tu', 'tua', 'tuas', 'tém', 'tínhamos', 'um', 'uma', 'você', 'vocês', 'vos', '{', '|', '}', '~', 'à', 'às', 'é', 'éramos'}
        # realizando assertion
        processamento = Processamento(texto = '', lingua = 'portuguese')
        self.assertEqual(
            processamento.conjunto_stopwords, conjunto_stopwords
        )

    def test_tokens_sentencas(self, filename = 'the-sorrow-of-love-william-butler-yeats.txt'):
        # 1. carregar o texto a ser tokenizado em sentencas
        f = open(filename, 'r')
        texto = ''.join(f.readlines())
        f.close()
        # 2. definir lista de sentencas (tokenizadas)
        tokens_sentencas = ["The brawling of a sparrow in the eaves,   \nThe brilliant moon and all the milky sky,   \nAnd all that famous harmony of leaves,   \nHad blotted out man's image and his cry.",
 "A girl arose that had red mournful lips\nAnd seemed the greatness of the world in tears,   \nDoomed like Odysseus and the labouring ships   \nAnd proud as Priam murdered with his peers;\n\nArose, and on the instant clamorous eaves,   \nA climbing moon upon an empty sky,   \nAnd all that lamentation of the leaves,   \nCould but compose man's image and his cry."]
        # 3. realizar assertion
        processamento = Processamento(texto = texto)
        self.assertEqual(
            processamento.tokens_sentencas, tokens_sentencas
        )

    def test_tokens_palavras(self, filename = 'the-sorrow-of-love-william-butler-yeats.txt'):
        # 1. carregar o texto a ser tokenizado em palavras
        f = open(filename, 'r')
        texto = ''.join(f.readlines())
        f.close()
        # 2. definir lista de palavras (tokenizadas)
        tokens_palavras = ['the', 'brawling', 'of', 'a', 'sparrow', 'in', 'the', 'eaves', ',', 'the', 'brilliant', 'moon', 'and', 'all', 'the', 'milky', 'sky', ',', 'and', 'all', 'that', 'famous', 'harmony', 'of', 'leaves', ',', 'had', 'blotted', 'out', 'man', "'s", 'image', 'and', 'his', 'cry', '.', 'a', 'girl', 'arose', 'that', 'had', 'red', 'mournful', 'lips', 'and', 'seemed', 'the', 'greatness', 'of', 'the', 'world', 'in', 'tears', ',', 'doomed', 'like', 'odysseus', 'and', 'the', 'labouring', 'ships', 'and', 'proud', 'as', 'priam', 'murdered', 'with', 'his', 'peers', ';', 'arose', ',', 'and', 'on', 'the', 'instant', 'clamorous', 'eaves', ',', 'a', 'climbing', 'moon', 'upon', 'an', 'empty', 'sky', ',', 'and', 'all', 'that', 'lamentation', 'of', 'the', 'leaves', ',', 'could', 'but', 'compose', 'man', "'s", 'image', 'and', 'his', 'cry', '.']
        # 3. relizar assertion
        processamento = Processamento(texto = texto)
        self.assertEqual(
            processamento.tokens_palavras, tokens_palavras
        )

    def test_remocao_stopwords(self, filename = 'the-sorrow-of-love-william-butler-yeats.txt'):
        # 1. carregar o texto a ser tokenizado em palavras
        f = open(filename, 'r')
        texto = ''.join(f.readlines())
        f.close()
        # 2. definir texto sem stopwords para ser comparado
        texto_sem_stopwords = ['brawling', 'sparrow', 'eaves', 'brilliant', 'moon', 'milky', 'sky', 'famous', 'harmony', 'leaves', 'blotted', 'man', "'s", 'image', 'cry', 'girl', 'arose', 'red', 'mournful', 'lips', 'seemed', 'greatness', 'world', 'tears', 'doomed', 'like', 'odysseus', 'labouring', 'ships', 'proud', 'priam', 'murdered', 'peers', 'arose', 'instant', 'clamorous', 'eaves', 'climbing', 'moon', 'upon', 'empty', 'sky', 'lamentation', 'leaves', 'could', 'compose', 'man', "'s", 'image', 'cry']
        # 3. remover stopwords
        processamento = Processamento(texto = texto)
        processamento.remover_stopwords()
        # 4. relizar assertion
        self.assertEqual(
            processamento.texto_sem_stopwords, texto_sem_stopwords
        )

    def test_frequencia_nao_stopwords(self, filename = 'the-sorrow-of-love-william-butler-yeats.txt'):
        # 1. carregar o texto a ser tokenizado em palavras
        f = open(filename, 'r')
        texto = ''.join(f.readlines())
        f.close()
        # 2. definir frequencias para ser comparada
        frequencias = {'brawling': 1, 'sparrow': 1, 'eaves': 2, 'brilliant': 1, 'moon': 2, 'milky': 1, 'sky': 2, 'famous': 1, 'harmony': 1, 'leaves': 2, 'blotted': 1, 'man': 2, "'s": 2, 'image': 2, 'cry': 2, 'girl': 1, 'arose': 2, 'red': 1, 'mournful': 1, 'lips': 1, 'seemed': 1, 'greatness': 1, 'world': 1, 'tears': 1, 'doomed': 1, 'like': 1, 'odysseus': 1, 'labouring': 1, 'ships': 1, 'proud': 1, 'priam': 1, 'murdered': 1, 'peers': 1, 'instant': 1, 'clamorous': 1, 'climbing': 1, 'upon': 1, 'empty': 1, 'lamentation': 1, 'could': 1, 'compose': 1}
        # 3. remover stopwords
        processamento = Processamento(texto = texto)
        processamento.remover_stopwords()
        # 4. calcular frequencia das não stopwords
        processamento.calcular_frequencia_nao_stopwords()
        # 5. realizar assertion
        self.assertEqual(
            frequencias, dict(processamento.frequencia_nao_stopwords)
        )

    def test_palavras_mais_importantes(self, filename = 'the-sorrow-of-love-william-butler-yeats.txt'):
        # 1. carregar o texto a ser tokenizado em palavras
        f = open(filename, 'r')
        texto = ''.join(f.readlines())
        f.close()
        # 2. definir as 3 palavras mais importantes (ocorrentes)
        # do texto para comparação
        palavras_mais_importantes_referencia = [('eaves', 2), ('moon', 2), ('sky', 2)]
        # 3. remover stopwords
        processamento = Processamento(texto = texto)
        processamento.remover_stopwords()
        # 4. calcular frequencia das não stopwords
        processamento.calcular_frequencia_nao_stopwords()
        # 5. solicitar as 3 palavras mais importantes
        # ao objeto processamento
        palavras_mais_importantes_computadas = processamento.palavras_mais_importantes(3)
        # 6. realizar assertion
        self.assertEqual(
            palavras_mais_importantes_computadas,
            palavras_mais_importantes_referencia
        )
        # 7. estabelecer mais comparativos, computar palavras importantes e realizar mais assertions
        palavras_mais_importantes_referencia = [('eaves', 2), ('moon', 2), ('sky', 2), ('leaves', 2), ('man', 2)]
        palavras_mais_importantes_computadas = processamento.palavras_mais_importantes(5)
        self.assertEqual(
            palavras_mais_importantes_computadas,
            palavras_mais_importantes_referencia
        )

if __name__ == "__main__":
    unittest.main()
