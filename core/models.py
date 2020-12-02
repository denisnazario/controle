from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField()
    user_default = models.BooleanField()

    class Meta:
        db_table = 'USER'

    def __str__(self):
        return self.name


class Budget(models.Model):
    title = models.CharField(max_length=50)
    host = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        related_name='+'
    )
    guest = models.ForeignKey(
        'User',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='+'
    )
    estimate = models.FloatField()
    cost = models.FloatField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField()

    class Meta:
        db_table = 'BUDGET'

    def __str__(self):
        return self.title


class PaymentData(models.Model):
    title = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    number = models.IntegerField()
    user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        related_name='+'
    )

    class Meta:
        db_table = 'PAYMENT_DATA'

    def __str__(self):
        return self.title


class Account(PaymentData):
    agency = models.IntegerField()
    operation = models.IntegerField()
    enable = models.BooleanField()

    class Meta:
        db_table = 'ACCOUNT'

    def __str__(self):
        return self.title


class CreditCard(PaymentData):
    flag = models.CharField(max_length=20)
    enable = models.BooleanField()

    class Meta:
        db_table = 'CREDIT_CARD'

    def __str__(self):
        return self.title


class PaymentSplit(models.Model):
    personal_1 = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        related_name='+'
    )
    percentage_1 = models.IntegerField()
    personal_2 = models.ForeignKey(
        'User',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    percentage_2 = models.IntegerField()
    personal_3 = models.ForeignKey(
        'User',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    percentage_3 = models.IntegerField()
    personal_4 = models.ForeignKey(
        'User',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    percentage_4 = models.IntegerField()

    class Meta:
        db_table = 'PAYMENT_SPLIT'


class Category(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    enable = models.BooleanField()

    class Meta:
        db_table = 'CATEGORY'

    def __str__(self):
        return self.title

class Transact(models.Model):
    DAILY = 'day'
    WEEKLY = 'week'
    MONTHLY = 'month'
    SEMIANNUAL = 'semiannual'
    YEARLY = 'year'

    CASH = 'cash'
    CREDIT = 'credit'
    DEBIT = 'debit'
    ETV = 'etv'

    PERIOD = [
        (DAILY, 'daily'),
        (WEEKLY, 'weekly'),
        (MONTHLY, 'monthly'),
        (SEMIANNUAL, 'semiannual'),
        (YEARLY, 'yearly')
    ]

    METHOD = [
        (CASH, 'cash'),
        (CREDIT,'credit card'),
        (DEBIT, 'debit'),
        (ETV, 'electronic transfer of values')
    ]

    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    date = models.DateTimeField()
    value = models.FloatField()
    parceled_out = models.BooleanField()
    parceled_times = models.IntegerField()
    parceled_freq = models.CharField(
        max_length=10,
        choices=PERIOD,
        default=MONTHLY
    )
    payment_meth = models.CharField(
        max_length=6,
        choices=METHOD,
        default=CREDIT
    )
    paid = models.BooleanField()
    date_paid = models.DateTimeField()
    payment_split = models.ForeignKey(
        'PaymentSplit',
        on_delete=models.DO_NOTHING,
        related_name='+'
    )
    payment_data = models.ForeignKey(
        'PaymentData',
        on_delete=models.DO_NOTHING,
        related_name='+'
        )
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING,
        related_name='+'
    )
    budget = models.ForeignKey(
        'Budget',
        on_delete=models.DO_NOTHING,
        related_name='+'
    )

    class Meta:
        db_table = 'TRANSACT'

    def __str__(self):
        return self.title