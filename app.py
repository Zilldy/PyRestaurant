from modelos.restaurante import Restaurante
from modelos.cardapio.Bebida import Bebida
from modelos.cardapio.Prato import Prato

# restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_pao = Prato('Paozinho', 2.0, 'Quentinho e Fresco')

def main():
    print(bebida_suco)
    print(prato_pao)

if __name__ == '__main__':
    main()