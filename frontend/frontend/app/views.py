from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .serializers import FlatSerializer, SheduleSerializer
from . import constants
import requests
from datetime import datetime


def index(request):
    return HttpResponseRedirect('flat')


def flat(request):
    template = loader.get_template('app/index.html')
    context_dict = {'is_logged': is_logged(request)}
    try:
        if request.REQUEST.has_key('page'):
            page = request.REQUEST['page']
        else:
            page = 1
        r = requests.get(constants.BACKFLAT + 'flat/', params={
            'page': page,
        })
        data = r.json()
        serializer = FlatSerializer(data=data["results"], many=True)
        if serializer.is_valid():
            flat_list = serializer.save()
            context_dict['flat_list'] = flat_list
        context_dict['count'] = data['count']
        context_dict['service_available'] = True
    except:
        context_dict['service_available'] = False

    # if request.REQUEST.has_key('page'):
    #     current_page = request.REQUEST['page']
    # else:
    #     current_page = 1
    # context_dict['current_page'] = current_page
    # context_dict['prev_page'] = int(current_page) - 1
    # context_dict['next_page'] = int(current_page) + 1
    context = RequestContext(request, context_dict)
    return HttpResponse(template.render(context))


def flat_detail(request, pk):
    template = loader.get_template('app/flat_detail.html')
    context_dict = {'is_logged': is_logged(request), 'flat_id': pk}
    try:
        r = requests.get(constants.BACKFLAT + 'flat/' + pk)
        data = r.json()
        serializer = FlatSerializer(data=data)
        if serializer.is_valid():
            flat = serializer.save()
            context_dict['flat'] = flat
        context_dict['service_available'] = True
    except:
        context_dict['service_available'] = False

    context = RequestContext(request, context_dict)
    return HttpResponse(template.render(context))


def flat_my(request):
    template = loader.get_template('app/flat_my.html')
    user_id = is_logged(request)
    if user_id:
        context_dict = {'is_logged': True}
        try:
            r = requests.get(constants.BACKFLAT + 'flat/my/', params={
                'user_id': user_id,
            })
            data = r.json()
            serializer = FlatSerializer(data=data["results"], many=True)
            if serializer.is_valid():
                flat_list = serializer.save()
                context_dict['flat_list'] = flat_list
            context_dict['service_available'] = True
        except:
            context_dict['service_available'] = False

        context = RequestContext(request, context_dict)
        return HttpResponse(template.render(context))

    return HttpResponseRedirect(reverse('login'))


def flat_my_detail(request, pk):
    template = loader.get_template('app/flat_my_detail.html')
    user_id = is_logged(request)
    if user_id:
        context_dict = {'is_logged': True}
        try:
            r = requests.get(constants.BACKFLAT + 'flat/my/' + pk, params={
                'user_id': user_id
            })
            data = r.json()
            serializer = FlatSerializer(data=data)
            if serializer.is_valid():
                flat = serializer.save()
                context_dict['flat'] = flat
            context_dict['service_available'] = True
        except:
            context_dict['service_available'] = False

        context = RequestContext(request, context_dict)
        return HttpResponse(template.render(context))

    return HttpResponseRedirect(reverse('login'))


def flat_my_create(request):
    template = loader.get_template('app/flat_my_create.html')
    user_id = is_logged(request)
    if user_id:
        context_dict = {'is_logged': True, 'service_available': True}
        if request.method == 'POST':
            try:
                r = requests.post(constants.BACKFLAT + 'flat/my/', data={
                    'user_id': user_id,
                    'name': request.POST['name'],
                    'rooms': request.POST['rooms'],
                    'cost': request.POST['cost'],
                    'latitude': request.POST['latitude'],
                    'longitude': request.POST['longitude'],
                })
            except:
                context_dict['service_available'] = False
                context = RequestContext(request, context_dict)
                return HttpResponse(template.render(context))

            if r.status_code == 201:
                return HttpResponseRedirect(reverse('flat_my'))
            else:
                context_dict['data'] = r.json()
                context = RequestContext(request, context_dict)
                return HttpResponse(template.render(context))

        else:
            context = RequestContext(request, context_dict)
            return HttpResponse(template.render(context))

    return HttpResponseRedirect(reverse('login'))


def shedule(request, pk):
    template = loader.get_template('app/shedule.html')
    if 'date' in request.REQUEST:
        date = datetime.strptime(request.REQUEST['date'], '%Y-%m-%d')
    else:
        date = datetime.now()
    date = date.strftime('%Y-%m-%d')
    context_dict = {'is_logged': is_logged(request), 'date': date, 'pk': pk}
    try:
        r = requests.get(constants.BACKSHEDULE + 'shedule/', params={
            'date': date,
            'flat_id': pk
        })
        data = r.json()
        serializer = SheduleSerializer(data=data, many=True)
        if serializer.is_valid():
            shedule_list = serializer.save()
            context_dict['shedule_list'] = shedule_list
        context_dict['service_available'] = True
    except:
        context_dict['service_available'] = False

    context = RequestContext(request, context_dict)
    return HttpResponse(template.render(context))


def reservation(request, pk):
    template = loader.get_template('app/reservation.html')
    user_id = is_logged(request)
    if user_id:
        context_dict = {'is_logged': True, 'service_available': True}
        if request.method == 'POST':
            try:
                r = requests.post(constants.BACKRESERVATION + 'reservation/', data={
                    'user_id': user_id,
                    'flat_id': pk,
                    'date': request.POST['date'],
                    'date_to': request.POST['date_to'],
                    'busy_from': request.POST['busy_from'],
                    'busy_to': request.POST['busy_to'],
                })
            except:
                context_dict['service_available'] = False
                context = RequestContext(request, context_dict)
                return HttpResponse(template.render(context))

            if r.status_code == 201:
                return HttpResponseRedirect(reverse('index'))
            else:
                context_dict['data'] = r.json()
                context = RequestContext(request, context_dict)
                return HttpResponse(template.render(context))

        else:
            context = RequestContext(request, context_dict)
            return HttpResponse(template.render(context))

    return HttpResponseRedirect(reverse('login'))


def register(request):
    template = loader.get_template('app/register.html')
    context_dict = {'service_available': True}
    if request.method == 'GET':
        context = RequestContext(request, context_dict)
        return HttpResponse(template.render(context))
    elif request.method == 'POST':
        try:
            r = requests.post(constants.BACKSESSION + 'register/', data={
                "username": request.POST["username"],
                "password": request.POST["password"],
            })
        except:
            context_dict['service_available'] = False
            context = RequestContext(request, context_dict)
            return HttpResponse(template.render(context))

        if r.status_code == 201:
            return HttpResponseRedirect(reverse('login'))
        else:
            context_dict['data'] = r.json()
            context = RequestContext(request, context_dict)
            return HttpResponse(template.render(context))


def login(request):
    template = loader.get_template('app/login.html')
    context_dict = {'service_available': True}
    if request.method == 'GET':
        context = RequestContext(request, context_dict)
        return HttpResponse(template.render(context))
    elif request.method == 'POST':
        try:
            r = requests.post(constants.BACKSESSION + 'login/', data={
                'username': request.POST['username'],
                'password': request.POST['password'],
            })
        except:
            context_dict['service_available'] = False
            context = RequestContext(request, context_dict)
            return HttpResponse(template.render(context))

        data = r.json()
        if r.status_code == 200:
            token = data['token']
            response = HttpResponseRedirect('/')
            response.set_cookie('token', token)
        else:
            context_dict['data'] = data
            context = RequestContext(request, context_dict)
            response = HttpResponse(template.render(context))

        return response


def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('token')
    return response


def is_logged(request):
    if 'token' in request.COOKIES:
        headers = {'Authorization': 'Token ' + request.COOKIES['token']}
        try:
            r = requests.get(constants.BACKSESSION + 'logged-user/', headers=headers)
            if r.status_code == 200:
                data = r.json()
                return HttpResponse(data['user_id'])
            else:
                return None
        except:
            return None

    return None
