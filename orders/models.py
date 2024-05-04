from django.db import models
from customers.models import customer
from products.models import product 
# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))

    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    CART_STAGE=0
    ORDER_CONFORMED=1
    ORDER_PROCESSED=2
    ORDER_DELEVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES=((ORDER_PROCESSED,"ORDER_PROCESSed"),
                    (ORDER_DELEVERED,"ORDER_DELEVERED"),
                    (ORDER_REJECTED,"ORDER_REJECTED"),
                    )
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)

    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   
class orderedItem(models.Model):
    product=models.ForeignKey(product,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE, null=True)
    