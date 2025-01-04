from django.urls import path
from .views import import_csv_view, list_accounts, account_detail, transfer_funds

urlpatterns = [
    path('import/', import_csv_view, name='import_accounts'),
    path('list/', list_accounts, name='list_accounts'),
    path('<uuid:account_id>/', account_detail, name='account_detail'),
    path('transfer/', transfer_funds, name='transfer_funds'),
]
