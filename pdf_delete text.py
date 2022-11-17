import fitz

TOTAL_FILES = 3
# search and delete text
TEXT = 'Tekla structures'

for i in range(TOTAL_FILES):
    file_name = f"{i}.pdf"
    doc = fitz.open(file_name)
    page = doc.load_page(0)
    rl = page.search_for(TEXT, quads = True)
    page.add_redact_annot(rl[0])
    page.apply_redactions()
    out_file_name = f"final_{i}.pdf"
    print(f'File {file_name} complete')
    doc.save(f'./final/{out_file_name}')
    doc.close()