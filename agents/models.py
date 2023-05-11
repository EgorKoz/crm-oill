from django.db import models

PRIORITIES = (
    ('l', 'Низкий'),
    ('m', 'Средний'),
    ('h', 'Высокий'),
)


class Address(models.Model):
    state = models.CharField('Страна', max_length=64)
    city = models.CharField('Город', max_length=64)
    street = models.CharField('Улица', max_length=64)
    address = models.CharField('Строение', max_length=64, blank=True, default="")
    postcode = models.CharField('Почтовый индекс', max_length=32, blank=True, default="")

    def __str__(self):
        return self.get_complete_address()

    def get_complete_address(self):
        full_address = ""
        if self.state:
            full_address += self.state
        if self.city:
            if full_address:
                full_address += ", " + self.city
            else:
                full_address += self.city
        if self.street:
            if full_address:
                full_address += ", " + self.street
            else:
                full_address += self.street
        if self.address:
            if full_address:
                full_address += ", " + self.address
            else:
                full_address += self.address
        if self.postcode:
            if full_address:
                full_address += ", " + self.postcode
            else:
                full_address += self.postcode
        return full_address


class Org(models.Model):
    name = models.CharField('Название', max_length=64)
    web_site = models.CharField('Web-сайт', max_length=64, blank=True, default='')

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    email = models.EmailField('Email', max_length=128, unique=True)
    phone = models.CharField('Номер телефона', max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(''))
    org = models.ForeignKey(
        Org,
        null=True,
        on_delete=models.SET(None),
        blank=True,
        related_name="user_org",
    )
    address = models.ForeignKey(
        Address,
        related_name="adress_users",
        on_delete=models.SET(None),
        blank=True,
        null=True,
    )
    has_sales_access = models.BooleanField('Скидка', default=False)
    priority = models.CharField('Приоритет', max_length=3, choices=PRIORITIES, blank=True, default='')
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True)
    description = models.TextField('Описание', blank=True, null=True)
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return f'{self.user}, {self.org}'
