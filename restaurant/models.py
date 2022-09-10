from django.db import models


class Customer(models.Model):
    table = models.CharField(max_length=255)

    def __str__(self):
        return 'Стол номер {}'.format(self.table)

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = "Клиент"


class Order(models.Model):
    STATUS_CHOISES = (
        ("new", 'Поступил заказ'),
        ("cooking", 'Готовится'),
        ("cooked", 'Приготовлен'),
        ("finished", 'Заказ отдан'),
    )
    status = models.CharField(choices=STATUS_CHOISES, max_length=50, verbose_name='Статус заказа', default='new')
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return 'Заказ для {}, статус {}'.format(self.customer, self.status)

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = "Заказ"


class Dish(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}, {} сом'.format(self.name, self.price)

    class Meta:
        verbose_name_plural = 'Блюда'
        verbose_name = "Блюдо"


class Order_Dish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def get_price(self):
        return self.dish.price * self.amount

    def __str__(self):
        return '{}, {} шт'.format(self.dish, self.amount)

    class Meta:
        verbose_name_plural = 'Заказанные блюда'
        verbose_name = "Заказанное блюдо"
