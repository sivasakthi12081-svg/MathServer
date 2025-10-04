from django.shortcuts import render
def bmi(request):
   context={}
   context['w']="0"
   context['h']="0"
   context['bmi']="0"
   if request.method=='POST':
      print("POST method is used")
      w=request.POST.get('weight','0')
      h=request.POST.get('height','0')
      print('request=',request)
      print('Weight=',w)
      print('Height=',h)
      a=float(w)
      b=float(h)
      bmi=a/((b/100)**2)
      context['w']=w
      context['h']=h
      context['bmi']=bmi
      print('BMI=',bmi)
   return render(request,'mathapp/math.html',context)