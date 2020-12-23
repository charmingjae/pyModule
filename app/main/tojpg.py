from pdf2image import convert_from_path
import glob


def convertPDF():
    # pdf 경로 설정
    path = r'./app/static/temp'
    pdf_dir = glob.glob(path+"/*")
    print(pdf_dir)
    img_dir = r'./app/static/img/'

    # to jpg
    for pdf_ in pdf_dir:
        pages = convert_from_path(pdf_, dpi=500)
        for i, page in enumerate(pages):
            page.save(
                f'{img_dir+pdf_[len(path):-4]}_page{i+1:0>2d}.jpg', 'JPEG')
            print(f'{pdf_[len(path):-4]}_page{i+1:0>2d}.jpg saved...')
