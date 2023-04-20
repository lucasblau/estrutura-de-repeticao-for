produtos = [{'id': 1, 'desc': 'raçao', 'est': 2},
            {'id': 2, 'desc': 'osso', 'est': 5},
            {'id': 3, 'desc': 'caminha', 'est': 9}]
carrinho_produtos = [{'id': 1, 'qtd': 2},
                     {'id': 2, 'qtd': 5},
                     {'id': 3, 'qtd': 10}]


def verificar_estoque():
    for carrinho_produto in carrinho_produtos:
        id_carrinho = carrinho_produto['id']
        qtd_carrinho = carrinho_produto['qtd']

        for produto in produtos:
            id_produto = produto['id']
            est_produto = produto['est']

            if id_carrinho == id_produto:
                desc_produto = produto['desc']
                if est_produto >= qtd_carrinho:
                    print(
                        f'compra do produto {desc_produto} realizada com sucesso')
                else:
                    print(f'produto {desc_produto} nao tem estoque')


verificar_estoque()
