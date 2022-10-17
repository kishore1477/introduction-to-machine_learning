 
from django.http import HttpResponse
from django.shortcuts import render
import joblib
from django.views.decorators.csrf import csrf_exempt 

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is app")
@csrf_exempt
def result(request):
    if request.method == "POST":
        exp= request.POST.get('exp')
        numExp = int(exp)
        print("Experience",type(numExp))
        print(numExp)
        ml = joblib.load('pickle_of_MLmodel')
        predictedSalary =ml.predict([[numExp]])
        print(predictedSalary)
        context = {"salary":predictedSalary,  "year":numExp}
        return render(request, 'result.html', context)
