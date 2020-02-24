from django.shortcuts import render
from django.db.models import Count
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def tables(request):
    items = TopList.objects.raw('SELECT * from bootstrap_toplist')
    context = {
        'items': items,
    }
    return render(request, 'tables.html', context)

def display_1789612160(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612160"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612160"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612160.html', context)

def display_1838827994(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838827994"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838827994"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838827994.html', context)

def display_1838641106(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838641106"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838641106"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838641106.html', context)
def display_183921662X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183921662X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183921662X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183921662X.html', context)
def display_1789618517(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789618517"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789618517"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789618517.html', context)
def display_1789951755(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789951755"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789951755"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789951755.html', context)
def display_1838557741(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838557741"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838557741"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838557741.html', context)
def display_1838824308(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838824308"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838824308"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838824308.html', context)
def display_1838829091(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838829091"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838829091"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838829091.html', context)
def display_1838820299(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838820299"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838820299"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838820299.html', context)
def display_1838826998(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838826998"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838826998"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838826998.html', context)
def display_1838824413(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838824413"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838824413"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838824413.html', context)
def display_1838987738(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838987738"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838987738"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838987738.html', context)
def display_183921953X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183921953X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183921953X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183921953X.html', context)
def display_1838559914(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838559914"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838559914"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838559914.html', context)
def display_1839214678(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839214678"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839214678"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839214678.html', context)
def display_183864900X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183864900X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183864900X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183864900X.html', context)
def display_1838825487(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838825487"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838825487"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838825487.html', context)
def display_1838981268(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838981268"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838981268"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838981268.html', context)
def display_1789131618(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131618"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131618"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131618.html', context)
def display_1838554491(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838554491"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838554491"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838554491.html', context)
def display_1838821902(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838821902"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838821902"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838821902.html', context)
def display_183921306X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183921306X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183921306X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183921306X.html', context)
def display_1800208073(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1800208073"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1800208073"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1800208073.html', context)
def display_1838824987(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838824987"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838824987"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838824987.html', context)
def display_1789806313(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789806313"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789806313"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789806313.html', context)
def display_1789957648(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789957648"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789957648"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789957648.html', context)
def display_183864881X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183864881X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183864881X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183864881X.html', context)
def display_1838553533(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838553533"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838553533"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838553533.html', context)
def display_178980700X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178980700X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178980700X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980700X.html', context)
def display_1838828885(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838828885"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838828885"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838828885.html', context)
def display_1839214937(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839214937"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839214937"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839214937.html', context)
def display_1789538947(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538947"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538947"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538947.html', context)
def display_178961208X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178961208X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178961208X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178961208X.html', context)
def display_183882779X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183882779X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183882779X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183882779X.html', context)
def display_1838647945(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838647945"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838647945"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838647945.html', context)
def display_1838642358(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838642358"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838642358"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838642358.html', context)
def display_1839213388(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839213388"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839213388"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839213388.html', context)
def display_1839211024(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839211024"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839211024"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839211024.html', context)
def display_1838981128(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838981128"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838981128"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838981128.html', context)
def display_1789537614(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789537614"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789537614"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537614.html', context)
def display_1789610133(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789610133"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789610133"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610133.html', context)
def display_1789955106(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789955106"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789955106"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789955106.html', context)
def display_1789950228(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789950228"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789950228"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789950228.html', context)
def display_1838823417(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838823417"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838823417"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838823417.html', context)
def display_1839216581(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839216581"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839216581"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839216581.html', context)
def display_1789958350(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789958350"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789958350"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789958350.html', context)
def display_183882491X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183882491X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183882491X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183882491X.html', context)
def display_1838984135(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838984135"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838984135"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838984135.html', context)
def display_178913241X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178913241X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178913241X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913241X.html', context)
def display_1789805546(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789805546"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789805546"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789805546.html', context)
def display_1789807409(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807409"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807409"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807409.html', context)
def display_1789951259(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789951259"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789951259"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789951259.html', context)
def display_1789954932(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954932"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954932"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954932.html', context)
def display_1838649328(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838649328"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838649328"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838649328.html', context)
def display_1789538777(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538777"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538777"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538777.html', context)
def display_1789616719(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789616719"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789616719"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789616719.html', context)
def display_1838643508(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838643508"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838643508"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838643508.html', context)
def display_1838821473(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838821473"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838821473"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838821473.html', context)
def display_1789530512(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789530512"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789530512"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789530512.html', context)
def display_178995617X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178995617X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178995617X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178995617X.html', context)
def display_1789955750(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789955750"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789955750"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789955750.html', context)
def display_1839217472(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839217472"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839217472"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839217472.html', context)
def display_1839211709(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839211709"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839211709"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839211709.html', context)
def display_1789804108(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804108"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804108"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804108.html', context)
def display_1789800935(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800935"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800935"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800935.html', context)
def display_1789805821(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789805821"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789805821"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789805821.html', context)
def display_1838552200(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838552200"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838552200"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838552200.html', context)
def display_1838556516(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838556516"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838556516"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838556516.html', context)
def display_1838553002(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838553002"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838553002"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838553002.html', context)
def display_1838645357(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838645357"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838645357"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838645357.html', context)
def display_1838641912(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838641912"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838641912"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838641912.html', context)
def display_1838984658(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838984658"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838984658"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838984658.html', context)
def display_1838988823(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838988823"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838988823"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838988823.html', context)
def display_1838983279(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838983279"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838983279"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838983279.html', context)
def display_1838643540(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838643540"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838643540"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838643540.html', context)
def display_1838647511(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838647511"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838647511"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838647511.html', context)
def display_1838824537(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838824537"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838824537"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838824537.html', context)
def display_1838827366(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838827366"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838827366"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838827366.html', context)
def display_1839211741(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839211741"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839211741"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839211741.html', context)
def display_1800200668(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1800200668"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1800200668"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1800200668.html', context)
def display_1800209371(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1800209371"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1800209371"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1800209371.html', context)
def display_1800204736(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1800204736"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1800204736"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1800204736.html', context)
def display_1800206623(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1800206623"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1800206623"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1800206623.html', context)
def display_1838821732(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838821732"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838821732"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838821732.html', context)
def display_1839216409(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839216409"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839216409"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839216409.html', context)
def display_1789614678(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789614678"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789614678"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789614678.html', context)
def display_1789615860(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615860"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615860"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615860.html', context)
def display_1789951224(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789951224"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789951224"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789951224.html', context)
def display_1838823816(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838823816"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838823816"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838823816.html', context)
def display_1838983996(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838983996"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838983996"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838983996.html', context)
def display_1838982361(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838982361"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838982361"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838982361.html', context)
def display_1789611806(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789611806"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789611806"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789611806.html', context)
def display_1838826327(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838826327"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838826327"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838826327.html', context)
def display_1788995201(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995201"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995201"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995201.html', context)
def display_1838643893(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838643893"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838643893"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838643893.html', context)
def display_178934834X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178934834X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178934834X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934834X.html', context)
def display_1839218851(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839218851"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839218851"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839218851.html', context)
def display_1789956714(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789956714"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789956714"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956714.html', context)
def display_1788478126(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788478126"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788478126"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788478126.html', context)
def display_1789343623(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343623"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343623"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343623.html', context)
def display_178953657X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178953657X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178953657X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178953657X.html', context)
def display_1789536898(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536898"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536898"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536898.html', context)
def display_1838551964(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838551964"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838551964"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838551964.html', context)
def display_1838642366(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838642366"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838642366"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838642366.html', context)
def display_1838648917(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838648917"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838648917"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838648917.html', context)
def display_1838648577(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838648577"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838648577"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838648577.html', context)
def display_1838828842(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838828842"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838828842"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838828842.html', context)
def display_1838821139(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838821139"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838821139"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838821139.html', context)
def display_1839213469(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839213469"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839213469"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839213469.html', context)
def display_1838986693(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838986693"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838986693"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838986693.html', context)
def display_1789343232(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343232"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343232"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343232.html', context)
def display_1838642730(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838642730"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838642730"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838642730.html', context)
def display_1789803322(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789803322"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789803322"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803322.html', context)
def display_1839213337(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839213337"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839213337"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839213337.html', context)
def display_1789131111(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131111"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131111"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131111.html', context)
def display_1789530660(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789530660"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789530660"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789530660.html', context)
def display_1838555277(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838555277"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838555277"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838555277.html', context)
def display_1838641440(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838641440"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838641440"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838641440.html', context)
def display_1839218045(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839218045"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839218045"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839218045.html', context)
def display_1839219688(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839219688"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839219688"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839219688.html', context)
def display_1789802989(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802989"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802989"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802989.html', context)
def display_1789950694(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789950694"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789950694"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789950694.html', context)
def display_1838550917(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838550917"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838550917"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550917.html', context)
def display_1838555722(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838555722"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838555722"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838555722.html', context)
def display_1838827544(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838827544"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838827544"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838827544.html', context)
def display_183921435X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183921435X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183921435X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183921435X.html', context)
def display_1789341787(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341787"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341787"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341787.html', context)
def display_1789534143(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534143"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534143"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534143.html', context)
def display_1789138744(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789138744"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789138744"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138744.html', context)
def display_1838820213(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838820213"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838820213"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838820213.html', context)
def display_1838826211(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838826211"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838826211"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838826211.html', context)
def display_1839211962(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839211962"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839211962"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839211962.html', context)
def display_178883982X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178883982X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178883982X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178883982X.html', context)
def display_1788996240(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788996240"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788996240"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788996240.html', context)
def display_1789348269(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348269"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348269"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348269.html', context)
def display_1789959276(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789959276"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789959276"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789959276.html', context)
def display_1838550186(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838550186"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838550186"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550186.html', context)
def display_1838552278(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838552278"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838552278"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838552278.html', context)
def display_1789613477(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789613477"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789613477"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789613477.html', context)
def display_1789807603(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807603"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807603"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807603.html', context)
def display_1789801419(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789801419"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789801419"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789801419.html', context)
def display_1789954118(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954118"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954118"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954118.html', context)
def display_1789615550(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615550"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615550"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615550.html', context)
def display_1838559353(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838559353"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838559353"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838559353.html', context)
def display_1838644482(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838644482"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838644482"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838644482.html', context)
def display_1788996089(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788996089"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788996089"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788996089.html', context)
def display_1789533732(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533732"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533732"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533732.html', context)
def display_1789536308(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536308"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536308"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536308.html', context)
def display_1789804167(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804167"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804167"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804167.html', context)
def display_1788838106(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788838106"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788838106"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788838106.html', context)
def display_1789133637(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133637"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133637"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133637.html', context)
def display_1789535360(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535360"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535360"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535360.html', context)
def display_1789953006(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789953006"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789953006"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789953006.html', context)
def display_1838550135(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838550135"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838550135"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550135.html', context)
def display_1838643109(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838643109"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838643109"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838643109.html', context)
def display_1839214945(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839214945"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839214945"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839214945.html', context)
def display_1838559337(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838559337"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838559337"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838559337.html', context)
def display_1789808154(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808154"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808154"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808154.html', context)
def display_1789134501(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789134501"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789134501"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789134501.html', context)
def display_1789347068(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789347068"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789347068"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347068.html', context)
def display_1789807352(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807352"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807352"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807352.html', context)
def display_1789957753(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789957753"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789957753"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789957753.html', context)
def display_1838823859(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838823859"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838823859"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838823859.html', context)
def display_1789530091(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789530091"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789530091"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789530091.html', context)
def display_1789958547(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789958547"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789958547"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789958547.html', context)
def display_178980020X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178980020X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178980020X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980020X.html', context)
def display_1838649239(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838649239"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838649239"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838649239.html', context)
def display_1789340993(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340993"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340993"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340993.html', context)
def display_1789531284(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531284"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531284"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531284.html', context)
def display_1789804027(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804027"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804027"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804027.html', context)
def display_1839218266(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839218266"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839218266"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839218266.html', context)
def display_1839217642(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1839217642"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1839217642"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1839217642.html', context)
def display_1789133041(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133041"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133041"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133041.html', context)
def display_1789615321(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615321"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615321"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615321.html', context)
def display_1789344158(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344158"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344158"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344158.html', context)
def display_1787284433(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1787284433"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1787284433"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787284433.html', context)
def display_1789612853(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612853"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612853"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612853.html', context)
def display_1789800986(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800986"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800986"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800986.html', context)
def display_1789802547(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802547"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802547"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802547.html', context)
def display_1838552863(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838552863"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838552863"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838552863.html', context)
def display_1838550364(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838550364"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838550364"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550364.html', context)
def display_1789951291(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789951291"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789951291"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789951291.html', context)
def display_1789533392(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533392"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533392"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533392.html', context)
def display_1789615690(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615690"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615690"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615690.html', context)
def display_1789952069(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789952069"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789952069"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789952069.html', context)
def display_1789534623(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534623"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534623"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534623.html', context)
def display_1789133645(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133645"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133645"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133645.html', context)
def display_1789804078(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804078"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804078"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804078.html', context)
def display_1789805465(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789805465"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789805465"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789805465.html', context)
def display_1838559868(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838559868"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838559868"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838559868.html', context)
def display_1789349028(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789349028"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789349028"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349028.html', context)
def display_1789615534(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615534"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615534"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615534.html', context)
def display_1789807336(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807336"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807336"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807336.html', context)
def display_1838980415(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838980415"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838980415"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838980415.html', context)
def display_1838986189(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838986189"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838986189"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838986189.html', context)
def display_1838980849(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838980849"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838980849"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838980849.html', context)
def display_1789616131(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789616131"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789616131"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789616131.html', context)
def display_1838558128(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838558128"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838558128"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838558128.html', context)
def display_1789532582(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532582"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532582"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532582.html', context)
def display_183855422X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183855422X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183855422X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183855422X.html', context)
def display_1789531365(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531365"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531365"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531365.html', context)
def display_1838553061(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838553061"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838553061"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838553061.html', context)
def display_1800201206(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1800201206"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1800201206"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1800201206.html', context)
def display_1838550291(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838550291"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838550291"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550291.html', context)
def display_178829811X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178829811X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178829811X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178829811X.html', context)
def display_1789610788(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789610788"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789610788"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610788.html', context)
def display_1789617316(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617316"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617316"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617316.html', context)
def display_1838985298(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838985298"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838985298"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838985298.html', context)
def display_1787288943(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1787288943"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1787288943"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787288943.html', context)
def display_1788629159(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788629159"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788629159"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629159.html', context)
def display_1789137756(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137756"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137756"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137756.html', context)
def display_1789538513(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538513"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538513"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538513.html', context)
def display_178980437X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178980437X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178980437X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980437X.html', context)
def display_178980941X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178980941X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178980941X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980941X.html', context)
def display_1789612349(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612349"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612349"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612349.html', context)
def display_1789950686(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789950686"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789950686"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789950686.html', context)
def display_1789954398(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954398"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954398"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954398.html', context)
def display_1838558802(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838558802"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838558802"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838558802.html', context)
def display_1838550356(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838550356"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838550356"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838550356.html', context)
def display_1838552189(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838552189"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838552189"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838552189.html', context)
def display_1838556338(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838556338"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838556338"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838556338.html', context)
def display_1838644652(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838644652"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838644652"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838644652.html', context)
def display_1838640169(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838640169"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838640169"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838640169.html', context)
def display_1838829024(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838829024"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838829024"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838829024.html', context)
def display_1788830644(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788830644"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788830644"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788830644.html', context)
def display_1788992598(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992598"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992598"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992598.html', context)
def display_1789136369(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136369"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136369"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136369.html', context)
def display_1789802350(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802350"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802350"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802350.html', context)
def display_1789952298(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789952298"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789952298"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789952298.html', context)
def display_1789538548(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538548"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538548"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538548.html', context)
def display_1789616190(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789616190"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789616190"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789616190.html', context)
def display_178995231X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178995231X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178995231X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178995231X.html', context)
def display_1838825665(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838825665"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838825665"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838825665.html', context)
def display_1789802075(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802075"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802075"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802075.html', context)
def display_178961290X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178961290X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178961290X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178961290X.html', context)
def display_1838822364(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838822364"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838822364"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838822364.html', context)
def display_1789538920(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538920"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538920"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538920.html', context)
def display_1789808286(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808286"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808286"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808286.html', context)
def display_1838649956(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838649956"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838649956"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838649956.html', context)
def display_1789349796(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789349796"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789349796"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349796.html', context)
def display_1838823735(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838823735"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838823735"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838823735.html', context)
def display_1951442008(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1951442008"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1951442008"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1951442008.html', context)
def display_1789341078(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341078"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341078"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341078.html', context)
def display_1785284894(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1785284894"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1785284894"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1785284894.html', context)
def display_1789349869(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789349869"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789349869"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349869.html', context)
def display_1951442016(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1951442016"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1951442016"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1951442016.html', context)
def display_1788839250(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788839250"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788839250"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839250.html', context)
def display_1789130557(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789130557"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789130557"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789130557.html', context)
def display_1789133416(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133416"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133416"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133416.html', context)
def display_1789346118(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346118"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346118"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346118.html', context)
def display_1789348811(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348811"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348811"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348811.html', context)
def display_1789340721(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340721"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340721"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340721.html', context)
def display_1789538203(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538203"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538203"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538203.html', context)
def display_1789535301(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535301"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535301"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535301.html', context)
def display_1789537584(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789537584"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789537584"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537584.html', context)
def display_1789806984(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789806984"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789806984"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789806984.html', context)
def display_1838645578(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838645578"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838645578"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838645578.html', context)
def display_1789950341(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789950341"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789950341"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789950341.html', context)
def display_1787121321(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1787121321"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1787121321"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787121321.html', context)
def display_1788478290(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788478290"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788478290"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788478290.html', context)
def display_1788834135(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788834135"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788834135"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788834135.html', context)
def display_1788834097(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788834097"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788834097"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788834097.html', context)
def display_1788998081(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788998081"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788998081"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788998081.html', context)
def display_1789136725(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136725"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136725"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136725.html', context)
def display_1789136202(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136202"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136202"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136202.html', context)
def display_1789137799(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137799"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137799"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137799.html', context)
def display_1789139864(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789139864"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789139864"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789139864.html', context)
def display_1789132878(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789132878"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789132878"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132878.html', context)
def display_1789346460(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346460"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346460"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346460.html', context)
def display_1789345367(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789345367"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789345367"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789345367.html', context)
def display_1789345073(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789345073"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789345073"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789345073.html', context)
def display_1789345375(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789345375"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789345375"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789345375.html', context)
def display_1789534100(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534100"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534100"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534100.html', context)
def display_1789535603(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535603"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535603"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535603.html', context)
def display_1789534887(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534887"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534887"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534887.html', context)
def display_1789614813(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789614813"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789614813"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789614813.html', context)
def display_1789619890(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789619890"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789619890"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789619890.html', context)
def display_1789807212(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807212"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807212"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807212.html', context)
def display_1789808898(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808898"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808898"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808898.html', context)
def display_1789804930(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804930"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804930"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804930.html', context)
def display_1789809312(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789809312"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789809312"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789809312.html', context)
def display_1789615402(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615402"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615402"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615402.html', context)
def display_1789954339(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954339"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954339"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954339.html', context)
def display_1789956501(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789956501"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789956501"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956501.html', context)
def display_1789957052(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789957052"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789957052"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789957052.html', context)
def display_1838551026(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838551026"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838551026"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838551026.html', context)
def display_183855226X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183855226X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183855226X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183855226X.html', context)
def display_1838551069(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838551069"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838551069"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838551069.html', context)
def display_1838828974(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838828974"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838828974"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838828974.html', context)
def display_1789345154(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789345154"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789345154"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789345154.html', context)
def display_1789531373(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531373"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531373"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531373.html', context)
def display_1789618924(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789618924"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789618924"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789618924.html', context)
def display_1789619785(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789619785"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789619785"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789619785.html', context)
def display_1789809770(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789809770"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789809770"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789809770.html', context)
def display_1789804590(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804590"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804590"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804590.html', context)
def display_1789954924(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954924"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954924"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954924.html', context)
def display_1789955319(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789955319"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789955319"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789955319.html', context)
def display_1788835654(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788835654"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788835654"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788835654.html', context)
def display_178980115X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178980115X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178980115X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980115X.html', context)
def display_1789800269(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800269"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800269"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800269.html', context)
def display_1838555072(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838555072"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838555072"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838555072.html', context)
def display_1789345804(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789345804"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789345804"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789345804.html', context)
def display_1789803306(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789803306"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789803306"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803306.html', context)
def display_1788295862(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788295862"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788295862"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788295862.html', context)
def display_1789955289(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789955289"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789955289"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789955289.html', context)
def display_1788834933(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788834933"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788834933"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788834933.html', context)
def display_1788994078(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788994078"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788994078"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788994078.html', context)
def display_1789139007(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789139007"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789139007"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789139007.html', context)
def display_1789344077(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344077"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344077"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344077.html', context)
def display_1789344522(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344522"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344522"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344522.html', context)
def display_1789344964(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344964"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344964"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344964.html', context)
def display_1789530172(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789530172"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789530172"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789530172.html', context)
def display_1789536103(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536103"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536103"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536103.html', context)
def display_1789532051(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532051"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532051"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532051.html', context)
def display_1789536081(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536081"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536081"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536081.html', context)
def display_1789533589(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533589"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533589"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533589.html', context)
def display_1789618509(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789618509"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789618509"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789618509.html', context)
def display_1789613019(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789613019"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789613019"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789613019.html', context)
def display_1789615224(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615224"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615224"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615224.html', context)
def display_1789617871(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617871"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617871"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617871.html', context)
def display_1789802164(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802164"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802164"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802164.html', context)
def display_1789808456(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808456"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808456"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808456.html', context)
def display_1789800226(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800226"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800226"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800226.html', context)
def display_1789956870(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789956870"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789956870"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956870.html', context)
def display_1789954045(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954045"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954045"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954045.html', context)
def display_1789959411(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789959411"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789959411"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789959411.html', context)
def display_1789340764(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340764"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340764"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340764.html', context)
def display_1789349338(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789349338"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789349338"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349338.html', context)
def display_1789346347(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346347"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346347"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346347.html', context)
def display_1789344913(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344913"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344913"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344913.html', context)
def display_1789535298(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535298"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535298"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535298.html', context)
def display_178953075X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178953075X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178953075X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178953075X.html', context)
def display_1789611857(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789611857"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789611857"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789611857.html', context)
def display_1789809509(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789809509"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789809509"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789809509.html', context)
def display_1789802563(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802563"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802563"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802563.html', context)
def display_1789958091(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789958091"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789958091"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789958091.html', context)
def display_1789952301(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789952301"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789952301"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789952301.html', context)
def display_1838644334(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838644334"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838644334"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838644334.html', context)
def display_183864413X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183864413X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183864413X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183864413X.html', context)
def display_1788999894(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788999894"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788999894"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788999894.html', context)
def display_1789130751(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789130751"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789130751"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789130751.html', context)
def display_1789801516(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789801516"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789801516"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789801516.html', context)
def display_1789802377(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802377"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802377"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802377.html', context)
def display_1789802997(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802997"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802997"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802997.html', context)
def display_1789612365(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612365"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612365"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612365.html', context)
def display_1788839528(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788839528"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788839528"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839528.html', context)
def display_1789803829(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789803829"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789803829"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803829.html', context)
def display_1789956277(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789956277"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789956277"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956277.html', context)
def display_1789956390(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789956390"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789956390"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956390.html', context)
def display_1789133270(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133270"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133270"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133270.html', context)
def display_1789951542(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789951542"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789951542"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789951542.html', context)
def display_1838646116(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838646116"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838646116"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838646116.html', context)
def display_1789804531(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804531"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804531"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804531.html', context)
def display_1789801737(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789801737"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789801737"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789801737.html', context)
def display_1789801494(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789801494"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789801494"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789801494.html', context)
def display_178961337X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178961337X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178961337X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178961337X.html', context)
def display_1789808731(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808731"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808731"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808731.html', context)
def display_1789612071(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612071"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612071"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612071.html', context)
def display_1789610702(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789610702"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789610702"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610702.html', context)
def display_1788296222(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788296222"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788296222"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788296222.html', context)
def display_1788390415(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788390415"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788390415"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788390415.html', context)
def display_1788479122(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788479122"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788479122"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788479122.html', context)
def display_1788628462(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788628462"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788628462"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788628462.html', context)
def display_1788620445(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788620445"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788620445"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788620445.html', context)
def display_1788994019(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788994019"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788994019"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788994019.html', context)
def display_178899406X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178899406X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178899406X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178899406X.html', context)
def display_1788995171(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995171"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995171"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995171.html', context)
def display_1788990226(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788990226"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788990226"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788990226.html', context)
def display_1789138906(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789138906"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789138906"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138906.html', context)
def display_1789348277(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348277"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348277"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348277.html', context)
def display_1789346649(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346649"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346649"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346649.html', context)
def display_1789342481(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342481"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342481"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342481.html', context)
def display_1789340780(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340780"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340780"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340780.html', context)
def display_1789533880(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533880"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533880"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533880.html', context)
def display_1789532426(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532426"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532426"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532426.html', context)
def display_1789536707(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536707"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536707"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536707.html', context)
def display_1789536669(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536669"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536669"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536669.html', context)
def display_1789532019(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532019"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532019"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532019.html', context)
def display_1789617375(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617375"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617375"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617375.html', context)
def display_1789616727(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789616727"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789616727"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789616727.html', context)
def display_1789800943(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800943"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800943"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800943.html', context)
def display_1789808537(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808537"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808537"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808537.html', context)
def display_1789802814(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802814"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802814"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802814.html', context)
def display_1789800110(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800110"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800110"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800110.html', context)
def display_1789803233(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789803233"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789803233"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803233.html', context)
def display_1789610087(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789610087"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789610087"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610087.html', context)
def display_178995603X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178995603X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178995603X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178995603X.html', context)
def display_1789619459(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789619459"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789619459"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789619459.html', context)
def display_183864010X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="183864010X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="183864010X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '183864010X.html', context)
def display_1789346207(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346207"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346207"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346207.html', context)
def display_1789343240(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343240"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343240"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343240.html', context)
def display_1789617405(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617405"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617405"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617405.html', context)
def display_178995276X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178995276X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178995276X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178995276X.html', context)
def display_1789132304(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789132304"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789132304"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132304.html', context)
def display_1789530725(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789530725"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789530725"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789530725.html', context)
def display_178953481X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178953481X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178953481X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178953481X.html', context)
def display_1789138418(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789138418"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789138418"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138418.html', context)
def display_1789613965(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789613965"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789613965"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789613965.html', context)
def display_1789954525(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954525"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954525"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954525.html', context)
def display_1788627857(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788627857"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788627857"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788627857.html', context)
def display_1788399234(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788399234"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788399234"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788399234.html', context)
def display_1789802024(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802024"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802024"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802024.html', context)
def display_1788477545(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788477545"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788477545"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788477545.html', context)
def display_1788623797(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788623797"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788623797"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788623797.html', context)
def display_1788627962(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788627962"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788627962"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788627962.html', context)
def display_1788623762(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788623762"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788623762"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788623762.html', context)
def display_1788830571(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788830571"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788830571"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788830571.html', context)
def display_1788836294(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788836294"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788836294"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788836294.html', context)
def display_178883786X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178883786X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178883786X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178883786X.html', context)
def display_1788834445(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788834445"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788834445"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788834445.html', context)
def display_1788836065(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788836065"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788836065"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788836065.html', context)
def display_1788629302(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788629302"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788629302"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629302.html', context)
def display_1788991923(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788991923"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788991923"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991923.html', context)
def display_1788990862(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788990862"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788990862"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788990862.html', context)
def display_1788992660(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992660"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992660"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992660.html', context)
def display_1788994612(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788994612"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788994612"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788994612.html', context)
def display_1788994175(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788994175"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788994175"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788994175.html', context)
def display_1788996925(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788996925"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788996925"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788996925.html', context)
def display_178899082X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178899082X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178899082X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178899082X.html', context)
def display_1789134528(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789134528"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789134528"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789134528.html', context)
def display_1789136431(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136431"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136431"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136431.html', context)
def display_1789136679(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136679"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136679"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136679.html', context)
def display_1789136601(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136601"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136601"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136601.html', context)
def display_1789132983(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789132983"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789132983"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132983.html', context)
def display_1789349109(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789349109"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789349109"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349109.html', context)
def display_1789346576(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346576"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346576"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346576.html', context)
def display_1789341159(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341159"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341159"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341159.html', context)
def display_1789342759(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342759"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342759"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342759.html', context)
def display_1789349257(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789349257"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789349257"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789349257.html', context)
def display_1789341698(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341698"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341698"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341698.html', context)
def display_1789533384(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533384"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533384"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533384.html', context)
def display_1789531241(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531241"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531241"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531241.html', context)
def display_1789535468(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535468"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535468"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535468.html', context)
def display_1789533996(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533996"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533996"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533996.html', context)
def display_1789614503(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789614503"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789614503"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789614503.html', context)
def display_1789618002(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789618002"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789618002"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789618002.html', context)
def display_1789804035(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804035"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804035"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804035.html', context)
def display_1789803055(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789803055"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789803055"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803055.html', context)
def display_1789800102(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800102"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800102"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800102.html', context)
def display_1789802598(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802598"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802598"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802598.html', context)
def display_1838551603(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838551603"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838551603"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838551603.html', context)
def display_1838555137(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1838555137"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1838555137"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1838555137.html', context)
def display_1788831438(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788831438"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788831438"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788831438.html', context)
def display_1788832566(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788832566"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788832566"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788832566.html', context)
def display_1788990773(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788990773"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788990773"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788990773.html', context)
def display_178913322X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178913322X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178913322X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913322X.html', context)
def display_178934056X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178934056X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178934056X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934056X.html', context)
def display_1789615704(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615704"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615704"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615704.html', context)
def display_1789139392(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789139392"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789139392"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789139392.html', context)
def display_1789956021(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789956021"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789956021"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789956021.html', context)
def display_178899552X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178899552X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178899552X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178899552X.html', context)
def display_1789346134(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346134"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346134"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346134.html', context)
def display_1789342678(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342678"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342678"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342678.html', context)
def display_1789340268(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340268"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340268"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340268.html', context)
def display_1789348463(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348463"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348463"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348463.html', context)
def display_1789617847(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617847"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617847"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617847.html', context)
def display_1789807948(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807948"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807948"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807948.html', context)
def display_178913224X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178913224X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178913224X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913224X.html', context)
def display_1788629353(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788629353"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788629353"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629353.html', context)
def display_1788992288(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992288"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992288"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992288.html', context)
def display_1788995597(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995597"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995597"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995597.html', context)
def display_1788992873(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992873"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992873"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992873.html', context)
def display_1789139902(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789139902"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789139902"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789139902.html', context)
def display_178934641X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178934641X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178934641X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934641X.html', context)
def display_178934252X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178934252X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178934252X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934252X.html', context)
def display_1789532191(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532191"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532191"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532191.html', context)
def display_1789536642(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536642"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536642"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536642.html', context)
def display_1789534208(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534208"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534208"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534208.html', context)
def display_1789950066(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789950066"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789950066"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789950066.html', context)
def display_1788475143(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788475143"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788475143"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788475143.html', context)
def display_178913871X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178913871X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178913871X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913871X.html', context)
def display_1789131014(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131014"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131014"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131014.html', context)
def display_1789532361(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532361"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532361"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532361.html', context)
def display_1789532477(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532477"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532477"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532477.html', context)
def display_1789617057(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617057"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617057"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617057.html', context)
def display_178995455X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178995455X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178995455X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178995455X.html', context)
def display_1788476247(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788476247"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788476247"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788476247.html', context)
def display_1788997824(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788997824"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788997824"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997824.html', context)
def display_1789533570(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533570"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533570"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533570.html', context)
def display_1789537509(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789537509"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789537509"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537509.html', context)
def display_1789612764(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612764"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612764"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612764.html', context)
def display_1789807972(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807972"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807972"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807972.html', context)
def display_1787289281(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1787289281"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1787289281"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787289281.html', context)
def display_178829274X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178829274X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178829274X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178829274X.html', context)
def display_1788838017(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788838017"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788838017"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788838017.html', context)
def display_1788992741(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992741"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992741"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992741.html', context)
def display_1789137888(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137888"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137888"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137888.html', context)
def display_178913336X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178913336X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178913336X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913336X.html', context)
def display_1789346568(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346568"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346568"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346568.html', context)
def display_1789341655(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341655"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341655"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341655.html', context)
def display_1789344875(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344875"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344875"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344875.html', context)
def display_1789532221(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532221"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532221"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532221.html', context)
def display_1789614953(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789614953"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789614953"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789614953.html', context)
def display_1789617588(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617588"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617588"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617588.html', context)
def display_178980454X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178980454X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178980454X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980454X.html', context)
def display_1789955653(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789955653"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789955653"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789955653.html', context)
def display_1789135567(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789135567"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789135567"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789135567.html', context)
def display_1789348668(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348668"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348668"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348668.html', context)
def display_1789534097(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534097"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534097"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534097.html', context)
def display_1789805651(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789805651"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789805651"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789805651.html', context)
def display_178980776X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178980776X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178980776X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178980776X.html', context)
def display_1789805023(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789805023"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789805023"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789805023.html', context)
def display_1789959632(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789959632"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789959632"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789959632.html', context)
def display_1789954940(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954940"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954940"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954940.html', context)
def display_1789347033(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789347033"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789347033"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347033.html', context)
def display_1788992245(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992245"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992245"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992245.html', context)
def display_1789133939(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133939"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133939"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133939.html', context)
def display_1789340500(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340500"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340500"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340500.html', context)
def display_1789806429(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789806429"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789806429"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789806429.html', context)
def display_1789801656(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789801656"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789801656"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789801656.html', context)
def display_1788622596(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788622596"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788622596"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788622596.html', context)
def display_1789808979(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808979"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808979"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808979.html', context)
def display_1788475682(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788475682"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788475682"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788475682.html', context)
def display_1788390075(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788390075"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788390075"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788390075.html', context)
def display_178862582X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178862582X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178862582X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178862582X.html', context)
def display_1788839560(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788839560"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788839560"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839560.html', context)
def display_1788620909(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788620909"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788620909"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788620909.html', context)
def display_1788626893(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788626893"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788626893"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788626893.html', context)
def display_1788997271(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788997271"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788997271"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997271.html', context)
def display_1788991672(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788991672"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788991672"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991672.html', context)
def display_1788993403(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788993403"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788993403"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788993403.html', context)
def display_1789139406(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789139406"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789139406"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789139406.html', context)
def display_1789137233(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137233"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137233"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137233.html', context)
def display_1789132339(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789132339"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789132339"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132339.html', context)
def display_1789132215(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789132215"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789132215"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132215.html', context)
def display_1789130387(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789130387"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789130387"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789130387.html', context)
def display_1789341175(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341175"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341175"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341175.html', context)
def display_1789345391(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789345391"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789345391"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789345391.html', context)
def display_1789343739(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343739"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343739"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343739.html', context)
def display_1789341094(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341094"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341094"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341094.html', context)
def display_1789340624(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340624"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340624"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340624.html', context)
def display_1789344697(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344697"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344697"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344697.html', context)
def display_178934753X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178934753X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178934753X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934753X.html', context)
def display_1789341221(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341221"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341221"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341221.html', context)
def display_1789347394(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789347394"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789347394"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347394.html', context)
def display_1789538335(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538335"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538335"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538335.html', context)
def display_1789533910(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789533910"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789533910"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789533910.html', context)
def display_1789534348(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534348"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534348"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534348.html', context)
def display_1789610443(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789610443"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789610443"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610443.html', context)
def display_1789618827(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789618827"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789618827"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789618827.html', context)
def display_1789615267(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615267"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615267"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615267.html', context)
def display_1789804957(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804957"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804957"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804957.html', context)
def display_1788998367(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788998367"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788998367"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788998367.html', context)
def display_1788996348(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788996348"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788996348"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788996348.html', context)
def display_1789340748(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340748"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340748"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340748.html', context)
def display_1789342228(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342228"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342228"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342228.html', context)
def display_1789347327(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789347327"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789347327"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347327.html', context)
def display_1789531098(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531098"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531098"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531098.html', context)
def display_1789537223(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789537223"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789537223"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537223.html', context)
def display_1789531942(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531942"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531942"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531942.html', context)
def display_1789617693(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617693"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617693"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617693.html', context)
def display_1789610257(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789610257"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789610257"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610257.html', context)
def display_1789806267(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789806267"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789806267"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789806267.html', context)
def display_1789803551(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789803551"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789803551"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803551.html', context)
def display_1788474392(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788474392"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788474392"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788474392.html', context)
def display_1788997425(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788997425"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788997425"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997425.html', context)
def display_1788993918(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788993918"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788993918"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788993918.html', context)
def display_1789132762(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789132762"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789132762"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132762.html', context)
def display_1789343054(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343054"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343054"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343054.html', context)
def display_1789131510(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131510"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131510"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131510.html', context)
def display_1789954533(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789954533"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789954533"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789954533.html', context)
def display_1951442059(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1951442059"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1951442059"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1951442059.html', context)
def display_1789806194(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789806194"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789806194"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789806194.html', context)
def display_1786468654(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1786468654"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1786468654"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1786468654.html', context)
def display_1787127885(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1787127885"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1787127885"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787127885.html', context)
def display_1788629418(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788629418"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788629418"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629418.html', context)
def display_178862288X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178862288X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178862288X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178862288X.html', context)
def display_1788621751(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788621751"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788621751"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788621751.html', context)
def display_1788837681(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788837681"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788837681"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788837681.html', context)
def display_178883884X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178883884X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178883884X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178883884X.html', context)
def display_1788836308(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788836308"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788836308"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788836308.html', context)
def display_1788629698(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788629698"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788629698"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788629698.html', context)
def display_1788994590(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788994590"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788994590"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788994590.html', context)
def display_1788998472(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788998472"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788998472"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788998472.html', context)
def display_1788995570(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995570"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995570"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995570.html', context)
def display_1788995473(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995473"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995473"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995473.html', context)
def display_1788991060(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788991060"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788991060"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991060.html', context)
def display_1788995406(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995406"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995406"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995406.html', context)
def display_1789131499(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131499"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131499"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131499.html', context)
def display_1789133203(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133203"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133203"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133203.html', context)
def display_1789134803(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789134803"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789134803"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789134803.html', context)
def display_1789137381(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137381"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137381"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137381.html', context)
def display_1789131952(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131952"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131952"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131952.html', context)
def display_178913028X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178913028X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178913028X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913028X.html', context)
def display_1789130662(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789130662"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789130662"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789130662.html', context)
def display_1788997093(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788997093"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788997093"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997093.html', context)
def display_1789138736(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789138736"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789138736"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138736.html', context)
def display_1788999835(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788999835"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788999835"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788999835.html', context)
def display_1789343046(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343046"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343046"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343046.html', context)
def display_1789342872(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342872"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342872"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342872.html', context)
def display_178934414X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178934414X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178934414X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934414X.html', context)
def display_1789538505(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538505"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538505"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538505.html', context)
def display_1789617723(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789617723"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789617723"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789617723.html', context)
def display_1789806070(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789806070"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789806070"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789806070.html', context)
def display_1789802865(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789802865"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789802865"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789802865.html', context)
def display_1789807328(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789807328"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789807328"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789807328.html', context)
def display_1789808812(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789808812"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789808812"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789808812.html', context)
def display_1789958172(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789958172"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789958172"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789958172.html', context)
def display_1788994728(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788994728"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788994728"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788994728.html', context)
def display_1789133602(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133602"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133602"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133602.html', context)
def display_1789343704(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343704"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343704"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343704.html', context)
def display_1789340314(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340314"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340314"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340314.html', context)
def display_1789537819(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789537819"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789537819"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537819.html', context)
def display_1789536596(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536596"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536596"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536596.html', context)
def display_1789612489(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612489"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612489"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612489.html', context)
def display_1789615852(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789615852"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789615852"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789615852.html', context)
def display_1789616700(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789616700"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789616700"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789616700.html', context)
def display_1789803810(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789803810"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789803810"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789803810.html', context)
def display_1788622014(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788622014"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788622014"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788622014.html', context)
def display_1788836960(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788836960"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788836960"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788836960.html', context)
def display_1789341760(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341760"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341760"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341760.html', context)
def display_1789138728(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789138728"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789138728"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138728.html', context)
def display_1788997468(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788997468"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788997468"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997468.html', context)
def display_1789344107(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344107"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344107"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344107.html', context)
def display_1789535425(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535425"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535425"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535425.html', context)
def display_1789616603(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789616603"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789616603"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789616603.html', context)
def display_178913496X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178913496X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178913496X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178913496X.html', context)
def display_1789135710(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789135710"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789135710"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789135710.html', context)
def display_1788991214(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788991214"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788991214"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991214.html', context)
def display_1789138051(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789138051"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789138051"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138051.html', context)
def display_1788474295(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788474295"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788474295"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788474295.html', context)
def display_1787284956(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1787284956"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1787284956"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787284956.html', context)
def display_1789136326(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136326"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136326"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136326.html', context)
def display_1788298594(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788298594"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788298594"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788298594.html', context)
def display_1788397649(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788397649"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788397649"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788397649.html', context)
def display_1788477324(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788477324"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788477324"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788477324.html', context)
def display_1788623444(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788623444"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788623444"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788623444.html', context)
def display_1788624351(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788624351"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788624351"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788624351.html', context)
def display_1788831861(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788831861"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788831861"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788831861.html', context)
def display_1788833341(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788833341"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788833341"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788833341.html', context)
def display_1788993705(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788993705"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788993705"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788993705.html', context)
def display_1788991613(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788991613"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788991613"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991613.html', context)
def display_1788994469(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788994469"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788994469"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788994469.html', context)
def display_178899616X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178899616X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178899616X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178899616X.html', context)
def display_1789132355(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789132355"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789132355"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789132355.html', context)
def display_1789139627(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789139627"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789139627"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789139627.html', context)
def display_1789135796(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789135796"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789135796"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789135796.html', context)
def display_1789343712(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343712"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343712"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343712.html', context)
def display_1789342090(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342090"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342090"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342090.html', context)
def display_1789348013(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348013"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348013"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348013.html', context)
def display_1789346487(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346487"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346487"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346487.html', context)
def display_1789535549(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535549"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535549"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535549.html', context)
def display_1789532558(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532558"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532558"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532558.html', context)
def display_1789534607(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534607"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534607"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534607.html', context)
def display_178961774X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178961774X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178961774X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178961774X.html', context)
def display_1789619637(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789619637"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789619637"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789619637.html', context)
def display_1789619475(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789619475"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789619475"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789619475.html', context)
def display_1789612012(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612012"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612012"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612012.html', context)
def display_1788471156(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788471156"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788471156"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788471156.html', context)
def display_178883058X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178883058X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178883058X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178883058X.html', context)
def display_1788838688(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788838688"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788838688"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788838688.html', context)
def display_1788995236(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995236"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995236"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995236.html', context)
def display_1788991443(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788991443"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788991443"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991443.html', context)
def display_1788992512(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992512"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992512"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992512.html', context)
def display_1788993489(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788993489"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788993489"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788993489.html', context)
def display_1789136245(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789136245"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789136245"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789136245.html', context)
def display_1789342252(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342252"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342252"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342252.html', context)
def display_1789343534(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343534"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343534"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343534.html', context)
def display_1789346797(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789346797"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789346797"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789346797.html', context)
def display_178953786X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178953786X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178953786X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178953786X.html', context)
def display_1789534496(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789534496"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789534496"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789534496.html', context)
def display_1789532930(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789532930"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789532930"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789532930.html', context)
def display_1789538831(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538831"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538831"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538831.html', context)
def display_1789539978(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789539978"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789539978"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789539978.html', context)
def display_1789535751(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789535751"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789535751"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789535751.html', context)
def display_1789612713(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612713"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612713"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612713.html', context)
def display_1789612152(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612152"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612152"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612152.html', context)
def display_1789612896(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612896"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612896"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612896.html', context)
def display_1789801664(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789801664"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789801664"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789801664.html', context)
def display_1788470419(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788470419"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788470419"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788470419.html', context)
def display_1788625447(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788625447"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788625447"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788625447.html', context)
def display_1788627903(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788627903"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788627903"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788627903.html', context)
def display_1788993128(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788993128"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788993128"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788993128.html', context)
def display_1789137616(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137616"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137616"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137616.html', context)
def display_1789133807(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133807"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133807"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133807.html', context)
def display_1789342384(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342384"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342384"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342384.html', context)
def display_1789619270(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789619270"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789619270"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789619270.html', context)
def display_1789612993(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789612993"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789612993"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789612993.html', context)
def display_1789800617(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789800617"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789800617"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789800617.html', context)
def display_1788470710(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788470710"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788470710"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788470710.html', context)
def display_1788479742(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788479742"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788479742"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788479742.html', context)
def display_1789348293(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348293"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348293"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348293.html', context)
def display_1789344492(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344492"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344492"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344492.html', context)
def display_178953173X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178953173X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178953173X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178953173X.html', context)
def display_1789610362(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789610362"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789610362"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789610362.html', context)
def display_1788997379(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788997379"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788997379"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997379.html', context)
def display_1788999096(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788999096"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788999096"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788999096.html', context)
def display_1788626745(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788626745"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788626745"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788626745.html', context)
def display_1789343445(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343445"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343445"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343445.html', context)
def display_1789135508(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789135508"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789135508"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789135508.html', context)
def display_1789344204(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344204"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344204"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344204.html', context)
def display_1787280543(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1787280543"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1787280543"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1787280543.html', context)
def display_1788392493(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788392493"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788392493"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788392493.html', context)
def display_1788471903(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788471903"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788471903"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788471903.html', context)
def display_1788479505(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788479505"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788479505"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788479505.html', context)
def display_1788626869(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788626869"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788626869"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788626869.html', context)
def display_1788627253(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788627253"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788627253"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788627253.html', context)
def display_1788620798(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788620798"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788620798"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788620798.html', context)
def display_1788628888(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788628888"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788628888"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788628888.html', context)
def display_1788837363(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788837363"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788837363"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788837363.html', context)
def display_1788837487(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788837487"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788837487"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788837487.html', context)
def display_1788831306(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788831306"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788831306"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788831306.html', context)
def display_1788833287(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788833287"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788833287"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788833287.html', context)
def display_1788830822(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788830822"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788830822"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788830822.html', context)
def display_1788992997(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788992997"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788992997"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788992997.html', context)
def display_1788995511(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995511"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995511"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995511.html', context)
def display_1789131898(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131898"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131898"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131898.html', context)
def display_1789130964(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789130964"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789130964"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789130964.html', context)
def display_1789137950(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137950"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137950"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137950.html', context)
def display_1789133998(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789133998"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789133998"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789133998.html', context)
def display_1789138396(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789138396"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789138396"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789138396.html', context)
def display_1789131685(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789131685"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789131685"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789131685.html', context)
def display_1788991516(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788991516"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788991516"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788991516.html', context)
def display_1789342058(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789342058"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789342058"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789342058.html', context)
def display_1789341795(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789341795"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789341795"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789341795.html', context)
def display_1789340365(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340365"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340365"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340365.html', context)
def display_1789344182(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789344182"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789344182"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789344182.html', context)
def display_1789343259(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343259"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343259"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343259.html', context)
def display_1789537126(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789537126"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789537126"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537126.html', context)
def display_1789536138(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789536138"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789536138"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789536138.html', context)
def display_1789531705(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531705"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531705"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531705.html', context)
def display_178953755X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178953755X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178953755X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178953755X.html', context)
def display_1789538254(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538254"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538254"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538254.html', context)
def display_1789611555(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789611555"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789611555"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789611555.html', context)
def display_1789804744(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789804744"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789804744"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789804744.html', context)
def display_1783980729(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1783980729"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1783980729"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1783980729.html', context)
def display_1788624068(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788624068"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788624068"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788624068.html', context)
def display_1788626508(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788626508"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788626508"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788626508.html', context)
def display_1788835441(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788835441"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788835441"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788835441.html', context)
def display_1788997050(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788997050"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788997050"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788997050.html', context)
def display_1789137403(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789137403"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789137403"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789137403.html', context)
def display_1789347998(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789347998"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789347998"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347998.html', context)
def display_178934557X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178934557X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178934557X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178934557X.html', context)
def display_1789343321(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789343321"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789343321"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789343321.html', context)
def display_1789538912(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789538912"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789538912"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789538912.html', context)
def display_1789537002(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789537002"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789537002"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789537002.html', context)
def display_1789611156(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789611156"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789611156"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789611156.html', context)
def display_1788835832(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788835832"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788835832"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788835832.html', context)
def display_1788839153(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788839153"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788839153"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788839153.html', context)
def display_1789130484(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789130484"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789130484"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789130484.html', context)
def display_1789134617(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789134617"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789134617"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789134617.html', context)
def display_1789135990(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789135990"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789135990"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789135990.html', context)
def display_1789347564(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789347564"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789347564"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347564.html', context)
def display_1789531756(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789531756"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789531756"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789531756.html', context)
def display_1789614821(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789614821"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789614821"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789614821.html', context)
def display_1788626176(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788626176"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788626176"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788626176.html', context)
def display_1789130336(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789130336"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789130336"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789130336.html', context)
def display_1788995392(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995392"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995392"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995392.html', context)
def display_1789340470(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789340470"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789340470"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789340470.html', context)
def display_1789348609(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789348609"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789348609"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789348609.html', context)
def display_1789347467(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1789347467"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1789347467"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1789347467.html', context)
def display_178899289X(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="178899289X"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="178899289X"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '178899289X.html', context)
def display_1788999045(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788999045"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788999045"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788999045.html', context)
def display_1788830628(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788830628"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788830628"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788830628.html', context)
def display_1788995783(request):
    items = RawData.objects.raw('SELECT * from bootstrap_rawdata Where isbn=="1788995783"')
    collections = TopList.objects.raw('SELECT * from bootstrap_toplist  Where isbn=="1788995783"')
    context = {
        'items': items,
        'collections' : collections,
    }
    return render(request, '1788995783.html', context)
