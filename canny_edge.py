import os
import cv2

# 현재 디렉토리와 edge_outputs 디렉토리 설정
current_directory = os.getcwd()+'/video_version3_samples'
output_directory = os.path.join(current_directory, 'edge_outputs')

# edge_outputs 디렉토리가 존재하지 않으면 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 이미지 파일 확장자 리스트
image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']

# 현재 디렉토리에 있는 파일 리스트
files = os.listdir(current_directory)

# 이미지 파일 필터링
image_files = [file for file in files if any(file.lower().endswith(ext) for ext in image_extensions)]

# 각 이미지 파일에 대해 Canny Edge Detection 수행
for image_file in image_files:
    # 이미지 파일 경로
    image_path = os.path.join(current_directory, image_file)
    
    # 이미지 읽기
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print(f"이미지 파일을 읽을 수 없습니다: {image_file}")
        continue
    
    # 이미지 equalization
    equalized_image = cv2.equalizeHist(image)

    # 이미지 가우시안 블러
    blur_img  = cv2.GaussianBlur(equalized_image, (5, 5), 0, 0)

    # Canny Edge Detection 수행
    edges = cv2.Canny(blur_img, 100, 200)
    
    # 결과 이미지 파일 경로
    output_path = os.path.join(output_directory, image_file)
    
    # 결과 이미지 저장
    cv2.imwrite(output_path, edges)
    
    print(f"Edge detection 결과를 저장했습니다: {output_path}")

print("모든 이미지에 대해 Canny Edge Detection을 완료했습니다.")
