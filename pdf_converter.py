from pathlib import Path
from docling.document_converter import DocumentConverter

def convert_pdf_txt_only(pdf_path, output_dir="output"):
    """Converter PDF para TXT apenas"""
    # Converter PDF
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    
    # Criar pasta de saída
    Path(output_dir).mkdir(exist_ok=True)
    filename = Path(pdf_path).stem
    
    # Salvar APENAS TXT
    txt_file = f"{output_dir}/{filename}.txt"
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(result.document.export_to_text())
    
    print(f"✅ Convertido: {txt_file}")
    return txt_file

# USO: Altere o caminho abaixo
if __name__ == "__main__":
    pdf_path = "habitos-atomicos-by-james-clear-z-liborg.pdf"  # ← ALTERE AQUI para seu livro
    try:
        txt_file = convert_pdf_txt_only(pdf_path)
        print(f"🎉 SUCESSO! Arquivo criado:")
        print(f"📄 TXT: {txt_file}")
    except Exception as e:
        print(f"❌ ERRO: {e}")