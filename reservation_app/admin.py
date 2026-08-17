from django.contrib import admin

# Register your models here.

from .models import (
    Customer,
    TableCategory,
    Table,
    ReservationStatus,
    Reservation,
    Payment,
    AuditLog,
)

admin.site.register(Customer)
admin.site.register(TableCategory)
admin.site.register(Table)
admin.site.register(ReservationStatus)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(AuditLog)