import os
import cv2
import numpy as np

# 현재 디렉토리와 overlayed_outputs 디렉토리 설정
current_directory = os.getcwd()+'/original_samples'
overlay_output_directory = os.path.join(current_directory, 'overlayed_outputs')

# overlayed_outputs 디렉토리가 존재하지 않으면 생성
if not os.path.exists(overlay_output_directory):
    os.makedirs(overlay_output_directory)

# 이미지 파일 확장자 리스트
image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']

# 현재 디렉토리에 있는 파일 리스트
files = os.listdir(current_directory)

# 이미지 파일 필터링
image_files = [file for file in files if any(file.lower().endswith(ext) for ext in image_extensions)]

# 각 이미지 파일에 대해 Canny Edge Detection 수행하고 결과를 원본 이미지에 겹침
for image_file in image_files:
    # 이미지 파일 경로
    image_path = os.path.join(current_directory, image_file)
    
    # 이미지 읽기
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"이미지 파일을 읽을 수 없습니다: {image_file}")
        continue
    
    # 회색조 이미지로 변환
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Canny Edge Detection 수행
    edges = cv2.Canny(gray_image, 50, 100)
    
    # Edge를 BGR 이미지로 변환 (3채널)
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    # 원본 이미지와 Edge 이미지를 겹침
    overlayed_image = cv2.addWeighted(image, 0.8, edges_colored, 0.2, 0)
    
    # 결과 이미지 파일 경로
    overlay_output_path = os.path.join(overlay_output_directory, image_file)
    
    # 결과 이미지 저장
    cv2.imwrite(overlay_output_path, overlayed_image)
    
    print(f"Overlayed 결과를 저장했습니다: {overlay_output_path}")

print("모든 이미지에 대해 Canny Edge Detection 결과를 겹치는 작업을 완료했습니다.")
