import os
from PyPDF2 import PdfReader


class Leitor_PDF:
    def __init__(self, caminho):
        self.caminho = caminho
        self.resultados = []

    def lerPDFs(self):
        for i in os.listdir(self.caminho):
            if i.endswith('.pdf'):
                caminho_completo = os.path.join(self.caminho, i)
                print(f"Reading of archive: {i}")

                with open(caminho_completo, 'rb') as arquivo_pdf:
                    leitor_pdf = PdfReader(arquivo_pdf)
                    num_paginas = len(leitor_pdf.pages)

                    texto_completo = ""
                    for pagina in leitor_pdf.pages:
                        texto_completo += pagina.extract_text()

                    titulo = leitor_pdf.metadata.title if leitor_pdf.metadata else None

                    self.resultados.append({
                        'nome_arquivo': i,
                        'titulo': titulo,
                        'conteudo': texto_completo
                    })

    def buscarPDF(self):
        key_user = input("Enter the title or keyword to be searched: ")
        encontrados = []

        for arquivo_info in self.resultados:
            if arquivo_info['titulo'] is not None and key_user.lower() in arquivo_info['titulo'].lower():
                encontrados.append(arquivo_info)

        return encontrados


def main():
    print('''*******************
    *  Reader of PDF  *
    *******************''')

    pasta = input('Enter the path of the folder where you want to search for your PDFs:\n')
    arquivos_pdf = Leitor_PDF(pasta)

    while True:
        print('''
            \nWhat do you want to do?
            1. Search for a specific word or title
            2. Close the program.''')
        e = input('')
        if e == '1':
            arquivos_pdf.lerPDFs()
            resultado = arquivos_pdf.buscarPDF()
            if resultado:
                for i, arquivo in enumerate(resultado, start=1):
                    print(f"{i}. Archive Found: {arquivo['nome_arquivo']}")
                    print(f" Title: {arquivo['titulo']}")
                abrirCont = input("Enter the file number you want to search for (or press Enter to return to the main menu): ")
                if abrirCont.isdigit():
                    arquivo_escolhido = resultado[int(abrirCont) - 1]
                    print(f"\nContent of {arquivo_escolhido['nome_arquivo']}:\n")
                    print(arquivo_escolhido['conteudo'])
        elif e == '2':
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
