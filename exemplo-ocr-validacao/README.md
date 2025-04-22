
# 🧾 Exemplo: Validação de Boletim com OCR + Python

Este script demonstra como usar OCR para extrair dados de uma imagem de boletim de aposta e validar as informações visualmente.

---

## 🔍 O que o script faz

- Lê a imagem `boletim_exemplo.png`
- Extrai o texto com Tesseract OCR
- Compara os dados extraídos com:
  - Plataforma: **Bet365**
  - Evento: **Union Española vs. Fluminense**
  - Valor: **R$ 37,21**
- Exibe o resultado da validação

---

## ✅ Resultado da Execução (Exemplo real)

```
🧾 Texto extraído da imagem:

Bet365  
Union Española vs. Fluminense  
R$ 37.21

🔍 Iniciando validação simples dos dados extraídos...
✅ Validação concluída com sucesso. Todos os dados estão corretos.
```

---

## 🧠 Requisitos (para testar localmente)

- Python 3.x instalado
- Biblioteca `pytesseract`
- Biblioteca `Pillow`
- Tesseract OCR instalado no seu sistema  
  👉 Windows: https://github.com/UB-Mannheim/tesseract/wiki

---

## ▶️ Como executar (opcional)

Se quiser rodar este exemplo localmente:

```bash
pip install pytesseract pillow
```

Execute:

```bash
python ocr_validador.py
```

---

## 🗂 Estrutura da pasta

```
📁 exemplo-ocr-validacao
├── ocr_validador.py
├── boletim_exemplo.png
└── README.md
```

---

Autor: [Luan Nascimento Faria](https://www.linkedin.com/in/luan-nascimento-faria-81370497/)
📧 equipeeletrofusion@gmail.com
