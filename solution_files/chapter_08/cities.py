def describle_city(cidade, país='brasil'):
    """Exibe uma simples frase."""
    print(f"\n{cidade.title()} fica no {país.title()}")

describle_city('sao paulo')
describle_city('rio de janeiro')
describle_city(cidade='valparaíso', país='chile')