from django.db import models


class Goods(models.Model):
    goodsId = models.IntegerField(primary_key=True)
    goodsName = models.CharField(max_length = 127)
    goodsPrice = models.IntegerField(null=True)

        
class Members(models.Model):
    memberId = models.IntegerField(primary_key=True)
    memberName = models.CharField(max_length=127)
    home = models.CharField(max_length=1023)

class Orders(models.Model):
    memberId = models.ForeignKey(Members, on_delete=models.SET_NULL, null=True, blank=True) #원본이 삭제되면 null
    orderId = models.IntegerField(primary_key=True)

class Sheets(models.Model):
    memberId = models.ForeignKey(Members, on_delete=models.SET_NULL, null=True, blank=True)
    orderId = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True, blank=True)
    GoodsId = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True)


    
