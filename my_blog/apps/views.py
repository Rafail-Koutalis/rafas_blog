from django.shortcuts import render

class AppsViews :

    def all_apps(request) :
        return render(request,'apps/all_apps.html')
    def e_wallet(request) :
        return render(request,('apps/e_wallet.html'))
    
    def payments(request) :
        return render(request,'apps/payments.html')
    
    def study(request) :
        return render(request,'apps/study.html')
    
    def bio(request) :
        return render(request,'apps/bio.html')
      