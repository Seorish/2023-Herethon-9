from django.shortcuts import render
import json

# Create your views here.

def main(request):
    return render(request, "html/main.html")


# with open('static/json/convenience_store.json', encoding='utf-8') as json_file:
#     data = json.load(json_file)
#     convenience_stores = data['response']['body']['items']['item']
#     convenience_list = []
# for store in convenience_stores:
#     if store.get('mapx') and store.get('mapy'):
#         convenience = {
#                 "name": store['BIZPLC_NM'],
#                 "state": store['BSN_STATE_NM'],
#                 "address": store['REFINE_LOTNO_ADDR'],
#         }
#         convenience_list.append(convenience)
#         convenience_json = json.dumps(convenience_list, ensure_ascii=False)
#         return render(request, 'html/main.html', {'convenience_json': convenience_json})