from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class TableCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Table(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_number = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        TableCategory,
        on_delete=models.PROTECT,
        related_name='tables'
    )
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.table_number
    
    
class ReservationStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class Reservation(models.Model):
    id = models.BigAutoField(primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    table = models.ForeignKey(
        Table,
        on_delete=models.PROTECT,
        related_name='reservations'
    )

    reservation_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    guests = models.PositiveIntegerField()

    status = models.ForeignKey(
        ReservationStatus,
        on_delete=models.PROTECT,
        related_name='reservations'
    )

    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.reservation_date}"
    
    
class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)

    reservation = models.OneToOneField(
        Reservation,
        on_delete=models.CASCADE,
        related_name='payment'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(max_length=50)

    payment_status = models.CharField(max_length=20)

    paid_at = models.DateTimeField(null=True, blank=True)

    transaction_ref = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for {self.reservation}"
    
    
class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='audit_logs'
    )

    action = models.CharField(max_length=100)

    performed_by = models.CharField(max_length=100)

    action_time = models.DateTimeField(auto_now_add=True)

    details = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.action} - Reservation {self.reservation.id}"