library = {
    '文学区': {
        '小说类': {
            '平凡的世界': {'馆藏': 5, '借出': 3, '作者': '路遥'},
            '活着': {'馆藏': 4, '借出': 2, '作者': '余华'},
            '三体':{'馆藏':11,'借出':4,'作者':'刘慈欣'}
        },
        '诗歌类': {
            '唐诗三百首': {'馆藏': 3, '借出': 1},
            '宋词':{'馆藏':5,'借出':0},
            '元曲':{'馆藏':7,'借出':2}
        }
    }
}

# 按区域-类别-书籍的顺序，每个级别内按馆藏排序
for area_name, area in library.items():
    print(f"\n【{area_name}】")

    for category_name, category in area.items():
        print(f"\n  {category_name}：")

        # 当前类别内按馆藏降序排序
        sorted_books = sorted(
            category.items(),
            key=lambda x: x[1]['馆藏'],
            reverse=True
        )

        for book_name, book_info in sorted_books:
            available = book_info['馆藏'] - book_info['借出']
            print(f"    《{book_name}》 - 馆藏: {book_info['馆藏']}本, 可借: {available}本")

# 在Python中查看安装路径
import sys
print(sys.executable)  # Python解释器路径
print(sys.prefix)      # Python安装目录

# print(bool(""))
my_list = [1, 2, 3]
def modify_list():
    my_list.append(4)
    print(my_list)
modify_list()
print(my_list)

x = 10
print(id(x))
x += 1
print(id(x))
