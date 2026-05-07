# Dicionário de teste
configuracoes_teste = {
    "tema": "claro",
    "notificacoes": "ativadas"
}

def adicionar_configuracao(configuracoes: dict, par: tuple):
    chave, valor = par
    chave = str(chave).lower()
    valor = str(valor).lower()

    if chave in configuracoes:
        return f"A configuração '{chave}' já existe! Não é possível adicionar uma nova configuração com este nome."
    
    configuracoes[chave] = valor
    return f"Configuração '{chave}' adicionada com o valor '{valor}' com sucesso!"


def atualizar_configuracao(configuracoes: dict, par: tuple):
    chave, valor = par
    chave = str(chave).lower()
    valor = str(valor).lower()

    if chave in configuracoes:
        configuracoes[chave] = valor
        return f"Configuração '{chave}' atualizada para '{valor}' com sucesso!"
    
    return f"A configuração '{chave}' não existe! Não é possível atualizar uma configuração inexistente."


def deletar_configuracao(configuracoes: dict, chave):
    chave = str(chave).lower()

    if chave in configuracoes:
        del configuracoes[chave]
        return f"Configuração '{chave}' deletada com sucesso!"
    
    return "Configuração não encontrada!"


def visualizar_configuracoes(configuracoes: dict):
    if not configuracoes:
        return "Nenhuma configuração disponível."
    
    resultado = "Configurações Atuais do Usuário:\n"
    
    for chave, valor in configuracoes.items():
        resultado += f"{chave.capitalize()}: {valor}\n"
    
    return resultado