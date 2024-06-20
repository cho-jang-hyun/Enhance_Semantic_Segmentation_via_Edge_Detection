import cv2
import os
import numpy as np

# 디렉토리 경로 설정
input_dir = "video_version3_samples/removed_edges"
output_dir = "video_version3_samples/filtered_edges"

# output 디렉토리가 존재하지 않으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 모든 이미지 파일에 대해 dilate 연산 수행
for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        # 이미지 읽기
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        
        # opening 연산
        # kernel = np.ones((3,3), np.uint8)
        # opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

        # dilate 연산
        dilated_image1 = cv2.dilate(image, kernel, iterations = 2)
        #dilated_image2 = cv2.dilate(dilated_image1, kernel)

        # erosion 연산
        #eroded_image1 = cv2.erode(dilated_image2, kernel)
        #eroded_image2 = cv2.erode(eroded_image1, kernel)

        # 결과 저장
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, dilated_image1)

print("모든 이미지에 대해 filter 연산을 완료했습니다.")
