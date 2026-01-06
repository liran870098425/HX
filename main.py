# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import  redis
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按装订区域中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

redis_util = redis.Redis(
          host='192.168.3.163',
          port=6379,
          password='sinzeeaA@188',
          decode_responses=False,
          db=0
            )
redis_util.set("HXSH",123)
value = redis_util.get("HXSH")
print(f"键 HXSH 对应的值：{value}")