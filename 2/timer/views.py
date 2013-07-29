# Create your views here.
from Login import CheckIn
from django.http import HttpResponse
def check_in(request):
    user1 = CheckIn('dollarzhaole', '0312zhl')
    user1.login()
    user1.checkin()

    # user2 = CheckIn('dollar625', '0312zhl')
    # user2.login()
    # user2.checkin()
    return HttpResponse("hello world")
