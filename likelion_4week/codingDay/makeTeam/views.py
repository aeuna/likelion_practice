from django.shortcuts import render
import random

# Create your views here.
def home(request):
  arr = ['강민지', '강채원', '김재훈',
         '김지은', '김진우', '김명환',
         '박지윤', '서바다', '우인아',
         '이민정', '이예빈', '이은아',
         '정지원', '차주희', '김희찬'
  ]
  random.shuffle(arr)
  arr1 = arr[:3]
  arr2 = arr[3:6]
  arr3 = arr[6:9]
  arr4 = arr[9:12]
  arr5 = arr[12:15]
  return render(request, 'index.html',{"arr": arr,"arr1": arr1,"arr2": arr2,"arr2": arr2,"arr3": arr3,"arr4": arr4,"arr5": arr5, "range": range(3,16,3)})