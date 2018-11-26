# -*- coding: utf-8 -*-

def fluxo_caixa():
    fluxo = db(MovimentoCaixa).select()
    return locals()


def entradas():
    entradas = db(Entradas).select()    
    
    return locals()


def n_entrada():
    entrada_id = request.vars.entrada
    if entrada_id is None:
        form = SQLFORM(Entradas, fields=['descricao', 'valor', 'obs', 'created_on'])
    else:
        form = SQLFORM(Entradas, entrada_id, showid=False, deletable=True,
                       fields=['descricao', 'valor', 'obs', 'created_on'])

    if form.process().accepted:
        valor = float(request.vars.valor)
        saldo = soma_saldo(valor)
        MovimentoCaixa.insert(saldo_inicial=saldo[0], entrada=valor,
                              saida=0, saldo_final=saldo[1])                     
        redirect(URL('financeiro', 'entradas'))
    elif form.errors:
        response.flash = 'Ops, confira os campos!'
    
    return locals()


def saidas():
    saidas = db(Saidas).select()    
    return locals()


def n_saida():
    saida_id = request.vars.saida_id    
    if saida_id is None:
        form = SQLFORM(Saidas, fields=['descricao', 'valor', 'obs', 'created_on'])
    else:
        form = SQLFORM(Saidas, saida_id, showid=False, deletable=True,
                       fields=['descricao', 'valor', 'obs', 'created_on'])

    if form.process().accepted:                     
        redirect(URL('financeiro', 'saidas'))
    elif form.errors:
        response.flash = 'Ops, confira os campos!'
    
    return locals()