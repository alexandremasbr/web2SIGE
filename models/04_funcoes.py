# Funções extras se necessário

def soma_saldo(x):
    '''
    Soma x ao ultimo saldo da tabela MovimentoCaixa;
    Retorna saldo anterior e saldo atualizado
    '''
    saldo_anterior = db(MovimentoCaixa).select(MovimentoCaixa.saldo_final,
                                               orderby=~MovimentoCaixa.id).first()
    saldo_final = (saldo_anterior['saldo_final'] if saldo_anterior is not None else 0) + x
    return (saldo_anterior, saldo_final)

def diminui_saldo(x):
    '''
    Subtrai x ao ultimo saldo da tabela MovimentoCaixa;
    Retorna saldo anterior e saldo atualizado
    '''
    saldo_anterior = db(MovimentoCaixa).select(MovimentoCaixa.saldo_final,
                                               orderby=~MovimentoCaixa.id).first()
    saldo_final = (saldo_anterior['saldo_final'] if saldo_anterior is not None else 0) - x
    return (saldo_anterior, saldo_final)