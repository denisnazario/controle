from django.contrib import admin
from . import models


# User class wil not used for now.
#admin.site.register(models.User)
admin.site.register(models.Budget)
admin.site.register(models.PaymentData)
admin.site.register(models.Account)
admin.site.register(models.CreditCard)
admin.site.register(models.PaymentSplit)
admin.site.register(models.Category)
admin.site.register(models.Transact)
admin.site.register(models.Calendar)