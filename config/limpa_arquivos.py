def limpa_arquivos():

    arquivo = open("database/servidor/jogada_ai.txt",'w')
    arquivo.write("")
    arquivo.close()

    arquivo = open("database/servidor/jogada_humano.txt",'w')
    arquivo.write("")
    arquivo.close()

    arquivo = open("database/cliente/jogada_ai.txt",'w')
    arquivo.write("")
    arquivo.close()

    arquivo = open("database/cliente/jogada_humano.txt",'w')
    arquivo.write("")
    arquivo.close()