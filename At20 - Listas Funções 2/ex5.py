def notas(*num, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    nota = {}

    for c in range(0,len(num)):



        nota['total'] = len(num)
        if c == 0:
            media = 0
            nota['maior'] = num[c]
            nota['menor'] = num[c]
        elif num[c] > nota['maior']:
            nota['maior'] = num[c]
        elif num[c] < nota['menor']:
            nota['menor'] = num[c]

        media = media + num[c]/len(num)
        nota['media'] = media


    if sit == True:
        if nota['media'] < 5.0:
            nota['situação'] = 'RUIM'
        elif nota['media'] >= 5.0 and nota['media'] <= 7.0:
            nota['situação'] = 'RAZOÁVEL'
        else:
            nota['situação'] = 'BOA'
    return nota



nota = notas(9.5,10,9.5,10,sit=True)
print(nota)
help(notas)