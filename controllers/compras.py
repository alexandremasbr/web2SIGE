# -*- coding: utf-8 -*-

def compras():
    compras = db(Compras).select(Compras.id, Compras.created_on,
                               Compras.total, Compras.fornecedor,
                               orderby=~Compras.created_on)
    return dict(compras=compras)


def n_compra():   
    # Cria nova venda ou eida existente
    compra_id = request.vars.compra
    if compra_id is None:
        novaCompra = Compras.insert(itens=[])
        db.commit()
        redirect(URL('compras', 'n_compra', vars={'compra':novaCompra}))
    
    # Consultas
    itens = db(ComprasProduto.codCompra == compra_id).select(
                                                          ComprasProduto.id,
                                                          ComprasProduto.produto,
                                                          ComprasProduto.valorUnit,
                                                          ComprasProduto.quantidade,
                                                          ComprasProduto.desconto,
                                                          ComprasProduto.total
    )
    total_compra = sum([float(i.total) for i in itens])

    # Formulários
    compra = SQLFORM(Compras, compra_id, fields=['fornecedor'],
                    showid=False, submit_button='Finalizar Compra')
    compra.element(_type='submit')['_class']='btn btn-success'
    
    form = SQLFORM(ComprasProduto, submit_button='Adicionar ítem')
    form.vars.codCompra = compra_id
    ComprasProduto.codCompra.writable = False
    form.element(_name="codCompra")['_disabled'] = ""
    
    if compra.process().accepted:
        db(Compras.id == compra_id).update(total=total_compra)             
        redirect(URL('compras', 'imprimir_compra', vars={'compra':compra_id}))    
    
    if form.process().accepted:                     
        redirect(URL('compras', 'n_compra', vars={'compra':compra_id}))

    return dict(form=form, compra=compra, compra_id=compra_id,
                itens=itens, total_compra=total_compra)


def cancelar_compra():
    compra_id = request.vars.compra
    db(Compras.id == compra_id).delete()
    redirect(URL('compras', 'compras'))


def excluir_produto_compra():    
    compra_id = request.args[0]
    p_id = request.args[1]
    db(ComprasProduto.id == p_id).delete()
    redirect(URL('compras', 'n_compra', vars={'compra':compra_id}))


def imprimir_compra():
    compra_id = request.vars.compra
    itens = db(ComprasProduto.codCompra == compra_id).select(
                                                          ComprasProduto.produto,
                                                          ComprasProduto.valorUnit,
                                                          ComprasProduto.quantidade,
                                                          ComprasProduto.total
    )
    compra = db(Compras.id == compra_id).select(Compras.id, Compras.created_on,
                                             Compras.fornecedor, Compras.total).first()

    return dict(itens=itens, compra=compra)