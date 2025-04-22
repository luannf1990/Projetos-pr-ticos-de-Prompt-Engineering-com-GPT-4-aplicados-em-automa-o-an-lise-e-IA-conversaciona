# 🧾 Exemplo: Validação de Boletim com OCR + Regras de Negócio

Este exemplo mostra como usar **OCR (Reconhecimento Óptico de Caracteres)** com **Python + Tesseract** para extrair informações de uma imagem de boletim de apostas e validar se os dados extraídos estão corretos.

---

## 🔍 O que o script faz?

1. **Lê uma imagem (`boletim_exemplo.png`)** usando OCR.
2. **Extrai o texto bruto** da imagem.
3. **Compara os dados extraídos** com os valores esperados:
   - Nome da plataforma (ex: `"Bet365"`)
   - Nome do evento (ex: `"Union Española vs. Fluminense"`)
   - Valor apostado (ex: `"37.21"`)
4. Informa se os dados estão corretos ou se há erros.

---

## 🧠 Tecnologias usadas

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Pillow (PIL) para manipulação de imagens

---

## ▶️ Como executar

1. Instale as dependências:

```bash
pip install pytesseract pillow
