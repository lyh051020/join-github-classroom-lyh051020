#一
import pandas as pd

# 用字典创建DataFrame
data_dict = {
    "name": ["Tom", "Jerry", "Mike"],
    "score": [85, 92, 78],
    "gender": ["男", "女", "男"]
}
df1 = pd.DataFrame(data_dict)
print("用字典创建的DataFrame：")
print(df1)

# 查看前1行
print("\n前1行数据：")
print(df1.head(1))

# 查看形状（行数, 列数）
print("\nDataFrame形状：", df1.shape)

# 查看列名
print("\n列名：", df1.columns.tolist())

# 查看数据类型
print("\n各列数据类型：")
print(df1.dtypes)

data_list = [[1, "A"], [2, "B"], [3, "C"]]
df2 = pd.DataFrame(data_list, columns=["id", "tag"])
print("\n用列表创建的DataFrame：")
print(df2)

#二
import pandas as pd

# 先创建基础DataFrame
data = {
    "name": ["Tom", "Jerry", "Mike"],
    "score": [85, 92, 78],
    "gender": ["男", "女", "男"]
}
df = pd.DataFrame(data)

# 1. 选取 score 和 gender 两列
df[["score", "gender"]]

# 2. 选取索引 0、2 的行
df.loc[[0, 2]]

# 3. 筛选 score>80 的行
df[df["score"] > 80]

# 4. 新增一列 grade：score≥90 为优秀，否则为良好
df["grade"] = df["score"].apply(lambda x: "优秀" if x >= 90 else "良好")

# 5. 删除 gender 列
df.drop(columns=["gender"], inplace=True)  # 或 df = df.drop(columns=["gender"])

#三
import pandas as pd

# 1. 创建含缺失值的 DataFrame
data = {"x": [1, None, 3], "y": [None, 5, 6]}
df = pd.DataFrame(data)

print("=== 原始 DataFrame ===")
print(df)

# 检测缺失值并统计每列缺失数量
print("\n=== 缺失值检测（布尔矩阵） ===")
print(df.isnull())

print("\n=== 每列缺失值数量 ===")
print(df.isnull().sum())

# 2. 用 0 填充缺失值
df_fill = df.fillna(0)
print("\n=== 用 0 填充缺失值后的 DataFrame ===")
print(df_fill)

# 删除含缺失值的行
df_drop = df.dropna()
print("\n=== 删除含缺失值的行后的 DataFrame ===")
print(df_drop)

#四
import pandas as pd

# 原始数据
data = {
    "name": ["Tom", "Jerry", "Mike"],
    "score": [85, 92, 78],
    "gender": ["男", "女", "男"]
}
df = pd.DataFrame(data)

# === 四、分组聚合 ===
# 1. 按 gender 分组，求 score 的均值和最大值
grouped_result = df.groupby("gender")["score"].agg(["mean", "max"])
print("按 gender 分组的 score 均值和最大值：")
print(grouped_result)

# 2. 按 gender 分组，统计每组人数
count_result = df.groupby("gender").size()
print("\n按 gender 分组的人数统计：")
print(count_result)

#五
# === 五、排序与去重 ===
# 1. 按 score 升序排序
df_sorted = df.sort_values(by="score", ascending=True)
print("\n按 score 升序排序的结果：")
print(df_sorted)

# 2. 添加重复数据并去重
df = pd.concat([df, pd.DataFrame([{"name": "Tom", "score": 85, "gender": "男"}])], ignore_index=True)
print("\n添加重复数据后的 DataFrame：")
print(df)

df_dedup = df.drop_duplicates()
print("\n去重后的 DataFrame：")
print(df_dedup)

#六
import pandas as pd

# 1. 横向合并
df1 = pd.DataFrame({"id": [1, 2], "name": ["X", "Y"]})
df2 = pd.DataFrame({"id": [1, 2], "age": [20, 30]})
merged_df = pd.merge(df1, df2, on="id")
print("横向合并结果：")
print(merged_df)

# 2. 纵向拼接
df_a = pd.DataFrame({"val": [1, 2]})
df_b = pd.DataFrame({"val": [3, 4]})
concatenated_df = pd.concat([df_a, df_b], ignore_index=True)
print("\n纵向拼接并重置索引结果：")
print(concatenated_df)

#七
import pandas as pd

# ===== 七、时间处理 =====
# 1. 创建时间列并转为datetime
date_list = ["2025-01-01", "2025-01-02", "2025-01-03"]
df_time = pd.DataFrame({"date": date_list})
df_time["date"] = pd.to_datetime(df_time["date"])

# 2. 提取月份、星期
df_time["month"] = df_time["date"].dt.month
df_time["weekday"] = df_time["date"].dt.weekday
df_time["weekday_name"] = df_time["date"].dt.day_name()

print("===== 时间处理结果 =====")
print(df_time)


#八
# ===== 八、高级操作 =====
df = pd.DataFrame({
    "name": ["Tom", "Jerry", "Mike"],
    "score": [85, 92, 78],
    "gender": ["男", "女", "男"]
})

# 1. score列标准化
mean_score = df["score"].mean()
std_score = df["score"].std()
df["score_std"] = (df["score"] - mean_score) / std_score

# 2. 透视表求中位数
pivot_table = pd.pivot_table(df, index="gender", values="score", aggfunc="median")

print("\n===== 高级操作结果 =====")
print("标准化后的score列：")
print(df[["score", "score_std"]])
print("\n透视表（gender为行，score中位数）：")
print(pivot_table)