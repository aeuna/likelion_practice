from django.shortcuts import render
from .models import Orders,Members,Goods,Sheets

# Create your views here.
def index(request):
    order_rows = Orders.objects.all()
    sheet_rows = Sheets.objects.all()

    return render(request,'index.html', {"order_rows":order_rows, "sheet_rows":sheet_rows})