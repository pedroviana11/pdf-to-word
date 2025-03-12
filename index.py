from pdf2docx import Converter

# coloca o caminho dos arquivos aqui
pdf_path = "documento.pdf"
word_path = "documento.docx"

# codiguim pra converter
cv = Converter(pdf_path)
cv.convert(word_path, start=0, end=None)  # procura todas as páginas
cv.close()

print(f"Conversão concluída! Arquivo salvo como {word_path}")
