def best_fit(tamanho_ram, processos):
    blocos_livres = [[0, tamanho_ram]]
    
    alocados_ram = {} 
    alocados_virtual = []

    print("--- Iniciando Simulação de Alocação Best-Fit ---")
    print(f"Memória RAM Total: {tamanho_ram} KB\n")

    for nome_processo, tamanho_processo in processos.items():
        print(f"-> Tentando alocar {nome_processo} ({tamanho_processo} KB)...")
        
        melhor_bloco = None
        indice_melhor_bloco = -1

        for i, bloco in enumerate(blocos_livres):
            if bloco[1] >= tamanho_processo:
                if melhor_bloco is None or bloco[1] < melhor_bloco[1]:
                    melhor_bloco = bloco
                    indice_melhor_bloco = i
        
        if melhor_bloco is not None:
            endereco_alocacao = melhor_bloco[0]
            alocados_ram[nome_processo] = [endereco_alocacao, tamanho_processo]
            print(f"   [SUCESSO] {nome_processo} alocado na RAM no endereço {endereco_alocacao}.")

            tamanho_restante = melhor_bloco[1] - tamanho_processo
            
            if tamanho_restante == 0:
                blocos_livres.pop(indice_melhor_bloco)
            else:
                blocos_livres[indice_melhor_bloco][0] += tamanho_processo
                blocos_livres[indice_melhor_bloco][1] = tamanho_restante
        
        else:
            alocados_virtual.append(nome_processo)
            print(f"   [FALHA] Não há espaço suficiente na RAM. {nome_processo} enviado para memória virtual.")
            
        print(f"   Blocos Livres Atuais: {blocos_livres}\n")

    return alocados_ram, blocos_livres, alocados_virtual

def imprimir_relatorio_final(tamanho_ram, alocados_ram, blocos_livres, alocados_virtual):
    print("\n--- Relatório Final do Estado da Memória RAM ---")
    print("-" * 50)
    print(f"{'Endereço (KB)':<15} | {'Tamanho (KB)':<15} | {'Conteúdo':<15}")
    print("-" * 50)

    mapa_memoria = []
    for processo, info in alocados_ram.items():
        mapa_memoria.append({'endereco': info[0], 'tamanho': info[1], 'conteudo': processo})
    for bloco in blocos_livres:
        mapa_memoria.append({'endereco': bloco[0], 'tamanho': bloco[1], 'conteudo': '**Livre**'})
    
    mapa_memoria.sort(key=lambda x: x['endereco'])

    total_ocupado = 0
    for item in mapa_memoria:
        print(f"{item['endereco']:<15} | {item['tamanho']:<15} | {item['conteudo']:<15}")
        if item['conteudo'] != '**Livre**':
            total_ocupado += item['tamanho']
    
    total_livre = tamanho_ram - total_ocupado
    
    print("-" * 50)
    print(f"Memória Ocupada: {total_ocupado} KB")
    print(f"Memória Livre Total: {total_livre} KB (Fragmentação Externa)")
    print("\nProcessos em Memória Virtual (Disco):")
    if alocados_virtual:
        for processo in alocados_virtual:
            print(f"- {processo}")
    else:
        print("Nenhum.")
    print("-" * 50)

RAM_SIZE = 64 
PROCESSOS_INICIAIS = {
    'P1': 20,
    'P2': 15,
    'P3': 25,
    'P4': 10,
    'P5': 18
}

if __name__ == "__main__":
    alocados, livres, virtuais = best_fit(RAM_SIZE, PROCESSOS_INICIAIS)
    imprimir_relatorio_final(RAM_SIZE, alocados, livres, virtuais)