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


import math

r1 = -2 / 3 * math.log(2 / 3, 2) - 1 / 3 * math.log(1 / 3, 2)

info_gain = 1 - r1
print(info_gain)
