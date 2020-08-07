from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django import forms
from .forms import SignUpForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,  HttpResponse
from django.views.decorators.cache import never_cache


# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('sign_in')

@never_cache
@login_required(login_url='sign_in')
def index(request):
    dct = { '01':'Jan',
		'02':'Feb',
		'03':'Mar',
		'04':'Apr',
		'05':'May',
		'06':'Jun',
		'07':'Jul',
		'08':'Aug',
		'09':'Sept',
		'10':'Oct',
		'11':'Nov',
		'12':'Dec',
	}

    label = []
    data = []

    mnth = request.POST.get("month_value")
    month = str(mnth)

    queryset = RawData.objects.raw("SELECT id,strftime('%m', bootstrap_rawdata.date_found) as month_values, count(link_type) As count FROM bootstrap_rawdata group by month_values")
    FH_no = RawData.objects.raw('SELECT id, COUNT(link_type) as tc FROM bootstrap_rawdata WHERE link_type = "Filehoster"')
    Ws_no = RawData.objects.raw('SELECT id, COUNT(link_type) as tc FROM bootstrap_rawdata WHERE link_type = "Website"')
    Tr_no = RawData.objects.raw('SELECT id, COUNT(link_type) as tc FROM bootstrap_rawdata WHERE link_type = "Torrent"')
    Top_pirated_books = RawData.objects.raw('''SELECT bootstrap_rawdata.id, book_name, COUNT(book_name) As totalcount FROM bootstrap_rawdata JOIN bootstrap_toplist On bootstrap_rawdata.isbn = bootstrap_toplist.isbn Where strftime("%Y-%m", DATE(date_found)) == '{}' group by book_name Order By COUNT(book_name) DESC LIMIT 10'''.format(month))
    Top_pirating_websites = RawData.objects.raw('''SELECT bootstrap_rawdata.id, SUBSTR(SUBSTR(link, INSTR(link, "//") + 2), 0, INSTR(SUBSTR(link, INSTR(link, "//") + 2), "/")) As website, COUNT(*) As tcnt FROM bootstrap_rawdata Where strftime("%Y-%m", DATE(date_found)) == '{}' group by 2 Order by tcnt DESC LIMIT 10'''.format(month))

    for a in queryset:
        mnth1 = dct[a.month_values]
        month1 = str(mnth1)
        label.append(month1)
        data.append(a.count)


    context = {
        'FH_no': FH_no,
        'Ws_no': Ws_no,
        'Tr_no': Tr_no,
        'Top_pirated_books': Top_pirated_books,
        'Top_pirating_websites': Top_pirating_websites,
        'label':label,
        'data':data,
    }
    return render(request, 'index.html', context)

@login_required(login_url='sign_in')
def tables(request):
    items = TopList.objects.raw('SELECT * from bootstrap_toplist ORDER BY id DESC')
    context = {
        'items': items,
    }
    return render(request, 'tables.html', context)

@login_required(login_url='sign_in')
def display_prod(request, isbn1):
    isn = str(isbn1)
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="{}"'.format(isn))
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="{}"'.format(isn)) #%s' % isn)
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, 'products.html', context)