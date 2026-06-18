# Sistema de Controle de Elevador com 2 elevadores
# - 4 andares + 2 subsolos (andares: -2, -1, 0, 1, 2, 3, 4)
# - Usuário informa andar desejado
# - Sistema escolhe o elevador de forma inteligente:
#   * Elevador mais próximo do andar desejado
#   * Se ambos estão no mesmo andar, escolhe o com menos pessoas
# - Menu interativo para gerenciar os elevadores

import random

class Elevador:
    def __init__(self, numero: int, capacidade: int = 8, andar_minimo: int = -2, andar_maximo: int = 4):
        self.numero = numero
        self.capacidade = capacidade
        self.andar_minimo = andar_minimo
        self.andar_maximo = andar_maximo
        # Andar inicial aleatório
        self.andar_atual = random.randint(self.andar_minimo, self.andar_maximo)
        self.pessoas_no_elevador = 0

    def entrar(self):
        """Adiciona uma pessoa ao elevador"""
        if self.pessoas_no_elevador < self.capacidade:
            self.pessoas_no_elevador += 1
            print(f"✓ Uma pessoa entrou no elevador {self.numero}.")
            return True
        else:
            print(f"❌ O elevador {self.numero} está cheio. Não é possível entrar.")
            return False

    def sair(self):
        """Remove uma pessoa do elevador"""
        if self.pessoas_no_elevador > 0:
            self.pessoas_no_elevador -= 1
            print(f"✓ Uma pessoa saiu do elevador {self.numero}.")
            return True
        else:
            print(f"❌ O elevador {self.numero} está vazio. Não é possível sair.")
            return False

    def subir(self):
        """Move o elevador um andar para cima"""
        if self.andar_atual < self.andar_maximo:
            self.andar_atual += 1
            print(f"   ⬆️  Elevador {self.numero} subiu para o andar {self._formatar_andar(self.andar_atual)}")
            return True
        return False

    def descer(self):
        """Move o elevador um andar para baixo"""
        if self.andar_atual > self.andar_minimo:
            self.andar_atual -= 1
            print(f"   ⬇️  Elevador {self.numero} desceu para o andar {self._formatar_andar(self.andar_atual)}")
            return True
        return False

    def _formatar_andar(self, andar: int) -> str:
        """Formata o número do andar para exibição (Subsolo/Térreo/Andar)"""
        if andar < 0:
            return f"Subsolo {abs(andar)}"
        elif andar == 0:
            return "Térreo"
        else:
            return f"{andar}"

    def ir_para_andar(self, andar_destino: int):
        """Move o elevador para o andar destino"""
        if andar_destino < self.andar_minimo or andar_destino > self.andar_maximo:
            return False
        
        if andar_destino == self.andar_atual:
            print(f"✓ Elevador {self.numero} já está no andar {self._formatar_andar(self.andar_atual)}.")
            return True
        
        print(f"\n🛗 Elevador {self.numero} movendo para o andar {self._formatar_andar(andar_destino)}...")
        
        while self.andar_atual < andar_destino:
            self.subir()
        
        while self.andar_atual > andar_destino:
            self.descer()
        
        print(f"✓ Elevador {self.numero} chegou ao andar {self._formatar_andar(self.andar_atual)}!\n")
        return True

    def obter_distancia(self, andar: int) -> int:
        """Retorna a distância até o andar especificado"""
        return abs(self.andar_atual - andar)

    def mostrar_status(self):
        """Exibe o status do elevador"""
        andar_formatado = self._formatar_andar(self.andar_atual)
        ocupacao_percentual = (self.pessoas_no_elevador / self.capacidade) * 100
        barra_ocupacao = "█" * int(ocupacao_percentual / 10) + "░" * (10 - int(ocupacao_percentual / 10))
        
        print(f"Elevador {self.numero}: Andar {andar_formatado} | Pessoas: {self.pessoas_no_elevador}/{self.capacidade} [{barra_ocupacao}]")


class SistemaElevadores:
    def __init__(self):
        self.elevadores = [
            Elevador(1),
            Elevador(2)
        ]
        self.andar_minimo = -2
        self.andar_maximo = 4

    def _formatar_andar(self, andar: int) -> str:
        """Formata o número do andar para exibição"""
        if andar < 0:
            return f"Subsolo {abs(andar)}"
        elif andar == 0:
            return "Térreo"
        else:
            return f"{andar}"

    def escolher_elevador(self, andar_destino: int) -> Elevador:
        """
        Escolhe o elevador de forma inteligente:
        - Elevador mais próximo do andar desejado
        - Se ambos estão no mesmo andar, escolhe o com menos pessoas
        """
        distancias = [elev.obter_distancia(andar_destino) for elev in self.elevadores]
        
        if distancias[0] < distancias[1]:
            return self.elevadores[0]
        elif distancias[1] < distancias[0]:
            return self.elevadores[1]
        else:  # Mesma distância
            if self.elevadores[0].pessoas_no_elevador <= self.elevadores[1].pessoas_no_elevador:
                return self.elevadores[0]
            else:
                return self.elevadores[1]

    def chamar_elevador(self, andar_destino: int):
        """Chama o elevador mais apropriado para atender o andar"""
        if andar_destino < self.andar_minimo or andar_destino > self.andar_maximo:
            print(f"❌ Erro: Andar {andar_destino} não existe!")
            print(f"   Andares disponíveis: Subsolo 2 até Andar 4")
            return
        
        elevador = self.escolher_elevador(andar_destino)
        print(f"\n📍 Chamando o elevador {elevador.numero} para o andar {self._formatar_andar(andar_destino)}...")
        elevador.ir_para_andar(andar_destino)

    def mostrar_status_sistema(self):
        """Exibe o status de ambos os elevadores"""
        print(f"\n{'='*60}")
        print("📊 STATUS DO SISTEMA DE ELEVADORES")
        print('='*60)
        for elevador in self.elevadores:
            elevador.mostrar_status()
        print('='*60 + "\n")


def menu_principal():
    """Menu interativo do sistema de elevadores"""
    sistema = SistemaElevadores()
    
    print("\n" + "="*60)
    print("🏢 SISTEMA DE CONTROLE DE ELEVADORES 🏢".center(60))
    print("="*60)
    print("✓ 2 Elevadores disponíveis")
    print("✓ Andares: Subsolo 2, Subsolo 1, Térreo, 1, 2, 3, 4")
    print("✓ Capacidade por elevador: 8 pessoas")
    print("="*60)
    
    while True:
        sistema.mostrar_status_sistema()
        
        print("\n📋 MENU DE OPÇÕES:")
        print("1. Chamar elevador para um andar")
        print("2. Entrar no elevador 1")
        print("3. Entrar no elevador 2")
        print("4. Sair do elevador 1")
        print("5. Sair do elevador 2")
        print("6. Ver status dos elevadores")
        print("7. Sair do programa")
        print("-" * 60)
        
        opcao = input("Escolha uma opção (1-7): ").strip()
        
        if opcao == "1":
            try:
                print("\nAndares disponíveis:")
                print("  -2: Subsolo 2")
                print("  -1: Subsolo 1")
                print("   0: Térreo")
                print("   1: Andar 1")
                print("   2: Andar 2")
                print("   3: Andar 3")
                print("   4: Andar 4")
                andar = int(input("\nDigite o número do andar desejado: "))
                sistema.chamar_elevador(andar)
            except ValueError:
                print("❌ Entrada inválida! Digite um número inteiro.")
        
        elif opcao == "2":
            sistema.elevadores[0].entrar()
        
        elif opcao == "3":
            sistema.elevadores[1].entrar()
        
        elif opcao == "4":
            sistema.elevadores[0].sair()
        
        elif opcao == "5":
            sistema.elevadores[1].sair()
        
        elif opcao == "6":
            sistema.mostrar_status_sistema()
        
        elif opcao == "7":
            print("\n👋 Obrigado por usar o sistema! Até logo!\n")
            break
        
        else:
            print("❌ Opção inválida! Escolha uma opção de 1 a 7.")
        
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    menu_principal()


