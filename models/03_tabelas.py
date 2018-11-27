# Cadastros
Fornecedores = db.define_table('fornecedores',
                               Field('nome', 'string', label=T('Name')),
                               Field('telefone', 'list:string', Label=T('Telephone')),
                               format='%(nome)s')


Clientes = db.define_table('clientes',
                           Field('nome', 'string', Label=T('Name')),
                           Field('telefone', 'list:string', label=T('Telephone')),
                           format='%(nome)s')
Clientes.nome.requires = IS_NOT_EMPTY(error_message='Insira o nome do cliente')


Produtos = db.define_table('produtos',
                           Field('nome', 'string'),
                           Field('precoCompra', 'double', default=0.0, label='Preço de compra'),
                           Field('precoVenda', 'double', default=0.0, label='Preço de venda'),
                           format='%(nome)s')


# Saídas
Compras = db.define_table('compras',
                          Field('fornecedor', 'reference fornecedores', label='Fornecedor'),
                          Field('total', 'double', default=0.0, label='Total'),
                          auth.signature)
Compras.fornecedor.requires = IS_IN_DB(db, 'fornecedores.id', '%(nome)s',
                                   error_message='Preencha com o nome do Fornecedor',
                                   zero=T('Choose one...'))


ComprasProduto = db.define_table('comprasProduto',
                         Field('codCompra', 'reference compras'), 
                         Field('produto', 'reference produtos', label='Produto'),
                         Field('valorUnit', 'double', label='Valor unitário'),
                         Field('quantidade', 'double', label='Quantidade'),
                         Field('desconto', 'integer', default=0, label='Desconto'),
                         Field('total', 
                               compute=lambda r: r['valorUnit'] * r['quantidade'] * (1.0 - r['desconto'] / 100)),)


Saidas = db.define_table('saidas',
                          Field('descricao', 'string', label='Descrição'),
                          Field('valor', 'double', label='Valor'),
                          Field('obs', 'text', label='OBS.'),
                          auth.signature)


# Entradas
Vendas = db.define_table('vendas',
                         Field('cliente', 'reference clientes', label='Cliente'),
                         Field('total', 'double', default=0.0, label='Total'),
                         auth.signature)
Vendas.cliente.requires = IS_IN_DB(db, 'clientes.id', '%(nome)s',
                                   error_message='Preencha com o nome do Cliente',
                                   zero=T('Choose one...'))


VendasProduto = db.define_table('vendasProduto',
                         Field('codVenda', 'reference vendas'),                        
                         Field('produto', 'reference produtos', label='Produto'),
                         Field('valorUnit', 'double', label='Valor unitário'),
                         Field('quantidade', 'double', label='Quantidade'),
                         Field('desconto', 'integer', default=0, label='Desconto'),
                         Field('total', 
                               compute=lambda r: r['valorUnit'] * r['quantidade'] * (1.0 - r['desconto'] / 100)),                         
                         )


Entradas = db.define_table('entradas',
                            Field('descricao', 'string', label='Descrição'),
                            Field('valor', 'double', label='Valor'),
                            Field('obs', 'text', label='OBS.'),
                            auth.signature)


# Movimentação de Caixa
# To-Do
MovimentoCaixa = db.define_table('movimento_caixa',
                                 Field('dia', 'datetime', label='Data', default=request.now),
                                 Field('saldo_inicial', 'double', default=0.00),
                                 Field('entrada', 'double', default=0.00),
                                 Field('saida', 'double', default=0.00),
                                 Field('saldo_final', 'double', default=0.00),)