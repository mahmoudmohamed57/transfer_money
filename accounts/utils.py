import csv
from uuid import UUID
from .models import Account

def import_accounts_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            Account.objects.create(
                id=UUID(row['ID']),
                name=row['Name'],
                balance=row['Balance']
            )
