from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
from .models import Event, Person, Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


#consts
error_image = '/assets/images/error.png'
success_image = '/assets/images/success.png'

# Create your views here.
def home(request):
    return render(request, "index.html")

@login_required(login_url='login')
def explore(request):
    social = Event.objects.filter(event_type='social', approved=True, expired=False)
    health = Event.objects.filter(event_type='health', approved=True, expired=False)
    return render(request, "explore.html", {"social": social, 'health': health})

def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        try:
            name = request.POST.get('eventname')
            type = request.POST.get('eventtype')
            date = request.POST.get('eventdate') 
            startime = request.POST.get('starttime') 
            endtime = request.POST.get('endtime') 
            venue = request.POST.get('venue')
            area = request.POST.get('area')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            user_recom = request.user.email
            description = request.POST.get('description')

            startime = datetime.datetime.strptime(startime, "%H:%M").time()
            endtime = datetime.datetime.strptime(endtime, "%H:%M").time()
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            user_recom = User.objects.all().get(email=user_recom)

            if startime > endtime or date < datetime.datetime.now().date():
                return JsonResponse({'message' : "Time invalid" , "status" : '401'})

            event = Event(event_name=name, 
                          event_type=type,
                          event_description=description,
                          event_date=date,
                          event_starttime=startime, 
                          event_endtime=endtime,
                          event_venue=venue,
                          event_area=area,
                          event_city=city,
                          event_pincode=int(pincode))
            event.save()
            return JsonResponse({"message":"success", "status":"200"})
        except Exception as e:
            print(e)
            return JsonResponse({"message":e, "status":"401"})
    return render(request, "contact.html")


@login_required(login_url='login')
def profile(request):
    try:
        person = Person.objects.get(email=request.user.email)
        events = Registration.objects.all().filter(person=person)
        return render(request, "profile.html", context={'person': person, 'events': events})
    except Exception as e:
        print(e)
        return render(request, 'alert.html', {"alert_type": "Information about is missing", "image": error_image})


@login_required(login_url='login')
def event(request, pk):
    event = Event.objects.all().get(id=pk)
    if request.method == 'POST':
        try:
            person = Person.objects.all().get(email=request.user.email)
            if event and person:
                registration = Registration(person=person, event=event)
                registration.save()
                return render(request, "alert.html", {'alert_type': "You have been successfully registered!", 'image': success_image})
            else:
                raise Exception()
        except Exception as e:
            print(e)
            return render(request, "alert.html", {'alert_type': "Something went wrong. Please try again!", 'image': error_image})
    return render(request, "event.html", {'event': event})


def alert(request):
    heading = "Sucess"
    img = error_image
    return render(request, "alert.html", {'alert_type': heading, 'image':img})


def login_(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user == None:
                raise Exception("Invalid email or password")
            login(request, user)
            return redirect('home')
        except Exception as e:
            print(e)
            return render(request, 'alert.html', {"alert_type": "Something went wrong!", "image": error_image})
    return render(request, "login.html")


@login_required(login_url='login')
def logout_(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            about = request.POST.get('about')
            area = request.POST.get('area')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            password = request.POST.get('password')


            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()

            user = User.objects.all().get(email=email)
            person = Person(user=user, name=name, email=email, gender=gender, area=area, city=city, pincode=pincode, phone=phone, about=about)
            person.save()
            
            return render(request, 'alert.html', {"alert_type": "Account Created Successfully", "image": success_image, "login" : True})

        except Exception as e:
            print(e)
            return render(request, 'alert.html', {"alert_type": "Something went wrong!", "image": error_image})
        
    return render(request, 'register.html')