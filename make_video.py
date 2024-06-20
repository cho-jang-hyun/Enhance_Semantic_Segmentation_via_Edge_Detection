import os
import cv2

def png_to_mp4(png_dir, output_video):
    # 정렬된 png 파일 목록 가져오기
    png_files = sorted([f for f in os.listdir(png_dir) if f.endswith('.png')])

    # 첫 번째 PNG 파일을 기준으로 프레임 크기 가져오기
    first_file = os.path.join(png_dir, png_files[0])
    frame = cv2.imread(first_file)
    height, width, layers = frame.shape

    # VideoWriter 객체 초기화
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 코덱 설정 (H.264 코덱을 사용할 경우 'mp4v' 사용)
    fps = 30.0  # 초당 프레임 수
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # 각 프레임을 동영상에 추가
    for png_file in png_files:
        image_path = os.path.join(png_dir, png_file)
        frame = cv2.imread(image_path)
        video.write(frame)

    # 마지막으로 VideoWriter 객체 해제
    video.release()

    print(f'동영상 파일 {output_video} 생성 완료.')

# 사용 예시:
if __name__ == "__main__":
    input_directory = 'samples/outputs'
    output_video_file = 'output.mp4'

    png_to_mp4(input_directory, output_video_file)
