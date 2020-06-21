
import json
from django.http import HttpResponse
from django.http import JsonResponse
from testdj import models
from django.views.decorators.csrf import csrf_exempt
 
def hello(request):
    return HttpResponse("Hello world ! ")

@csrf_exempt
def score(request):
    content_type='application/json;charset=utf-8'
    if request.method == 'POST':
        pass
        data = json.loads(request.body)
        print(data)
        name = data.get('name', None)
        score = data.get('score', None)
        if not name or not score:
            print(name)
            return JsonResponse(dict(code=10001, message='缺少参数'))
        if score < 1 or score > 10000000:
            return JsonResponse(dict(code=10002, message='score超出范围'))
        t_score = models.Score.objects.get(name=name)
        print(t_score)
        if not t_score:
            t_score = models.Score()
            t_score.name = name
            t_score.score = score
            t_score.save()
        else:
            if t_score.score < score:
                t_score.score = score
                t_score.save()
        return JsonResponse(dict(code=200, message='提交成功'))
    elif request.method == 'GET':
        name = request.GET.get('name', '')
        if not name:
            return JsonResponse(dict(code=10001, message='缺少client参数'))
        start = request.GET.get('start', default=1)
        end = request.GET.get('end', default=-1)
        print(end)
        scores = models.Score.objects.all().order_by('-score')
        result = []
        score_target = None
        for i, score in enumerate(scores, 1):
            _score = {}
            _score['排名'] = i
            _score['客户端'] = score.name
            _score['分数'] = score.score
            if score.name == name:
                score_target = _score
            result.append(_score)
        
        print(result)
        if end < 0 or end > len(result): end = len(result)
        print('end %s' % end)
        result = result[start-1:end]
        print('resut: %s' % result)
        print(score_target)
        if score_target:
            print(score_target)
            result.append(score_target)
        return JsonResponse({'code': 200, 'data': result, 'message': 'ok'})

