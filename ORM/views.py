from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

# Create your views here.


def index_1(request):
    borrowers = []
    print(get_object_or_404(Loan, pk='-6'))
    print(Loan.objects.get(id=6))
    for loan in Loan.objects.filter(status=2):
        if loan.borrower not in borrowers:
            borrowers.append(loan.borrower)
    return HttpResponse(len(borrowers))


def index_2(request):
    borrowers = []
    start = datetime(year=2022, day=1, month=1) - timedelta(microseconds=1)
    end = datetime(year=2022, day=31, month=12) + timedelta(days=1)
    for loan in Loan.objects.filter(created_at__gte=start, created_at__lte=end):
        if loan.borrower not in borrowers:
            borrowers.append(loan.borrower)
    return HttpResponse(len(borrowers))


def index_3(request):
    total_amount = 0
    start = datetime(year=2021, day=1, month=1) - timedelta(microseconds=1)
    end = datetime(year=2021, day=31, month=12) + timedelta(days=1)
    for borrower in Borrower.objects.filter(created_at__gte=start, created_at__lte=end):
        for load in borrower.loans.filter(status=1):
            total_amount += load.amount
    print(total_amount)
    return HttpResponse(total_amount)
