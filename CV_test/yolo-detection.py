import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO # 直接调用YOLO 模型
                            # YOLO v1 - v13, v26


# github主页 https://github.com/ultralytics/ultralytics
# yolo系列文档 https://docs.ultralytics.com/#where-to-start


model = YOLO('yolo11m.pt')

# 初始化摄像头 ID = 0 代表默认摄像头
# cap = cv2.VideoCapture(0)
# 初始化视频 文件
path = r'F:\足球\9158727437010.mp4'
cap = cv2.VideoCapture(path)

# 设置摄像头参数以优化实时性能

# 将内部缓冲队列大小设置为 1，避免缓存帧数过多
cap.set(cv2.CAP_PROP_BUFFERSIZE , 1)

# 请求每秒处理30帧图像
cap.set(cv2.CAP_PROP_FPS, 30)

# 初始化帧计数器（用于保存图像时的命名）
frame_id = 0

# 主循环开启，持续从摄像头中获取图像并进行推理
while True:
    # 读取一帧图像 frame 是读到的画面，类型为 numpy 数组
    # ret 是一个布尔值，表示是否成功读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("摄像头未开，无法读取图像")
        break

    # 使用YOLO模型对当前帧进行推理
    # 可以设定图像大小，默认为640x640
    results = model(frame, imgsz=320, verbose= False)# 关闭每帧的打印日志

    # 获取第一个（也是唯一一个）结果对象（YOLO 返回的是列表，每一帧画面都有一个结果）
    result = results[0]

    # 在原始帧上绘制检测结果（ 目标检测框、目标类别、目标置信度）
    plotted_img = result.plot() # plotted_img 是numpy 数组格式 BGR

    # 显示带标注后的画面
    cv2.imshow('YOLO Real-Time Detection', plotted_img)



    # 控制帧率: 每处理完一帧画面后，等待1/24 秒
    # waitKey() 的时间参数单位为毫秒，但必须为整数，
    # 如果输入的参数为0，则表示无限期等待，直到按下ESC键
    key = cv2.waitKey(int(1000/30))

    # 设置一个推出按键，默认为ESC 比如q键
    if key == ord('q'):
        print('用户按了q键，退出程序')
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()