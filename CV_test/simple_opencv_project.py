# simple_opencv_project.py
import cv2
import numpy as np
import os


def create_output_dir():
    """创建输出目录"""
    if not os.path.exists("output"):
        os.makedirs("output")
        print("创建输出目录: output/")
    return "output"


def save_image(image, filename):
    """保存图像"""
    output_dir = create_output_dir()
    filepath = os.path.join(output_dir, filename)
    cv2.imwrite(filepath, image)
    print(f"保存: {filepath}")
    return filepath


def main():
    print("OpenCV 小型图片项目")
    print("=" * 40)

    # 1. 创建基础图形图像
    print("\n1. 创建基础图形图像...")
    img1 = np.ones((400, 600, 3), dtype=np.uint8) * 255  # 白色背景

    # 绘制各种图形
    cv2.rectangle(img1, (50, 50), (200, 200), (0, 255, 0), -1)  # 绿色矩形
    cv2.circle(img1, (300, 150), 80, (255, 0, 0), -1)  # 蓝色圆形
    cv2.line(img1, (400, 50), (550, 200), (0, 0, 255), 5)  # 红色线条

    # 添加文字
    cv2.putText(img1, "OpenCV Demo", (200, 300),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.putText(img1, "Basic Shapes", (220, 350),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)

    save_image(img1, "basic_shapes.png")

    # 2. 创建渐变效果图像
    print("\n2. 创建渐变效果图像...")
    img2 = np.zeros((400, 600, 3), dtype=np.uint8)

    # 创建水平渐变
    for x in range(600):
        r = int(255 * x / 600)
        g = int(128 + 127 * np.sin(2 * np.pi * x / 300))
        b = 255 - r
        cv2.line(img2, (x, 0), (x, 200), (b, g, r), 1)

    # 创建径向渐变
    center_x, center_y = 300, 300
    for r in range(100, 0, -1):
        intensity = int(255 * r / 100)
        cv2.circle(img2, (center_x, center_y), r,
                   (intensity, intensity // 2, 255 - intensity), -1)

    cv2.putText(img2, "Gradient Effects", (180, 380),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    save_image(img2, "gradient_effects.png")

    # 3. 创建滤镜效果图像
    print("\n3. 创建滤镜效果图像...")
    # 使用img1作为基础应用滤镜
    img3 = img1.copy()

    # 转换为灰度
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # 应用阈值
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 转换为彩色并添加
    binary_colored = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    # 创建对比图像
    img3 = np.hstack([img1, binary_colored])

    cv2.putText(img3, "Original      vs      Binary Filter",
                (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    save_image(img3, "filter_comparison.png")

    # 4. 创建最终合成图像
    print("\n4. 创建最终合成图像...")
    final_img = np.ones((500, 800, 3), dtype=np.uint8) * 240

    # 添加标题
    cv2.putText(final_img, "OpenCV Art Collection", (150, 80),
                cv2.FONT_HERSHEY_COMPLEX, 1.8, (50, 50, 150), 3)

    # 添加说明
    cv2.putText(final_img, "Generated Images:", (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    images_info = [
        ("• Basic Shapes", "basic_shapes.png"),
        ("• Gradient Effects", "gradient_effects.png"),
        ("• Filter Comparison", "filter_comparison.png")
    ]

    y_start = 200
    for i, (name, filename) in enumerate(images_info):
        y = y_start + i * 50
        cv2.putText(final_img, name, (100, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2)

    # 添加装饰
    cv2.rectangle(final_img, (30, 30), (770, 470), (100, 100, 200), 3)

    # 底部信息
    cv2.putText(final_img, "All images saved to 'output/' directory",
                (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 2)

    save_image(final_img, "final_summary.png")

    print("\n" + "=" * 40)
    print("项目完成！")
    print("生成的文件：")
    for file in os.listdir("output"):
        if file.endswith(".png"):
            print(f"  - {file}")


if __name__ == "__main__":
    main()