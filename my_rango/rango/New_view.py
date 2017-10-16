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


def DelegationProcess(Request, delegation):
#这个view想要把一个团组的整个申请填报流程都展现出来，每一步的信息全都表现出来。
    context_dict = {}
    passport = []
    try:
        Deleg = Delegation.objects.get(*delegation)
#        members.append(Delegation.Members.objects.filter())
#        for members in Deleg.Members:
#            passport.append(PassportInformation.object.filter(person=members))
#        visa = VisaInformation.object.filter(Passport=passport)
        permission = Permission.objects.filter(delegation=Deleg)
        budget = BudgetInformation.objects.filter(delegation=Deleg)
        summary = SummaryInformation.object.filter(delegation=Deleg)

#        context_dict['Passport'] = passport
#        context_dict['Visa'] = visa
        context_dict['Permision'] = permission
        context_dict['Budget'] = budget
        context_dict['Summary'] = summary

    except Delegation.DoesNotExist:
        context_dict['delegation'] = None
    return render(Request,'rang/category_2.html',context_dict)
#


