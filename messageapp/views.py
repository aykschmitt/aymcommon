# Create your views here.
from AYMCommonMessage.messageapp.models import *
from AYMCommonMessage.messageapp.forms import *
from django.forms.models import modelformset_factory
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.mail import send_mail
#from django.views.generic.simple import direct_to_template
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404

#def mail_chooser(m):
#    emailaddress = form.cleaned_data['plant']
#    if isinstance (emailaddress, 'DBQ'):
#        emailaddress = ('kkiefer@aymcdonald.com',)
#    elif isinstance (emailaddress, 'ALB'):
#        emailaddress = ('kschmitt@aymcdonald.com')
#    return emailaddress

def create_newuser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            subject = 'New User Request Submitted for    %s,    %s' % (form.cleaned_data['last_name'],form.cleaned_data['first_name'])
            message = '\n First Name:    %s \n\n Last Name:    %s \n\n Start Date:    %s \n\n Requestor:    %s \n\n Job Title:    %s \n\n Phone Ext:    %s \n\n Fax Num:    %s \n\n Replacing Someone:    %s \n\n Replace or Setup Like:    %s \n\n Manager:    %s \n\n Dept Num:    %s \n\n PC ID:    %s \n\n Access to printers:    %s \n\n Email Via:    %s \n\n CadKey 19:    %s \n\n CadKey Viewer:    %s \n\n Pro/E:    %s \n\n Printscreen Deluxe:    %s \n\n Form Pilot Pro:    %s \n\n Comments:    %s' % (form.cleaned_data['first_name'], form.cleaned_data['last_name'], form.cleaned_data['start_date'], form.cleaned_data['requested_by'], form.cleaned_data['job_title'], form.cleaned_data['phone_ext'], form.cleaned_data['fax_ext'], form.cleaned_data['replace_check'], form.cleaned_data['replacing'], form.cleaned_data['manager'], form.cleaned_data['dept_num'], form.cleaned_data['pc_id'], form.cleaned_data['printers'], form.cleaned_data['mail_access'], form.cleaned_data['cad19'], form.cleaned_data['cadview'], form.cleaned_data['proe'], form.cleaned_data['printscreen'], form.cleaned_data['form_pilot'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['support@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(create_newuser)
    users = NewUser.objects.all()
    form = NewUserForm()
    context = Context({'title': 'New User Form', 'users': users, 'form': form})
    return render_to_response('form_table.html', context, context_instance=RequestContext(request))

def earlyclockout(request):
    if request.method == 'POST':
        form = EarlyClockOutForm(request.POST)
        if form.is_valid():
            subject = 'Dubuque Early Clock Out for    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time:    %s \n\n Reason for early clock out:    %s' % (form.cleaned_data['name'], form.cleaned_data['datetime'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com','cbrady@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'dwatson@aymcdonald.com', 'dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'cheim@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'dberning@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'dhein@aymcdonald.com@aymcdonald.com', 'dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'rmccullough@aymcdonald.com', 'rdryer@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(earlyclockout)
    clock = EarlyClockOut.objects.all()
    form = EarlyClockOutForm()
    context = Context({'title': 'Dubuque Early Clock Out', 'clock': clock, 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def earlyclockoutfactory(request):
    if request.method == 'POST':
        form = EarlyClockOutFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Factory Early Clock Out for    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time:    %s \n\n Reason for early clock out:    %s' % (form.cleaned_data['name'], form.cleaned_data['datetime'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(earlyclockoutfactory)
    clock = EarlyClockOutFactory.objects.all()
    form = EarlyClockOutFactoryForm()
    context = Context({'title': 'Factory Early Clock Out', 'clock': clock, 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def earlyclockoutfoundry(request):
    if request.method == 'POST':
        form = EarlyClockOutFoundryForm(request.POST)
        if form.is_valid():
            subject = 'Foundry Early Clock Out for    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time:    %s \n\n Reason for early clock out:    %s' % (form.cleaned_data['name'], form.cleaned_data['datetime'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dwatson@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'jsaunders@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(earlyclockoutfoundry)
    clock = EarlyClockOutFoundry.objects.all()
    form = EarlyClockOutFoundryForm()
    context = Context({'title': 'Foundry Early Clock Out', 'clock': clock, 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def earlyclockoutmaint(request):
    if request.method == 'POST':
        form = EarlyClockOutMaintForm(request.POST)
        if form.is_valid():
            subject = 'Maintenance Early Clock Out for    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time:    %s \n\n Reason for early clock out:    %s' % (form.cleaned_data['name'], form.cleaned_data['datetime'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dscherbring@aymcdonald.com', 'schumacher@aymcdonald.com', 'dwatson@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(earlyclockoutmaint)
    clock = EarlyClockOutMaint.objects.all()
    form = EarlyClockOutMaintForm()
    context = Context({'title': 'Maintenace Early Clock Out', 'clock': clock, 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def earlyclockoutship(request):
    if request.method == 'POST':
        form = EarlyClockOutShipForm(request.POST)
        if form.is_valid():
            subject = 'Shipping Early Clock Out for    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time:    %s \n\n Reason for early clock out:    %s' % (form.cleaned_data['name'], form.cleaned_data['datetime'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'msullivan@aymcdonald.com', 'pjentz@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(earlyclockoutship)
    clock = EarlyClockOutShip.objects.all()
    form = EarlyClockOutShipForm()
    context = Context({'title': 'Shipping Early Clock Out', 'clock': clock, 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def issuemiscmaterial(request):
    if request.method == 'POST':
        form = IssueMiscMaterialForm(request.POST)
        if form.is_valid():
            subject = 'DBQ Issue Miscellaneous Material    %s' % (form.cleaned_data['part'])
            message = '\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Reference:    %s \n\n Reason:    %s \n\n Bin:    %s \n\n Description:    %s' % (form.cleaned_data['part'], form.cleaned_data['quantity'], form.cleaned_data['part02'], form.cleaned_data['quantity02'], form.cleaned_data['part03'], form.cleaned_data['quantity03'], form.cleaned_data['part04'], form.cleaned_data['quantity04'], form.cleaned_data['part05'], form.cleaned_data['quantity05'], form.cleaned_data['part06'], form.cleaned_data['quantity06'], form.cleaned_data['part07'], form.cleaned_data['quantity07'], form.cleaned_data['reference'], form.cleaned_data['reason'], form.cleaned_data['bin_loc'], form.cleaned_data['description']) 
            from_addr = (request.user.email)
            recipient_list = ['dscherbring@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'gbrown@aymcdonald.com' , 'rmccullough@aymcdonald.com', 'pjentz@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(issuemiscmaterial)
    users = IssueMiscMaterial.objects.all()
    form = IssueMiscMaterialForm()
    context = Context({'title': 'DBQ Issue Miscellaneous Material', 'form': form})
    return render_to_response('issuemiscmaterial.html', context, context_instance=RequestContext(request))

def terminateemployee(request):
    if request.method == 'POST':
        form = TerminateEmployeeForm(request.POST)
        if form.is_valid():
            subject = 'Terminate Employee    %s    %s' % (form.cleaned_data['first_name'], form.cleaned_data['last_name'])
            message = '\n First Name:    %s \n\n Last Name:    %s \n\n Term Date:    %s \n\n Job Title:    %s \n\n Department:    %s \n\n Comments:    %s' % (form.cleaned_data['first_name'], form.cleaned_data['last_name'], form.cleaned_data['term_date'], form.cleaned_data['job_title'], form.cleaned_data['department'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['jboll@aymcdonald.com', 'thall@aymcdonald.com', 'kschmitt@aymcdonald.com', 'chillers@aymcdonald.com', 'nblack@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(terminateemployee)
    form = TerminateEmployeeForm()
    context = Context({'title': 'Terminate Employee', 'form': form})
    return render_to_response('termemp.html', context, context_instance=RequestContext(request))

def terminateemployeembu(request):
    if request.method == 'POST':
        form = TerminateEmployeeMBUForm(request.POST)
        if form.is_valid():
            subject = 'Terminate Employee-MBU    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Term Date:    %s \n\n Job Title:    %s \n\n Department:    %s' % (form.cleaned_data['name'],  form.cleaned_data['term_date'], form.cleaned_data['job_title'], form.cleaned_data['department']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jremakel@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com','dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'dgibbs@aymcdonald.com', 'jblack@aymcdonald.com', 'dhein@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', 'cbrady@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(terminateemployeembu)
    users = TerminateEmployeeMBU.objects.all()
    form = TerminateEmployeeMBUForm()
    context = Context({'title': 'Terminate Employee-MBU', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def terminateemployeefactory(request):
    if request.method == 'POST':
        form = TerminateEmployeeFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Terminate Employee-Factory    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Term Date:    %s \n\n Job Title:    %s \n\n Department:    %s' % (form.cleaned_data['name'],  form.cleaned_data['term_date'], form.cleaned_data['job_title'], form.cleaned_data['department']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'dhein@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', 'dgibbs@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(terminateemployeefactory)
    users = TerminateEmployeeFactory.objects.all()
    form = TerminateEmployeeFactoryForm()
    context = Context({'title': 'Terminate Employee-Factory', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def terminateemployeefoundry(request):
    if request.method == 'POST':
        form = TerminateEmployeeFoundryForm(request.POST)
        if form.is_valid():
            subject = 'Terminate Employee-Foundry    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Term Date:    %s \n\n Job Title:    %s \n\n Department:    %s' % (form.cleaned_data['name'],  form.cleaned_data['term_date'], form.cleaned_data['job_title'], form.cleaned_data['department']) 
            from_addr = (request.user.email)
            recipient_list = ['cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dwatson@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'dhein@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', 'sstankovich@aymcdonald.com', 'dgibbs@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(terminateemployeefoundry)
    users = TerminateEmployeeFoundry.objects.all()
    form = TerminateEmployeeFoundryForm()
    context = Context({'title': 'Terminate Employee-Foundry', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def terminateemployeemaint(request):
    if request.method == 'POST':
        form = TerminateEmployeeMaintForm(request.POST)
        if form.is_valid():
            subject = 'Terminate Employee-Maintenance    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Term Date:    %s \n\n Job Title:    %s \n\n Department:    %s' % (form.cleaned_data['name'],  form.cleaned_data['term_date'], form.cleaned_data['job_title'], form.cleaned_data['department']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dscherbring@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'dwatson@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'dhein@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', 'sstankovich@aymcdonald.com', 'dgibbs@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(terminateemployeemaint)
    users = TerminateEmployeeMaint.objects.all()
    form = TerminateEmployeeMaintForm()
    context = Context({'title': 'Terminate Employee-Maintenance', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def terminateemployeeship(request):
    if request.method == 'POST':
        form = TerminateEmployeeShipForm(request.POST)
        if form.is_valid():
            subject = 'Terminate Employee-Shipping    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Term Date:    %s \n\n Job Title:    %s \n\n Department:    %s' % (form.cleaned_data['name'],  form.cleaned_data['term_date'], form.cleaned_data['job_title'], form.cleaned_data['department']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'msullivan@aymcdonald.com', 'pjentz@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'dhein@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', 'dgibbs@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(terminateemployeeship)
    users = TerminateEmployeeShip.objects.all()
    form = TerminateEmployeeShipForm()
    context = Context({'title': 'Terminate Employee-Shipping', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def weekinjillfactory(request):
    if request.method == 'POST':
        form = WeekInjIllFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Week Inj-Ill Factory    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Department:    %s \n\n Shift:    %s \n\n Description of Inj/Ill:    %s \n\n Date/Time:    %s \n\n  Medical Provider:    %s \n\n Work Restrictions:    %s \n\n Next Appt Date/Time:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['description'], form.cleaned_data['datetime'], form.cleaned_data['medical_provider'], form.cleaned_data['work_restrictions'], form.cleaned_data['next_datetime']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'chuntington@aymcdonald.com', 'gbrown@aymcdonald.com', 'jbettcher@aymcdonald.com', 'dgibbs@aymcdonald.com',  'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(weekinjillfactory)
    users = WeekInjIllFactory.objects.all()
    form = WeekInjIllFactoryForm()
    context = Context({'title': 'Week Inj/Ill Factory', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def weekinjillfoundry(request):
    if request.method == 'POST':
        form = WeekInjIllFoundryForm(request.POST)
        if form.is_valid():
            subject = 'Week Inj-Ill Foundry    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Department:    %s \n\n Shift:    %s \n\n Description of Inj/Ill:    %s \n\n Date/Time:    %s \n\n  Medical Provider:    %s \n\n Work Restrictions:    %s \n\n Next Appt Date/Time:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['description'], form.cleaned_data['datetime'], form.cleaned_data['medical_provider'], form.cleaned_data['work_restrictions'], form.cleaned_data['next_datetime'])  
            from_addr = (request.user.email)
            recipient_list = ['cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dberning@aymcdonald.com', 'dboleyn@aymcdonald.com', 'jkirk@aymcdonald.com', 'dwatson@aymcdonald.com', 'jbettcher@aymcdonald.com', 'dgibbs@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'sstankovich@aymcdonald.com', 'jsaunders@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(weekinjillfoundry)
    users = WeekInjIllFoundry.objects.all()
    form = WeekInjIllFoundryForm()
    context = Context({'title': 'Week Inj/Ill Foundry', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def weekinjillmaint(request):
    if request.method == 'POST':
        form = WeekInjIllMaintForm(request.POST)
        if form.is_valid():
            subject = 'Week Inj-Ill Maintenance    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Department:    %s \n\n Shift:    %s \n\n Description of Inj/Ill:    %s \n\n Date/Time:    %s \n\n  Medical Provider:    %s \n\n Work Restrictions:    %s \n\n Next Appt Date/Time:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['description'], form.cleaned_data['datetime'], form.cleaned_data['medical_provider'], form.cleaned_data['work_restrictions'], form.cleaned_data['next_datetime'])  
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'dberning@aymcdonald.com', 'jbettcher@aymcdonald.com', 'dgibbs@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'msullivan@aymcdonald.com', 'rdryer@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(weekinjillmaint)
    users = WeekInjIllMaint.objects.all()
    form = WeekInjIllMaintForm()
    context = Context({'title': 'Week Inj/Ill Maintenance', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def weekinjillshipping(request):
    if request.method == 'POST':
        form = WeekInjIllShippingForm(request.POST)
        if form.is_valid():
            subject = 'Week Inj-Ill Shipping    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Department:    %s \n\n Shift:    %s \n\n Description of Inj/Ill:    %s \n\n Date/Time:    %s \n\n  Medical Provider:    %s \n\n Work Restrictions:    %s \n\n Next Appt Date/Time:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['description'], form.cleaned_data['datetime'], form.cleaned_data['medical_provider'], form.cleaned_data['work_restrictions'], form.cleaned_data['next_datetime']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'jbettcher@aymcdonald.com', 'dgibbs@aymcdonald.com',  'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(weekinjillshipping)
    users = WeekInjIllShipping.objects.all()
    form = WeekInjIllShippingForm()
    context = Context({'title': 'Week Inj/Ill Shipping', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def maintrequest(request):
    if request.method == 'POST':
        form = MaintRequestForm(request.POST)
        if form.is_valid():
            subject = 'Maintenance Request' 
            message = '\n Department:    %s \n\n Dept Num:    %s \n\n Machine:    %s \n\n Safety:    %s \n\n Description:    %s \n\n Lout:    %s \n\n Cell:    %s \n\n Request:    %s' % (form.cleaned_data['department'],  form.cleaned_data['department_num'], form.cleaned_data['machine'], form.cleaned_data['safety'], form.cleaned_data['description'], form.cleaned_data['lout'], form.cleaned_data['cell'], form.cleaned_data['request']) 
            from_addr = (request.user.email)
            recipient_list = ['rdryer@aymcdonald.com', 'dberning@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(maintrequest)
    users = MaintRequest.objects.all()
    form = MaintRequestForm()
    context = Context({'title': 'Maintenance Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def callin(request):
    if request.method == 'POST':
        form = CallInForm(request.POST)
        if form.is_valid():
            subject = 'Call In    %s' % (form.cleaned_data['name']) 
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Date/Time of Callin:    %s \n\n Date Requested:    %s \n\n Department:    %s \n\n Reason:    %s \n\n FMLA Cond (Y/N):    %s \n\n Did not request vacation' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['datetime'], form.cleaned_data['date_call'], form.cleaned_data['department'], form.cleaned_data['reason'], form.cleaned_data['fmla']) 
            from_addr = (request.user.email)
            recipient_list = ['dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jremakel@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'mvarley@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com','rdryer@aymcdonald.com', 'dberning@aymcdonald.com', 'asheehy@aymcdonald.com', 'mdolan@aymcdonald.com', 'cbrady@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(callin)
    users = CallIn.objects.all()
    form = CallInForm()
    context = Context({'title': 'Call In', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def callinfactory(request):
    if request.method == 'POST':
        form = CallInFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Call In-Factory    %s' % (form.cleaned_data['name']) 
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Date/Time of Callin:    %s \n\n Date Requested:    %s \n\n Department:    %s \n\n Reason:    %s \n\n FMLA Cond (Y/N):    %s \n\n Did not request vacation' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['datetime'], form.cleaned_data['date_call'], form.cleaned_data['department'], form.cleaned_data['reason'], form.cleaned_data['fmla']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(callinfactory)
    users = CallInFactory.objects.all()
    form = CallInFactoryForm()
    context = Context({'title': 'Call In - Factory', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def callinfoundry(request):
    if request.method == 'POST':
        form = CallInFoundryForm(request.POST)
        if form.is_valid():
            subject = 'Call In-Foundry    %s' % (form.cleaned_data['name']) 
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Date/Time of Callin:    %s \n\n Date Requested:    %s \n\n Department:    %s \n\n Reason:    %s \n\n FMLA Cond (Y/N):    %s \n\n Did not request vacation' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['datetime'], form.cleaned_data['date_call'], form.cleaned_data['department'], form.cleaned_data['reason'], form.cleaned_data['fmla']) 
            from_addr = (request.user.email)
            recipient_list = ['cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dwatson@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'jsaunders@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(callinfoundry)
    users = CallInFoundry.objects.all()
    form = CallInFoundryForm()
    context = Context({'title': 'Call In-Foundry', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def callinmaint(request):
    if request.method == 'POST':
        form = CallInMaintForm(request.POST)
        if form.is_valid():
            subject = 'Call In-Maintenance    %s' % (form.cleaned_data['name']) 
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Date/Time of Callin:    %s \n\n Date Requested:    %s \n\n Department:    %s \n\n Reason:    %s \n\n FMLA Cond (Y/N):    %s \n\n Did not request vacation' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['datetime'], form.cleaned_data['date_call'], form.cleaned_data['department'], form.cleaned_data['reason'], form.cleaned_data['fmla']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dberning@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dscherbring@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'dwatson@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(callinmaint)
    users = CallInMaint.objects.all()
    form = CallInMaintForm()
    context = Context({'title': 'Call In-Maintenance', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def callinship(request):
    if request.method == 'POST':
        form = CallInShipForm(request.POST)
        if form.is_valid():
            subject = 'Call In-Shipping    %s' % (form.cleaned_data['name']) 
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Date/Time of Callin:    %s \n\n Date Requested:    %s \n\n Department:    %s \n\n Reason:    %s \n\n FMLA Cond (Y/N):    %s \n\n Did not request vacation' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['datetime'], form.cleaned_data['date_call'], form.cleaned_data['department'], form.cleaned_data['reason'], form.cleaned_data['fmla']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'msullivan@aymcdonald.com', 'pjentz@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(callinship)
    users = CallInShip.objects.all()
    form = CallInShipForm()
    context = Context({'title': 'Call In-Shipping', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def instructsheetorder(request):
    if request.method == 'POST':
        form = InstructSheetOrderForm(request.POST)
        if form.is_valid():
            subject = 'Instruction Sheet Order' 
            message = '\n Part Num:    %s \n\n Instruction Sheet Title:    %s \n\n Quantity Required:    %s \n\n Deliver to Plant:    %s \n\n Deliver to Dept:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['title'], form.cleaned_data['quantity'], form.cleaned_data['plant'], form.cleaned_data['department']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'dgreenwood@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'jkendell@aymcdonald.com', 'pmartelli@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(instructsheetorder)
    users = InstructSheetOrder.objects.all()
    form = InstructSheetOrderForm()
    context = Context({'title': 'Instruction Sheet Order', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def injuryreport(request):
    if request.method == 'POST':
        form = InjuryReportForm(request.POST)
        if form.is_valid():
            subject = 'Injury Report    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time Injury:    %s \n\n Date/Time Reported:    %s \n\n Tool/Mach/Epuip Involved:    %s \n\n Body Part Injured:    %s \n\n Type of Injury:    %s \n\n How did Injury Occur:    %s \n\n Sent for Medical Treatment:    %s \n\n Facility:    %s \n\n First Aid Administered    %s \n\n First Aid Provided(Band Aid, Ice, etc)    %s \n\n Supervisor"s Recommendation to Prevent Similar:    %s' % (form.cleaned_data['name'],  form.cleaned_data['datetimeinj'], form.cleaned_data['datetimerep'], form.cleaned_data['equipment'], form.cleaned_data['body'], form.cleaned_data['typeinj'], form.cleaned_data['actions'], form.cleaned_data['treatment'], form.cleaned_data['facility'], form.cleaned_data['firstaid'], form.cleaned_data['firstaidprov'], form.cleaned_data['recommendation']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com','jremakel@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'rmccullough@aymcdonald.com', 'dgibbs@aymcdonald.com', 'sstankovich@aymcdonald.com', 'msullivan@aymcdonald.com', 'sstankovich@aymcdonald.com', 'bjohnson@aymcdonald.com', 'cheim@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dberning@aymcdonald.com', 'dwatson@aymcdonald.com', 'jsullivan@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jkirk@aymcdonald.com', 'pludowitz@aymcdonald.com', 'bmorgan@aymcdonald.com', 'gbrown@aymcdonald.com', 'jschoop@aymcdonald.com', 'jherrig@aymcdonald.com', 'mbeadle@aymcdonald.com', 'mkirby@aymcdonald.com', 'rdryer@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'jsaunders@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(injuryreport)
    users = InjuryReport.objects.all()
    form = InjuryReportForm()
    context = Context({'title': 'Injury Report', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def changeofstatus(request):
    if request.method == 'POST':
        form = ChangeOfStatusForm(request.POST)
        if form.is_valid():
            subject = 'Change Of Status'
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Effective Date:    %s \n\n Sub Shift:    %s \n\n Classification:    %s \n\n Department:    %s \n\n Shift:    %s \n\n AWD Date of Bid:    %s \n\n Supervisor:    %s \n\n Office use Only:    %s \n\n Reason:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['date'], form.cleaned_data['sub_shift'], form.cleaned_data['classification'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['awd_date'], form.cleaned_data['supervisor'], form.cleaned_data['officeuse'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'cbrady@aymcdonald.com','jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jremakel@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'jremakel@aymcdonald.com', 'dgibbs@aymcdonald.com', 'jblack@aymcdonald.com', 'dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(changeofstatus)
    users = ChangeOfStatus.objects.all()
    form = ChangeOfStatusForm()
    context = Context({'title': 'Change Of Status', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def changeofstatusfactory(request):
    if request.method == 'POST':
        form = ChangeOfStatusFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Change Of Status-Factory'
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Effective Date:    %s \n\n Sub Shift:    %s \n\n Classification:    %s \n\n Indirect/Direct    %s \n\n Department:    %s \n\n Shift:    %s \n\n AWD Date of Bid:    %s \n\n Supervisor:    %s \n\n Office use Only:    %s \n\n Reason:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['date'], form.cleaned_data['sub_shift'], form.cleaned_data['classification'], form.cleaned_data['inddir'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['awd_date'], form.cleaned_data['supervisor'], form.cleaned_data['officeuse'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'dgibbs@aymcdonald.com',  'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(changeofstatusfactory)
    users = ChangeOfStatusFactory.objects.all()
    form = ChangeOfStatusFactoryForm()
    context = Context({'title': 'Change Of Status - Factory', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def changeofstatusfoundry(request):
    if request.method == 'POST':
        form = ChangeOfStatusFoundryForm(request.POST)
        if form.is_valid():
            subject = 'Change Of Status-Foundry'
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Effective Date:    %s \n\n Sub Shift:    %s \n\n Classification:    %s \n\n Indirect/Direct    %s \n\n Department:    %s \n\n Shift:    %s \n\n AWD Date of Bid:    %s \n\n Supervisor:    %s \n\n Office use Only:    %s \n\n Reason:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['date'], form.cleaned_data['sub_shift'], form.cleaned_data['classification'], form.cleaned_data['inddir'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['awd_date'], form.cleaned_data['supervisor'], form.cleaned_data['officeuse'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dwatson@aymcdonald.com', 'jbettcher@aymcdonald.com', 'dgibbs@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(changeofstatusfoundry)
    users = ChangeOfStatusFoundry.objects.all()
    form = ChangeOfStatusFoundryForm()
    context = Context({'title': 'Change Of Status-Foundry', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def changeofstatusmaint(request):
    if request.method == 'POST':
        form = ChangeOfStatusMaintForm(request.POST)
        if form.is_valid():
            subject = 'Change Of Status-Maintenance'
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Effective Date:    %s \n\n Sub Shift:    %s \n\n Classification:    %s \n\n Indirect/Direct    %s \n\n Department:    %s \n\n Shift:    %s \n\n AWD Date of Bid:    %s \n\n Supervisor:    %s \n\n Office use Only:    %s \n\n Reason:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['date'], form.cleaned_data['sub_shift'], form.cleaned_data['classification'], form.cleaned_data['inddir'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['awd_date'], form.cleaned_data['supervisor'], form.cleaned_data['officeuse'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dscherbring@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'dwatson@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'dgibbs@aymcdonald.com',  'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(changeofstatusmaint)
    users = ChangeOfStatusMaint.objects.all()
    form = ChangeOfStatusMaintForm()
    context = Context({'title': 'Change Of Status-Maintenance', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def changeofstatusship(request):
    if request.method == 'POST':
        form = ChangeOfStatusShipForm(request.POST)
        if form.is_valid():
            subject = 'Change Of Status-Shipping'
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Effective Date:    %s \n\n Sub Shift:    %s \n\n Classification:    %s \n\n Indirect/Direct    %s \n\n Department:    %s \n\n Shift:    %s \n\n AWD Date of Bid:    %s \n\n Supervisor:    %s \n\n Office use Only:    %s \n\n Reason:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['date'], form.cleaned_data['sub_shift'], form.cleaned_data['classification'], form.cleaned_data['inddir'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['awd_date'], form.cleaned_data['supervisor'], form.cleaned_data['officeuse'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jbettcher@aymcdonald.com', 'dgibbs@aymcdonald.com', 'jblack@aymcdonald.com', 'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'msullivan@aymcdonald.com', 'pjentz@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(changeofstatusship)
    users = ChangeOfStatusShip.objects.all()
    form = ChangeOfStatusShipForm()
    context = Context({'title': 'Change Of Status-Shipping', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def toolchange(request):
    if request.method == 'POST':
        form = ToolChangeForm(request.POST)
        if form.is_valid():
            subject = 'Tool Change Order' 
            message = '\n Tool Num:    %s \n\n Revision:    %s \n\n Type of Change:    %s \n\n Price:    %s \n\n Vendor:    %s \n\n Instructions    %s' % (form.cleaned_data['tool_num'],  form.cleaned_data['revision'], form.cleaned_data['type_change'], form.cleaned_data['price'], form.cleaned_data['vendor'], form.cleaned_data['instructions']) 
            from_addr = (request.user.email)
            recipient_list = ['kwagner@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(toolchange)
    users = ToolChange.objects.all()
    form = ToolChangeForm()
    context = Context({'title': 'Tool Change Order', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def castingproblem(request):
    if request.method == 'POST':
        form = CastingProblemForm(request.POST)
        if form.is_valid():
            subject = 'Casting Problem' 
            message = '\n Part Num:    %s \n\n Order Num:    %s \n\n Casting Part Num:    %s \n\n Department:    %s \n\n Casting Order Num:    %s \n\n Description of Problem:    %s \n\n Investigated By:    %s \n\n Corrective Action Taken:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['order_num'], form.cleaned_data['cast_part_num'], form.cleaned_data['department'], form.cleaned_data['cast_order_num'], form.cleaned_data['description'], form.cleaned_data['investigated'], form.cleaned_data['corrective']) 
            from_addr = (request.user.email)
            recipient_list = ['adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'ashea@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bhaas@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cheim@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dratterman@aymcdonald.com', 'dthen@aymcdonald.com', 'dwatson@aymcdonald.com', 'ewolter@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jburdt@aymcdonald.com', 'jcabana@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jschoop@aymcdonald.com', 'keller@aymcdonald.com', 'lotting@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'rmccullough@aymcdonald.com', 'rrokusek@aymcdonald.com', 'rwagner@aymcdonald.com', 'stefft@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(castingproblem)
    users = CastingProblem.objects.all()
    form = CastingProblemForm()
    context = Context({'title': 'Casting Problem', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def cartonnochange(request):
    if request.method == 'POST':
        form = CartonNoChangeForm(request.POST)
        if form.is_valid():
            subject = 'Carton No. Change' 
            message = '\n Part Num:    %s \n\n Old Carton Num:    %s \n\n New Carton Num:    %s \n\n Comments:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['old_num'], form.cleaned_data['new_num'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['dconnolly@aymcdonald.com', 'bhaas@aymcdonald.com', 'kduex@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(cartonnochange)
    users = CartonNoChange.objects.all()
    form = CartonNoChangeForm()
    context = Context({'title': 'Carton No. Change', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def cartonwgtchange(request):
    if request.method == 'POST':
        form = CartonWgtChangeForm(request.POST)
        if form.is_valid():
            subject = 'Carton Wgt Change' 
            message = '\n Part Num:    %s \n\n Carton Quantity:    %s \n\n Carton Weight:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['carton_qty'], form.cleaned_data['carton_wgt']) 
            from_addr = (request.user.email)
            recipient_list = ['dschoenberger@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jcabana@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(cartonwgtchange)
    users = CartonWgtChange.objects.all()
    form = CartonWgtChangeForm()
    context = Context({'title': 'Carton Wgt Change', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def cellsetup(request):
    if request.method == 'POST':
        form = CellSetupForm(request.POST)
        if form.is_valid():
            subject = 'Cell Setup    %s' % (form.cleaned_data['cell_name'])
            message = '\n Plant:    %s \n\n Cell Identifier:    %s \n\n Cell Name:    %s \n\n Department:    %s \n\n Base Part:    %s \n\n Base Routing Standard:    %s \n\n Add all Routing Steps:    %s \n\n From/To Reference Locs:    %s \n\n Run Rate for Schedule Report (Mark):    %s \n\n Work Center to Identify Parts to Change    %s' % (form.cleaned_data['plant'],  form.cleaned_data['cell_id'], form.cleaned_data['cell_name'], form.cleaned_data['department'], form.cleaned_data['base_part'], form.cleaned_data['base_route'], form.cleaned_data['add_route'], form.cleaned_data['ref_locs'], form.cleaned_data['run_rate'], form.cleaned_data['work_center']) 
            from_addr = (request.user.email)
            recipient_list = ['dratterman@aymcdonald.com', 'jboll@aymcdonald.com', 'jremakel@aymcdonald.com', 'lsaylor@aymcdonald.com', 'marling@aymcdonald.com', 'msullivan@aymcdonald.com', 'shasken@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(cellsetup)
    users = CellSetup.objects.all()
    form = CellSetupForm()
    context = Context({'title': 'Cell Setup', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def gatepass(request):
    if request.method == 'POST':
        form = GatePassForm(request.POST)
        if form.is_valid():
            subject = 'Gate Pass    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date:    %s \n\n Clock #:    %s \n\n Sold:    %s \n\n Given To:    %s \n\n Borrowed Date:    %s \n\n Returned Date:    %s \n\n Approval:    %s \n\n Cost:    %s \n\n Description:    %s' % (form.cleaned_data['name'],  form.cleaned_data['date'], form.cleaned_data['clock_num'], form.cleaned_data['sold'], form.cleaned_data['given'], form.cleaned_data['borrow_date'], form.cleaned_data['return_date'], form.cleaned_data['approval'], form.cleaned_data['cost'], form.cleaned_data['description']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com','dberning@aymcdonald.com', 'dhein@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'kwilliams@aymcdonald.com', 'msullivan@aymcdonald.com', 'pnugent@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'rpetrick@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(gatepass)
    form = GatePassForm()
    context = Context({'title': 'Gate Pass', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def machinedownlog(request):
    if request.method == 'POST':
        form = MachineDownLogForm(request.POST)
        if form.is_valid():
            subject = 'Machine Down Log    %s' % (form.cleaned_data['machine_num'])
            message = '\n Machine #:    %s \n\n Machine Description:    %s \n\n Reason Down:    %s \n\n Duration Days:    %s' % (form.cleaned_data['machine_num'], form.cleaned_data['machine_desc'], form.cleaned_data['reason'], form.cleaned_data['duration']) 
            from_addr = (request.user.email)
            recipient_list = ['msullivan@aymcdonald.com', 'dratterman@aymcdonald.com', 'rmccullough@aymcdonald.com', 'jremakel@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jburdt@aymcdonald.com', 'dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jremakel@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(machinedownlog)
    users = MachineDownLog.objects.all()
    form = MachineDownLogForm()
    context = Context({'title': 'Machine Down Log', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def changeorderrequest(request):
    if request.method == 'POST':
        form = ChangeOrderRequestForm(request.POST)
        if form.is_valid():
            subject = 'Change Order Request'
            message = '\n Info:    %s' % (form.cleaned_data['info']) 
            from_addr = (request.user.email)
            recipient_list = ['ashea@aymcdonald.com', 'awickham@aymcdonald.com', 'bhaas@aymcdonald.com', 'dconnolly@aymcdonald.com', 'dratterman@aymcdonald.com', 'dthen@aymcdonald.com', 'jburdt@aymcdonald.com', 'jzurcher@aymcdonald.com', 'kduex@aymcdonald.com', 'lotting@aymcdonald.com', 'marling@aymcdonald.com', 'parnold@aymcdonald.com', 'raspen@aymcdonald.com', 'sbreitbach@aymcdonald.com', 'stefft@aymcdonald.com', 'thast@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(changeorderrequest)
    clock = ChangeOrderRequest.objects.all()
    form = ChangeOrderRequestForm()
    context = Context({'title': 'Change Order Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiacallin(request):
    if request.method == 'POST':
        form = AlbiaCallInForm(request.POST)
        if form.is_valid():
            subject = 'Albia Call In' 
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Date/Time of Callin:    %s \n\n Date Required:    %s \n\n Department/Shift:    %s \n\n Reason:    %s \n\n FMLA Cond (Y/N):    %s \n\n' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['datetime'], form.cleaned_data['date'], form.cleaned_data['department'], form.cleaned_data['reason'], form.cleaned_data['fmla']) 
            from_addr = (request.user.email)
            recipient_list = ['mdobraska@aymcdonald.com', 'cbrady@aymcdonald.com', 'sperry@aymcdonald.com', 'mrockwell@aymcdonald.com', 'lbrown@aymcdonald.com','ltucker@aymcdonald.com', 'kdavis@aymcdonald.com',  'dpendleton@aymcdonald.com', 'msullivan@aymcdonald.com', 'jkelley@aymcdonald.com', 'cskelton@aymcdonald.com', 'tmcvey@aymcdonald.com', 'chuntington@aymcdonald.com', 'sohara@aymcdonald.com', 'dschoenberger@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiacallin)
    users = AlbiaCallIn.objects.all()
    form = AlbiaCallInForm()
    context = Context({'title': 'Albia Call In', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiainjuryreport(request):
    if request.method == 'POST':
        form = AlbiaInjuryReportForm(request.POST)
        if form.is_valid():
            subject = 'Albia Injury Report    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time Injury:    %s \n\n Date/Time Reported:    %s \n\n Tool/Mach/Epuip Involved:    %s \n\n Body Part Injured:    %s \n\n Type of Injury:    %s \n\n How did Injury Occur:    %s \n\n Sent for Medical Treatment:    %s \n\n First Aid Administered    %s \n\n First Aid Provided(Band Aid, Ice, etc)    %s \n\n Supervisor"s Recommendation to Prevent Similar:    %s' % (form.cleaned_data['name'],  form.cleaned_data['datetimeinj'], form.cleaned_data['datetimerep'], form.cleaned_data['equipment'], form.cleaned_data['body'], form.cleaned_data['typeinj'], form.cleaned_data['actions'], form.cleaned_data['treatment'], form.cleaned_data['firstaid'], form.cleaned_data['firstaidprov'], form.cleaned_data['recommendation'])  
            from_addr = (request.user.email)
            recipient_list = ['mdobraska@aymcdonald.com', 'msullivan@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'chuntington@aymcdonald.com', 'dgibbs@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiainjuryreport)
    users = AlbiaInjuryReport.objects.all()
    form = AlbiaInjuryReportForm()
    context = Context({'title': 'Albia Injury Report', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tenncallin(request):
    if request.method == 'POST':
        form = TennCallInForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Call In' 
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Date/Time of Callin:    %s \n\n Date Required:    %s \n\n Department:    %s \n\n Reason:    %s \n\n FMLA Cond (Y/N):    %s \n\n' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['datetime'], form.cleaned_data['date'], form.cleaned_data['department'], form.cleaned_data['reason'], form.cleaned_data['fmla']) 
            from_addr = (request.user.email)
            recipient_list = ['keller@aymcdonald.com', 'msullivan@aymcdonald.com', 'sdayton@aymcdonald.com', 'dsimerly@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'tkennett@aymcdonald.com', 'jsommers@aymcdonald.com', 'lbarr@aymcdonald.com', 'acollins@aymcdonald.com', 'jcombs@aymcdonald.com', 'sohara@aymcdonald.com', 'tharmon@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tenncallin)
    users = TennCallIn.objects.all()
    form = TennCallInForm()
    context = Context({'title': 'Tennessee Call In', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tenninjuryreport(request):
    if request.method == 'POST':
        form = TennInjuryReportForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Injury Report    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time Injury:    %s \n\n Date/Time Reported:    %s \n\n Tool/Mach/Epuip Involved:    %s \n\n Body Part Injured:    %s \n\n Type of Injury:    %s \n\n How did Injury Occur:    %s \n\n Sent for Medical Treatment:    %s \n\n First Aid Administered    %s \n\n First Aid Provided(Band Aid, Ice, etc)    %s \n\n Supervisor"s Recommendation to Prevent Similar:    %s' % (form.cleaned_data['name'],  form.cleaned_data['datetimeinj'], form.cleaned_data['datetimerep'], form.cleaned_data['equipment'], form.cleaned_data['body'], form.cleaned_data['typeinj'], form.cleaned_data['actions'], form.cleaned_data['treatment'], form.cleaned_data['firstaid'], form.cleaned_data['firstaidprov'], form.cleaned_data['recommendation'])  
            from_addr = (request.user.email)
            recipient_list = ['keller@aymcdonald.com', 'chuntington@aymcdonald.com', 'msullivan@aymcdonald.com', 'shuschik@aymcdonald.com', 'jsommers@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'dgibbs@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tenninjuryreport)
    users = TennInjuryReport.objects.all()
    form = TennInjuryReportForm()
    context = Context({'title': 'Tennessee Injury Report', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiaweekinjillfactory(request):
    if request.method == 'POST':
        form = AlbiaWeekInjIllFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Albia Week Inj-Ill Factory    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee Num:    %s \n\n Department:    %s \n\n Shift:    %s \n\n Description of Inj/Ill:    %s \n\n Date/Time:    %s \n\n Medical Provider:    %s \n\n Work Restrictions:    %s \n\n Next Appt Date/Time:    %s' % (form.cleaned_data['name'],  form.cleaned_data['employee_num'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['description'], form.cleaned_data['datetime'], form.cleaned_data['medical_provider'], form.cleaned_data['work_restrictions'], form.cleaned_data['next_datetime']) 
            from_addr = (request.user.email)
            recipient_list = ['mdobraska@aymcdonald.com', 'msullivan@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'chuntington@aymcdonald.com', 'dgibbs@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'sstankovich@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiaweekinjillfactory)
    users = AlbiaWeekInjIllFactory.objects.all()
    form = AlbiaWeekInjIllFactoryForm()
    context = Context({'title': 'Albia Week Inj/Ill Factory', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiaearlyclockout(request):
    if request.method == 'POST':
        form = AlbiaEarlyClockOutForm(request.POST)
        if form.is_valid():
            subject = 'Albia Early Clock Out for    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time:    %s \n\n Reason for early clock out:    %s' % (form.cleaned_data['name'], form.cleaned_data['datetime'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['mdobraska@aymcdonald.com', 'cbrady@aymcdonald.com', 'sperry@aymcdonald.com', 'mrockwell@aymcdonald.com', 'lbrown@aymcdonald.com', 'ltucker@aymcdonald.com', 'kdavis@aymcdonald.com',  'dpendleton@aymcdonald.com', 'msullivan@aymcdonald.com', 'jkelley@aymcdonald.com', 'cskelton@aymcdonald.com', 'tmcvey@aymcdonald.com', 'chuntington@aymcdonald.com', 'sohara@aymcdonald.com', 'dschoenberger@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiaearlyclockout)
    clock = AlbiaEarlyClockOut.objects.all()
    form = AlbiaEarlyClockOutForm()
    context = Context({'title': 'Albia Early Clock Out', 'clock': clock, 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tennearlyclockout(request):
    if request.method == 'POST':
        form = TennEarlyClockOutForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Early Clock Out for    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date/Time:    %s \n\n Reason for early clock out:    %s' % (form.cleaned_data['name'], form.cleaned_data['datetime'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['keller@aymcdonald.com', 'msullivan@aymcdonald.com', 'sdayton@aymcdonald.com', 'dsimerly@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'tkennett@aymcdonald.com', 'jsommers@aymcdonald.com', 'lbarr@aymcdonald.com', 'acollins@aymcdonald.com', 'jcombs@aymcdonald.com', 'sohara@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tennearlyclockout)
    clock = TennEarlyClockOut.objects.all()
    form = TennEarlyClockOutForm()
    context = Context({'title': 'Tennessee Early Clock Out', 'clock': clock, 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiaissuemiscmaterial(request):
    if request.method == 'POST':
        form = AlbiaIssueMiscMaterialForm(request.POST)
        if form.is_valid():
            subject = 'Albia Issue Miscellanous Material    %s' % (form.cleaned_data['part'])
            message = '\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Reference:    %s \n\n Reason:    %s \n\n Bin:    %s \n\n Description:    %s' % (form.cleaned_data['part'], form.cleaned_data['quantity'], form.cleaned_data['part02'], form.cleaned_data['quantity02'], form.cleaned_data['part03'], form.cleaned_data['quantity03'], form.cleaned_data['part04'], form.cleaned_data['quantity04'], form.cleaned_data['part05'], form.cleaned_data['quantity05'], form.cleaned_data['part06'], form.cleaned_data['quantity06'], form.cleaned_data['part07'], form.cleaned_data['quantity07'], form.cleaned_data['reference'], form.cleaned_data['reason'], form.cleaned_data['bin_loc'], form.cleaned_data['description']) 
            from_addr = (request.user.email)
            recipient_list = ['dschoenberger@aymcdonald.com', 'sperry@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiaissuemiscmaterial)
    users = AlbiaIssueMiscMaterial.objects.all()
    form = AlbiaIssueMiscMaterialForm()
    context = Context({'title': 'Albia Issue Miscellaneous Material', 'form': form})
    return render_to_response('issuemiscmaterial.html', context, context_instance=RequestContext(request))

def tennissuemiscmaterial(request):
    if request.method == 'POST':
        form = TennIssueMiscMaterialForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Issue Miscellanous Material    %s' % (form.cleaned_data['part'])
            message = '\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Reference:    %s \n\n Reason:    %s \n\n Bin:    %s \n\n Description:    %s' % (form.cleaned_data['part'], form.cleaned_data['quantity'], form.cleaned_data['part02'], form.cleaned_data['quantity02'], form.cleaned_data['part03'], form.cleaned_data['quantity03'], form.cleaned_data['part04'], form.cleaned_data['quantity04'], form.cleaned_data['part05'], form.cleaned_data['quantity05'], form.cleaned_data['part06'], form.cleaned_data['quantity06'], form.cleaned_data['part07'], form.cleaned_data['quantity07'], form.cleaned_data['reference'], form.cleaned_data['reason'], form.cleaned_data['bin_loc'], form.cleaned_data['description'])
            from_addr = (request.user.email)
            recipient_list = ['keller@aymcdonald.com', 'sdayton@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tennissuemiscmaterial)
    users = TennIssueMiscMaterial.objects.all()
    form = TennIssueMiscMaterialForm()
    context = Context({'title': 'Tennessee Issue Miscellaneous Material', 'form': form})
    return render_to_response('issuemiscmaterial.html', context, context_instance=RequestContext(request))

def nevissuemiscmaterial(request):
    if request.method == 'POST':
        form = NevIssueMiscMaterialForm(request.POST)
        if form.is_valid():
            subject = 'Sparks Issue Miscellanous Material    %s' % (form.cleaned_data['part'])
            message = '\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Part:    %s    Quantity:    %s \n\n Reference:    %s \n\n Reason:    %s \n\n Bin:    %s \n\n Description:    %s' % (form.cleaned_data['part'], form.cleaned_data['quantity'], form.cleaned_data['part02'], form.cleaned_data['quantity02'], form.cleaned_data['part03'], form.cleaned_data['quantity03'], form.cleaned_data['part04'], form.cleaned_data['quantity04'], form.cleaned_data['part05'], form.cleaned_data['quantity05'], form.cleaned_data['part06'], form.cleaned_data['quantity06'], form.cleaned_data['part07'], form.cleaned_data['quantity07'], form.cleaned_data['reference'], form.cleaned_data['reason'], form.cleaned_data['bin_loc'], form.cleaned_data['description']) 
            from_addr = (request.user.email)
            recipient_list = ['stierney@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(nevissuemiscmaterial)
    users = NevIssueMiscMaterial.objects.all()
    form = NevIssueMiscMaterialForm()
    context = Context({'title': 'Sparks Issue Miscellaneous Material', 'form': form})
    return render_to_response('issuemiscmaterial.html', context, context_instance=RequestContext(request))

def foundrytoolrec(request):
    if request.method == 'POST':
        form = FoundryToolRecForm(request.POST)
        if form.is_valid():
            subject = 'Foundry Tool Received'
            message = '\n Pattern:    %s \n\n Corebox:    %s \n\n Part #:    %s \n\n Change Order #:    %s' % (form.cleaned_data['pattern'], form.cleaned_data['corebox'], form.cleaned_data['part_num'], form.cleaned_data['changeorder_num']) 
            from_addr = (request.user.email)
            recipient_list = ['bhaas@aymcdonald.com', 'dconnolly@aymcdonald.com', 'ewolter@aymcdonald.com', 'jzurcher@aymcdonald.com', 'kduex@aymcdonald.com', 'parnold@aymcdonald.com', 'raspen@aymcdonald.com', 'stefft@aymcdonald.com', 'thast@aymcdonald.com', 'qmccullough@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'dwatson@aymcdonald.com', 'msullivan@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(foundrytoolrec)
    users = FoundryToolRec.objects.all()
    form = FoundryToolRecForm()
    context = Context({'title': 'Foundry Tooling Received', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def machinefollowup(request):
    if request.method == 'POST':
        form = MachineFollowUpForm(request.POST)
        if form.is_valid():
            subject = 'Machine Follow Up    %s' % (form.cleaned_data['department'])
            message = '\n Supervisor:    %s \n\n Department:    %s \n\n Work Center:    %s \n\n Machine #:    %s \n\n Operator:    %s \n\n Time:    %s \n\n Program #:    %s \n\n Part #:    %s \n\n Est Damage Cost:    %s \n\n Time Incurred for Repairs:    %s \n\n Drug Tested:    %s \n\n Explaination:    %s \n\n Machine Note:    %s ' % (form.cleaned_data['supervisor'],  form.cleaned_data['department'], form.cleaned_data['work_center'], form.cleaned_data['machine_num'], form.cleaned_data['operator'], form.cleaned_data['time'], form.cleaned_data['program_num'], form.cleaned_data['part_num'], form.cleaned_data['estdamcost'], form.cleaned_data['timeofrepair'], form.cleaned_data['drug'], form.cleaned_data['explaination'], form.cleaned_data['machine_notes']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'dscherbring@aymcdonald.com',  'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jburdt@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'jkendell@aymcdonald.com', 'efaust@aymcdonald.com', 'gryan@aymcdonald.com' , 'gryan@aymcdonald.com' , 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'pmartelli@aymcdonald.com',  'tbanwarth@aymcdonald.com','tbanwarth@aymcdonald.com', 'parnold@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(machinefollowup)
    users = MachineFollowUp.objects.all()
    form = MachineFollowUpForm()
    context = Context({'title': 'Machine Follow Up', 'form': form})
    return render_to_response('machinefollowup.html', context, context_instance=RequestContext(request))

def albiamachinefollowup(request):
    if request.method == 'POST':
        form = AlbiaMachineFollowUpForm(request.POST)
        if form.is_valid():
            subject = 'Albia Machine Follow Up    %s' % (form.cleaned_data['department'])
            message = '\n Supervisor:    %s \n\n Department:    %s \n\n Work Center:    %s \n\n Machine #:    %s \n\n Operator:    %s \n\n Time:    %s \n\n Program #:    %s \n\n Part #:    %s \n\n Est Damage Cost:    %s \n\n Time Incurred for Repairs:    %s \n\n Drug Tested:    %s \n\n Explaination:     %s \n\n Machine Note:    %s' % (form.cleaned_data['supervisor'],  form.cleaned_data['department'], form.cleaned_data['work_center'], form.cleaned_data['machine_num'], form.cleaned_data['operator'], form.cleaned_data['time'], form.cleaned_data['program_num'], form.cleaned_data['part_num'], form.cleaned_data['estdamcost'], form.cleaned_data['timeofrepair'], form.cleaned_data['drug'], form.cleaned_data['explaination'], form.cleaned_data['machine_notes']) 
            from_addr = (request.user.email)
            recipient_list = ['mrockwell@aymcdonald.com', 'msullivan@aymcdonald.com', 'pmcdanel@aymcdonald.com', 'gcurtis@aymcdonald.com', 'slampier@aymcdonald.com', 'rdryer@aymcdonald.com', 'dschoenberger@aymcdonald.com',  'dpendleton@aymcdonald.com', 'jkelley@aymcdonald.com', 'dmalone@aymcdonald.com', 'cskelton@aymcdonald.com', 'kdavis@aymcdonald.com', 'ltucker@aymcdonald.com', 'tmcvey@aymcdonald.com', 'spangburn@aymcdonald.com', 'sduncan@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiamachinefollowup)
    users = AlbiaMachineFollowUp.objects.all()
    form = AlbiaMachineFollowUpForm()
    context = Context({'title': 'Albia Machine Follow Up', 'form': form})
    return render_to_response('machinefollowup.html', context, context_instance=RequestContext(request))

def tennmachinefollowup(request):
    if request.method == 'POST':
        form = TennMachineFollowUpForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Machine Follow Up    %s' % (form.cleaned_data['department'])
            message = '\n Supervisor:    %s \n\n Department:    %s \n\n Work Center:    %s \n\n Machine #:    %s \n\n Operator:    %s \n\n Time:    %s \n\n Program #:    %s \n\n Part #:    %s \n\n Est Damage Cost:    %s \n\n Time Incurred for Repairs:    %s \n\n Drug Tested:    %s \n\n Explaination:    %s \n\n Machine Note:    %s' % (form.cleaned_data['supervisor'],  form.cleaned_data['department'], form.cleaned_data['work_center'], form.cleaned_data['machine_num'], form.cleaned_data['operator'], form.cleaned_data['time'], form.cleaned_data['program_num'], form.cleaned_data['part_num'], form.cleaned_data['estdamcost'], form.cleaned_data['timeofrepair'], form.cleaned_data['drug'], form.cleaned_data['explaination'], form.cleaned_data['machine_note']) 
            from_addr = (request.user.email)
            recipient_list = ['keller@aymcdonald.com', 'msullivan@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'tkennett@aymcdonald.com', 'lbarr@mcdonald.com', 'jsommers@aymcdonald.com','glaughlin@aymcdonald.com', 'amehlhorn@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'kgrindstaff@aymcdonald.com', 'cmorton@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tennmachinefollowup)
    users = TennMachineFollowUp.objects.all()
    form = TennMachineFollowUpForm()
    context = Context({'title': 'Tennessee Machine Follow Up', 'form': form})
    return render_to_response('machinefollowup.html', context, context_instance=RequestContext(request))

def setupexceptionchallenge(request):
    if request.method == 'POST':
        form = SetupExceptionChallengeForm(request.POST)
        if form.is_valid():
            subject = '%s Setup Exception Challenge' % (form.cleaned_data['work_center'])
            message = '\n Employee:    %s \n\n Shift    %s \n\n Date of Exception:    %s \n\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Cumulative Time:    %s \n\n Exception Time:    %s \n\n Difference of Actual/Exception:    %s \n\n Open/Closed:    %s \n\n Original Exception:    %s \n\n Challenge    %s' % (form.cleaned_data['employee'], form.cleaned_data['shift'], form.cleaned_data['date'], form.cleaned_data['part_num'], form.cleaned_data['job_num'], form.cleaned_data['resource_num'], form.cleaned_data['cum_time'], form.cleaned_data['excep_time'], form.cleaned_data['difference'], form.cleaned_data['open_closed'], form.cleaned_data['orig_except'], form.cleaned_data['challenge'],) 
            from_addr = (request.user.email)
            recipient_list = ['jremakel@aymcdonald.com', 'msullivan@aymcdonald.com', 'rmccullough@aymcdonald.com', 'svanek@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(setupexceptionchallenge)
    users = SetupExceptionChallenge.objects.all()
    form = SetupExceptionChallengeForm()
    context = Context({'title': 'Setup Exception Challenge', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def setupexceptionresponse(request):
    if request.method == 'POST':
        form = SetupExceptionResponseForm(request.POST)
        if form.is_valid():
            subject = '%s Setup Exception Response' % (form.cleaned_data['work_center'])
            message = '\n Employee:    %s \n\n Shift    %s \n\n Date of Exception:    %s \n\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Cumulative Time:    %s \n\n Exception Time:    %s \n\n Difference of Actual/Exception:    %s \n\n Original Exception:    %s \n\n Response    %s' % (form.cleaned_data['employee'], form.cleaned_data['shift'], form.cleaned_data['date'], form.cleaned_data['part_num'], form.cleaned_data['job_num'], form.cleaned_data['resource_num'], form.cleaned_data['cum_time'], form.cleaned_data['excep_time'], form.cleaned_data['difference'], form.cleaned_data['orig_except'], form.cleaned_data['response'],) 
            from_addr = (request.user.email)
            recipient_list = ['jremakel@aymcdonald.com', 'msullivan@aymcdonald.com', 'rmccullough@aymcdonald.com', 'svanek@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(setupexceptionresponse)
    users = SetupExceptionResponse.objects.all()
    form = SetupExceptionResponseForm()
    context = Context({'title': 'Setup Exception Response', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tennsetupexception(request):
    if request.method == 'POST':
        form = TennSetupExceptionForm(request.POST)
        if form.is_valid():
            subject = '%s Tennessee Setup Exception' % (form.cleaned_data['work_center'])
            message = '\n Employee:    %s \n\n Shift    %s \n\n Date of Exception:    %s \n\n Part #:    %s \n\n Previous Part #:    %s \n\n Begin Setup (hundreths):    %s \n\n End Setup (hundreths):    %s \n\n Cumulative Time:    %s \n\n Exception Time:    %s \n\n Difference of Actual/Exception:    %s \n\n Time Supervisor Notified:    %s \n\n Time I.E. Notified:    %s \n\n Breaks:    %s \n\n Explanation:    %s' % (form.cleaned_data['employee'], form.cleaned_data['shift'], form.cleaned_data['date'], form.cleaned_data['part_num'], form.cleaned_data['prev_part_num'], form.cleaned_data['begin_setup'], form.cleaned_data['end_setup'], form.cleaned_data['cum_time'], form.cleaned_data['excep_time'], form.cleaned_data['difference'], form.cleaned_data['time_sup'], form.cleaned_data['time_ie'], form.cleaned_data['breaks'], form.cleaned_data['explanation'],) 
            from_addr = (request.user.email)
            recipient_list = ['keller@aymcdonald.com', 'msullivan@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'tkennett@aymcdonald.com', 'lbarr@aymcdonald.com', 'jsommers@aymcdonald.com','dsimerly@aymcdonald.com', 'amehlhorn@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'acollins@aymcdonald.com', 'amehlhorn@aymcdonald.com', 'jmullins@aymcdonald.com', 'cmiller@aymcdonald.com', 'tshelton@aymcdonald.com', 'cstrong@aymcdonald.com', 'kwagner@aymcdonald.com', 'mjustin@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tennsetupexception)
    users = TennSetupException.objects.all()
    form = TennSetupExceptionForm()
    context = Context({'title': 'Tennessee Setup Exception', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def timestudy(request):
    if request.method == 'POST':
        form = TimeStudyForm(request.POST)
        if form.is_valid():
            subject = 'Time Study'
            message = '\n Clock #:    %s \n\n Part #:    %s \n\n Operation #:    %s \n\n Machine #:    %s \n\n Pieces Remaining:    %s \n\n Comments:    %s' % (form.cleaned_data['clock_num'],  form.cleaned_data['part_num'], form.cleaned_data['operation_num'], form.cleaned_data['machine_num'], form.cleaned_data['pieces'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['jcabana@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmalek@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(timestudy)
    users = TimeStudy.objects.all()
    form = TimeStudyForm()
    context = Context({'title': 'Time Study', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def requesttopost(request):
    if request.method == 'POST':
        form = RequestToPostForm(request.POST)
        if form.is_valid():
            subject = 'Request To Post'
            message = '\n Classification:    %s \n\n Department:    %s \n\n Shift:    %s \n\n Posting Date:    %s \n\n Explaination:    %s' % (form.cleaned_data['classification'],  form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['post_date'], form.cleaned_data['explaination']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'jremakel@aymcdonald.com', 'rmccullough@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'msullivan@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(requesttopost)
    users = RequestToPost.objects.all()
    form = RequestToPostForm()
    context = Context({'title': 'Request To Post', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def toolroomrequest(request):
    if request.method == 'POST':
        form = ToolRoomRequestForm(request.POST)
        if form.is_valid():
            subject = 'Tool Room Request    %s' % (form.cleaned_data['tool'])
            message = '\n Tool/Fixture:    %s \n\n Description:    %s \n\n Work Center:    %s \n\n Requestor:    %s \n\n Date:    %s \n\n Date Required:    %s \n\n Comments:    %s' % (form.cleaned_data['tool'],  form.cleaned_data['description'], form.cleaned_data['work_center'], form.cleaned_data['requestor'], form.cleaned_data['date'], form.cleaned_data['date_req'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'dscherbring@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'rmccullough@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(toolroomrequest)
    users = ToolRoomRequest.objects.all()
    form = ToolRoomRequestForm()
    context = Context({'title': 'Tool Room Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def weightchange(request):
    if request.method == 'POST':
        form = WeightChangeForm(request.POST)
        if form.is_valid():
            subject = 'Weight Change    %s' % (form.cleaned_data['part_num'])
            message = '\n Part #:    %s \n\n Weight Per Piece:    %s' % (form.cleaned_data['part_num'], form.cleaned_data['weight']) 
            from_addr = (request.user.email)
            recipient_list = ['jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(weightchange)
    users = WeightChange.objects.all()
    form = WeightChangeForm()
    context = Context({'title': 'Weight Change', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def vacationrequest(request):
    if request.method == 'POST':
        form = VacationRequestForm(request.POST)
        if form.is_valid():
            subject = 'Vacation Request    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee #:    %s \n\n Date/Time Requested:    %s \n\n Date of Vacation:    %s \n\n Dept/Shift:    %s \n\n One Day:    %s \n\n 1/2 Day from beginning of shift:    %s \n\n 1/2 Day from end of shift:    %s \n\n 2 hr from beginning of shift:       %s \n\n 2 hr from end of shift:       %s \n\n Reason for exception:    %s \n \n \n Employee Signature:________________________________________         Date:__________ \n \n \n Supervisor Signature:________________________________________          Date:__________ \n \n \n HR Signature:________________________________________          Date:__________' %(form.cleaned_data['name'],  form.cleaned_data['employee_num'],  form.cleaned_data['date'],  form.cleaned_data['date_vaca'], form.cleaned_data['dept_shift'],  form.cleaned_data['day'],  form.cleaned_data['half_begin'],  form.cleaned_data['half_end'], form.cleaned_data['two_hour'], form.cleaned_data['two_hour_end'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jremakel@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'mvarley@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com','rdryer@aymcdonald.com', 'dberning@aymcdonald.com', 'asheehy@aymcdonald.com', 'mdolan@aymcdonald.com', 'cbrady@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(vacationrequest)
    users = VacationRequest.objects.all()
    form = VacationRequestForm()
    context = Context({'title': 'Vacation Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def vacationrequestfactory(request):
    if request.method == 'POST':
        form = VacationRequestFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Vacation Request-Factory    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee #:    %s \n\n Date/Time Requested:    %s \n\n Date of Vacation:    %s \n\n Dept/Shift:    %s \n\n One Day:    %s \n\n 1/2 Day from beginning of shift:    %s \n\n 1/2 Day from end of shift:    %s \n\n 2 hr from beginning of shift:       %s \n\n 2 hr from end of shift:       %s \n\n Reason for exception:    %s \n \n \n Employee Signature:________________________________________         Date:__________ \n \n \n Supervisor Signature:________________________________________          Date:__________ \n \n \n HR Signature:________________________________________          Date:__________' %(form.cleaned_data['name'],  form.cleaned_data['employee_num'],  form.cleaned_data['date'],  form.cleaned_data['date_vaca'], form.cleaned_data['dept_shift'],  form.cleaned_data['day'],  form.cleaned_data['half_begin'],  form.cleaned_data['half_end'], form.cleaned_data['two_hour'], form.cleaned_data['two_hour_end'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(vacationrequestfactory)
    users = VacationRequestFactory.objects.all()
    form = VacationRequestFactoryForm()
    context = Context({'title': 'Vacation Request-Factory', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def vacationrequestfoundry(request):
    if request.method == 'POST':
        form = VacationRequestFoundryForm(request.POST)
        if form.is_valid():
            subject = 'Vacation Request-Foundry    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee #:    %s \n\n Date/Time Requested:    %s \n\n Date of Vacation:    %s \n\n Dept/Shift:    %s \n\n One Day:    %s \n\n 1/2 Day from beginning of shift:    %s \n\n 1/2 Day from end of shift:    %s \n\n 2 hr from beginning of shift:       %s \n\n 2 hr from end of shift:       %s \n\n Reason for exception:    %s \n \n \n Employee Signature:________________________________________         Date:__________ \n \n \n Supervisor Signature:________________________________________          Date:__________ \n \n \n HR Signature:________________________________________          Date:__________' %(form.cleaned_data['name'],  form.cleaned_data['employee_num'],  form.cleaned_data['date'],  form.cleaned_data['date_vaca'], form.cleaned_data['dept_shift'],  form.cleaned_data['day'],  form.cleaned_data['half_begin'],  form.cleaned_data['half_end'], form.cleaned_data['two_hour'], form.cleaned_data['two_hour_end'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dwatson@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'jsaunders@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(vacationrequestfoundry)
    users = VacationRequestFoundry.objects.all()
    form = VacationRequestFoundryForm()
    context = Context({'title': 'Vacation Request-Foundry', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def vacationrequestmaint(request):
    if request.method == 'POST':
        form = VacationRequestMaintForm(request.POST)
        if form.is_valid():
            subject = 'Vacation Request-Maintenance    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee #:    %s \n\n Date/Time Requested:    %s \n\n Date of Vacation:    %s \n\n Dept/Shift:    %s \n\n One Day:    %s \n\n 1/2 Day from beginning of shift:    %s \n\n 1/2 Day from end of shift:    %s \n\n 2 hr from beginning of shift:       %s \n\n 2 hr from end of shift:       %s \n\n Reason for exception:    %s \n \n \n Employee Signature:________________________________________         Date:__________ \n \n \n Supervisor Signature:________________________________________          Date:__________ \n \n \n HR Signature:________________________________________          Date:__________' %(form.cleaned_data['name'],  form.cleaned_data['employee_num'],  form.cleaned_data['date'],  form.cleaned_data['date_vaca'], form.cleaned_data['dept_shift'],  form.cleaned_data['day'],  form.cleaned_data['half_begin'],  form.cleaned_data['half_end'], form.cleaned_data['two_hour'], form.cleaned_data['two_hour_end'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dberning@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dscherbring@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'dwatson@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(vacationrequestmaint)
    users = VacationRequestMaint.objects.all()
    form = VacationRequestMaintForm()
    context = Context({'title': 'Vacation Request-Maintenance', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def vacationrequestship(request):
    if request.method == 'POST':
        form = VacationRequestShipForm(request.POST)
        if form.is_valid():
            subject = 'Vacation Request-Shipping    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Employee #:    %s \n\n Date/Time Requested:    %s \n\n Date of Vacation:    %s \n\n Dept/Shift:    %s \n\n One Day:    %s \n\n 1/2 Day from beginning of shift:    %s \n\n 1/2 Day from end of shift:    %s \n\n 2 hr from beginning of shift:       %s \n\n 2 hr from end of shift:       %s \n\n Reason for exception:    %s \n \n \n Employee Signature:________________________________________         Date:__________ \n \n \n Supervisor Signature:________________________________________          Date:__________ \n \n \n HR Signature:________________________________________          Date:__________' %(form.cleaned_data['name'],  form.cleaned_data['employee_num'],  form.cleaned_data['date'],  form.cleaned_data['date_vaca'], form.cleaned_data['dept_shift'],  form.cleaned_data['day'],  form.cleaned_data['half_begin'],  form.cleaned_data['half_end'], form.cleaned_data['two_hour'], form.cleaned_data['two_hour_end'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'msullivan@aymcdonald.com', 'pjentz@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(vacationrequestship)
    users = VacationRequestShip.objects.all()
    form = VacationRequestShipForm()
    context = Context({'title': 'Vacation Request-Shipping', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def prototypesamples(request):
    if request.method == 'POST':
        form = PrototypeSamplesForm(request.POST)
        if form.is_valid():
            subject = 'Prototype/Samples'
            message = '\n Message:    %s \n\n Part #:    %s \n\n Quantitiy Needed:    %s \n\n Prints Provided:    %s \n\n Mat.Prov(2 XTRA):    %s \n\n Date Needed:    %s \n\n Similar to Part #:    %s \n\n Account Number:    %s \n\n Requestor:    %s \n\n Deliver Part To:    %s' % (form.cleaned_data['message'],  form.cleaned_data['part_num'],  form.cleaned_data['quantity'],  form.cleaned_data['prints'],  form.cleaned_data['mat'],  form.cleaned_data['date'],  form.cleaned_data['similar_part'],  form.cleaned_data['account_num'],  form.cleaned_data['requestor'],  form.cleaned_data['deliver']) 
            from_addr = (request.user.email)
            recipient_list = ['tpiggott@aymcdonald.com', 'stefft@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(prototypesamples)
    form = PrototypeSamplesForm()
    context = Context({'title': 'Prototype/Samples', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def routingchangerequest(request):
    if request.method == 'POST':
        form = RoutingChangeRequestForm(request.POST)
        if form.is_valid():
            subject = 'Routing Change Request'
            message = '\n Part #:    %s \n\n Operation #:    %s \n\n Requestor:    %s \n\n Date:    %s \n\n Reason:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['operation_num'],  form.cleaned_data['requestor'],  form.cleaned_data['date'],  form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'msullivan@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(routingchangerequest)
    form = RoutingChangeRequestForm()
    context = Context({'title': 'Routing Change Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def scrappedtooling(request):
    if request.method == 'POST':
        form = ScrappedToolingForm(request.POST)
        if form.is_valid():
            subject = 'Scrapped Tooling'
            message = '\n Tool #:    %s \n\n Quantity:    %s \n\n Remaining Tools on Hand:    %s \n\n Date:    %s \n\n Scrapped By:    %s \n\n Comments:    %s' % (form.cleaned_data['tool_num'],  form.cleaned_data['quantity'],  form.cleaned_data['remaining'],  form.cleaned_data['date'],  form.cleaned_data['scrapped'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jcabana@aymcdonald.com', 'tjohnson@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(scrappedtooling)
    form = ScrappedToolingForm()
    context = Context({'title': 'Scrapped Tooling', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def sandsieveanalysis(request):
    if request.method == 'POST':
        form = SandSieveAnalysisForm(request.POST)
        if form.is_valid():
            subject = 'Sand Sieve Analysis'
            message = '\n Sand Sieve Analysis Results Dated:    %s \n\n #6 Screen pct:    %s \n\n #12 Screen pct:    %s \n\n #20 Screen pct:    %s \n\n #30 Screen pct:    %s \n\n #40 Screen pct:    %s \n\n #50 Screen pct:    %s \n\n #70 Screen pct:    %s \n\n #100 Screen pct:    %s \n\n #140 Screen pct:    %s \n\n #200 Screen pct:    %s \n\n #270 Screen pct:    %s \n\n Pan pct:    %s \n\n AFS Grain Fineness # (Calc):    %s' % (form.cleaned_data['date'],  form.cleaned_data['a6screen'],  form.cleaned_data['a12screen'],  form.cleaned_data['a20screen'],  form.cleaned_data['a30screen'], form.cleaned_data['a40screen'], form.cleaned_data['a50screen'], form.cleaned_data['a70screen'], form.cleaned_data['a100screen'], form.cleaned_data['a140screen'], form.cleaned_data['a200screen'], form.cleaned_data['a270screen'], form.cleaned_data['pan'], form.cleaned_data['afs']) 
            from_addr = (request.user.email)
            recipient_list = ['dboleyn@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'ashea@aymcdonald.com', 'dberning@aymcdonald.com', 'ewolter@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(sandsieveanalysis)
    form = SandSieveAnalysisForm()
    context = Context({'title': 'Sand Sieve Analysis', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiashiftreport(request):
    if request.method == 'POST':
        form = AlbiaShiftReportForm(request.POST)
        if form.is_valid():
            subject = 'Albia Shift Report'
            message = '\n Cell:    %s    Setup:    %s    Part #:    %s   Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s     Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n  Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Cell:    %s    Setup:    %s    Part #:    %s    Status:    %s \n \n Additional Shift Notes:    %s' % (form.cleaned_data['z500'], form.cleaned_data['setup500'], form.cleaned_data['part_num500'], form.cleaned_data['status500'], form.cleaned_data['z702'], form.cleaned_data['setup702'], form.cleaned_data['part_num702'], form.cleaned_data['status702'], form.cleaned_data['z703'], form.cleaned_data['setup703'], form.cleaned_data['part_num703'], form.cleaned_data['status703'], form.cleaned_data['z704'], form.cleaned_data['setup704'], form.cleaned_data['part_num704'], form.cleaned_data['status704'], form.cleaned_data['z900'], form.cleaned_data['setup900'], form.cleaned_data['part_num900'], form.cleaned_data['status900'], form.cleaned_data['z901'], form.cleaned_data['setup901'], form.cleaned_data['part_num901'], form.cleaned_data['status901'], form.cleaned_data['z902a'], form.cleaned_data['setup902a'], form.cleaned_data['part_num902a'], form.cleaned_data['status902a'], form.cleaned_data['z902b'], form.cleaned_data['setup902b'], form.cleaned_data['part_num902b'], form.cleaned_data['status902b'], form.cleaned_data['z902c'], form.cleaned_data['setup902c'], form.cleaned_data['part_num902c'], form.cleaned_data['status902c'], form.cleaned_data['z904a'], form.cleaned_data['setup904a'], form.cleaned_data['part_num904a'], form.cleaned_data['status904a'], form.cleaned_data['z904b'], form.cleaned_data['setup904b'], form.cleaned_data['part_num904b'], form.cleaned_data['status904b'], form.cleaned_data['z904c'], form.cleaned_data['setup904c'], form.cleaned_data['part_num904c'], form.cleaned_data['status904c'], form.cleaned_data['z904d'], form.cleaned_data['setup904d'], form.cleaned_data['part_num904d'], form.cleaned_data['status904d'], form.cleaned_data['z904e'], form.cleaned_data['setup904e'], form.cleaned_data['part_num904e'], form.cleaned_data['status904e'],form.cleaned_data['z905'], form.cleaned_data['setup905'], form.cleaned_data['part_num905'], form.cleaned_data['status905'], form.cleaned_data['z908'], form.cleaned_data['setup908'], form.cleaned_data['part_num908'], form.cleaned_data['status908'], form.cleaned_data['z1101'], form.cleaned_data['setup1101'], form.cleaned_data['part_num1101'], form.cleaned_data['status1101'], form.cleaned_data['z1102'], form.cleaned_data['setup1102'], form.cleaned_data['part_num1102'], form.cleaned_data['status1102'], form.cleaned_data['z1103'], form.cleaned_data['setup1103'], form.cleaned_data['part_num1103'], form.cleaned_data['status1103'], form.cleaned_data['z1104'], form.cleaned_data['setup1104'], form.cleaned_data['part_num1104'], form.cleaned_data['status1104'],form.cleaned_data['z1201'], form.cleaned_data['setup1201'], form.cleaned_data['part_num1201'], form.cleaned_data['status1201'], form.cleaned_data['z1202'], form.cleaned_data['setup1202'], form.cleaned_data['part_num1202'], form.cleaned_data['status1202'], form.cleaned_data['z1203'], form.cleaned_data['setup1203'], form.cleaned_data['part_num1203'], form.cleaned_data['status1203'], form.cleaned_data['z1301'], form.cleaned_data['setup1301'], form.cleaned_data['part_num1301'], form.cleaned_data['status1301'],form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['mrockwell@aymcdonald.com', 'kdavis@aymcdonald.com', 'sperry@aymcdonald.com', 'ltucker@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'msullivan@aymcdonald.com', 'jkelley@aymcdonald.com', 'cskelton@aymcdonald.com', 'tmcvey@aymcdonald.com',  'dpendleton@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiashiftreport)
    form = AlbiaShiftReportForm()
    context = Context({'title': 'Albia Shift Report', 'form': form})
    return render_to_response('albiashiftreporttable.html', context, context_instance=RequestContext(request))

def loto(request):
    if request.method == 'POST':
        form = LoToForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Machine Lockout/Tagout'
            message = '\n Machine #/Cell:    %s \n\n Date/Time:    %s \n\n Comments:    %s' % (form.cleaned_data['machine_num'], form.cleaned_data['datetime'],  form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['keller@aymcdonald.com', 'sdayton@aymcdonald.com', 'dsimerly@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'tkennett@aymcdonald.com', 'jsommers@aymcdonald.com', 'lbarr@aymcdonald.com', 'acollins@aymcdonald.com', 'kgrindstaff@aymcdonald.com', 'cmorton@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(loto)
    form = LoToForm()
    context = Context({'title': 'Tennessee Machine Lockout/Tagout', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tempemployeembu(request):
    if request.method == 'POST':
        form = TempEmployeeMBUForm(request.POST)
        if form.is_valid():
            subject = 'Temp Employee-MBU    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Start Date:    %s \n\n Position:    %s \n\n Department:    %s \n\n Shift:    %s' % (form.cleaned_data['name'], form.cleaned_data['date'],  form.cleaned_data['position'], form.cleaned_data['department'], form.cleaned_data['shift']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jremakel@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com','dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'dgibbs@aymcdonald.com', 'jblack@aymcdonald.com', 'cbrady@aymcdonald.com', 'dhein@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tempemployeembu)
    form = TempEmployeeMBUForm()
    context = Context({'title': 'Temp Employee-MBU', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tempemployeefactory(request):
    if request.method == 'POST':
        form = TempEmployeeFactoryForm(request.POST)
        if form.is_valid():
            subject = 'Temp Employee-Factory    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Start Date:    %s \n\n Position:    %s \n\n Department:    %s \n\n Shift:    %s' % (form.cleaned_data['name'], form.cleaned_data['date'],  form.cleaned_data['position'], form.cleaned_data['department'], form.cleaned_data['shift']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tempemployeefactory)
    form = TempEmployeeFactoryForm()
    context = Context({'title': 'Temp Employee-Factory', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tempemployeefoundry(request):
    if request.method == 'POST':
        form = TempEmployeeFoundryForm(request.POST)
        if form.is_valid():
            subject = 'Temp Employee-Foundry    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Start Date:    %s \n\n Position:    %s \n\n Department:    %s \n\n Shift:    %s' % (form.cleaned_data['name'], form.cleaned_data['date'],  form.cleaned_data['position'], form.cleaned_data['department'], form.cleaned_data['shift']) 
            from_addr = (request.user.email)
            recipient_list = ['cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dwatson@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'dhein@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'pnugent@aymcdonald.com', 'rpetrick@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tempemployeefoundry)
    form = TempEmployeeFoundryForm()
    context = Context({'title': 'Temp Employee-Foundry', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tempemployeemaint(request):
    if request.method == 'POST':
        form = TempEmployeeMaintForm(request.POST)
        if form.is_valid():
            subject = 'Temp Employee-Maintenance    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Start Date:    %s \n\n Position:    %s \n\n Department:    %s \n\n Shift:    %s' % (form.cleaned_data['name'], form.cleaned_data['date'],  form.cleaned_data['position'], form.cleaned_data['department'], form.cleaned_data['shift']) 
            from_addr = (request.user.email)
            recipient_list = ['bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'cheim@aymcdonald.com', 'chuntington@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dscherbring@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'dwatson@aymcdonald.com', 'gbrown@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jcabana@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jkirk@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jremakel@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jschoop@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com',  'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tempemployeemaint)
    form = TempEmployeeMaintForm()
    context = Context({'title': 'Temp Employee-Maintenance', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tempemployeeship(request):
    if request.method == 'POST':
        form = TempEmployeeShipForm(request.POST)
        if form.is_valid():
            subject = 'Temp Employee-Shipping    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Start Date:    %s \n\n Position:    %s \n\n Department:    %s \n\n Shift:    %s' % (form.cleaned_data['name'], form.cleaned_data['date'],  form.cleaned_data['position'], form.cleaned_data['department'], form.cleaned_data['shift']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'cbrady@aymcdonald.com', 'chuntington@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jherrig@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'msullivan@aymcdonald.com', 'pjentz@aymcdonald.com',  'rmccullough@aymcdonald.com', 'shuschik@aymcdonald.com', 'ebradley@aymcdonald.com', 'sohara@aymcdonald.com', 'svanek@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tempemployeeship)
    form = TempEmployeeShipForm()
    context = Context({'title': 'Temp Employee-Shipping', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def aheirreport(request):
    if request.method == 'POST':
        form = AHEIRReportForm(request.POST)
        if form.is_valid():
            subject = 'AHE & IR Report' 
            message = '\n Date:    %s \n\n Supervisor:    %s \n\n Employee:    %s \n\n Rate Authorized:    %s \n\n Least Senior in Class (Y/N):    %s \n\n For Lack of Work (Y/N):    %s \n\n Details:    %s' % (form.cleaned_data['date'], form.cleaned_data['supervisor'], form.cleaned_data['employee'], form.cleaned_data['rate'], form.cleaned_data['senior'], form.cleaned_data['work'], form.cleaned_data['details']) 
            from_addr = (request.user.email)
            recipient_list = ['jremakel@aymcdonald.com', 'msullivan@aymcdonald.com', 'rmccullough@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(aheirreport)
    form = AHEIRReportForm()
    context = Context({'title': 'AHE & IR Report', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def instructionsheetupdate(request):
    if request.method == 'POST':
        form = InstructionSheetUpdateForm(request.POST)
        if form.is_valid():
            subject = 'Instruction Sheet Update' 
            message = '\n Instruction Sheet Release Notice:    %s \n\n Stocking Plants:    %s \n\n Revision Date:    %s \n\n New Release (Y/N):    %s \n\n Revised (Y/N):    %s \n\n Sales Intranet Needed (Y/N):    %s \n\n Product Section:    %s \n\n Replaces Inst. Sheet(s) When:    %s \n\n C.O. #:    %s \n\n Time Delay (Y/N):    %s \n\n Hole Size:    %s \n\n Hole Location:    %s \n\n Paper Type:    %s \n\n Paper Color:    %s \n\n Comments:    %s' % (form.cleaned_data['release'], form.cleaned_data['stocking'], form.cleaned_data['date'], form.cleaned_data['new_release'], form.cleaned_data['revised'], form.cleaned_data['intranet'], form.cleaned_data['product'], form.cleaned_data['replace'], form.cleaned_data['co_num'], form.cleaned_data['delay'], form.cleaned_data['hole_size'], form.cleaned_data['hole_loc'], form.cleaned_data['paper_type'], form.cleaned_data['paper_color'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['bhaas@aymcdonald.com', 'dconnolly@aymcdonald.com', 'dgreenwood@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'ewolter@aymcdonald.com', 'gbrown@aymcdonald.com', 'jremakel@aymcdonald.com', 'jzurcher@aymcdonald.com', 'kduex@aymcdonald.com', 'keller@aymcdonald.com', 'syaklin@aymcdonald.com', 'qmccullough@aymcdonald.com', 'rmccullough@aymcdonald.com', 'stefft@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'thast@aymcdonald.com', 'jkendell@aymcdonald.com', 'pmartelli@aymcdonald.com', 'ssabers@aymcdonald.com', 'lvannatta@aymcdonald.com',   (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(instructionsheetupdate)
    form = InstructionSheetUpdateForm()
    context = Context({'title': 'Instruction Sheet Update', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def overtimerequest(request):
    if request.method == 'POST':
        form = OvertimeRequestForm(request.POST)
        if form.is_valid():
            subject = 'Overtime Request' 
            message = '\n Date:    %s \n\n Dept(s) Individual Employee:    %s \n\n Shift:    %s \n\n Time:    %s \n\n Change Start/Finish Time:    %s \n\n Post (Y/N):    %s \n\n Posting Date:    %s' % (form.cleaned_data['date'], form.cleaned_data['department'], form.cleaned_data['shift'], form.cleaned_data['time'], form.cleaned_data['change'], form.cleaned_data['post'], form.cleaned_data['post_date']) 
            from_addr = (request.user.email)
            recipient_list = ['dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jremakel@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com','jboll@aymcdonald.com', 'cbrady@aymcdonald.com', 'dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com',  'svanek@aymcdonald.com' , 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(overtimerequest)
    form = OvertimeRequestForm()
    context = Context({'title': 'Overtime Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def packingstandard(request):
    if request.method == 'POST':
        form = PackingStandardForm(request.POST)
        if form.is_valid():
            subject = 'Packing Standard' 
            message = '\n Part #:    %s \n\n Carton #:    %s \n\n Carton Weight:    %s \n\n Pieces per Carton:    %s \n\n Pieces per Totepan:    %s \n\n Jolts per Carton:    %s \n\n Weight of 3 Pieces:    %s \n\n 1/Hand Simo:    %s \n\n 2/Hand Simo:    %s \n\n 2 Hands/PC:    %s \n\n Stacked:    %s \n\n Random:    %s \n\n Quantity of Subassemblies:    %s \n\n Quantity of Instruction Sheets:    %s \n\n Needs:    %s \n\n # of PCs in Order:    %s' % (form.cleaned_data['part_num'], form.cleaned_data['carton_num'], form.cleaned_data['carton_wgt'], form.cleaned_data['pcs_carton'], form.cleaned_data['pcs_tote'], form.cleaned_data['jolts_carton'], form.cleaned_data['wgt_three_pcs'], form.cleaned_data['one_hand'], form.cleaned_data['two_hand'], form.cleaned_data['two_hand_pc'], form.cleaned_data['stacked'], form.cleaned_data['random'], form.cleaned_data['qty_sub'], form.cleaned_data['qty_inst'], form.cleaned_data['needs'], form.cleaned_data['num_pcs'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jcabana@aymcdonald.com', 'jmalek@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(packingstandard)
    form = PackingStandardForm()
    context = Context({'title': 'Packing Standard', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def productionorderchange(request):
    if request.method == 'POST':
        form = ProductionOrderChangeForm(request.POST)
        if form.is_valid():
            subject = 'Production Order Change' 
            message = '\n Work Center:    %s \n\n Order #:    %s \n\n Due Date:    %s \n\n Order Qty:    %s \n\n Part #:    %s \n\n Priority Code:    %s \n\n Describe what happened/current status:    %s' % (form.cleaned_data['work'], form.cleaned_data['order_num'], form.cleaned_data['date'], form.cleaned_data['order_qty'], form.cleaned_data['part_num'], form.cleaned_data['priority'], form.cleaned_data['description']) 
            from_addr = (request.user.email)
            recipient_list = ['amehlhorn@aymcdonald.com', 'ashea@aymcdonald.com', 'bmorgan@aymcdonald.com', 'dratterman@aymcdonald.com', 'dthen@aymcdonald.com',  'gbrown@aymcdonald.com', 'jherrig@aymcdonald.com', 'jremakel@aymcdonald.com', 'jschoop@aymcdonald.com', 'jkendell@aymcdonald.com', 'efaust@aymcdonald.com', 'gryan@aymcdonald.com' , 'marling@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'rmccullough@aymcdonald.com', 'pmartelli@aymcdonald.com',  'tbanwarth@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(productionorderchange)
    form = ProductionOrderChangeForm()
    context = Context({'title': 'Production Order Change', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def projectrequest(request):
    if request.method == 'POST':
        form = ProjectRequestForm(request.POST)
        if form.is_valid():
            subject = 'Project Request' 
            message = '\n Requestor:    %s \n\n Date:    %s \n\n Project Title:    %s \n\n New:    %s \n\n Chg:    %s \n\n Deploy:    %s \n\n Description:    %s \n\n Reason:    %s' % (form.cleaned_data['requestor'], form.cleaned_data['date'], form.cleaned_data['project'], form.cleaned_data['new'], form.cleaned_data['chg'], form.cleaned_data['deploy'], form.cleaned_data['description'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['jboll@aymcdonald.com', 'lmiller@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(projectrequest)
    form = ProjectRequestForm()
    context = Context({'title': 'Project Request', 'form': form})
    return render_to_response('projectrequest.html', context, context_instance=RequestContext(request))

def fabrequest(request):
    if request.method == 'POST':
        form = FabRequestForm(request.POST)
        if form.is_valid():
            subject = 'Fab Request' 
            message = '\n Date:    %s \n\n Request Date:    %s \n\n Plate #:    %s \n\n Part #:    %s \n\n Quantity:    %s \n\n Order #:    %s \n\n Fab From:    %s \n\n Description:    %s' % (form.cleaned_data['date'], form.cleaned_data['req_date'], form.cleaned_data['plate'], form.cleaned_data['part_num'], form.cleaned_data['quantity'], form.cleaned_data['order_num'], form.cleaned_data['fab'], form.cleaned_data['description']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'mkirby@aymcdonald.com', 'pjentz@aymcdonald.com', 'rmccullough@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'tbanwarth@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(fabrequest)
    form = FabRequestForm()
    context = Context({'title': 'Fab Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def toolboxminutes(request):
    if request.method == 'POST':
        form = ToolboxMinutesForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Toolbox Minutes' 
            message = '\n Notes:    %s' % (form.cleaned_data['notes']) 
            from_addr = (request.user.email)
            recipient_list = ['msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'rmccullough@aymcdonald.com', 'jremakel@aymcdonald.com', 'gbrown@aymcdonald.com', 'kdavis@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'dsimerly@aymcdonald.com', 'jsommers@aymcdonald.com', 'tkennett@aymcdonald.com', 'lbarr@aymcdonald.com', 'acollins@aymcdonald.com', 'keller@aymcdonald.com', 'jkelley@aymcdonald.com', 'dpendleton@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bfebhard@aymcdonald.com','dschoenberger@aymcdonald.com', 'ltucker@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(toolboxminutes)
    form = ToolboxMinutesForm()
    context = Context({'title': 'Tennessee Toolbox Minutes', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def shiftreport(request):
    if request.method == 'POST':
        form = ShiftReportForm(request.POST)
        if form.is_valid():
            subject = 'Shift Report' 
            message = '\n Message:    %s' % (form.cleaned_data['message']) 
            from_addr = (request.user.email)
            recipient_list = ['msullivan@aymcdonald.com', 'dscherbring@aymcdonald.com', 'mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rmccullough@aymcdonald.com', 'jremakel@aymcdonald.com', 'gbrown@aymcdonald.com' , 'jschoop@aymcdonald.com', 'kdavis@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'dsimerly@aymcdonald.com', 'jsommers@aymcdonald.com', 'tkennett@aymcdonald.com', 'lbarr@aymcdonald.com', 'acollins@aymcdonald.com', 'keller@aymcdonald.com', 'jkelley@aymcdonald.com', 'jjohnson@aymcdonald.com',  'dpendleton@aymcdonald.com', 'dmalone@aymcdonald.com', 'cskelton@aymcdonald.com', 'amehlhorn@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com','ltucker@aymcdonald.com', 'mdobraska@aymcdonald.com', 'lbrown@aymcdonald.com', 'pmcdaniel@aymcdonald.com', 'tmcvey@aymcdonald.com', 'slampier@aymcdonald.com', 'gcurtis@aymcdonald.com', 'mrockwell@aymcdonald.com', 'kdavis@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'jburdt@aymcdonald.com', 'rdryer@aymcdonald.com', 'jherrig@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(shiftreport)
    form = ShiftReportForm()
    context = Context({'title': 'Shift Report', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiasetupexception(request):
    if request.method == 'POST':
        form = AlbiaSetupExceptionForm(request.POST)
        if form.is_valid():
            subject = '%s Albia Setup Exception' % (form.cleaned_data['work_center'])
            message = 'Employee:    %s \n\n Shift    %s \n\n Date of Exception:    %s \n\n Part #:    %s \n\n Previous Part #:    %s \n\n Begin Setup (hundreths):    %s \n\n End Setup (hundreths):    %s \n\n Cumulative Time:    %s \n\n Exception Time:    %s \n\n Difference of Actual/Exception:    %s \n\n Time Supervisor Notified:    %s \n\n Time I.E. Notified:    %s \n\n Breaks:    %s \n\n Explanation:    %s' % (form.cleaned_data['employee'], form.cleaned_data['shift'], form.cleaned_data['date'], form.cleaned_data['part_num'], form.cleaned_data['prev_part_num'], form.cleaned_data['begin_setup'], form.cleaned_data['end_setup'], form.cleaned_data['cum_time'], form.cleaned_data['excep_time'], form.cleaned_data['difference'], form.cleaned_data['time_sup'], form.cleaned_data['time_ie'], form.cleaned_data['breaks'], form.cleaned_data['explanation'],) 
            from_addr = (request.user.email)
            recipient_list = ['amehlhorn@aymcdonald.com','kdavis@aymcdonald.com',  'dpendleton@aymcdonald.com', 'jkelley@aymcdonald.com', 'cskelton@aymcdonald.com', 'ltucker@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'msullivan@aymcdonald.com', 'tmcvey@aymcdonald.com', 'kwagner@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiasetupexception)
    form = AlbiaSetupExceptionForm()
    context = Context({'title': 'Albia Setup Exception', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiamaintrequest(request):
    if request.method == 'POST':
        form = AlbiaMaintRequestForm(request.POST)
        if form.is_valid():
            subject = 'Albia Maintenance Request' 
            message = '\n Department:    %s \n\n Dept Num:    %s \n\n Machine:    %s \n\n Safety:    %s \n\n Description:    %s \n\n Lout:    %s \n\n Cell:    %s \n\n Request:    %s' % (form.cleaned_data['department'],  form.cleaned_data['department_num'], form.cleaned_data['machine'], form.cleaned_data['safety'], form.cleaned_data['description'], form.cleaned_data['lout'], form.cleaned_data['cell'], form.cleaned_data['request']) 
            from_addr = (request.user.email)
            recipient_list = ['ltucker@aymcdonald.com', 'mdobraska@aymcdonald.com',  'jkelley@aymcdonald.com', 'lbrown@aymcdonald.com', 'pmcdanel@aymcdonald.com', 'spangburn@aymcdonald.com', 'msullivan@aymcdonald.com', 'tmcvey@aymcdonald.com', 'slampier@aymcdonald.com',  'dpendleton@aymcdonald.com', 'gcurtis@aymcdonald.com', 'mrockwell@aymcdonald.com', 'dmalone@aymcdonald.com', 'cskelton@aymcdonald.com', 'kdavis@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiamaintrequest)
    form = AlbiaMaintRequestForm()
    context = Context({'title': 'Albia Maintenance Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiamachinedownlog(request):
    if request.method == 'POST':
        form = AlbiaMachineDownLogForm(request.POST)
        if form.is_valid():
            subject = 'Albia Machine Down Log    %s' % (form.cleaned_data['machine_num'])
            message = '\n Date:    %s \n\n Machine #:    %s \n\n Cell #:    %s \n\n Machine Description:    %s \n\n Reason Down:    %s \n\n Duration Days:    %s' % (form.cleaned_data['date'],  form.cleaned_data['machine_num'], form.cleaned_data['cell_num'], form.cleaned_data['machine_desc'], form.cleaned_data['reason'], form.cleaned_data['duration']) 
            from_addr = (request.user.email)
            recipient_list = ['msullivan@aymcdonald.com','lotting@aymcdonald.com', 'marling@aymcdonald.com', 'jremakel@aymcdonald.com', 'dschumacher@aymcdonald.com', 'mbeadle@aymcdonald.com', 'mrockwell@aymcdonald.com', 'pmcdanel@aymcdonald.com', 'gcurtis@aymcdonald.com', 'dberning@aymcdonald.com', 'slampier@aymcdonald.com', 'dmalone@aymcdonald.com', 'cskelton@aymcdonald.com', 'jkelley@aymcdonald.com',  'dpendleton@aymcdonald.com', 'ltucker@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'rdryer@aymcdonald.com', 'amehlhorn@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'kdavis@aymcdonald.com', 'spangburn@aymcdonald.com', 'sduncan@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiamachinedownlog)
    form = AlbiaMachineDownLogForm()
    context = Context({'title': 'Albia Machine Down Log', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiarejectedparts(request):
    if request.method == 'POST':
        form = AlbiaRejectedPartsForm(request.POST)
        if form.is_valid():
            subject = 'Albia Rejected Parts'
            message = '\n Rejected #:    %s \n\n Part #:    %s \n\n Quantity:    %s \n\n Department:    %s \n\n PO #:    %s \n\n Vendor:    %s \n\n Tracking Order Required:    %s \n\n Tracking Order #:    %s \n\n Reason for Rejection:    %s \n\n Disposition:    %s' % (form.cleaned_data['reject_num'],  form.cleaned_data['part_num'], form.cleaned_data['quantity'], form.cleaned_data['department'], form.cleaned_data['po_num'], form.cleaned_data['vendor'], form.cleaned_data['tracking'], form.cleaned_data['tracking_num'], form.cleaned_data['description'], form.cleaned_data['reason'], form.cleaned_data['disposition']) 
            from_addr = (request.user.email)
            recipient_list = ['msullivan@aymcdonald.com','lotting@aymcdonald.com', 'marling@aymcdonald.com', 'jremakel@aymcdonald.com', 'jburdt@aymcdonald.com', 'mrockwell@aymcdonald.com', 'tmcvey@aymcdonald.com', 'rhall@aymcdonald.com', 'kdavis@aymcdonald.com', 'bhaas@aymcdonald.com', 'stefft@aymcdonald.com', 'shall@aymcdonald.com', 'rmccullough@aymcdonald.com',  'dpendleton@aymcdonald.com', 'ltucker@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'ashea@aymcdonald.com',  (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiarejectedparts)
    form = AlbiaRejectedPartsForm()
    context = Context({'title': 'Albia Rejected Parts', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiarejectstostk(request):
    if request.method == 'POST':
        form = AlbiaRejectsToStkForm(request.POST)
        if form.is_valid():
            subject = 'Albia Rejects To STK'
            message = '\n Part #:    %s \n\n Tracking Order #:    %s \n\n Return to Stock Ticket #:    %s \n\n Quantity:    %s \n\n Comments:    %s' % (form.cleaned_data['part_num'], form.cleaned_data['tracking_num'], form.cleaned_data['returnstk'], form.cleaned_data['quantity'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['lotting@aymcdonald.com', 'marling@aymcdonald.com', 'tmcvey@aymcdonald.com', 'ashea@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiarejectstostk)
    form = AlbiaRejectsToStkForm()
    context = Context({'title': 'Albia Rejects To Stk', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiagatepass(request):
    if request.method == 'POST':
        form = AlbiaGatePassForm(request.POST)
        if form.is_valid():
            subject = 'Albia Gate Pass    %s' % (form.cleaned_data['name'])
            message = '\n Name:    %s \n\n Date:    %s \n\n Clock #:    %s \n\n Sold:    %s \n\n Given To:    %s \n\n Borrowed Date:    %s \n\n Returned Date:    %s \n\n Approval:    %s \n\n Cost:    %s \n\n Description    %s' % (form.cleaned_data['name'],  form.cleaned_data['date'], form.cleaned_data['clock_num'], form.cleaned_data['sold'], form.cleaned_data['given'], form.cleaned_data['borrow_date'], form.cleaned_data['return_date'], form.cleaned_data['approval'], form.cleaned_data['cost'], form.cleaned_data['description']) 
            from_addr = (request.user.email)
            recipient_list = ['jremakel@aymcdonald.com', 'msullivan@aymcdonald.com', 'mdobraska@aymcdonald.com', 'lbrown@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com', 'mrockwell@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiagatepass)
    form = AlbiaGatePassForm()
    context = Context({'title': 'Albia Gate Pass', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def albiascrapnotice(request):
    if request.method == 'POST':
        form = AlbiaScrapNoticeForm(request.POST)
        if form.is_valid():
            subject = 'Albia Scrap Notice' 
            message = '\n Part # Scrapped:    %s \n\n Part # Scrapped Unit Goes Into:    %s \n\n Order # of Production Order:    %s \n\n Quantity Scrapped:    %s \n\n Order Quantity:    %s \n\n Cell # Part is running in:    %s \n\n Reason for Scrap:    %s' % (form.cleaned_data['part_num_scp'],  form.cleaned_data['part_num_scp_unt'], form.cleaned_data['order_num'], form.cleaned_data['quantity'], form.cleaned_data['order_qty'], form.cleaned_data['cell_num'], form.cleaned_data['reason']) 
            from_addr = (request.user.email)
            recipient_list = ['msullivan@aymcdonald.com', 'rmccullough@aymcdonald.com','stefft@aymcdonald.com', 'lotting@aymcdonald.com', 'marling@aymcdonald.com', 'ashea@aymcdonald.com', 'kdavis@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com',  'dpendleton@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkelley@aymcdonald.com', 'dmalone@aymcdonald.com', 'cskelton@aymcdonald.com',  'jjohnson@aymcdonald.com', 'tmcvey@aymcdonald.com', 'ltucker@aymcdonald.com', 'sduncan@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiascrapnotice)
    form = AlbiaScrapNoticeForm()
    context = Context({'title': 'Albia Scrap Notice', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def tennmachinedownlog(request):
    if request.method == 'POST':
        form = TennMachineDownLogForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Machine Down Log    %s' % (form.cleaned_data['machine_num'])
            message = '\n Date:    %s \n\n Machine #:    %s \n\n Cell #:    %s \n\n Machine Description:    %s \n\n Reason Down:    %s \n\n Duration Days:    %s' % (form.cleaned_data['date'],  form.cleaned_data['machine_num'], form.cleaned_data['cell_num'], form.cleaned_data['machine_desc'], form.cleaned_data['reason'], form.cleaned_data['duration']) 
            from_addr = (request.user.email)
            recipient_list = ['msullivan@aymcdonald.com', 'keller@aymcdonald.com','rdryer@aymcdonald.com','hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'dsimerly@aymcdonald.com', 'jsommers@aymcdonald.com', 'tkennett@aymcdonald.com', 'lbarr@aymcdonald.com', 'acollins@aymcdonald.com', 'jimbus@aymcdonald.com', 'kgrindstaff@aymcdonald.com', 'cmorton@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tennmachinedownlog)
    form = TennMachineDownLogForm()
    context = Context({'title': 'Tennessee Machine Down Log', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))


def resourcegrpsetup(request):
    if request.method == 'POST':
        form = ResourceGrpSetupForm(request.POST)
        if form.is_valid():
            subject = 'Resource Group Setup' 
            message = '\n Plant:    %s \n\n Department:    %s \n\n Center:    %s \n\n Class:    %s \n\n FDY Mold:    %s \n\n Short Desc:    %s \n\n Contain:    %s \n\n Group:    %s \n\n Long Desc:    %s \n\n EST Setup Time:    %s' % (form.cleaned_data['plant'],  form.cleaned_data['department'], form.cleaned_data['center'], form.cleaned_data['class_desc'], form.cleaned_data['fdy_mold'], form.cleaned_data['short_desc'], form.cleaned_data['contain'], form.cleaned_data['group'], form.cleaned_data['long_desc'], form.cleaned_data['setup_time']) 
            from_addr = (request.user.email)
            recipient_list = ['ashea@aymcdonald.com', 'bfee@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'bhaas@aymcdonald.com', 'bmorgan@aymcdonald.com', 'bwoods@aymcdonald.com', 'dberning@aymcdonald.com', 'dconnolly@aymcdonald.com', 'dratterman@aymcdonald.com', 'dscherbring@aymcdonald.com', 'dthen@aymcdonald.com', 'ewolter@aymcdonald.com', 'gbrown@aymcdonald.com', 'hdao@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jburdt@aymcdonald.com', 'jcabana@aymcdonald.com', 'jherrig@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'jimbus@aymcdonald.com', 'jmalek@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jschoop@aymcdonald.com', 'jzurcher@aymcdonald.com', 'kduex@aymcdonald.com', 'lotting@aymcdonald.com', 'marling@aymcdonald.com', 'mkirby@aymcdonald.com', 'msullivan@aymcdonald.com', 'parnold@aymcdonald.com', 'pnowachek@aymcdonald.com', 'raspen@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'rrokusek@aymcdonald.com', 'rwagner@aymcdonald.com', 'sbrietbach@aymcdonald.com', 'stefft@aymcdonald.com', 'thast@aymcdonald.com', 'tlucey@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(resourcegrpsetup)
    form = ResourceGrpSetupForm()
    context = Context({'title': 'Resource Group Setup', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def blastsandsieve(request):
    if request.method == 'POST':
        form = BlastSandSieveForm(request.POST)
        if form.is_valid():
            subject = 'Blast Sand Sieve' 
            message = '\n Indicate Which Machine:    %s \n\n #18 Screen pct:    %s    Specification \n\n #20 Screen pct:    %s \n\n #25 Screen pct:    %s \n\n #30 Screen pct:    %s   (35%%-50%%) \n\n #35 Screen pct:    %s \n\n #40 Screen pct:    %s \n\n #45 Screen pct:    %s \n\n #50 Screen pct:    %s \n\n #60 Screen pct:    %s \n\n Pan pct:    %s' % (form.cleaned_data['machines'], form.cleaned_data['z18screen'],  form.cleaned_data['z20screen'], form.cleaned_data['z25screen'], form.cleaned_data['z30screen'], form.cleaned_data['z35screen'], form.cleaned_data['z40screen'], form.cleaned_data['z45screen'], form.cleaned_data['z50screen'], form.cleaned_data['z60screen'], form.cleaned_data['pan']) 
            from_addr = (request.user.email)
            recipient_list = ['ashea@aymcdonald.com', 'dberning@aymcdonald.com', 'dboleyn@aymcdonald.com', 'ewolter@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(blastsandsieve)
    form = BlastSandSieveForm()
    context = Context({'title': 'Blast Sand Sieve', 'form': form})
    return render_to_response('blastsandsieve.html', context, context_instance=RequestContext(request))

def productionproblemreport(request):
    if request.method == 'POST':
        form = ProductionProblemReportForm(request.POST)
        if form.is_valid():
            subject = 'Production Problem Report' 
            message = '\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s \n\n -------------------------------------------- \n\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['job_num'], form.cleaned_data['resource_num'], form.cleaned_data['cast_num'], form.cleaned_data['pri_code'], form.cleaned_data['due_date'], form.cleaned_data['job_qty'], form.cleaned_data['qty_ran'], form.cleaned_data['good_qty'], form.cleaned_data['description'], form.cleaned_data['reported'], form.cleaned_data['corrective'], form.cleaned_data['part_num2'],  form.cleaned_data['job_num2'], form.cleaned_data['resource_num2'], form.cleaned_data['cast_num2'], form.cleaned_data['pri_code2'], form.cleaned_data['due_date2'], form.cleaned_data['job_qty2'], form.cleaned_data['qty_ran2'], form.cleaned_data['good_qty2'], form.cleaned_data['description2'], form.cleaned_data['reported2'], form.cleaned_data['corrective2']) 
            from_addr = (request.user.email)
            recipient_list = ['parnold@aymcdonald.com', 'jremakel@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'dratterman@aymcdonald.com', 'msullivan@aymcdonald.com', 'gbrown@aymcdonald.com', 'jschoop@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', 'jmalek@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'cchrest@aymcdonald.com', 'ssabers@aymcdonald.com', 'mkirby@aymcdonald.com', 'bmorgan@aymcdonald.com', 'rmccullough@aymcdonald.com','lotting@aymcdonald.com', 'rwagner@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jkirk@aymcdonald.com', 'stefft@aymcdonald.com', 'dthen@aymcdonald.com', 'ashea@aymcdonald.com', 'rrokusek@aymcdonald.com', 'jburdt@aymcdonald.com', 'dboleyn@aymcdonald.com', 'bhaas@aymcdonald.com', 'jherrig@aymcdonald.com', 'pludowitz@aymcdonald.com', 'bolberding@aymcdonald.com', 'droush@aymcdonald.com', 'dcosley@aymcdonald.com', 'erauen@aymcdonald.com', 'jimbus@aymcdonald.com', 'klenz@aymcdonald.com', 'marling@aymcdonald.com', 'rdavid@aymcdonald.com',  'jkendell@aymcdonald.com', 'efaust@aymcdonald.com', 'gryan@aymcdonald.com' , 'pmartelli@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'jrissman@aymcdonald.com', 'astelken@aymcdonald.com', 'amehlhorn@aymcdonald.com', 'tlucey@aymcdonald.com', 'cheim@aymcdonald.com', 'ewolter@aymcdonald.com', 'kcarroll@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(productionproblemreport)
    form = ProductionProblemReportForm()
    context = Context({'title': 'Production Problem Report', 'form': form})
    return render_to_response('productionproblemreport.html', context, context_instance=RequestContext(request))

def albiaproductionproblemreport(request):
    if request.method == 'POST':
        form = AlbiaProductionProblemReportForm(request.POST)
        if form.is_valid():
            subject = 'Albia Production Problem Report' 
            message = '\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s \n\n -------------------------------------------- \n\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['job_num'], form.cleaned_data['resource_num'], form.cleaned_data['cast_num'], form.cleaned_data['pri_code'], form.cleaned_data['due_date'], form.cleaned_data['job_qty'], form.cleaned_data['qty_ran'], form.cleaned_data['good_qty'], form.cleaned_data['description'], form.cleaned_data['reported'], form.cleaned_data['corrective'], form.cleaned_data['part_num2'],  form.cleaned_data['job_num2'], form.cleaned_data['resource_num2'], form.cleaned_data['cast_num2'], form.cleaned_data['pri_code2'], form.cleaned_data['due_date2'], form.cleaned_data['job_qty2'], form.cleaned_data['qty_ran2'], form.cleaned_data['good_qty2'], form.cleaned_data['description2'], form.cleaned_data['reported2'], form.cleaned_data['corrective2']) 
            from_addr = (request.user.email)
            recipient_list = ['tpiggott@aymcdonald.com', 'msullivan@aymcdonald.com', 'kdavis@aymcdonald.com', 'sperry@aymcdonald.com', 'dschoenberger@aymcdonald.com',  'dpendleton@aymcdonald.com', 'lotting@aymcdonald.com', 'marling@aymcdonald.com', 'ashea@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jkelley@aymcdonald.com', 'dmalone@aymcdonald.com', 'cskelton@aymcdonald.com',  'tmcvey@aymcdonald.com', 'ltucker@aymcdonald.com', 'sduncan@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(albiaproductionproblemreport)
    form = AlbiaProductionProblemReportForm()
    context = Context({'title': 'Albia Production Problem Report', 'form': form})
    return render_to_response('productionproblemreport.html', context, context_instance=RequestContext(request))

def tennproductionproblemreport(request):
    if request.method == 'POST':
        form = TennProductionProblemReportForm(request.POST)
        if form.is_valid():
            subject = 'Tennessee Production Problem Report' 
            message = '\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s \n\n -------------------------------------------- \n\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['job_num'], form.cleaned_data['resource_num'], form.cleaned_data['cast_num'], form.cleaned_data['pri_code'], form.cleaned_data['due_date'], form.cleaned_data['job_qty'], form.cleaned_data['qty_ran'], form.cleaned_data['good_qty'], form.cleaned_data['description'], form.cleaned_data['reported'], form.cleaned_data['corrective'], form.cleaned_data['part_num2'],  form.cleaned_data['job_num2'], form.cleaned_data['resource_num2'], form.cleaned_data['cast_num2'], form.cleaned_data['pri_code2'], form.cleaned_data['due_date2'], form.cleaned_data['job_qty2'], form.cleaned_data['qty_ran2'], form.cleaned_data['good_qty2'], form.cleaned_data['description2'], form.cleaned_data['reported2'], form.cleaned_data['corrective2']) 
            from_addr = (request.user.email)
            recipient_list = ['adixon@aymcdonald.com', 'heller@aymcdonald.com', 'jwoodby@aymcdonald.com',  'tkennett@aymcdonald.com', 'lbarr@aymcdonald.com', 'dsimerly@aymcdonald.com', 'jsommers@aymcdonald.com', 'acollins@aymcdonald.com','ashea@aymcdonald.com', 'msullivan@aymcdonald.com', 'jimbus@aymcdonald.com', 'marling@aymcdonald.com', 'bhaas@aymcdonald.com', 'keller@aymcdonald.com', 'rdavid@aymcdonald.com', 'dcosley@aymcdonald.com', 'bolberding@aymcdonald.com', 'droush@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jgaber@aymcdonald.com', 'ewolter@aymcdonald.com', 'rwagner@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(tennproductionproblemreport)
    form = TennProductionProblemReportForm()
    context = Context({'title': 'Tenn Production Problem Report', 'form': form})
    return render_to_response('productionproblemreport.html', context, context_instance=RequestContext(request))


def fdytoolroomrequest(request):
    if request.method == 'POST':
        form = FDYToolRoomRequestForm(request.POST)
        if form.is_valid():
            subject = 'Foundry Tool Room Request    %s' % (form.cleaned_data['tool'])
            message = '\n Tool/Fixture:    %s \n\n Description:    %s \n\n Work Center:    %s \n\n Requestor:    %s \n\n Date:    %s \n\n Date Required:    %s \n\n Comments:    %s' % (form.cleaned_data['tool'],  form.cleaned_data['description'], form.cleaned_data['work_center'], form.cleaned_data['requestor'], form.cleaned_data['date'], form.cleaned_data['date_req'], form.cleaned_data['comments']) 
            from_addr = (request.user.email)
            recipient_list = ['dboleyn@aymcdonald.com', 'jsteffes@aymcdonald.com', 'cheim@aymcdonald.com', 'dwatson@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'jscherbring@aymcdonald.com', 'jremakel@aymcdonald.com', 'jkirk@aymcdonald.com', 'msullivan@aymcdonald.com', 'pludowitz@aymcdonald.com', 'jmiller@aymcdonald.com', 'mbasten@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(fdytoolroomrequest)
    form = FDYToolRoomRequestForm()
    context = Context({'title': 'Tool Room Request', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))


def rcleaker(request):
    if request.method == 'POST':
        form = RCLeakerForm(request.POST)
        if form.is_valid():
            subject = 'RC %s Leaker Issue' % (form.cleaned_data['rcpartnum'])
            message = '\n RC Part #:    %s \n\n Mach Part #:    %s \n\n Percent Leakers:    %s \n\n Location of the leak:    %s \n\n Cause of the leak (shrink, gas holes, cold shut, etc) if known:    %s \n\n Foundry Job:    %s \n\n Pour Date:    %s \n\n Pattern #:    %s \n\n Pattern vented?:    %s' % (form.cleaned_data['rcpartnum'],  form.cleaned_data['machpartnum'], form.cleaned_data['percentleakers'], form.cleaned_data['location'], form.cleaned_data['cause'], form.cleaned_data['foundjobnum'], form.cleaned_data['date_poured'], form.cleaned_data['patternnum'], form.cleaned_data['patternvent']) 
            from_addr = (request.user.email)
            recipient_list = ['astelken@aymcdonald.com', 'ashea@aymcdonald.com', 'bjohnson@aymcdonald.com', 'bhaas@aymcdonald.com', 'ewolter@aymcdonald.com', 'jgaber@aymcdonald.com', 'jrissman@aymcdonald.com', 'pnowachek@aymcdonald.com', 'qmccullough@aymcdonald.com', 'rrokusek@aymcdonald.com', 'rwagner@aymcdonald.com', 'tlucey@aymcdonald.com', 'jkirk@aymcdonald.com', 'dboleyn@aymcdonald.com', 'dwatson@aymcdonald.com', 'pludowitz@aymcdonald.com', 'jscherbring@aymcdonald.com', 'cheim@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(rcleaker)
    form = RCLeakerForm()
    context = Context({'title': 'RC Leaker Issue', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def vendorvisit(request):
    if request.method == 'POST':
        form = VendorVisitForm(request.POST)
        if form.is_valid():
            subject = '%s Visit To A.Y. McDonald' % (form.cleaned_data['vendorname'])
            message = '\n Vendor Name:    %s \n\n Visitors Name:    %s \n\n Visitors Name:    %s \n\n Visitors Name:    %s \n\n Visitors Name:    %s \n\n Visitors Name:    %s \n\n Person Visiting:    %s \n\n Purpose Of Visit:    %s \n\n Approximate Duration:    %s' % (form.cleaned_data['vendorname'],  form.cleaned_data['visitor1'], form.cleaned_data['visitor2'], form.cleaned_data['visitor3'], form.cleaned_data['visitor4'], form.cleaned_data['visitor5'], form.cleaned_data['visiting'], form.cleaned_data['purpose'], form.cleaned_data['duration']) 
            from_addr = (request.user.email)
            recipient_list = ['chuntington@aymcdonald.com', 'jbettcher@aymcdonald.com', 'jkohlenberg@aymcdonald.com', 'eburgmeier@aymcdonald.com', 'svanek@aymcdonald.com', 'ebradley@aymcdonald.com', 'shuschik@aymcdonald.com', 'sohara@aymcdonald.com', 'msullivan@aymcdonald.com', 'jremakel@aymcdonald.com', 'rmccullough@aymcdonald.com', 'jgaber@aymcdonald.com', 'bjohnson@aymcdonald.com', 'rdryer@aymcdonald.com', 'dschumacher@aymcdonald.com', 'dberning@aymcdonald.com', 'mbeadle@aymcdonald.com','guard1@aymcdonald.com', 'guard2@aymcdonald.com', 'guard3@aymcdonald.com', 'dhein@aymcdonald.com', 'rpetrick@aymcdonald.com', 'pnugent@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(vendorvisit)
    form = VendorVisitForm()
    context = Context({'title': 'Vendor Visits', 'form': form})
    return render_to_response('earlyclockout.html', context, context_instance=RequestContext(request))

def fivesupdate(request):
    if request.method == 'POST':
        form = FiveSUpdateForm(request.POST)
        if form.is_valid():
            subject = '5S Update' 
            message = '\n Date:    %s \n\n Cell:    %s \n\n Progress:    %s \n\n Activity:    %s \n\n Completed:    %s \n\n \n\n Employee:    %s \n\n Cell:    %s \n\n Activity:    %s \n\n Approx Hours:    %s \n\n \n\n Employee:    %s \n\n Cell:    %s \n\n Activity:    %s \n\n Approx Hours:    %s \n\n \n\n Employee:    %s \n\n Cell:    %s \n\n Activity:    %s \n\n Approx Hours:    %s \n\n \n\n Employee:    %s \n\n Cell:    %s \n\n Activity:    %s \n\n Approx Hours:    %s \n\n \n\n Employee:    %s \n\n Cell:    %s \n\n Activity:    %s \n\n Approx Hours:    %s' % (form.cleaned_data['date'],  form.cleaned_data['cell'], form.cleaned_data['progress'], form.cleaned_data['activity'], form.cleaned_data['completed'], form.cleaned_data['employee'], form.cleaned_data['celltwo'], form.cleaned_data['activity2'], form.cleaned_data['approxhours'], form.cleaned_data['employee2'], form.cleaned_data['celltwo2'], form.cleaned_data['activity3'], form.cleaned_data['approxhours2'],  form.cleaned_data['employee3'], form.cleaned_data['celltwo3'], form.cleaned_data['activity4'], form.cleaned_data['approxhours3'], form.cleaned_data['employee4'], form.cleaned_data['celltwo4'], form.cleaned_data['activity5'], form.cleaned_data['approxhours4'], form.cleaned_data['employee5'], form.cleaned_data['celltwo5'], form.cleaned_data['activity6'], form.cleaned_data['approxhours5']) 
            from_addr = (request.user.email)
            recipient_list = ['bmorgan@aymcdonald.com','dberning@aymcdonald.com', 'dscherbring@aymcdonald.com', 'gbrown@aymcdonald.com', 'jschoop@aymcdonald.com', 'jherrig@aymcdonald.com', 'jremakel@aymcdonald.com', 'mbeadle@aymcdonald.com', 'msullivan@aymcdonald.com', 'mkirby@aymcdonald.com', 'rdryer@aymcdonald.com', 'rmccullough@aymcdonald.com', 'tbanwarth@aymcdonald.com', 'amehlhorn@aymcdonald.com', 'banderson@aymcdonald.com', 'bgebhard@aymcdonald.com', 'hlangkamp@aymcdonald.com', 'jkendell@aymcdonald.com', 'jmiller@aymcdonald.com', 'jmalek@aymcdonald.com', 'jcabana@aymcdonald.com', 'jheuer@aymcdonald.com', 'mbasten@aymcdonald.com', 'parnold@aymcdonald.com', 'cchrest@aymcdonald.com', 'efaust@aymcdonald.com', 'gryan@aymcdonald.com', 'jschmitt@aymcdonald.com', 'pjentz@aymcdonald.com', 'pmartelli@aymcdonald.com', 'ssabers@aymcdonald.com', (request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(fivesupdate)
    form = FiveSUpdateForm()
    context = Context({'title': '5S Update', 'form': form})
    return render_to_response('fivesupdate.html', context, context_instance=RequestContext(request))

def roughcastreject(request):
    if request.method == 'POST':
        form = RoughCastRejectForm(request.POST)
        if form.is_valid():
            subject = 'Rough Cast Reject' 
            message = '\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Supervisor:    %s \n\n Quality Personnel:    %s \n\n I.E. Personnel    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s \n\n -------------------------------------------- \n\n Part #:    %s \n\n Job #:    %s \n\n Resource #:    %s \n\n Casting #:    %s \n\n Priority Code:    %s \n\n Due Date:    %s \n\n Job Qty:    %s \n\n Qty Ran:    %s \n\n Qty Good:    %s \n\n Supervisor:    %s \n\n Quality Personnel:    %s \n\n I.E. Personnel    %s \n\n Description of Problem:    %s \n\n Reported By:    %s \n\n Corrective Action By:    %s' % (form.cleaned_data['part_num'],  form.cleaned_data['job_num'], form.cleaned_data['resource_num'], form.cleaned_data['cast_num'], form.cleaned_data['pri_code'], form.cleaned_data['due_date'], form.cleaned_data['job_qty'], form.cleaned_data['qty_ran'], form.cleaned_data['good_qty'], form.cleaned_data['super'], form.cleaned_data['quality'], form.cleaned_data['ie'], form.cleaned_data['description'], form.cleaned_data['reported'], form.cleaned_data['corrective'], form.cleaned_data['part_num2'],  form.cleaned_data['job_num2'], form.cleaned_data['resource_num2'], form.cleaned_data['cast_num2'], form.cleaned_data['pri_code2'], form.cleaned_data['due_date2'], form.cleaned_data['job_qty2'], form.cleaned_data['qty_ran2'], form.cleaned_data['good_qty2'], form.cleaned_data['super2'], form.cleaned_data['quality2'], form.cleaned_data['ie2'], form.cleaned_data['description2'], form.cleaned_data['reported2'], form.cleaned_data['corrective2']) 
            from_addr = (request.user.email)
            recipient_list = ['kschmitt@aymcdonald.com',(request.user.email)]
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(roughcastreject)
    form = RoughCastRejectForm()
    context = Context({'title': 'Rough Cast Reject', 'form': form})
    return render_to_response('roughcastreject.html', context, context_instance=RequestContext(request))


def test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            subject = 'test' 
            message = '\n Message:    %s' % (form.cleaned_data['message']) 
            from_addr = (request.user.email)
#            recipient_list = [form.cleaned_data['email'].split(',')]
            recipient_list = ['kschmitt@aymcdonald.com']
            send_mail(subject, message, from_addr, recipient_list)
            form.save()
            return redirect(test)
    form = TestForm()
    context = Context({'title': 'Test', 'form': form})
    return render_to_response('test.html', context, context_instance=RequestContext(request))



@login_required
def TOC(request):
#    return direct_to_template(request, 'toc.html')
	return render(request, 'toc.html')

#def login_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        if user.is_active:
#            login(request, user)
#            return render(request, 'toc.html')
#        else:
#            return render(request, 'disabled.html')
#    else:
#        return render(request, 'invalid.html')

#def create_newuser(request, id=None):
#    """
#    Create a New User model form
#    """
#    form_args = {}
#    if id is not None:
#        # Edit an exiting New User object
#        try:
#            newuser = NewUser.objects.get(pk=id)
#        except NewUser.DoesNotExist:
#            return Http404('New User not found')
#        form_args['instance'] = newuser
#
#    if request.POST:
#        form_args['data'] = request.POST
#        form = NewUserForm(**form_args)
#        if form.is_valid():
#            #Create a New User object
#            name = form.cleaned_data['start_date']
#            subject = form.cleaned_data['first_name']
#            message = form.cleaned_data['first_name']
#            sender = form.cleaned_data['requested_by']
#            
#            #Import send_mail module and send mail
#            from djanog.core.mail import send_mail
#            send_mail(subject, message, sender, recipients)
#            createnu = form.save(commit=False)
#            createnu.save()
#            newuser = form.save(commit=True)    
#    else:
#            form = NewUserForm(**form_args)
#            recipients = (instance.send_to)
#    return render_to_response('newuser.html', {'form': form}, context_instance=RequestContext(request))
#
#    else:
#       form = NewUserForm()
#       return render_to_response('newuser.html', {'NewUserForm': form,})
#
#    variables = RequestContext(request, {'NewUserForm': form})
#
#    return render_to_response('newuser.html', variables)        
