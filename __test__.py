# import time
# import sys
#
#
# def loading_animation():
#     frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
#
#     for i in range(20):
#         sys.stdout.write(f"\r{frames[i % len(frames)]} 加载中... {i * 5}%")
#         sys.stdout.flush()
#         time.sleep(0.5)
#
#     print("\r✅ 加载完成！ 100%")
#
#
# # 运行动画
# loading_animation()

# def cycle(n, k=0, res=[]):
#     if k > n:
#         return res
#     res.append(k)
#     cycle(n, k + 1, res)
#     if k ==0:
#         return res
#     res.append(k - 1)
#     return res
#
#
# print(cycle(5))

# def lastremaining(self, n: int) -> int:
#     MASK = 0x55555555
#     mask2 = (1 << (n.bit_length() - 1)) - 1
#     return ((n | MASK) & mask2 + 1)
#
#
# lastremaining(6,6)


# 保存为 diagnose_numpy.py


# import torch
# if torch.cuda.is_available():
#     print("GPU name:", torch.cuda.get_device_name(0))
#     print("CUDA version:", torch.version.cuda)
# else:
#     print("Using CPU only")
#
# import torch
# import time
#
# # 创建大张量
# x = torch.randn(20000, 20000)
#
# # CPU计算时间
# start = time.time()
# cpu_result = x @ x
# cpu_time = time.time() - start  # 保存CPU时间
# print(f"CPU计算时间: {cpu_time:.2f}秒")
#
# # GPU计算（如果可用）
# if torch.cuda.is_available():
#     x_gpu = x.cuda()
#     torch.cuda.synchronize()  # 同步等待
#     start = time.time()
#     gpu_result = x_gpu @ x_gpu
#     torch.cuda.synchronize()
#     gpu_time = time.time() - start  # 保存GPU时间
#     print(f"GPU计算时间: {gpu_time:.2f}秒")
#     print(f"速度提升: {cpu_time/gpu_time:.1f}倍")  # 现在变量已定义
# else:
#     print("CUDA不可用，跳过GPU测试")


# import math
#
# r1 = -2 / 3 * math.log(2 / 3, 2) - 1 / 3 * math.log(1 / 3, 2)
#
# info_gain = 1 - r1
# print(info_gain)


import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（确保中文标签正常显示）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义Leaky ReLU函数
def leaky_relu(x, alpha=0.01):
    """
    Leaky ReLU函数实现
    参数:
        x: 输入值（可以是单个值或数组）
        alpha: 负区间的斜率，默认0.01（常用值还有0.1）
    返回:
        Leaky ReLU的输出值
    """
    return np.where(x > 0, x, alpha * x)

# 生成x轴数据（范围覆盖正负区间，体现函数特性）
x = np.linspace(-10, 10, 1000)
# 计算两个不同alpha值的Leaky ReLU输出（对比展示）
y_default = leaky_relu(x, alpha=0.01)  # 默认alpha=0.01
y_alpha01 = leaky_relu(x, alpha=0.1)   # alpha=0.1（更常用的替代值）

# 创建画布
plt.figure(figsize=(10, 6))

# 绘制不同alpha的Leaky ReLU曲线
plt.plot(x, y_default, label=r'Leaky ReLU ($\alpha=0.01$)', linewidth=2, color='#2E86AB')
plt.plot(x, y_alpha01, label=r'Leaky ReLU ($\alpha=0.1$)', linewidth=2, color='#A23B72', linestyle='--')

# 绘制ReLU函数（对比参考）
y_relu = np.maximum(0, x)
plt.plot(x, y_relu, label='ReLU', linewidth=1.5, color='#F18F01', linestyle=':')

# 添加辅助线
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.7)
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8, alpha=0.7)

# 设置图表样式
plt.title('Leaky ReLU函数图像', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('输入值 (x)', fontsize=12)
plt.ylabel('输出值 (Leaky ReLU(x))', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(-10, 10)
plt.ylim(-2, 10)

# 显示图表
plt.tight_layout()
plt.show()






















