# -*- coding: utf-8 -*-

def clientes():
    clientes = db(Clientes).select()
    return locals()


def n_cliente():
    cliente_id = request.vars.cliente
    if cliente_id is None:
        form = SQLFORM(Clientes)
    else:
        form = SQLFORM(Clientes, cliente_id, showid=False, deletable=True)

    if form.process().accepted:                     
        redirect(URL('cadastros', 'clientes'))
    elif form.errors:
        response.flash = 'Ops, confira os campos!'
    
    return locals()


def fornecedores():
    fornecedores = db(Fornecedores).select()
    return locals()


def n_fornecedor():
    forn_id = request.vars.fornecedor
    if forn_id is None:
        form = SQLFORM(Fornecedores)
    else:
        form = SQLFORM(Fornecedores, forn_id, showid=False, deletable=True)

    if form.process().accepted:                     
        redirect(URL('cadastros', 'fornecedores'))
    elif form.errors:
        response.flash = 'Ops, confira os campos!'
    
    return locals()


def produtos():
    produtos = db(Produtos).select()
    return locals()


def n_produto():
    produto_id = request.vars.produto
    if produto_id is None:
        form = SQLFORM(Produtos)
    else:
        form = SQLFORM(Produtos, produto_id, showid=False, deletable=True)

    if form.process().accepted:                     
        redirect(URL('cadastros', 'produtos'))
    elif form.errors:
        response.flash = 'Ops, confira os campos!'
    return locals()