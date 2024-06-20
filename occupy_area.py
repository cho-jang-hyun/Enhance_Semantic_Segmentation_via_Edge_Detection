import cv2
import numpy as np
import os
import glob
from collections import Counter

# 디렉토리 경로
input1_dir = 'video_version3_samples/outputs'
input2_dir = 'video_version3_samples/contour_find'
output_dir = 'video_version3_samples/occupied_contour'

# 출력 디렉토리 생성
os.makedirs(output_dir, exist_ok=True)

# 파일 리스트 가져오기
original_files = glob.glob(os.path.join(input1_dir, '*.png'))
contour_files = glob.glob(os.path.join(input2_dir, '*.png'))

for original_file in original_files:
    # 파일 이름 추출
    filename = os.path.basename(original_file)
    
    # 같은 이름의 contour 파일 찾기
    contour_file = os.path.join(input2_dir, filename)
    if not os.path.exists(contour_file):
        continue
    
    # 이미지 읽기
    original_image = cv2.imread(original_file, cv2.IMREAD_COLOR)
    contour_image = cv2.imread(contour_file, cv2.IMREAD_COLOR)
    
    # 초록색 컨투어 영역 (BGR 포맷)
    green_color = (0, 255, 0)

    # 초록색 컨투어 찾기
    mask = cv2.inRange(contour_image, green_color, green_color)
    
    # 컨투어 찾기
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # 폐곡선 영역 내 마스크 생성
        mask = np.zeros_like(contour_image[:, :, 0])
        cv2.drawContours(mask, [contour], -1, 255, -1)
        
        # 원본 이미지에서 마스크 영역의 색상 추출
        pixels = original_image[mask == 255]
        
        # 가장 많이 나타나는 색상 찾기
        if len(pixels) == 0:
            continue
        most_common_color = Counter(map(tuple, pixels)).most_common(1)[0][0]
        
        # RGB 포맷 맞추기
        most_common_color_bgr = (int(most_common_color[0]), int(most_common_color[1]), int(most_common_color[2]))
        
        # 컨투어 영역을 가장 많이 나타나는 색상으로 채우기
        cv2.drawContours(original_image, [contour], -1, most_common_color_bgr, -1)
    
    # 수정된 이미지 저장
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, original_image)

print("Processed images have been saved.")
