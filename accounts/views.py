from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from .utils import import_accounts_from_csv

@csrf_exempt
def import_csv_view(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage()

        file_path = fs.save(csv_file.name, csv_file)
        file_location = fs.path(file_path)

        import_accounts_from_csv(file_location)

        total_accounts = Account.objects.count()
        total_balance = Account.objects.aggregate(Sum('balance'))['balance__sum']

        return render(request, 'csv_analysis.html', {
            'total_accounts': total_accounts,
            'total_balance': total_balance,
        })
    
    return render(request, 'import_csv.html')

def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, 'list_accounts.html', {'accounts': accounts})

def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'account_detail.html', {'account': account})

def transfer_funds(request):
    if request.method == 'POST':
        source_id = request.POST['source_account']
        target_id = request.POST['target_account']
        amount = float(request.POST['amount'])
        
        try:
            source_account = get_object_or_404(Account, id=source_id)
            target_account = get_object_or_404(Account, id=target_id)
            
            if source_account.transfer(target_account, amount):
                return redirect('list_accounts')
            else:
                return HttpResponse('Insufficient funds', status=400)
        
        except ValueError as e:
            return HttpResponse(f'Invalid UUID: {e}', status=400)
    else:
        accounts = Account.objects.all()
        reversed_accounts = accounts[::-1]
        return render(request, 'transfer_funds.html', {'accounts': accounts, 'reversed_accounts': reversed_accounts})
