# 模拟二叉树节点数据
nodes = [
    (0, 2, 15),   # (col, row, val)
    (-1, 1, 9),
    (1, 1, 20),
    (-1, 2, 10),
    (2, 2, 7),
    (0, 3, 12),
    (1, 3, 5),
    (-2, 3, 3)
]

print("原始数据:")
for col, row, val in nodes:
    print(f"列{col}, 行{row}, 值{val}")

print("\n1. 先按列排序:")
nodes_sorted_by_col = sorted(nodes, key=lambda x: x[0])
for col, row, val in nodes_sorted_by_col:
    print(f"列{col}, 行{row}, 值{val}")
# 结果：列-2, 列-1, 列-1, 列0, 列0, 列1, 列1, 列2

print("\n2. 按列和行排序:")
nodes_sorted_by_col_row = sorted(nodes, key=lambda x: (x[0], x[1]))
for col, row, val in nodes_sorted_by_col_row:
    print(f"列{col}, 行{row}, 值{val}")
# 列-2的行3, 列-1的行1, 列-1的行2, 列0的行2, 列0的行3...

print("\n3. 完整排序（列→行→值）:")
nodes_sorted = sorted(nodes, key=lambda x: (x[0], x[1], x[2]))
for col, row, val in nodes_sorted:
    print(f"列{col}, 行{row}, 值{val}")