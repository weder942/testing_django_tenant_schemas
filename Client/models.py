from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.DateField()
    created_on = models.DateField(auto_now_add=True)


class Domain(DomainMixin):
    pass
