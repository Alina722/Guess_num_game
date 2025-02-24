class 人:
    def __init__(self, 名字, 年齡):
        self.名字 = 名字  # 屬性（Attribute）
        self.年齡 = 年齡

    def 自我介紹(self):  # 方法（Method）
        print(f"大家好，我是{self.名字}，今年{self.年齡}歲！")