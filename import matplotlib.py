import matplotlib.pyplot as plt
import numpy as np

# 1. 准备数据
# 组中值（每一组的中点）
x = np.array([82.5, 87.5, 92.5, 97.5, 102.5, 107.5, 112.5, 117.5, 122.5, 127.5, 132.5])
# 频率/组距
freq_per_width = np.array([0.002, 0.004, 0.008, 0.028, 0.048, 0.030, 0.024, 0.018, 0.022, 0.012, 0.004])
# 组距
width = 5
# 计算频率
freq = freq_per_width * width

# 2. 绘制频率分布直方图
plt.figure(figsize=(10, 6))
plt.bar(x, freq_per_width, width=width, edgecolor='black')
plt.xlabel('周长/cm')
plt.ylabel('频率/组距')
plt.title('周长频率分布直方图')
plt.grid(axis='y', alpha=0.3)
plt.show()

# 3. 基础统计计算
# 平均数
mean = np.sum(x * freq)
# 中位数
cum_freq = np.cumsum(freq)
median_idx = np.where(cum_freq >= 0.5)[0][0]
median = x[median_idx]

print(f"平均数: {mean:.2f} cm")
print(f"中位数: {median:.2f} cm")