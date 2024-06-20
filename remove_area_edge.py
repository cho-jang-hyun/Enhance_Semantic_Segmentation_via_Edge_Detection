import cv2
import numpy as np
import os
import glob

# 디렉토리 경로
edge_dir = 'video_version3_samples/edge_outputs'
segmentation_dir = 'video_version3_samples/outputs'
output_dir = 'video_version3_samples/'+'removed_edges'

# 출력 디렉토리 생성
os.makedirs(output_dir, exist_ok=True)

# 특정 색상 (BGR 포맷)
vegetation_color = (35, 142, 107)
building_color = (70, 70, 70)

# Edge 이미지와 segmentation 이미지를 읽고 처리
edge_files = glob.glob(os.path.join(edge_dir, '*.png'))
segmentation_files = glob.glob(os.path.join(segmentation_dir, '*.png'))

for edge_file in edge_files:
    # 파일 이름 추출
    filename = os.path.basename(edge_file)
    
    # 같은 이름의 segmentation 파일 찾기
    seg_file = os.path.join(segmentation_dir, filename)
    if not os.path.exists(seg_file):
        continue
    
    # 이미지 읽기
    edge_image = cv2.imread(edge_file, cv2.IMREAD_GRAYSCALE)
    seg_image = cv2.imread(seg_file, cv2.IMREAD_COLOR)
    
    # 타겟 색상 영역 찾기
    mask_vegetation = cv2.inRange(seg_image, vegetation_color, vegetation_color)
    mask_building = cv2.inRange(seg_image, building_color, building_color)

    # 타겟 색상 영역과 겹치는 edge 제거
    edge_image[mask_vegetation == 255] = 0
    edge_image[mask_building == 255] = 0
    
    # 수정된 edge 이미지 저장
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, edge_image)

print("Edge images have been modified and saved.")
