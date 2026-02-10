# import torch
# if torch.cuda.is_available():
#     print("GPU name:", torch.cuda.get_device_name(0))
#     print("CUDA version:", torch.version.cuda)
# else:
#     print("Using CPU only")

import torch
import time

# 创建大张量
x = torch.randn(30000, 30000)

# CPU计算时间
start = time.time()
cpu_result = x @ x
cpu_time = time.time() - start  # 保存CPU时间
print(f"CPU计算时间: {cpu_time:.2f}秒")

# GPU计算（如果可用）
if torch.cuda.is_available():
    x_gpu = x.cuda()
    torch.cuda.synchronize()  # 同步等待
    start = time.time()
    gpu_result = x_gpu @ x_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start  # 保存GPU时间
    print(f"GPU计算时间: {gpu_time:.2f}秒")
    print(f"速度提升: {cpu_time/gpu_time:.1f}倍")  # 现在变量已定义
else:
    print("CUDA不可用，跳过GPU测试")