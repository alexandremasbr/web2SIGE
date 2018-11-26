# -*- coding: utf-8 -*-

def vendas():
    vendas = db(Vendas).select(Vendas.id, Vendas.created_on,
                               Vendas.total, Vendas.cliente,
                               orderby=~Vendas.created_on)
    return dict(vendas=vendas)


def n_venda():   
    # Cria nova venda ou edita existente
    venda_id = request.vars.venda
    if venda_id is None:
        novaVenda = Vendas.insert(itens=[])
        db.commit()
        redirect(URL('vendas', 'n_venda', vars={'venda':novaVenda}))
    
    # Consultas    
    itens = db(VendasProduto.codVenda == venda_id).select(
                                                          VendasProduto.produto,
                                                          VendasProduto.valorUnit,
                                                          VendasProduto.quantidade,
                                                          VendasProduto.desconto,
                                                          VendasProduto.total
    )
    total_venda = sum([float(i.total) for i in itens])

    # Formulários
    venda = SQLFORM(Vendas, venda_id, fields=['cliente'],
                    showid=False, submit_button='Finalizar Venda')
    venda.element(_type='submit')['_class']='btn btn-success'
    
    form = SQLFORM(VendasProduto, submit_button='Adicionar ítem', _id='form1')
    form.vars.codVenda = venda_id
    VendasProduto.codVenda.writable = False
    form.element(_name="codVenda")['_disabled'] = ""
    
    # Adiciona ítem
    if form.process().accepted:                     
        redirect(URL('vendas', 'n_venda', vars={'venda':venda_id}))
    
    #Faturar venda
    if venda.process().accepted:       
        db(Vendas.id == venda_id).update(total=total_venda)             
        redirect(URL('vendas', 'imprimir_venda', vars={'venda':venda_id}))

    return dict(form=form, venda=venda, venda_id=venda_id,
                itens=itens, total_venda=total_venda)


def imprimir_venda():
    venda_id = request.vars.venda
    itens = db(VendasProduto.codVenda == venda_id).select(
                                                          VendasProduto.produto,
                                                          VendasProduto.valorUnit,
                                                          VendasProduto.quantidade,
                                                          VendasProduto.total
    )
    venda = db(Vendas.id == venda_id).select(Vendas.id, Vendas.created_on,
                                             Vendas.cliente, Vendas.total).first()

    return dict(itens=itens, venda=venda)


def cancelar_venda():
    venda_id = request.vars.venda
    db(Vendas.id == venda_id).delete()
    redirect(URL('vendas', 'vendas'))