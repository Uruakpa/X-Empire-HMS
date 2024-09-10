from django.db import models

# Menu model - represents different menus (Breakfast, Lunch, Dinner)
class Menu(models.Model):
    name = models.CharField(max_length=100)  # E.g., Breakfast, Lunch, Dinner
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return self.name
    
class MenuItem(models.Model):
    image = models.ImageField(upload_to="media/menuimages")
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=255, null=True, blank=True)
    


# Order model - represents an order placed by customers
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('completed', 'Completed')],
        default='pending'
    )

    def __str__(self):
        return f'Order {self.id} - {self.status}'

# OrderItem model - individual items within an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.menu.name}'

# Staff model - represents staff in the restaurant (Waiter, Chef, etc.)
# class Staff(models.Model):
#     name = models.CharField(max_length=100)
#     role = models.CharField(
#         max_length=50, 
#         choices=[('waiter', 'Waiter'), ('chef', 'Chef'), ('manager', 'Manager')]
#     )
#     contact_number = models.CharField(max_length=20)

#     def __str__(self):
#         return f'{self.name} ({self.role})'


