import qrcode
from PIL import Image

def generate_qrcode(url, output_path):
    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # QR 코드 이미지 생성
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # 이미지 저장
    qr_img.save(output_path)

if __name__ == "__main__":
    # 사용자로부터 URL 입력 받기
    url = input("Enter the URL: ")

    # QR 코드 생성 및 저장
    output_path = "qrcode.png"  # 저장할 파일 경로 및 이름
    generate_qrcode(url, output_path)
    print(f"QR code for '{url}' has been generated and saved as '{output_path}'.")
