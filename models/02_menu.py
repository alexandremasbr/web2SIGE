# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Registration'), False, '#', [
        (T('Customers'), False, URL('cadastros', 'clientes'), []),
        (T('Providers'), False, URL('cadastros', 'fornecedores'), []),
        (T('Products'), False, URL('cadastros', 'produtos'), []),
    ]),    
    (T('Shopping'), False, URL('compras', 'compras'), []),
    (T('Sales'), False, URL('vendas', 'vendas'), []),
    (T('Financial'), False, '#', [
        (T('Fluxo de Caixa'), False, URL('financeiro', 'fluxo_caixa'), []),
        (T('Entradas'), False, URL('financeiro', 'entradas'), []),
        (T('Saídas'), False, URL('financeiro', 'saidas'), []),
    ]),   
]