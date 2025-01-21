# -*- coding: utf-8 -*-
class Product:
    """产品类，包含多个部件"""

    def __init__(self):
        self.parts = []

    def add(self, part):
        """添加部件"""
        self.parts.append(part)

    def show(self):
        """展示产品所有部件"""
        print("产品包含部件：", "，".join(self.parts))


class Builder:
    """抽象建造者"""

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        """构建部件A"""
        raise NotImplementedError

    def build_part_b(self):
        """构建部件B"""
        raise NotImplementedError

    def get_result(self):
        """获取最终产品"""
        return self.product


class ConcreteBuilder1(Builder):
    """具体建造者1"""

    def build_part_a(self):
        self.product.add('部件A')

    def build_part_b(self):
        self.product.add('部件B')


class ConcreteBuilder2(Builder):
    """具体建造者2"""

    def build_part_a(self):
        self.product.add('部件X')

    def build_part_b(self):
        self.product.add('部件Y')


class Director:
    """指挥者类，控制建造过程"""

    def construct(self, builder):
        """构建产品"""
        builder.build_part_a()
        builder.build_part_b()


if __name__ == '__main__':
    director = Director()

    # 使用建造者1构建产品
    builder1 = ConcreteBuilder1()
    director.construct(builder1)
    product1 = builder1.get_result()
    product1.show()

    # 使用建造者2构建产品
    builder2 = ConcreteBuilder2()
    director.construct(builder2)
    product2 = builder2.get_result()
    product2.show()
