# PDF para Word - Conversor Automático

Este projeto converte arquivos **PDF** em **Word (DOCX)** de forma inteligente. Ele detecta automaticamente se o PDF contém texto selecionável ou se é um documento escaneado e aplica o método mais adequado para a conversão.

## Funcionalidades
✅ **Preserva a formatação original** se o PDF tiver texto selecionável.
✅ **Usa OCR** para extrair texto se o PDF for um escaneamento.
✅ **Gera um documento Word** com o texto extraído.

## Tecnologias utilizadas
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) - Para ler PDFs e verificar se possuem texto.
- [pdf2docx](https://github.com/finloop/pdf2docx) - Para converter PDFs que já contêm texto em documentos Word.
- [pdf2image](https://github.com/Belval/pdf2image) - Para converter PDFs escaneados em imagens.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Para reconhecer texto em PDFs escaneados.
- [python-docx](https://python-docx.readthedocs.io/en/latest/) - Para gerar documentos Word.

## Instalação
Antes de rodar o código, instale as dependências necessárias:

```bash
pip install pymupdf pdf2image pytesseract python-docx pdf2docx
```

**OBS:** Certifique-se de que o Tesseract OCR está instalado no seu sistema. No Linux, pode ser instalado com:
```bash
sudo apt install tesseract-ocr
```

## Como usar
1. Coloque o arquivo **PDF** na pasta do projeto.
2. Edite o script e defina os caminhos dos arquivos:
   ```python
   pdf_path = "documento.pdf"
   word_path = "documento.docx"
   ```
3. Execute o script:
   ```bash
   python script.py
   ```
4. O arquivo Word convertido será salvo no mesmo diretório.

## Funcionamento do Script
1. **Verifica se o PDF tem texto selecionável** usando PyMuPDF.
2. **Se tiver texto**, usa `pdf2docx` para manter a formatação original.
3. **Se for um PDF escaneado**, converte as páginas em imagens e usa OCR (Tesseract) para extrair o texto.
4. **Salva o texto extraído** em um arquivo Word.

## Exemplo de Saída
```
Conversão concluída! Arquivo salvo como documento.docx
```

## Contribuição
Sinta-se à vontade para sugerir melhorias ou relatar problemas!

## Licença
Este projeto está sob a licença MIT.

