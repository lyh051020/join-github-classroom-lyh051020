import numpy as np

# 你的代码：
import numpy as np

# 1. 使用arange()创建1到12的一维数组
arr = np.arange(1, 13)
# 2. 用reshape()重塑为3行4列的二维数组
arr_reshaped = arr.reshape(3, 4)

# 3. 打印维度、形状、元素总个数
print("数组的维度(ndim)：", arr_reshaped.ndim)
print("数组的形状(shape)：", arr_reshaped.shape)
print("数组的元素总个数(size)：", arr_reshaped.size)

# 可选：打印数组本身查看结果
print("数组本身：\n", arr_reshaped)