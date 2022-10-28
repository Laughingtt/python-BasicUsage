#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 引入契约式设计

"""
Design By Contract or DBC defines that methods should have defined input and output verifications. 
Therefore, you can be sure you are always working with a usable set of data in all methods and everything 
is behaving as expected. If not, exceptions or errors should be returned and handled from the methods. 
To read more on DBC read the wikipedia page here.

In our example here, we are working with input parameters that may possibly be null. 
As a result a NullReferenceException would be thrown from this method because we never verify 
that we have an instance. During the end of the method, we don’t ensure that we are returning a valid decimal 
to the consumer of this method and may introduce methods elsewhere.
"""


# 契约式设计(DBC，Design By Contract)定义了方法应该包含输入和输出验证。
# 因此，可以确保所有的工作都是基于可用的数据，并且所有的行为都是可预料的。
# 否则，将返回异常或错误并在方法中进行处理。要了解更多关于 DBC 的内容，可以访问 wikipedia。
# 在我们的示例中，输入参数很可能为 null。
# 由于没有进行验证，该方法最终会抛出 NullReferenceException。
# 在方法最后，我们也并不确定是否为用户返回了一个有效的 decimal，这可能导致在别的地方引入其他方法。

class CashRegister:
    @staticmethod
    def total_order(products, customer):
        order_total = sum([p.price for p in products])
        customer.balance += order_total
        return order_total


"""
The changes we can make here to introduce DBC checks is pretty easy. 
First we will assert that we don’t have a null customer, 
check that we have at least one product to total. 
Before we return the order total we will ensure that we have a valid amount for the order total. 
If any of these checks fail in this example we should throw targeted exceptions that 
detail exactly what happened and fail gracefully rather than throw an obscure NullReferenceException.

It seems as if there is some DBC framework methods and exceptions in the Microsoft.Contracts 
namespace that was introduced with .net framework 3.5. I personally haven’t played with these yet, 
but they may be worth looking at. This is the only thing I could find on msdn about the namespace.
"""


# 在此处引入 DBC 验证是十分简单的。
# 首先，我们要声明 customer 不能为 null，并且在计算总值时至少要有 一个 product。
# 在返回订单总值时，我们要确定其值是否有效。
# 如果此例中任何一个验证失败，我们将以友好的方式抛出相应的异常来描述具体信息，而不是抛出一个晦涩的 NullReferenceException。

class CashRegister:
    @staticmethod
    def total_order(products, customer):
        if customer is None:
            raise Exception('customer cannot be none')
        if len(products) == 0:
            raise Exception('at least one product to total')
        order_total = sum([p.price for p in products])
        customer.balance += order_total
        if order_total == 0:
            raise Exception('order total should not be zero')
        return order_total


"""
It does add more code to the method for validation checks and you can go overboard with DBC, 
but I think in most scenarios it is a worthwhile endeavor to catch sticky situations. 
It really stinks to chase after a NullReferenceException without detailed information.
"""
# 在验证过程中确实增加了不少代码，你也许会认为过度使用了 DBC。
# 但我认为在大多数情况下，处理这些棘手的问题所做的努力都是值得的。
# 追踪无详细内容的 NullReferenceException 的确不是什么美差。
