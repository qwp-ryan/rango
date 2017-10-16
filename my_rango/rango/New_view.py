from .models import *
from django.utils import timezone
from django.shortcuts import render



#def Welcom():
# 这个view sign in 或者 sign up



def ShowDelegation(Request):#这个view要把所有的团组列出来，普通人只能看到自己参加的和自己填报的团组情况
    Delegation_list = Delegation.objects.all()
#    Delegation_list = Delegation.objects.all(Delegation.time_leave-timezone.now)
    context_dict = {'delegations': Delegation_list}
    response = render(Request, 'rang/index_2.html', context_dict)
    return response



def DelegationProcess(Request,Delegation_title):
#这个view想要把一个团组的整个申请填报流程都展现出来，每一步的信息全都表现出来。
    context_dict = {}
    try:
        delegation = Delegation.objects.get(title = Delegation_title)
        passport = PassportInformation.object.get(person=delegation.Members)
        visa = VisaInformation.object.get(Passport=passport)
        permission = Permission.objects.get(delegation=delegation)
        budget = BudgetInformation.objects.get(delegation=delegation)
        summary = SummaryInformation.object.get(delegation=delegation)



        context_dict['delegation'] = delegation
        context_dict['Passport'] = passport
        context_dict['Visa'] = visa
        context_dict['Permision'] = permission
        context_dict['Budget'] = budget
        context_dict['Summary'] = summary



    except Delegation.DoesNotExist:
        context_dict['delegation'] = None
    return render(Request,'rang/category_2.html',context_dict)
#


