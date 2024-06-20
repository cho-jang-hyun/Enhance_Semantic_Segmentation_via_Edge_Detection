import cv2
import os

# 디렉토리 경로 설정
input_dir = "video_version3_samples/filtered_edges"
output_dir = "video_version3_samples/contour_find"

# output 디렉토리가 존재하지 않으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 모든 이미지 파일에 대해 폐곡선(contour) 검출 수행
for filename in os.listdir(input_dir):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # 이미지 읽기
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # 폐곡선 검출
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # 원본 이미지를 BGR로 변환
        contour_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        
        # 폐곡선 그리기
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
        
        # 결과 저장
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, contour_image)

print("모든 이미지에 대해 폐곡선 검출을 완료했습니다.")
