from PyPDF2 import PdfReader, PdfWriter, PageObject

files = [
    ["path to the directory which contains the pdf file","PDF title (without suffix: .pdf)"],
    ]

def split_pdf(input_pdf, output_pdf):
    # PDFファイルを読み込む
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 各ページを処理
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        
        # 元のページサイズを取得
        original_width = page.mediabox.width
        original_height = page.mediabox.height
        
        # 左半分のページを作成
        left_page = PageObject.create_blank_page(width=original_width / 2, height=original_height)
        left_page.mediabox.upper_right = (original_width / 2, original_height)
        left_page.merge_page(page)
        writer.add_page(left_page)

        # 右半分のページを作成
        right_page = PageObject.create_blank_page(width=original_width / 2, height=original_height)
        right_page.mediabox.upper_left = (original_width / 2, 0)
        right_page.mediabox.upper_right = (original_width, original_height)
        right_page.merge_page(page)
        writer.add_page(right_page)

    # 新しいPDFファイルとして出力
    with open(output_pdf, 'wb') as f:
        writer.write(f)
for file in files:
    split_pdf(f'{file[0]}/{file[1]}.pdf',f'{file[0]}/{file[1]}_split.pdf')
