from PyPDF2 import PdfReader, PdfWriter, PageObject

files = [
    ["/Users/osamukigoshi/Library/Mobile Documents/com~apple~CloudDocs/Downloads", "0919_German_Handout"],
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

        # 左上 (Top-left)
        page_left_bottom = page.cropbox
        page_left_bottom.lower_left = (0, 0)
        page_left_bottom.upper_right = (original_width / 2, original_height / 2)
        writer.add_page(page)
        
        # 右上 (Top-right)
        page_left_top = page.cropbox
        page_left_top.lower_left = (0, original_height / 2)
        page_left_top.upper_right = (original_width / 2, original_height)
        writer.add_page(page)

        # 左下 (Bottom-left)
        page_right_bottom = page.cropbox
        page_right_bottom.lower_left = (original_width / 2, 0)
        page_right_bottom.upper_right = (original_width, original_height / 2)
        writer.add_page(page)

        # 右下 (Bottom-right)
        page_right_top = page.cropbox
        page_right_top.lower_left = (original_width / 2, original_height / 2)
        page_right_top.upper_right = (original_width, original_height)
        writer.add_page(page)

    # 新しいPDFファイルとして出力
    with open(output_pdf, 'wb') as f:
        writer.write(f)

# ファイルを分割
for file in files:
    split_pdf(f'{file[0]}/{file[1]}.pdf', f'{file[0]}/{file[1]}_split.pdf')
