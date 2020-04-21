from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

import vk, json
from vk_api.helper import token


counter = 0

@csrf_exempt
@require_http_methods(['POST'])
def handler(request):
    json_data = json.loads(request.body)
    if 'type' not in json_data.keys():
        return HttpResponse('not ok')

    session = vk.Session()
    vk_api = vk.API(session, v=5.103)
    user_id = json_data['object']['message']['from_id']
    global counter
    counter += 1

    vk_api.messages.send(access_token=token, random_id=counter, user_id=user_id,
                         peer_id=user_id, message='Привет, я новый бот!')
    return HttpResponse('ok')

