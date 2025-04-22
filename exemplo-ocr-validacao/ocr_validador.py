import pytesseract
from PIL import Image

image_path = "exemplo-ocr-validacao/boletim_exemplo.png"
imagem = Image.open(image_path)
texto_extraido = pytesseract.image_to_string(imagem, lang="por")

print("🧾 Texto extraído da imagem:\n")
print(texto_extraido)

dados_esperados = {
    "plataforma": "Bet365",
    "evento": "Union Española vs. Fluminense",
    "valor": 37.21
}

erros = []

if dados_esperados["plataforma"].lower() not in texto_extraido.lower():
    erros.append("Plataforma não identificada corretamente.")

if dados_esperados["evento"].lower() not in texto_extraido.lower():
    erros.append("Evento não encontrado ou incorreto.")

if str(dados_esperados["valor"]) not in texto_extraido:
    erros.append("Valor apostado não encontrado.")

if not erros:
    print("✅ Validação concluída com sucesso. Todos os dados estão corretos.")
else:
    print("❌ Erros encontrados na validação:")
    for erro in erros:
        print(f" - {erro}")
