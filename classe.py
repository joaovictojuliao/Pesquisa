import pandas as pd
import datetime as dt


class Pesquisa():

    # Método construtor do código
    def __init__(self, perguntas, nomeDoArquivo):
        self.__perguntas = perguntas

        self.__pesquisaDF = pd.DataFrame(
            columns=["Nome", "Idade", "Genero", "Pergunta1", "Pergunta2", "Pergunta3", "Pergunta4", "Data"])
        #Columns - são colunas estrutururais de dados primários em DataFrame no Pandas

        self.nomeDoArquivo = nomeDoArquivo

    # Receber a autorização ou não para a pessoa ser entrevistada
    def querParticipar(self):

        aceitar = input("Quer participar desta pesquisa rápida? S/N : ")

        while aceitar.strip().upper() not in ["S", "N"]:
            aceitar = input("Input invalido, quer participar desta pesquisa rápida? S/N : ")

        return True if aceitar.strip().upper() == "S" else False

    # Inicializador da pesquisa, caso obtenha a autorização
    def iniciarPesquisa(self):
        querParticipar = self.querParticipar()

        while querParticipar:
            respostaDict = {}
            idade = self.getIdade()

            if idade > 0:
                nome = str(input("Informe o seu o nome: "))

                while nome == "":
                    nome = str(input("O campo nome não pode ser vazio, informe o seu o nome: "))
                genero = self.getGenero()

            elif idade == 0:
                print("Fim ! \nObrigado por participar da nossa pesquisa! ")
                break

            for i in range(4):
                rsp = self.getResposta(i)
                respostaDict[f"Pergunta{i + 1}"] = rsp

            dataHoraCadastrada = dt.datetime.now()
            respostaDict["Nome"] = nome
            respostaDict["Idade"] = idade
            respostaDict["Genero"] = genero
            respostaDict["Data"] = dataHoraCadastrada.strftime('%d/%m/%Y %H:%M:%S')
            #strftime - retorna os objectos de data e hora para string
            respostaDF = pd.DataFrame([respostaDict])

            self.__pesquisaDF = pd.concat([self.__pesquisaDF, respostaDF], axis=0, ignore_index=True)

        if len(self.__pesquisaDF.index) != 0:
            self.exportToCSV(self.nomeDoArquivo)
            print(f"Pesquisa salva no arquivo {self.nomeDoArquivo}")
        else:
            print("Sem dados para serem salvos.")

    # Recebendo os valores da pesquisa
    def getPesquisa(self):
        return self.__pesquisaDF

    # Exportando o código para csv
    def exportToCSV(self, nomeDoAqruivo):
        return self.__pesquisaDF.to_csv(nomeDoAqruivo)

    # Recebendo os valores de idade
    def getIdade(self):
        idade = input("Informe a sua idade: ")

        while not idade.isnumeric():
            idade = input("Input invalido, informe a sua idade corretamente: ")
        return int(idade)

    # Recebendo os valores do gênero
    def getGenero(self):
        genero = input("Informe qual o genero que você se identifica: "
                       "\n [F] Feminino\n [M] Masculino\n [T] Transgenero\n [NB] Nao-Binario\n [O] Outro\n")

        while genero.upper() not in ["F", "M", "T", "NB", "O"]:
            genero = input("Input invalido, informe novamente qual o genero que você se identifica: "
                           "\n [F] Feminino\n [M] Masculino\n [T] Transgenero\n [NB] Nao-Binario\n [O] Outro\n")

        generoFormatado = self.formatarGenero(genero.upper())
        return generoFormatado

    # Recebendo os valores da resposta
    def getResposta(self, index):
        pergunta = self.__perguntas[index]
        rsp = input(f"{pergunta} \n"
                    "[1] - Sim\n"
                    "[2] - Não\n"
                    "[3] - Não sei responder\n"
                    "Escolha uma das alternativas.")

        while rsp not in ["1", "2", "3"]:
            rsp = input(f"Resposta invalida, tente novamente. {pergunta} \n"
                        "[1] - Sim\n"
                        "[2] - Não\n"
                        "[3] - Não sei responder\n"
                        "Escolha uma das alternativas.")

        respostaFormatada = self.formatarResposta(int(rsp))
        return respostaFormatada

    # Informações sobre os gêneros
    def formatarGenero(self, genero):
        if genero == "F":
            generoFormatado = "Feminino"
            return generoFormatado

        elif genero == "M":
            generoFormatado = "Masculino"
            return generoFormatado

        elif genero == "T":
            generoFormatado = "Transgènero"
            return generoFormatado

        elif genero == "B":
            generoFormatado = "Binário"
            return generoFormatado

        elif genero == "O":
            generoFormatado = "Outro"
            return generoFormatado

    # Informações sobre as respostas
    def formatarResposta(self, resposta):
        if resposta == 1:
            respostaFormatada = "Sim"
            return respostaFormatada

        elif resposta == 2:
            respostaFormatada = "Nao"
            return respostaFormatada

        elif resposta == 3:
            respostaFormatada = "Nao sei responder"
            return respostaFormatada

    # Informações dos horários realizados das entrevistas
    def DataHora(self, dataHoraCadastrada):
        self.dataHoraCadastrada = dataHoraCadastrada
        return dataHoraCadastrada

    # Recebendo e reunindo as informações dos entrevistados
    def informacoesEntrevistado(self):
        resposta = [self.nome, self.idade, self.genero, self.resposta1,
                    self.resposta2, self.resposta3, self.resposta4]
        return resposta
