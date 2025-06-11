#!/usr/bin/env python3
"""
Calculadora Python Avançada - DZX-CORE
Calculadora completa com operações matemáticas e interface intuitiva
"""

import math
import sys

class CalculadoraAvancada:
    """Calculadora com operações matemáticas completas"""
    
    def __init__(self):
        self.historico = []
        print("🧮 Calculadora Python Avançada - DZX-CORE")
        print("=" * 50)
    
    def somar(self, a: float, b: float) -> float:
        """Soma dois números"""
        resultado = a + b
        self._salvar_historico(f"{a} + {b} = {resultado}")
        return resultado
    
    def subtrair(self, a: float, b: float) -> float:
        """Subtrai dois números"""
        resultado = a - b
        self._salvar_historico(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a: float, b: float) -> float:
        """Multiplica dois números"""
        resultado = a * b
        self._salvar_historico(f"{a} × {b} = {resultado}")
        return resultado
    
    def dividir(self, a: float, b: float) -> float:
        """Divide dois números com proteção contra divisão por zero"""
        if b == 0:
            raise ValueError("❌ Erro: Divisão por zero não é permitida!")
        resultado = a / b
        self._salvar_historico(f"{a} ÷ {b} = {resultado}")
        return resultado
    
    def potencia(self, base: float, expoente: float) -> float:
        """Calcula potência"""
        resultado = base ** expoente
        self._salvar_historico(f"{base}^{expoente} = {resultado}")
        return resultado
    
    def raiz_quadrada(self, numero: float) -> float:
        """Calcula raiz quadrada"""
        if numero < 0:
            raise ValueError("❌ Erro: Raiz quadrada de número negativo!")
        resultado = math.sqrt(numero)
        self._salvar_historico(f"√{numero} = {resultado}")
        return resultado
    
    def porcentagem(self, valor: float, percentual: float) -> float:
        """Calcula porcentagem"""
        resultado = (valor * percentual) / 100
        self._salvar_historico(f"{percentual}% de {valor} = {resultado}")
        return resultado
    
    def _salvar_historico(self, operacao: str):
        """Salva operação no histórico"""
        self.historico.append(operacao)
        if len(self.historico) > 10:  # Manter apenas últimas 10 operações
            self.historico.pop(0)
    
    def mostrar_historico(self):
        """Mostra histórico de operações"""
        if not self.historico:
            print("📝 Histórico vazio")
            return
        
        print("\n📝 Histórico de Operações:")
        print("-" * 30)
        for i, operacao in enumerate(self.historico, 1):
            print(f"{i:2d}. {operacao}")
        print("-" * 30)
    
    def menu_principal(self):
        """Interface principal da calculadora"""
        operacoes = {
            '1': ('Somar', self.somar),
            '2': ('Subtrair', self.subtrair),
            '3': ('Multiplicar', self.multiplicar),
            '4': ('Dividir', self.dividir),
            '5': ('Potência', self.potencia),
            '6': ('Raiz Quadrada', self.raiz_quadrada),
            '7': ('Porcentagem', self.porcentagem),
            '8': ('Histórico', self.mostrar_historico),
            '0': ('Sair', None)
        }
        
        while True:
            print("\n🧮 Menu Principal:")
            for key, (nome, _) in operacoes.items():
                print(f"  {key}. {nome}")
            
            try:
                opcao = input("\n➤ Escolha uma opção (0-8): ").strip()
                
                if opcao == '0':
                    print("\n👋 Obrigado por usar a Calculadora DZX-CORE!")
                    break
                
                if opcao == '8':
                    self.mostrar_historico()
                    continue
                
                if opcao not in operacoes or opcao in ['0', '8']:
                    print("❌ Opção inválida! Tente novamente.")
                    continue
                
                nome, funcao = operacoes[opcao]
                
                if opcao == '6':  # Raiz quadrada - apenas um número
                    numero = float(input("Digite o número: "))
                    resultado = funcao(numero)
                    print(f"✅ Resultado: √{numero} = {resultado:.4f}")
                
                elif opcao == '7':  # Porcentagem
                    valor = float(input("Digite o valor: "))
                    percentual = float(input("Digite o percentual: "))
                    resultado = funcao(valor, percentual)
                    print(f"✅ Resultado: {percentual}% de {valor} = {resultado:.4f}")
                
                else:  # Operações com dois números
                    a = float(input("Digite o primeiro número: "))
                    b = float(input("Digite o segundo número: "))
                    resultado = funcao(a, b)
                    print(f"✅ Resultado: {resultado:.4f}")
                
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("❌ Erro: Por favor, digite apenas números válidos!")
                else:
                    print(f"❌ {e}")
            except KeyboardInterrupt:
                print("\n\n👋 Calculadora encerrada pelo usuário.")
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")

def main():
    """Função principal"""
    calc = CalculadoraAvancada()
    calc.menu_principal()

if __name__ == "__main__":
    main()
