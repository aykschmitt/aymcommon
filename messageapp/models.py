from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import date
from django.forms import ModelForm
import datetime


# Create your models here.

class DistList(models.Model):
    distribution_name = models.CharField("Distribution Name", blank=True, max_length=25)
#    member_name = models.ForeignKey(User, verbose_name = "Member", blank=True)
#    giggles = models.ForeignKey(User, verbose_name = "Member1", blank=True)
#    member_name_2 = models.ForeignKey(User, verbose_name = "Member2", blank=True)

    def __str__(self):
        return self.distribution_name

class Members(models.Model):
    DistList = models.ForeignKey(DistList, blank=True)
    member_name = models.ForeignKey(User, verbose_name = "Member", blank=True)

class NewUser(models.Model):    
    OUTLOOK_CHOICES = (
        ('Outlook', 'Outlook'),
        ('OWA', 'Web Access'),
    )

    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default ='aysupport')
    first_name = models.CharField(max_length=20, blank=True, verbose_name = "First Name")
    last_name = models.CharField(max_length=20, blank=True, verbose_name = "Last Name")
    start_date = models.DateField()
    requested_by = models.CharField(max_length=30, blank=True, verbose_name = "Requestor")
    job_title = models.CharField(max_length=20, blank=True, verbose_name = "Job Title")
    phone_ext = models.IntegerField(max_length=5, blank=True, null=True)
    fax_ext = models.IntegerField(max_length=15, blank=True, null=True)
    replace_check = models.BooleanField(verbose_name = "Replacing Someone", blank=True)
    replacing = models.CharField(max_length=40, blank=True, null=True, verbose_name = "Replacing or Setup Like")
    manager = models.CharField(max_length=40, blank=True, null=True)
    dept_num = models.IntegerField(max_length=5, blank=True, null=True, verbose_name = "Department #")
    pc_id = models.CharField(max_length=15, blank=True, null=True)
    printers = models.CharField(max_length=75, blank=True, null=True, verbose_name = "Access to these network printers")
    mail_access = models.CharField(max_length=12, choices=OUTLOOK_CHOICES, blank=True, null=True)
    cad19 = models.BooleanField(verbose_name = "CadKey 19", blank=True)
    cadview = models.BooleanField(verbose_name = "Cadkey Viewer", blank=True)
    proe = models.BooleanField(verbose_name = "Pro/E", blank=True)
    printscreen = models.BooleanField(verbose_name = "Printscreen Deluxe", blank=True)
    form_pilot = models.BooleanField(verbose_name = "Form Pilot Pro", blank=True)
    comments = models.TextField(blank=True)    

    def __str__(self):
        return self.first_name

class EarlyClockOut(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,eburgmeier,svanek,ebradley,shuschik,sohara,cbrady,jscherbring,jremakel,dwatson,dboleyn,cheim,jsteffes,jgaber,bjohnson,dberning,jkirk,msullivan,dhein,dberning,dscherbring,gbrown,jschoop,jschoop,hlangkamp,jmiller,mbasten,jmalek,mkirby,bmorgan,jcabana,jheuer,banderson,banderson,bgebhard,cchrest,ssabers,rmccullough,rdryer,guard2,guard3,pnugent,rpetrick,jherrig')
    name = models.CharField(max_length=35, verbose_name = "Name", blank=True)
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    reason = models.CharField(max_length=70, verbose_name = "Reason", blank=True)

    def __str__(self):
        return self.name

class EarlyClockOutFactory(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,chuntington,dscherbring,gbrown,hlangkamp,jbettcher,jcabana,jherrig,jheuer,banderson,jkohlenberg,eburgmeier,eburgmeier,jmalek,jmiller,mbasten,jremakel,jschoop,mkirby,msullivan,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth,sstankovich')
    name = models.CharField(max_length=35, verbose_name = "Name", blank=True)
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    reason = models.CharField(max_length=70, verbose_name = "Reason", blank=True)

    def __str__(self):
        return self.name

class EarlyClockOutFoundry(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='cbrady,cheim,chuntington,dboleyn,dwatson,jbettcher,jgaber,jkirk,jkohlenberg,eburgmeier,eburgmeier,jremakel,jscherbring,msullivan,jsaunders,pludowitz,shuschik,ebradley,sohara,svanek')
    name = models.CharField(max_length=35, verbose_name = "Name", blank=True)
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    reason = models.CharField(max_length=70, verbose_name = "Reason", blank=True)

    def __str__(self):
        return self.name

class EarlyClockOutMaint(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,cheim,chuntington,dboleyn,dscherbring,schumacher,dwatson,gbrown,hlangkamp,jbettcher,jcabana,jherrig,jheuer,banderson,jgaber,jkirk,jkohlenberg,eburgmeier,eburgmeier,jmalek,jmiller,mbasten,jremakel,jscherbring,jschoop,mkirby,msullivan,pludowitz,rdryer,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth,dhein,guard2,guard3,pnugent,rpetrick')
    name = models.CharField(max_length=35, verbose_name = "Name", blank=True)
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    reason = models.CharField(max_length=70, verbose_name = "Reason", blank=True)

    def __str__(self):
        return self.name

class EarlyClockOutShip(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,cbrady,chuntington,dscherbring,gbrown,jbettcher,jherrig,jkohlenberg,eburgmeier,eburgmeier,jremakel,jschoop,msullivan,pjentz,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=35, verbose_name = "Name", blank=True)
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    reason = models.CharField(max_length=70, verbose_name = "Reason", blank=True)

    def __str__(self):
        return self.name

class IssueMiscMaterial(models.Model):
    REASON_CHOICES = (
        ('81/85', '81Brass Used as 85'),
        ('ALB', 'Albia Issue'),
        ('CART1', 'Cartons to Mailroom'),
        ('CART2', 'Cartons to Shipping'),
        ('COSTL', 'Cost Load'),
        ('CUSCO', 'Customer Co-Op'),
        ('CUSLO', 'Customer Loyalty'),
        ('CYCL1', 'Cycle Count Adj Raw Material'),
        ('CYCL2', 'Cycle Count No Change'),
        ('CYCL3', 'Cycle Count Adj Components'),
        ('CYCL4', 'Cycle Count Adj FG'),
        ('CYCL5', 'Cycle Count Adjustment'),
        ('DBQMA', "Dubuque Repair & Maint Mat'l"),
        ('DUB', 'Dubuque Factory Issue'),
        ('ENDPC', 'Ball Value End Piece On Floor'),
        ('FND', 'Foundry Issue'),
        ('LF', 'Lost & Found'),
        ('NAIER', 'Naier Donations'),       
        ('PEGRD', 'PE HP Gas R&D Samples'),
        ('PEGAS', 'PE HP Gas Samples'),
        ('PENRD', 'PE No Lead R&D Samples'),
        ('PENL', 'PE No Lead Samples'),
        ('PEPLR', 'PE Plumbing R&D Samples'),
        ('PESMP', 'PE Plumbing Samples'),
        ('PEPUR', 'PE Pump R&D Samples'),
        ('PEPUM', 'PE Pump Samples'), 
        ('PEWRD', 'PE Water Works R&D Samples'),
        ('PE', 'PE Water Works Samples'),
        ('PIC', 'PIC Adjustment Misc'),
        ('PICC', 'PIC Cycle Count'),
        ('PUCK', 'Puck to Ingot'),
        ('QA', 'QA Samples'),
        ('QAALB', 'QA Albia Misc Return'),
        ('QAFND', 'QA Foundry Misc Return'),
        ('QAR&D', 'QA R&D Samples'),
        ('QASTK', 'QA Misc Return'),
        ('QATEN', 'QA Tenn Misc Return'),
        ('QAVEN', 'QA Vendor Misc Return'),
        ('RMA', 'RMA Parts'),
        ('S&O', 'Surplus & Obsolesence Misc'),
        ('S&OB', 'Surplus & Obsolesence Brass'),
        ('SAL', 'Chips to Stock'),
        ('SAMPL', 'Internal Sales Samples'),
        ('SPLST', 'Samples to Stock'),
        ('STKLO', 'Ingot Adj due to Stack Loss'),
        ('TENN', 'Tenn Issue'),
        ('VEN', 'Vendor Issue'),
        ('VNOCH', 'Vendor No Charge REplacement'),
        ('WDCFB', 'WDC Fabrication'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dscherbring,tbanwarth,gbrown,rmccullough,pjentz')
    part = models.CharField(max_length=20, blank=True)
    part02 = models.CharField(max_length=20, blank=True)
    part03 = models.CharField(max_length=20, blank=True)
    part04 = models.CharField(max_length=20, blank=True)
    part05 = models.CharField(max_length=20, blank=True)
    part06 = models.CharField(max_length=20, blank=True)
    part07 = models.CharField(max_length=20, blank=True)
    quantity = models.CharField(max_length=6, blank=True)
    quantity02 = models.CharField(max_length=6, blank=True)
    quantity03 = models.CharField(max_length=6, blank=True)
    quantity04 = models.CharField(max_length=6, blank=True)
    quantity05 = models.CharField(max_length=6, blank=True)
    quantity06 = models.CharField(max_length=6, blank=True)
    quantity07 = models.CharField(max_length=6, blank=True)     
    reference = models.CharField(max_length=50, blank=True)
    reason = models.CharField(max_length=30, blank=True, choices=REASON_CHOICES)
    bin_loc = models.CharField(max_length=6, blank=True, verbose_name = "Bin")
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.part

class TerminateEmployee(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jboll,thall,kschmitt,chillers')
    first_name = models.CharField(max_length=20, blank=True, verbose_name = "First Name")
    last_name = models.CharField(max_length=20, blank=True, verbose_name = "Last Name")
    term_date = models.DateField()    
    job_title = models.CharField(max_length=20, blank=True, verbose_name = "Job Title")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    comments = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.first_name

class TerminateEmployeeMBU(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,dberning,dscherbring,gbrown,jschoop,jschoop,hlangkamp,jmiller,mbasten,jmalek,jremakel,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,msullivan,mkirby,bmorgan,rdryer,rmccullough,dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,jgaber,dgibbs,jblack,dhein,guard2,guard3,pnugent,rpetrick,cbrady')
    name = models.CharField(max_length=20, blank=True, verbose_name = "Employee Name")
    term_date = models.DateField()    
    job_title = models.CharField(max_length=20, blank=True, verbose_name = "Job Title")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")

    def __str__(self):
        return self.name

class TerminateEmployeeFactory(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,dberning,dscherbring,gbrown,jschoop,jschoop,hlangkamp,jmiller,mbasten,jmalek,jremakel,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,msullivan,mkirby,bmorgan,rdryer,rmccullough,dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,jgaber,dgibbs,dhein,guard2,guard3,pnugent,rpetrick,cbrady,tbanwarth,sstankovich,dgibbs')
    name = models.CharField(max_length=20, blank=True, verbose_name = "Employee Name")
    term_date = models.DateField()    
    job_title = models.CharField(max_length=20, blank=True, verbose_name = "Job Title")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")

    def __str__(self):
        return self.name

class TerminateEmployeeFoundry(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='cbrady,cheim,chuntington,dboleyn,dwatson,jbettcher,jgaber,jkirk,jkohlenberg,eburgmeier,jremakel,jscherbring,msullivan,pludowitz,shuschik,ebradley,sohara,svanek,dhein,guard2,guard3,pnugent,rpetrick,sstankovich,dgibbs')
    name = models.CharField(max_length=20, blank=True, verbose_name = "Employee Name")
    term_date = models.DateField()    
    job_title = models.CharField(max_length=20, blank=True, verbose_name = "Job Title")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")

    def __str__(self):
        return self.name

class TerminateEmployeeMaint(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,cheim,chuntington,dboleyn,dscherbring,dschumacher,mbeadle,dwatson,gbrown,hlangkamp,jbettcher,jcabana,jherrig,jheuer,banderson,jkirk,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jscherbring,jschoop,mkirby,msullivan,pludowitz,rdryer,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth,dhein,guard2,guard3,pnugent,rpetrick,tbanwarth,sstankovich,dgibbs')
    name = models.CharField(max_length=20, blank=True, verbose_name = "Employee Name")
    term_date = models.DateField()    
    job_title = models.CharField(max_length=20, blank=True, verbose_name = "Job Title")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")

    def __str__(self):
        return self.name

class TerminateEmployeeShip(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,cbrady,chuntington,dscherbring,gbrown,jbettcher,jherrig,jkohlenberg,eburgmeier,jremakel,jschoop,msullivan,pjentz,rmccullough,shuschik,ebradley,sohara,svanek,dhein,guard2,guard3,pnugent,rpetrick,tbanwarth,sstankovich,dgibbs')
    name = models.CharField(max_length=20, blank=True, verbose_name = "Employee Name")
    term_date = models.DateField()    
    job_title = models.CharField(max_length=20, blank=True, verbose_name = "Job Title")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")

    def __str__(self):
        return self.name

class WeekInjIllFactory(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,chuntington,gbrown,jbettcher,dgibbs,jherrig,jkohlenberg,eburgmeier,jremakel,jschoop,mkirby,msullivan,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth,sstankovich')
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    description = models.CharField(max_length=60, blank=True, verbose_name = "Description of Inj/Ill")
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    medical_provider = models.CharField(max_length=30, blank=True, verbose_name = "Medical Care Provider Seen")
    work_restrictions = models.TextField(max_length=300, blank=True, verbose_name = "Work Restrictions")
    next_datetime = models.DateTimeField(verbose_name = "Next Date/Time")

    def __str__(self):
        return self.employee_num

class WeekInjIllFoundry(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='cheim,chuntington,dberning,dboyeln,dwatson,jbettcher,dgibbs,jgaber,jkirk,jkohlenberg,eburgmeier,jremakel,jscherbring,msullivan,jsaunders,pludowitz,shuschik,ebradley,sohara,sstankovich')
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    description = models.CharField(max_length=60, blank=True, verbose_name = "Description of Inj/Ill")
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    medical_provider = models.CharField(max_length=30, blank=True, verbose_name = "Medical Care Provider Seen")
    work_restrictions = models.TextField(max_length=300, blank=True, verbose_name = "Work Restrictions")
    next_datetime = models.DateTimeField(verbose_name = "Next Date/Time")

    def __str__(self):
        return self.employee_num

class WeekInjIllMaint(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,dberning,jbettcher,dgibbs,jkohlenberg,eburgmeier,jremakel,msullivan,rdryer,shuschik,ebradley,sohara,svanek,tbanwarth,sstankovich')
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    description = models.CharField(max_length=60, blank=True, verbose_name = "Description of Inj/Ill")
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    medical_provider = models.CharField(max_length=30, blank=True, verbose_name = "Medical Care Provider Seen")
    work_restrictions = models.TextField(max_length=300, blank=True, verbose_name = "Work Restrictions")
    next_datetime = models.DateTimeField(verbose_name = "Next Date/Time")

    def __str__(self):
        return self.employee_num

class WeekInjIllShipping(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,dscherbring,jbettcher,dgibbs,jkohlenberg,eburgmeier,jremakel,msullivan,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth,sstankovich')
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    description = models.CharField(max_length=60, blank=True, verbose_name = "Description of Inj/Ill")
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    medical_provider = models.CharField(max_length=30, blank=True, verbose_name = "Medical Care Provider Seen")
    work_restrictions = models.TextField(max_length=300, blank=True, verbose_name = "Work Restrictions")
    next_datetime = models.DateTimeField(verbose_name = "Next Date/Time")

    def __str__(self):
        return self.employee_num

class MaintRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='rdryer,\
dberning')
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    department_num = models.CharField(max_length=30, blank=True, verbose_name = "Department #")
    machine = models.CharField(max_length=30, blank=True, verbose_name = "Machine")
    safety = models.CharField(max_length=30, blank=True, verbose_name = "Safety")
    description = models.CharField(max_length=30, blank=True, verbose_name = "Description")
    lout = models.CharField(max_length=30, blank=True, verbose_name = "Lout")
    cell = models.CharField(max_length=30, blank=True, verbose_name = "Cell")
    request = models.TextField(max_length=100, blank=True, verbose_name = "Request")

    def __str__(self):
        return self.department

class CallIn(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,dberning,dscherbring,gbrown,jschoop,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,mkirby,mvarley,bmorgan,rmccullough,rdryer,dberning,asheehy,mdolan,cbrady,jherrig,cheim,jsteffes')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    datetime = models.DateTimeField(verbose_name = "Date/Time of Callin")
    date_call =models.DateField(verbose_name = "Date Requested")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    reason = models.CharField(max_length=30, blank=True, verbose_name = "Reason")
    fmla = models.CharField(max_length=5, blank=True, verbose_name = "FMLA Cond (Y/N)", choices=BOOL_CHOICES)

    def __str__(self):
        return self.name

class CallInFactory(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,chuntington,dscherbring,gbrown,hlangkamp,jbettcher,jcabana,jherrig,jheuer,banderson,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jschoop,mkirby,msullivan,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    datetime = models.DateTimeField(verbose_name = "Date/Time of Callin")
    date_call =models.DateField(verbose_name = "Date Requested")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    reason = models.CharField(max_length=30, blank=True, verbose_name = "Reason")
    fmla = models.CharField(max_length=5, blank=True, verbose_name = "FMLA Cond (Y/N)", choices=BOOL_CHOICES)

    def __str__(self):
        return self.name

class CallInFoundry(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='cbrady,cheim,chuntington,dboleyn,dwatson,jbettcher,jgaber,jkirk,jkohlenberg,eburgmeier,jremakel,jscherbring,msullivan,jsaunders,pludowitz,shuschik,ebradley,sohara,svanek')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    datetime = models.DateTimeField(verbose_name = "Date/Time of Callin")
    date_call =models.DateField(verbose_name = "Date Requested")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    reason = models.CharField(max_length=30, blank=True, verbose_name = "Reason")
    fmla = models.CharField(max_length=5, blank=True, verbose_name = "FMLA Cond (Y/N)", choices=BOOL_CHOICES)

    def __str__(self):
        return self.name

class CallInMaint(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,cheim,chuntington,dberning,dbolyen,dscherbring,dschumacher,mbeadle,dwatson,gbrown,hlangkamp,jbettcher,jcabana,jgaber,jherrig,jheuer,banderson,jkirk,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jscherbring,jschoop,mkirby,msullivan,pludowitz,rdryer,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    datetime = models.DateTimeField(verbose_name = "Date/Time of Callin")
    date_call =models.DateField(verbose_name = "Date Requested")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    reason = models.CharField(max_length=30, blank=True, verbose_name = "Reason")
    fmla = models.CharField(max_length=5, blank=True, verbose_name = "FMLA Cond (Y/N)", choices=BOOL_CHOICES)

    def __str__(self):
        return self.name

class CallInShip(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,cbrady,chuntington,dscherbring,gbrown,jbettcher,jherrig,jkohlenberg,eburgmeier,jremakel,jschoop,msullivan,pjentz,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    datetime = models.DateTimeField(verbose_name = "Date/Time of Callin")
    date_call =models.DateField(verbose_name = "Date Requested")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    reason = models.CharField(max_length=30, blank=True, verbose_name = "Reason")
    fmla = models.CharField(max_length=5, blank=True, verbose_name = "FMLA Cond (Y/N)", choices=BOOL_CHOICES)

    def __str__(self):
        return self.name

class InstructSheetOrder(models.Model):
    PLANT_CHOICES = (
        ('ALB', 'Albia'),
        ('DBQ', 'Dubuque'),
        ('NEV', 'Sparks'),
        ('TENN', 'Elizabethton'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,dgreenwood,gbrown,hlangkamp,jcabana,jherrig,jheuer,banderson,jmalek,jmiller,mbasten,jremakel,jschoop,mkirby,msullivan,rdryer,rmccullough,tbanwarth,jkendell,ssabers,pmartelli')
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    title = models.CharField(max_length=30, blank=True, verbose_name = "Instruction Sheet Title")
    quantity = models.CharField(max_length=4, verbose_name = "Quantity Required")
    plant = models.CharField(max_length=30, blank=True, verbose_name = "Deliver to Plant", choices=PLANT_CHOICES)
    department = models.CharField(max_length=30, blank=True, verbose_name = "Deliver to Dept")

    def __str__(self):
        return self.part_num

class InjuryReport(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    BOOL_CHOICES2 = (
        ('TSOH', 'TSOH'),
        ('Acute Care', 'Acute Care'),
        ('Mercy ER', 'Mercy ER'),
        ('N/A', 'N/A'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,jremakel,jgaber,rmccullough,dgibbs,msullivan,sstankovich,.foundry,.factory')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    datetimeinj = models.DateTimeField(verbose_name = "Date/Time of Injury")
    datetimerep = models.DateTimeField(verbose_name = "Date/Time Reported")
    equipment = models.CharField(max_length=50, blank=True, verbose_name = "Equipment Involved")
    body = models.CharField(max_length=30, blank=True, verbose_name = "Body Part Injured")
    typeinj = models.CharField(max_length=30, blank=True, verbose_name = "Type of Injury")
    actions = models.CharField(max_length=60, blank=True, verbose_name = "How Did Injury Occur")
    treatment = models.CharField(max_length=6, blank=True, verbose_name = "Sent for Medical Treatment", choices=BOOL_CHOICES)
    facility = models.CharField(max_length=6, blank=True, verbose_name = "Facility", choices=BOOL_CHOICES2)
    firstaid = models.CharField(max_length=6, blank=True, verbose_name = "First Aid Administered", choices=BOOL_CHOICES)
    firstaidprov = models.CharField(max_length=50, blank=True, verbose_name = "First Aid Provided (Band Aid, Ice, etc)")
    recommendation = models.CharField(max_length=60, blank=True, verbose_name = "Supervisor's recommendation to Prevent Similar")

    def __str__(self):
        return self.name

class ChangeOfStatus(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,cbrady,jgaber,dberning,dscherbring,gbrown,jschoop,hlangkamp,jmiller,mbasten,jmalek,jremakel,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,msullivan,mkirby,bmorgan,rdryer,rmccullough,jremakel,dgibbs,jblack,dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,jherrig')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    date = models.DateField(verbose_name = "Effective Date")
    sub_shift = models.CharField(max_length=20, blank=True, verbose_name = "Sub Shift")
    classification = models.CharField(max_length=30, blank=True, verbose_name = "Classification")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    awd_date = models.DateField(null=True, blank=True, verbose_name = "AWD Date for Bid")
    supervisor = models.CharField(max_length=30, blank=True, verbose_name = "Supervisor")
    officeuse = models.CharField(max_length=30, blank=True, verbose_name = "Office Use Only")
    reason = models.TextField(max_length=100, blank=True, verbose_name = "Reason")

    def __str__(self):
        return self.name

class ChangeOfStatusFactory(models.Model):
    BOOL_CHOICES = (
        ('Indirect', 'Indirect'),
        ('Direct', 'Direct'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,chuntington,dscherbring,gbrown,hlangkamp,jbettcher,jcabana,dgibbs,jherrig,jheuer,banderson,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jschoop,mkirby,msullivan,rmccullough,shuschik,ebradley,sohara,svanektbanwarth,dgibbs,sstankovich')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    date = models.DateField(verbose_name = "Effective Date")
    sub_shift = models.CharField(max_length=20, blank=True, verbose_name = "Sub Shift")
    classification = models.CharField(max_length=30, blank=True, verbose_name = "Classification")
    inddir = models.CharField(max_length=10, blank=True, verbose_name = "Indirect/Direct", choices=BOOL_CHOICES)
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    awd_date = models.DateField(null=True, blank=True, verbose_name = "AWD Date for Bid")
    supervisor = models.CharField(max_length=30, blank=True, verbose_name = "Supervisor")
    officeuse = models.CharField(max_length=30, blank=True, verbose_name = "Office Use Only")
    reason = models.TextField(max_length=100, blank=True, verbose_name = "Reason")

    def __str__(self):
        return self.name

class ChangeOfStatusFoundry(models.Model):
    BOOL_CHOICES = (
        ('Indirect', 'Indirect'),
        ('Direct', 'Direct'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='cbrady,cheim,chuntinton,dboleyn,dwatson,jbettcher,dgibbs,jgaber,jkirk,jkohlenberg,eburgmeier,jremakel,jscherbring,msullivan,pludowitz,shuschik,ebradley,sohara,svanek,sstankovich')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    date = models.DateField(verbose_name = "Effective Date")
    sub_shift = models.CharField(max_length=20, blank=True, verbose_name = "Sub Shift")
    classification = models.CharField(max_length=30, blank=True, verbose_name = "Classification")
    inddir = models.CharField(max_length=10, blank=True, verbose_name = "Indirect/Direct", choices=BOOL_CHOICES)
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    awd_date = models.DateField(null=True, blank=True, verbose_name = "AWD Date for Bid")
    supervisor = models.CharField(max_length=30, blank=True, verbose_name = "Supervisor")
    officeuse = models.CharField(max_length=30, blank=True, verbose_name = "Office Use Only")
    reason = models.TextField(max_length=100, blank=True, verbose_name = "Reason")

    def __str__(self):
        return self.name

class ChangeOfStatusMaint(models.Model):
    BOOL_CHOICES = (
        ('Indirect', 'Indirect'),
        ('Direct', 'Direct'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='afossleman,bgebhard,cchrest,ssabers,bmorgan,cbrady,cheim,chuntington,dboleyn,dscherbring,dschumacher,mbeadle,dwatson,gbrown,hlangkamp,jbettcher,jcabana,jgaber,jherrig,jheuer,banderson,jkirk,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jscherbring,jschoop,mkirby,msullivan,pludowitz,rdryer,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth,dgibbs,sstankovich')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    date = models.DateField(verbose_name = "Effective Date")
    sub_shift = models.CharField(max_length=20, blank=True, verbose_name = "Sub Shift")
    classification = models.CharField(max_length=30, blank=True, verbose_name = "Classification")
    inddir = models.CharField(max_length=10, blank=True, verbose_name = "Indirect/Direct", choices=BOOL_CHOICES)
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    awd_date = models.DateField(null=True, blank=True, verbose_name = "AWD Date for Bid")
    supervisor = models.CharField(max_length=30, blank=True, verbose_name = "Supervisor")
    officeuse = models.CharField(max_length=30, blank=True, verbose_name = "Office Use Only")
    reason = models.TextField(max_length=100, blank=True, verbose_name = "Reason")

    def __str__(self):
        return self.name

class ChangeOfStatusShip(models.Model):
    BOOL_CHOICES = (
        ('Indirect', 'Indirect'),
        ('Direct', 'Direct'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,cbrady,chuntington,dscherbring,gbrown,jbettcher,dgibbs,jherrig,jkohlenberg,eburgmeier,jremakel,jschoop,msullivan,pjentz,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth,sstankovich')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    date = models.DateField(verbose_name = "Effective Date")
    sub_shift = models.CharField(max_length=20, blank=True, verbose_name = "Sub Shift")
    classification = models.CharField(max_length=30, blank=True, verbose_name = "Classification")
    inddir = models.CharField(max_length=10, blank=True, verbose_name = "Indirect/Direct", choices=BOOL_CHOICES)
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    awd_date = models.DateField(null=True, blank=True, verbose_name = "AWD Date for Bid")
    supervisor = models.CharField(max_length=30, blank=True, verbose_name = "Supervisor")
    officeuse = models.CharField(max_length=30, blank=True, verbose_name = "Office Use Only")
    reason = models.TextField(max_length=100, blank=True, verbose_name = "Reason")

    def __str__(self):
        return self.name

class ToolChange(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='kwagner')
    tool_num = models.CharField(max_length=30, blank=True, verbose_name = "Tool #")
    revision = models.CharField(max_length=20, blank=True,)
    type_change = models.CharField(max_length=20, verbose_name = "Type of Change")
    price = models.CharField(max_length=10, blank=True)
    vendor = models.CharField(max_length=30, blank=True)
    instructions = models.TextField(max_length=75, blank=True)

    def __str__(self):
        return self.tool_num

class CastingProblem(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='adixon,heller,jwoodby,ashea,bgebhard,cchrest,ssabers,bhaas,bmorgan,cheim,dboleyn,dratterman,dthen,dwatson,ewolter,gbrown,hlangkamp,jburdt,jcabana,jgaber,jherrig,jheuer,banderson,jkirk,jmalek,jmiller,mbasten,jremakel,jscherbring,jschoop,keller,lotting,mkirby,msullivan,rmccullough,rrokusek,rwagner,stefft,tbanwarth,tpiggott')
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    order_num = models.CharField(max_length=20, blank=True, verbose_name = "Order #")
    cast_part_num = models.CharField(max_length=20, blank=True, verbose_name = "Casting Part #")
    department = models.CharField(max_length=30, blank=True)
    cast_order_num = models.CharField(max_length=30, blank=True, verbose_name = "Casting Order #")
    description = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    investigated = models.CharField(max_length=30, blank=True, verbose_name = "Investigated By")
    corrective = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action Taken")

    def __str__(self):
        return self.part_num

class CartonNoChange(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dconnolly,bhaas,kduex')
    part_num = models.CharField(max_length=20, verbose_name = "Part #")
    old_num = models.CharField(max_length=30, blank=True, verbose_name = "Old Carton #")
    new_num = models.CharField(max_length=30, blank=True, verbose_name = "New Carton #")
    comments = models.TextField(max_length=75, blank=True)

    def __str__(self):
        return self.part_num

class CartonWgtChange(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dschoenberger,jheuer,banderson,bgebhard,cchrest,ssabers,hlangkamp,jcabana,jmiller,mbasten,jmalek')
    part_num = models.CharField(max_length=20, verbose_name = "Part #")
    carton_qty = models.CharField(max_length=4, blank=True, verbose_name = "Carton Qty")
    carton_wgt = models.CharField(max_length=20, blank=True, verbose_name = "Carton Weight")
    
    def __str__(self):
        return self.part_num

class CellSetup(models.Model):
    PLANT_CHOICES = (
        ('ALB', 'Albia'),
        ('DBQ', 'Dubuque'),
        ('NEV', 'Sparks'),
        ('TENN', 'Elizabethton'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dratterman,jboll,jremakel,lsaylor,marling,msullivan,shasken')
    plant = models.CharField(max_length=30, blank=True, choices=PLANT_CHOICES)
    cell_id = models.CharField(max_length=20, verbose_name = "Cell Identifier")
    cell_name = models.CharField(max_length=20, verbose_name = "Cell Name (20 char)")
    department = models.CharField(max_length=20)
    base_part = models.CharField(max_length=20, verbose_name = "Base Part")
    base_route = models.CharField(max_length=20, verbose_name = "Base Routing Standard")
    add_route = models.CharField(max_length=20, verbose_name = "Add all Routing Steps")
    ref_locs = models.CharField(max_length=20, verbose_name = "From/To Reference Locs")
    run_rate = models.CharField(max_length=20, verbose_name = "Run Rate for Schedule Report (Mark)")
    work_center = models.CharField(max_length=20, verbose_name = "Work Center to Identify Parts to Change")

    def __str__(self):
        return self.plant

class GatePass(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jkohlenberg,eburgmeier,shuschik,ebradley,sohara,dhein,guard2,guard3,pnugent,rpetrick,jremakel,msullivan,jgaber,rmccullough,rdryer,dberning,dschumacher,mbeadle,kwilliams')
    name = models.CharField(max_length=30, blank=True)
    date = models.DateField()
    clock_num = models.CharField(max_length=20, blank=True, verbose_name = "Clock #")
    sold = models.CharField(max_length=5, blank=True, choices=BOOL_CHOICES)
    given = models.CharField(max_length=5, blank=True, verbose_name = "Given To", choices=BOOL_CHOICES)
    borrow_date = models.DateField(verbose_name = "Borrowed Date", blank=True, null=True)
    return_date = models.DateField(verbose_name = "Returned Date", blank=True, null=True)
    approval = models.CharField(max_length=30, blank=True)
    cost = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True, verbose_name = "Description of Item")

    def __str__(self):
        return self.name

class MachineDownLog(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,dberning,dratterman,dscherbring,dschumacher,mbeadle,gbrown,hlangkamp,jburdt,jcabana,jheuer,banderson,jmalek,jmiller,mbasten,jremakel,jschoop,msullivan,tpiggott')
    machine_num = models.CharField(max_length=20, verbose_name = "Machine #")
    machine_desc = models.CharField(max_length=30, verbose_name = "Machine Description")
    reason = models.CharField(max_length=300, verbose_name = "Reason Down")
    duration = models.CharField(max_length=10, verbose_name = "Duration Days")

    def __str__(self):
        return self.date

class ChangeOrderRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='ashea,awickham,bhaas,dconnolly,dratterman,dthen,jburdt,jzurcher,kduex,lotting,marling,parnold,raspen,sbreitbach,stefft,thast')#cklein
    info = models.TextField(max_length=300, verbose_name = "Please prepare a change order as follows")

    def __str__(self):
        return self.info

class AlbiaCallIn(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mdobraska,cbrady,sperry,mrockwell,lbrown,ltucker,kdavis,dpendleton,msullivan,jkelley,cskelton,tmcvey,chuntington,sohara,dschoenberger')#jhollatz
    name = models.CharField(max_length=30, blank=True, verbose_name = "Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    datetime = models.DateTimeField(verbose_name = "Date/Time of Callin")
    date = models.DateField(blank=True, null=True, verbose_name = "Date Required")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department/Shift")
    reason = models.CharField(max_length=50, blank=True, verbose_name = "Reason")
    fmla = models.CharField(max_length=5, blank=True, verbose_name = "FMLA Cond (Y/N)", choices=BOOL_CHOICES)

    def __str__(self):
        return self.name

class AlbiaInjuryReport(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mdobraska,msullivan,jgaber,chuntington,dgibbs,sperry,dschoenberger,sstankovich')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    datetimeinj = models.DateTimeField(verbose_name = "Date/Time of Injury")
    datetimerep = models.DateTimeField(verbose_name = "Date/Time Reported")
    equipment = models.CharField(max_length=50, blank=True, verbose_name = "Equipment Involved")
    body = models.CharField(max_length=30, blank=True, verbose_name = "Body Part Injured")
    typeinj = models.CharField(max_length=30, blank=True, verbose_name = "Type of Injury")
    actions = models.CharField(max_length=60, blank=True, verbose_name = "How Did Injury Occur")
    treatment = models.CharField(max_length=6, blank=True, verbose_name = "Sent for Medical Treatment", choices=BOOL_CHOICES)
    firstaid = models.CharField(max_length=6, blank=True, verbose_name = "First Aid Administered", choices=BOOL_CHOICES)
    firstaidprov = models.CharField(max_length=50, blank=True, verbose_name = "First Aid Provided (Band Aid, Ice, etc)")
    recommendation = models.CharField(max_length=60, blank=True, verbose_name = "Supervisor's recommendation to Prevent Similar")

    def __str__(self):
        return self.name

class TennCallIn(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='keller,msullivan,sdayton,dsimerly,adixon,heller,jwoodby,tkennett,jsommers,lbarr,acollins,jcombs,sohara,tharmon')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Name")
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    datetime = models.DateTimeField(verbose_name = "Date/Time of Callin")
    date = models.DateField(blank=True, null=True, verbose_name = "Date Required")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department/Shift")
    reason = models.CharField(max_length=50, blank=True, verbose_name = "Reason")
    fmla = models.CharField(max_length=5, blank=True, verbose_name = "FMLA Cond (Y/N)", choices=BOOL_CHOICES)

    def __str__(self):
        return self.name

class TennInjuryReport(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='keller,chuntington,msullivan,shuschik,jsommers,jgaber,dgibbs,sstankovich')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    datetimeinj = models.DateTimeField(verbose_name = "Date/Time of Injury")
    datetimerep = models.DateTimeField(verbose_name = "Date/Time Reported")
    equipment = models.CharField(max_length=50, blank=True, verbose_name = "Equipment Involved")
    body = models.CharField(max_length=30, blank=True, verbose_name = "Body Part Injured")
    typeinj = models.CharField(max_length=30, blank=True, verbose_name = "Type of Injury")
    actions = models.CharField(max_length=60, blank=True, verbose_name = "How Did Injury Occur")
    treatment = models.CharField(max_length=6, blank=True, verbose_name = "Sent for Medical Treatment", choices=BOOL_CHOICES)
    firstaid = models.CharField(max_length=6, blank=True, verbose_name = "First Aid Administered", choices=BOOL_CHOICES)
    firstaidprov = models.CharField(max_length=50, blank=True, verbose_name = "First Aid Provided (Band Aid, Ice, etc)")
    recommendation = models.CharField(max_length=60, blank=True, verbose_name = "Supervisor's recommendation to Prevent Similar")

    def __str__(self):
        return self.name

class AlbiaWeekInjIllFactory(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mdobraska,msullivan,jgaber,chuntington,dgibbs,sperry,dschoenberger,sstankovich')
    employee_num = models.CharField(max_length=10, blank=True, verbose_name = "Employee #")
    name = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    shift = models.CharField(max_length=6, blank=True, verbose_name = "Shift")
    description = models.CharField(max_length=60, blank=True, verbose_name = "Description of Inj/Ill")
    datetime = models.DateTimeField(verbose_name = "Date/Time", blank=True, null=True)
    medical_provider = models.CharField(max_length=30, blank=True, verbose_name = "Medical Care Provider Seen")
    work_restrictions = models.TextField(max_length=300, blank=True, verbose_name = "Work Restrictions")
    next_datetime = models.DateTimeField(verbose_name = "Next Date/Time", blank=True, null=True)

    def __str__(self):
        return self.employee_num

class AlbiaEarlyClockOut(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mdobraska,cbrady,sperry,mrockwell,lbrown,ltucker,kdavis,dpendleton,msullivan,jkelley,cskelton,tmcvey,chuntington,sohara,dschoenberger')#jhollatz
    name = models.CharField(max_length=35, verbose_name = "Name", blank=True)
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    reason = models.CharField(max_length=70, verbose_name = "Reason", blank=True)

    def __str__(self):
        return self.name

class TennEarlyClockOut(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='keller,msullivan,sdayton,dsimerly,adixon,heller,jwoodby,tkennett,jsommers,lbarr,acollins,jcombs,sohara')
    name = models.CharField(max_length=35, verbose_name = "Name", blank=True)
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    reason = models.CharField(max_length=70, verbose_name = "Reason", blank=True)

    def __str__(self):
        return self.name

class AHEIRReport(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jremakel,msullivan,rmccullough')
    date = models.DateField()
    supervisor = models.CharField(max_length=30, blank=True)
    employee = models.CharField(max_length=30, blank=True)
    rate = models.CharField(max_length=30, blank=True, verbose_name = "Rate Authorized")
    senior = models.CharField(max_length=6, blank=True, verbose_name = "Least Senior in Class (Y/N)", choices=BOOL_CHOICES)
    work = models.CharField(max_length=30, blank=True, verbose_name = "For Lack of Work (Y/N)", choices=BOOL_CHOICES)
    details = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.employee

class AlbiaIssueMiscMaterial(models.Model):
    REASON_CHOICES = (
        ('81/85', '81Brass Used as 85'),
        ('ALB', 'Albia Issue'),
        ('CART1', 'Cartons to Mailroom'),
        ('CART2', 'Cartons to Shipping'),
        ('COSTL', 'Cost Load'),
        ('CUSCO', 'Customer Co-Op'),
        ('CUSLO', 'Customer Loyalty'),
        ('CYCL1', 'Cycle Count Adj Raw Material'),
        ('CYCL2', 'Cycle Count No Change'),
        ('CYCL3', 'Cycle Count Adj Components'),
        ('CYCL4', 'Cycle Count Adj FG'),
        ('CYCL5', 'Cycle Count Adjustment'),
        ('DBQMA', "Dubuque Repair & Maint Mat'l"),
        ('DUB', 'Dubuque Factory Issue'),
        ('ENDPC', 'Ball Value End Piece On Floor'),
        ('FND', 'Foundry Issue'),
        ('LF', 'Lost & Found'),
        ('NAIER', 'Naier Donations'),       
        ('PEGRD', 'PE HP Gas R&D Samples'),
        ('PEGAS', 'PE HP Gas Samples'),
        ('PENRD', 'PE No Lead R&D Samples'),
        ('PENL', 'PE No Lead Samples'),
        ('PEPLR', 'PE Plumbing R&D Samples'),
        ('PESMP', 'PE Plumbing Samples'),
        ('PEPUR', 'PE Pump R&D Samples'),
        ('PEPUM', 'PE Pump Samples'), 
        ('PEWRD', 'PE Water Works R&D Samples'),
        ('PE', 'PE Water Works Samples'),
        ('PIC', 'PIC Adjustment Misc'),
        ('PICC', 'PIC Cycle Count'),
        ('PUCK', 'Puck to Ingot'),
        ('QA', 'QA Samples'),
        ('QAALB', 'QA Albia Misc Return'),
        ('QAFND', 'QA Foundry Misc Return'),
        ('QAR&D', 'QA R&D Samples'),
        ('QASTK', 'QA Misc Return'),
        ('QATEN', 'QA Tenn Misc Return'),
        ('QAVEN', 'QA Vendor Misc Return'),
        ('RMA', 'RMA Parts'),
        ('S&O', 'Surplus & Obsolesence Misc'),
        ('S&OB', 'Surplus & Obsolesence Brass'),
        ('SAL', 'Chips to Stock'),
        ('SAMPL', 'Internal Sales Samples'),
        ('SPLST', 'Samples to Stock'),
        ('STKLO', 'Ingot Adj due to Stack Loss'),
        ('TENN', 'Tenn Issue'),
        ('VEN', 'Vendor Issue'),
        ('VNOCH', 'Vendor No Charge REplacement'),
        ('WDCFB', 'WDC Fabrication'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dschoenberger,sperry')
    part = models.CharField(max_length=20, blank=True)
    part02 = models.CharField(max_length=20, blank=True)
    part03 = models.CharField(max_length=20, blank=True)
    part04 = models.CharField(max_length=20, blank=True)
    part05 = models.CharField(max_length=20, blank=True)
    part06 = models.CharField(max_length=20, blank=True)
    part07 = models.CharField(max_length=20, blank=True)
    quantity = models.CharField(max_length=6, blank=True)
    quantity02 = models.CharField(max_length=6, blank=True)
    quantity03 = models.CharField(max_length=6, blank=True)
    quantity04 = models.CharField(max_length=6, blank=True)
    quantity05 = models.CharField(max_length=6, blank=True)
    quantity06 = models.CharField(max_length=6, blank=True)
    quantity07 = models.CharField(max_length=6, blank=True)       
    reference = models.CharField(max_length=50)
    reason = models.CharField(max_length=30, blank=True, choices=REASON_CHOICES)
    bin_loc = models.CharField(max_length=6, blank=True, verbose_name = "Bin")
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.part

class TennIssueMiscMaterial(models.Model):
    REASON_CHOICES = (
        ('81/85', '81Brass Used as 85'),
        ('ALB', 'Albia Issue'),
        ('CART1', 'Cartons to Mailroom'),
        ('CART2', 'Cartons to Shipping'),
        ('COSTL', 'Cost Load'),
        ('CUSCO', 'Customer Co-Op'),
        ('CUSLO', 'Customer Loyalty'),
        ('CYCL1', 'Cycle Count Adj Raw Material'),
        ('CYCL2', 'Cycle Count No Change'),
        ('CYCL3', 'Cycle Count Adj Components'),
        ('CYCL4', 'Cycle Count Adj FG'),
        ('CYCL5', 'Cycle Count Adjustment'),
        ('DBQMA', "Dubuque Repair & Maint Mat'l"),
        ('DUB', 'Dubuque Factory Issue'),
        ('ENDPC', 'Ball Value End Piece On Floor'),
        ('FND', 'Foundry Issue'),
        ('LF', 'Lost & Found'),
        ('NAIER', 'Naier Donations'),       
        ('PEGRD', 'PE HP Gas R&D Samples'),
        ('PEGAS', 'PE HP Gas Samples'),
        ('PENRD', 'PE No Lead R&D Samples'),
        ('PENL', 'PE No Lead Samples'),
        ('PEPLR', 'PE Plumbing R&D Samples'),
        ('PESMP', 'PE Plumbing Samples'),
        ('PEPUR', 'PE Pump R&D Samples'),
        ('PEPUM', 'PE Pump Samples'), 
        ('PEWRD', 'PE Water Works R&D Samples'),
        ('PE', 'PE Water Works Samples'),
        ('PIC', 'PIC Adjustment Misc'),
        ('PICC', 'PIC Cycle Count'),
        ('PUCK', 'Puck to Ingot'),
        ('QA', 'QA Samples'),
        ('QAALB', 'QA Albia Misc Return'),
        ('QAFND', 'QA Foundry Misc Return'),
        ('QAR&D', 'QA R&D Samples'),
        ('QASTK', 'QA Misc Return'),
        ('QATEN', 'QA Tenn Misc Return'),
        ('QAVEN', 'QA Vendor Misc Return'),
        ('RMA', 'RMA Parts'),
        ('S&O', 'Surplus & Obsolesence Misc'),
        ('S&OB', 'Surplus & Obsolesence Brass'),
        ('SAL', 'Chips to Stock'),
        ('SAMPL', 'Internal Sales Samples'),
        ('SPLST', 'Samples to Stock'),
        ('STKLO', 'Ingot Adj due to Stack Loss'),
        ('TENN', 'Tenn Issue'),
        ('VEN', 'Vendor Issue'),
        ('VNOCH', 'Vendor No Charge REplacement'),
        ('WDCFB', 'WDC Fabrication'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='keller,sdayton')
    part = models.CharField(max_length=20, blank=True)
    part02 = models.CharField(max_length=20, blank=True)
    part03 = models.CharField(max_length=20, blank=True)
    part04 = models.CharField(max_length=20, blank=True)
    part05 = models.CharField(max_length=20, blank=True)
    part06 = models.CharField(max_length=20, blank=True)
    part07 = models.CharField(max_length=20, blank=True)
    quantity = models.CharField(max_length=6, blank=True)
    quantity02 = models.CharField(max_length=6, blank=True)
    quantity03 = models.CharField(max_length=6, blank=True)
    quantity04 = models.CharField(max_length=6, blank=True)
    quantity05 = models.CharField(max_length=6, blank=True)
    quantity06 = models.CharField(max_length=6, blank=True)
    quantity07 = models.CharField(max_length=6, blank=True)       
    reference = models.CharField(max_length=50)
    reason = models.CharField(max_length=30, blank=True, choices=REASON_CHOICES)
    bin_loc = models.CharField(max_length=6, blank=True, verbose_name = "Bin")
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.part

class NevIssueMiscMaterial(models.Model):
    REASON_CHOICES = (
        ('81/85', '81Brass Used as 85'),
        ('ALB', 'Albia Issue'),
        ('CART1', 'Cartons to Mailroom'),
        ('CART2', 'Cartons to Shipping'),
        ('COSTL', 'Cost Load'),
        ('CUSCO', 'Customer Co-Op'),
        ('CUSLO', 'Customer Loyalty'),
        ('CYCL1', 'Cycle Count Adj Raw Material'),
        ('CYCL2', 'Cycle Count No Change'),
        ('CYCL3', 'Cycle Count Adj Components'),
        ('CYCL4', 'Cycle Count Adj FG'),
        ('CYCL5', 'Cycle Count Adjustment'),
        ('DBQMA', "Dubuque Repair & Maint Mat'l"),
        ('DUB', 'Dubuque Factory Issue'),
        ('ENDPC', 'Ball Value End Piece On Floor'),
        ('FND', 'Foundry Issue'),
        ('LF', 'Lost & Found'),
        ('NAIER', 'Naier Donations'),       
        ('PEGRD', 'PE HP Gas R&D Samples'),
        ('PEGAS', 'PE HP Gas Samples'),
        ('PENRD', 'PE No Lead R&D Samples'),
        ('PENL', 'PE No Lead Samples'),
        ('PEPLR', 'PE Plumbing R&D Samples'),
        ('PESMP', 'PE Plumbing Samples'),
        ('PEPUR', 'PE Pump R&D Samples'),
        ('PEPUM', 'PE Pump Samples'), 
        ('PEWRD', 'PE Water Works R&D Samples'),
        ('PE', 'PE Water Works Samples'),
        ('PIC', 'PIC Adjustment Misc'),
        ('PICC', 'PIC Cycle Count'),
        ('PUCK', 'Puck to Ingot'),
        ('QA', 'QA Samples'),
        ('QAALB', 'QA Albia Misc Return'),
        ('QAFND', 'QA Foundry Misc Return'),
        ('QAR&D', 'QA R&D Samples'),
        ('QASTK', 'QA Misc Return'),
        ('QATEN', 'QA Tenn Misc Return'),
        ('QAVEN', 'QA Vendor Misc Return'),
        ('RMA', 'RMA Parts'),
        ('S&O', 'Surplus & Obsolesence Misc'),
        ('S&OB', 'Surplus & Obsolesence Brass'),
        ('SAL', 'Chips to Stock'),
        ('SAMPL', 'Internal Sales Samples'),
        ('SPLST', 'Samples to Stock'),
        ('STKLO', 'Ingot Adj due to Stack Loss'),
        ('TENN', 'Tenn Issue'),
        ('VEN', 'Vendor Issue'),
        ('VNOCH', 'Vendor No Charge REplacement'),
        ('WDCFB', 'WDC Fabrication'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='stierney')
    part = models.CharField(max_length=20, blank=True)
    part02 = models.CharField(max_length=20, blank=True)
    part03 = models.CharField(max_length=20, blank=True)
    part04 = models.CharField(max_length=20, blank=True)
    part05 = models.CharField(max_length=20, blank=True)
    part06 = models.CharField(max_length=20, blank=True)
    part07 = models.CharField(max_length=20, blank=True)
    quantity = models.CharField(max_length=6, blank=True)
    quantity02 = models.CharField(max_length=6, blank=True)
    quantity03 = models.CharField(max_length=6, blank=True)
    quantity04 = models.CharField(max_length=6, blank=True)
    quantity05 = models.CharField(max_length=6, blank=True)
    quantity06 = models.CharField(max_length=6, blank=True)
    quantity07 = models.CharField(max_length=6, blank=True)       
    reference = models.CharField(max_length=50)
    reason = models.CharField(max_length=30, blank=True, choices=REASON_CHOICES)
    bin_loc = models.CharField(max_length=6, blank=True, verbose_name = "Bin")
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.part

class FoundryToolRec(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bhaas,dconnolly,ewolter,jzurcher,kduex,parnold,raspen,stefft,thast,qmccullough,jgaber,dwatson,msullivan')#cklein
    pattern = models.CharField(max_length=30, blank=True)
    corebox = models.CharField(max_length=30, blank=True)
    part_num = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    changeorder_num = models.CharField(max_length=30, blank=True, verbose_name = "Change Order #")

    def __str__(self):
        return self.pattern

class MachineFollowUp(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,scherbring,gbrown,hlangkamp,jburdt,jcabana,jherrig,jheuer,banderson,jmalek,jmiller,mbasten,jremakel,jschoop,jkendell,efaust,gryan,gryan,mkirby,msullivan,rdryer,rmccullough,pmartell,tbanwarth,parnold')#bbecker
    supervisor = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    work_center = models.CharField(max_length=30, blank=True, verbose_name = "Work Center")
    machine_num = models.CharField(max_length=30, blank=True, verbose_name = "Machine #")
    operator = models.CharField(max_length=30, blank=True)
    time = models.TimeField(blank=True, verbose_name = "Time of Incident")
    program_num = models.CharField(max_length=30, blank=True, verbose_name = "Program #")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    estdamcost = models.CharField(max_length=30, blank=True, verbose_name = "Est. Damage Cost")
    timeofrepair = models.CharField(max_length=30, blank=True, verbose_name = "Time Incurred for Repairs")
    drug = models.CharField(max_length=6, blank=True, verbose_name = "Drug Tested", choices=BOOL_CHOICES)
    explaination = models.TextField(max_length=100, blank=True)
    machine_notes = models.CharField(max_length=100, blank=True, verbose_name = "Machine Notes")

    def __str__(self):
        return self.department

class AlbiaMachineFollowUp(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mrockwell,msullivan,pmcdanel,gcurtis,slampier,rdryer,dschoenberger,dpendleton,jkelley,cskelton,kdavis,ltucker,tmcvey,spangburn')#jhollatz
    supervisor = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    work_center = models.CharField(max_length=30, blank=True, verbose_name = "Work Center")
    machine_num = models.CharField(max_length=30, blank=True, verbose_name = "Machine #")
    operator = models.CharField(max_length=30, blank=True)
    time = models.TimeField(blank=True, verbose_name = "Time of Incident")
    program_num = models.CharField(max_length=30, blank=True, verbose_name = "Program #")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    estdamcost = models.CharField(max_length=30, blank=True, verbose_name = "Est. Damage Cost")
    timeofrepair = models.CharField(max_length=30, blank=True, verbose_name = "Time Incurred for Repairs")
    drug = models.CharField(max_length=6, blank=True, verbose_name = "Drug Tested", choices=BOOL_CHOICES)
    explaination = models.TextField(max_length=100, blank=True)
    machine_notes = models.CharField(max_length=100, blank=True, verbose_name = "Machine Notes")

    def __str__(self):
        return self.department

class TennMachineFollowUp(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='keller,msullivan,adixon,heller,jwoodby,kgrindstaff,cmorton,tkennett,lbarr,jsommers,glaughlin,amehlhorn,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bgebhard,cchrest,tpiggott')
    supervisor = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    work_center = models.CharField(max_length=30, blank=True, verbose_name = "Work Center")
    machine_num = models.CharField(max_length=30, blank=True, verbose_name = "Machine #")
    operator = models.CharField(max_length=30, blank=True)
    time = models.TimeField(blank=True, verbose_name = "Time of Incident")
    program_num = models.CharField(max_length=30, blank=True, verbose_name = "Program #")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    estdamcost = models.CharField(max_length=30, blank=True, verbose_name = "Est. Damage Cost")
    timeofrepair = models.CharField(max_length=30, blank=True, verbose_name = "Time Incurred for Repairs")
    drug = models.CharField(max_length=6, blank=True, verbose_name = "Drug Tested", choices=BOOL_CHOICES)
    explaination = models.TextField(max_length=100, blank=True)
    machine_notes = models.CharField(max_length=100, blank=True, verbose_name = "Machine Notes")

    def __str__(self):
        return self.department

class SetupExceptionChallenge(models.Model):
    OPENCLOSED_CHOICES = (
        ('O', 'Open'),
        ('C', 'Closed'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jremakel,msullivan,rmccullough,svanek,tpiggott')
    employee = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    shift = models.CharField(max_length=5, blank=True)
    work_center = models.CharField(max_length=10, blank=True, verbose_name = "Work Center #")
    date = models.DateField(blank=True, null=True, verbose_name = "Date of Exception")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num = models.CharField(max_length=30, blank=True, verbose_name = "Job #")
    resource_num = models.CharField(max_length=30, blank=True, verbose_name = "Resource #")
    cum_time = models.CharField(max_length=30, blank=True, verbose_name = "Cumulative Time")
    excep_time = models.CharField(max_length=30, blank=True, verbose_name = "Exception Time")
    difference = models.CharField(max_length=30, blank=True, verbose_name = "Difference of Actual/Exception")
    open_closed = models.CharField(max_length=30, blank=True, verbose_name = 'Open/Closed', choices=OPENCLOSED_CHOICES, default='O')
    orig_except = models.TextField(max_length=200, blank=True, verbose_name = "Original Exception")
    challenge = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.employee

class SetupExceptionResponse(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jremakel,msullivan,rmccullough,svanek,tpiggott')
    employee = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    shift = models.CharField(max_length=5, blank=True)
    work_center = models.CharField(max_length=10, blank=True, verbose_name = "Work Center #")
    date = models.DateField(blank=True, null=True, verbose_name = "Date of Exception")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num = models.CharField(max_length=30, blank=True, verbose_name = "Job #")
    resource_num = models.CharField(max_length=30, blank=True, verbose_name = "Resource #")
    cum_time = models.CharField(max_length=30, blank=True, verbose_name = "Cumulative Time")
    excep_time = models.CharField(max_length=30, blank=True, verbose_name = "Exception Time")
    difference = models.CharField(max_length=30, blank=True, verbose_name = "Difference of Actual/Exception")
    orig_except = models.TextField(max_length=200, blank=True, verbose_name = "Original Exception")
    response = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.employee

class TennSetupException(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='keller,msullivan,adixon,heller,jwoodby,tkennett,lbarr,jsommers,dsimerly,amehlhorn,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bgebhard,cchrest,acollins,jmullins,cmiller,tshelton,cstrong,kwagner,mjustin')
    employee = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    shift = models.CharField(max_length=5, blank=True)
    work_center = models.CharField(max_length=10, blank=True, verbose_name = "Work Center #")
    date = models.DateField(blank=True, null=True, verbose_name = "Date of Exception")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    prev_part_num = models.CharField(max_length=30, blank=True, verbose_name = "Previous Part #")
    begin_setup = models.CharField(max_length=30, blank=True, verbose_name = "Begin Setup (hundreths)")
    end_setup = models.CharField(max_length=30, blank=True, verbose_name = "End Setup (hundreths)")
    cum_time = models.CharField(max_length=30, blank=True, verbose_name = "Cumulative Time")
    excep_time = models.CharField(max_length=30, blank=True, verbose_name = "Exception Time")
    difference = models.CharField(max_length=30, blank=True, verbose_name = "Difference of Actual/Exception")
    time_sup = models.TimeField(blank=True, null=True, verbose_name = "Time Supervisor Notified")
    time_ie = models.TimeField(blank=True, null=True, verbose_name = "Time I.E. Notified")
    breaks = models.CharField(max_length=30, blank=True, verbose_name = "Lunch/Break (Y or N / L or B)")
    explanation = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.employee

class TimeStudy(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jcabana,hlangkamp,jmalek')
    clock_num = models.CharField(max_length=30, blank=True, verbose_name = "Clock #")    
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    operation_num = models.CharField(max_length=30, blank=True, verbose_name = "Operation #")
    machine_num = models.CharField(max_length=30, blank=True, verbose_name = "Machine #")
    pieces = models.CharField(max_length=30, blank=True, verbose_name = "Pieces Remaining")
    comments = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.clock_num

class RequestToPost(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,jremakel,rmccullough,jgaber,msullivan')
    classification = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    shift = models.CharField(max_length=30, blank=True,)
    post_date = models.DateField(blank=True, verbose_name = "Posting Date")
    explaination = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.classification

class ToolRoomRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mkirby,bmorgan,gbrown,jschoop,dscherbring,jmiller,mbasten,rmccullough,jherrig')#bbecker
    tool = models.CharField(max_length=30, blank=True, verbose_name = "Tool/Fixture")
    description = models.CharField(max_length=30, blank=True)
    work_center = models.CharField(max_length=30, blank=True, verbose_name = "Work Center")
    requestor = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=True)
    date_req = models.DateField(blank=True, verbose_name = "Date Required")
    comments = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.tool

class WeightChange(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jcabana,jheuer,banderson,bgebhard,cchrest,ssabers')
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    weight = models.CharField(max_length=30, blank=True, verbose_name = "Weight Per Piece")

    def __str__(self):
        return self.part_num

class VacationRequest(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,dberning,dscherbring,gbrown,jschoop,hlangkamp,jmiller,mbasten,jmalek,jremakel,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,msullivan,mkirby,mvarley,bmorgan,rmccullough,rdryer,dberning,asheehy,mdolan,cbrady,jherrig')
    name = models.CharField(max_length=30, blank=True)
    employee_num = models.CharField(max_length=30, blank=True, verbose_name = "Employee #")
    date = models.DateTimeField(blank=True, verbose_name = "Date/Time Requested")
    date_vaca = models.DateField(blank=True, verbose_name = "Date of Vacation")
    dept_shift = models.CharField(max_length=30, blank=True, verbose_name = "Dept/Shift")
    day = models.CharField(max_length=5, blank=True, verbose_name = "One Day", choices=BOOL_CHOICES)
    half_begin = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from beginning of shift", choices=BOOL_CHOICES)
    half_end = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from end of shift", choices=BOOL_CHOICES)
    two_hour = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from beginning of shift", choices=BOOL_CHOICES)
    two_hour_end = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from end of shift", choices=BOOL_CHOICES)
    reason = models.TextField(max_length=200, blank=True, verbose_name = "Reason for Exception")

    def __str__(self):
        return self.name

class VacationRequestFactory(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,chuntington,dscherbring,gbrown,hlangkamp,jbettcher,jcabana,jherrig,jeuer,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jschoop,mkirby,msullivan,rmccullough,shuschik,ebradley,sohara,svanek,dhein,guard2,guard3,pnugent,rpetrick,tbanwarth')
    name = models.CharField(max_length=30, blank=True)
    employee_num = models.CharField(max_length=30, blank=True, verbose_name = "Employee #")
    date = models.DateTimeField(blank=True, verbose_name = "Date/Time Requested")
    date_vaca = models.DateField(blank=True, verbose_name = "Date of Vacation")
    dept_shift = models.CharField(max_length=30, blank=True, verbose_name = "Dept/Shift")
    day = models.CharField(max_length=5, blank=True, verbose_name = "One Day", choices=BOOL_CHOICES)
    half_begin = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from beginning of shift", choices=BOOL_CHOICES)
    half_end = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from end of shift", choices=BOOL_CHOICES)
    two_hour = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from beginning of shift", choices=BOOL_CHOICES)
    two_hour_end = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from end of shift", choices=BOOL_CHOICES)
    reason = models.TextField(max_length=200, blank=True, verbose_name = "Reason for Exception")

    def __str__(self):
        return self.name

class VacationRequestFoundry(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='cbrady,cheim,chuntington,dboleyn,dwatson,jbettcher,jgaber,jkirk,jkohlenberg,eburgmeier,jremakel,jscherbring,msullivan,jsaunders,pludowitz,shuschik,ebradley,sohara,svanek')
    name = models.CharField(max_length=30, blank=True)
    employee_num = models.CharField(max_length=30, blank=True, verbose_name = "Employee #")
    date = models.DateTimeField(blank=True, verbose_name = "Date/Time Requested")
    date_vaca = models.DateField(blank=True, verbose_name = "Date of Vacation")
    dept_shift = models.CharField(max_length=30, blank=True, verbose_name = "Dept/Shift")
    day = models.CharField(max_length=5, blank=True, verbose_name = "One Day", choices=BOOL_CHOICES)
    half_begin = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from beginning of shift", choices=BOOL_CHOICES)
    half_end = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from end of shift", choices=BOOL_CHOICES)
    two_hour = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from beginning of shift", choices=BOOL_CHOICES)
    two_hour_end = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from end of shift", choices=BOOL_CHOICES)
    reason = models.TextField(max_length=200, blank=True, verbose_name = "Reason for Exception")

    def __str__(self):
        return self.name

class VacationRequestMaint(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,cheim,chuntington,dberning,dboleyn,dscherbring,schumacher,dwatson,gbrown,hlangkamp,jbettcher,jcabana,jherrig,jheuer,banderson,jgaber,jkirk,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jscherbring,jschoop,mkirby,msullivan,pludowitz,rdryer,rmccullough,shuschik,ebradley,sohara,svanek,dhein,guard2,guard3,pnugent,rpetrick')
    name = models.CharField(max_length=30, blank=True)
    employee_num = models.CharField(max_length=30, blank=True, verbose_name = "Employee #")
    date = models.DateTimeField(blank=True, verbose_name = "Date/Time Requested")
    date_vaca = models.DateField(blank=True, verbose_name = "Date of Vacation")
    dept_shift = models.CharField(max_length=30, blank=True, verbose_name = "Dept/Shift")
    day = models.CharField(max_length=5, blank=True, verbose_name = "One Day", choices=BOOL_CHOICES)
    half_begin = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from beginning of shift", choices=BOOL_CHOICES)
    half_end = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from end of shift", choices=BOOL_CHOICES)
    two_hour = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from beginning of shift", choices=BOOL_CHOICES)
    two_hour_end = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from end of shift", choices=BOOL_CHOICES)
    reason = models.TextField(max_length=200, blank=True, verbose_name = "Reason for Exception")

    def __str__(self):
        return self.name

class VacationRequestShip(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,cbrady,chuntington,dscherbring,gbrown,jbettcher,jherrig,jkohlenberg,eburgmeier,jremakel,jschoop,msullivan,pjentz,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=30, blank=True)
    employee_num = models.CharField(max_length=30, blank=True, verbose_name = "Employee #")
    date = models.DateTimeField(blank=True, verbose_name = "Date/Time Requested")
    date_vaca = models.DateField(blank=True, verbose_name = "Date of Vacation")
    dept_shift = models.CharField(max_length=30, blank=True, verbose_name = "Dept/Shift")
    day = models.CharField(max_length=5, blank=True, verbose_name = "One Day", choices=BOOL_CHOICES)
    half_begin = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from beginning of shift", choices=BOOL_CHOICES)
    half_end = models.CharField(max_length=5, blank=True, verbose_name = "1/2 Day from end of shift", choices=BOOL_CHOICES)
    two_hour = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from beginning of shift", choices=BOOL_CHOICES)
    two_hour_end = models.CharField(max_length=5, blank=True, verbose_name = "2 hrs from end of shift", choices=BOOL_CHOICES)
    reason = models.TextField(max_length=200, blank=True, verbose_name = "Reason for Exception")

    def __str__(self):
        return self.name

class PrototypeSamples(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='tpiggott,stefft')
    message = models.TextField(max_length=200, blank=True)
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    quantity = models.CharField(max_length=5, blank=True, verbose_name = "Quantity Needed")
    prints = models.CharField(max_length=30, blank=True, verbose_name = "Prints Provided")
    mat = models.CharField(max_length=30, blank=True, verbose_name = "Mat. Prov (2 XTRA)")
    date = models.DateField(max_length=30, blank=True, verbose_name = "Date Needed")
    similar_part = models.CharField(max_length=30, blank=True, verbose_name = "Similar to Part #")
    account_num = models.CharField(max_length=30, blank=True, verbose_name = "Account #")
    requestor = models.CharField(max_length=30, blank=True)
    deliver = models.CharField(max_length=30, blank=True, verbose_name = "Deliver Parts To")

    def __str__(self):
        return self.part_num

class RoutingChangeRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,hlangkamp,jcabana,jheuer,banderson,jmalek,jmiller,mbasten,jremakel,msullivan,tpiggott')
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    operation_num = models.CharField(max_length=30, blank=True, verbose_name = "Operation #")
    requestor = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=True)
    reason = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.part_num

class ScrappedTooling(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mkirby,bmorgan,jheuer,banderson,bgebhard,cchrest,ssabers,hlangkamp,jmiller,mbasten,jcabana,jherrig')#bbecker
    tool_num = models.CharField(max_length=30, blank=True, verbose_name = "Tool #")
    quantity = models.CharField(max_length=5, blank=True)
    remaining = models.CharField(max_length=5, blank=True, verbose_name = "Remaining Tools on Hand")
    date = models.DateField(blank=True)
    scrapped = models.CharField(max_length=30, blank=True, verbose_name = "Scrapped By")
    comments = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.tool_num

class SandSieveAnalysis(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dboleyn,cheim,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,ashea,dberning,ewolter')
    date = models.DateField(blank=True, verbose_name = "Sand Sieve Analysis Results Dated")
    a6screen = models.CharField(max_length=5, blank=True, verbose_name = "#6 Screen %")
    a12screen = models.CharField(max_length=5, blank=True, verbose_name = "#12 Screen %")
    a20screen = models.CharField(max_length=5, blank=True, verbose_name = "#20 Screen %")
    a30screen = models.CharField(max_length=5, blank=True, verbose_name = "#30 Screen %")
    a40screen = models.CharField(max_length=5, blank=True, verbose_name = "#40 Screen %")
    a50screen = models.CharField(max_length=5, blank=True, verbose_name = "#50 Screen %")
    a70screen = models.CharField(max_length=5, blank=True, verbose_name = "#70 Screen %")
    a100screen = models.CharField(max_length=5, blank=True, verbose_name = "#100 Screen %")
    a140screen = models.CharField(max_length=5, blank=True, verbose_name = "#140 Screen %")
    a200screen = models.CharField(max_length=5, blank=True, verbose_name = "#200 Screen %")
    a270screen = models.CharField(max_length=5, blank=True, verbose_name = "#270 Screen %")
    pan = models.CharField(max_length=5, blank=True, verbose_name = "Pan %")
    afs = models.CharField(max_length=5, blank=True, verbose_name = "AFS Grain Fineness # (Calc)")

    def __str__(self):
        return self.tool_num

class AlbiaShiftReport(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='mrockwell,kdavis,sperry,ltucker,dschoenberger,msullivan,jkelley,cskelton,tmcvey,dpendleton')#jhollatz
    z500 = models.CharField(max_length=6, blank=True, default='500', editable=True,)
    z702 = models.CharField(max_length=6, blank=True, default='702', editable=True,)
    z703 = models.CharField(max_length=6, blank=True, default='703', editable=True,)
    z704 = models.CharField(max_length=6, blank=True, default='704', editable=True,)
    z900 = models.CharField(max_length=6, blank=True, default='900', editable=True,)
    z901 = models.CharField(max_length=6, blank=True, default='901', editable=True,)
    z902a = models.CharField(max_length=6, blank=True, default='902a', editable=True,)
    z902b = models.CharField(max_length=6, blank=True, default='902b', editable=True,)
    z902c = models.CharField(max_length=6, blank=True, default='902c', editable=True,)
    z904a = models.CharField(max_length=6, blank=True, default='904a', editable=True,)
    z904b = models.CharField(max_length=6, blank=True, default='904b', editable=True,)
    z904c = models.CharField(max_length=6, blank=True, default='904c', editable=True,)
    z904d = models.CharField(max_length=6, blank=True, default='904d', editable=True,)
    z904e = models.CharField(max_length=6, blank=True, default='904e', editable=True,)
    z905 = models.CharField(max_length=6, blank=True, default='905', editable=True,)
    z908 = models.CharField(max_length=6, blank=True, default='908', editable=True,)
    z1101 = models.CharField(max_length=6, blank=True, default='1101', editable=True,)
    z1102 = models.CharField(max_length=6, blank=True, default='1102', editable=True,)
    z1103 = models.CharField(max_length=6, blank=True, default='1103', editable=True,)
    z1104 = models.CharField(max_length=6, blank=True, default='1104', editable=True,)
    z1201 = models.CharField(max_length=6, blank=True, default='1201', editable=True,)
    z1202 = models.CharField(max_length=6, blank=True, default='1202', editable=True,)
    z1203 = models.CharField(max_length=6, blank=True, default='1203', editable=True,)
    z1301 = models.CharField(max_length=6, blank=True, default='1301', editable=True,)
    setup500 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup702 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup703 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup704 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup900 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup901 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup902a = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup902b = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup902c = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup904a = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup904b = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup904c = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup904d = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup904e = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup905 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup908 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1101 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1102 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1103 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1104 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1201 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1202 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1203 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    setup1301 = models.CharField(max_length=6, blank=True, choices=BOOL_CHOICES)
    part_num500 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num702 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num703 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num704 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num900 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num901 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num902a = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num902b = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num902c = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num904a = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num904b = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num904c = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num904d = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num904e = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num905 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num908 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1101 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1102 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1103 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1104 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1201 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1202 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1203 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    part_num1301 = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    status500 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status702 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status703 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status704 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status900 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status901 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status902a = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status902b = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status902c = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status904a = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status904b = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status904c = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status904d = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status904e = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status905 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status908 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1101 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1102 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1103 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1104 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1201 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1202 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1203 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    status1301 = models.CharField(max_length=60, blank=True, verbose_name = "Status/Comments")
    comments = models.TextField(max_length=100, blank=True, verbose_name = "Additional Shift Notes")

    def __str__(self):
        return self.part_num

class LoTo(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='keller,sdayton,dsimerly,adixon,heller,jwoodby,kgrindstaff,cmorton,tkennett,jsommers,lbarr,acollins')
    machine_num = models.CharField(max_length=20, blank=True, verbose_name = "Machine #/Cell")
    datetime = models.DateTimeField(verbose_name = "Date/Time")
    comments = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.machine_num

class TempEmployeeMBU(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,dberning,dscherbring,gbrown,jschoop,hlangkamp,jmiller,mbasten,jmalek,jremakel,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,msullivan,mkirby,bmorgan,rdryer,rmccullough,dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,dgibbs,jblack,cbrady,dhein,guard2,guard3,pnugent,rpetrick,jherrig')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Temp Employee Name")
    date = models.DateField(verbose_name = "Start Date")
    position = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    shift = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name

class TempEmployeeFactory(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bgebhard,cchrest,ssabers,bmorgan,cbrady,chuntington,dscherbring,gbrown,hlangkamp,jbettcher,jcabana,jherrig,jheuer,banderson,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jschoop,mkirby,msullivan,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Temp Employee Name")
    date = models.DateField(verbose_name = "Start Date")
    position = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    shift = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name

class TempEmployeeFoundry(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='cbrady,cheim,chuntington,dboleyn,dwatson,jbettcher,jgaber,jkirk,jkohlenberg,eburgmeier,jremakel,jscherbring,msullivan,pludowitz,shuschik,ebradley,sohara,svanek')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Temp Employee Name")
    date = models.DateField(verbose_name = "Start Date")
    position = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    shift = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name

class TempEmployeeMaint(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='afossleman,bgebhard,cchrest,ssabers,bmorgan,cbrady,cheim,chuntington,dboleyn,dscherbring,dschumacher,mbeadle,dwatson,gbrown,hlangkamp,jbettcher,jcabana,jgaber,jherrig,jheuer,banderson,jkirk,jkohlenberg,eburgmeier,jmalek,jmiller,mbasten,jremakel,jscherbring,jschoop,mkirby,msullivan,pludowitz,rdryer,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Temp Employee Name")
    date = models.DateField(verbose_name = "Start Date")
    position = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    shift = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name

class TempEmployeeShip(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,cbrady,chuntington,dscherbring,gbrown,jbettcher,jherrig,jkohlenberg,eburgmeier,jremakel,jschoop,msullivan,pjentz,rmccullough,shuschik,ebradley,sohara,svanek,tbanwarth')
    name = models.CharField(max_length=30, blank=True, verbose_name = "Temp Employee Name")
    date = models.DateField(verbose_name = "Start Date")
    position = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    shift = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name

class InstructionSheetUpdate(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    PAPER_TYPE_CHOICES = (
        ('Paper', 'Paper'),
        ('Label', 'Label'),
        ('Cardstock', 'Cardstock'),
    )
    PAPER_COLOR_CHOICES = (
        ('White', 'White'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Cherry', 'Cherry'),
        ('Salmon', 'Salmon'),
        ('Gold', 'Gold'),
        ('Yellow', 'Yellow'),
        ('Gray', 'Gray'),

    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bhaas,dconnolly,dgreenwood,dschoenberger,ewolter,gbrown,jremakel,jzurcher,kduex,keller,syaklin,qmccullough,lvannatta,rmccullough,stefft,tbanwarth,thast,jkendell,ssabers,pmartelli')#bbecker,#cklein
    release = models.CharField(max_length=30, blank=True, verbose_name = "Instruction Sheet Release Notice")
    stocking = models.CharField(max_length=30, blank=True, verbose_name = "Stocking Plants (DBQ,Albia,Tenn,Nev)")
    date = models.DateField(blank=True, verbose_name = "Revision Date")
    new_release = models.CharField(max_length=6, blank=True, verbose_name = "New Release (Y/N)", choices=BOOL_CHOICES)
    revised = models.CharField(max_length=6, blank=True, verbose_name = "Revised (Y/N)", choices=BOOL_CHOICES)
    intranet = models.CharField(max_length=6, blank=True, verbose_name = "Sales Intranet Needed (Y/N)", choices=BOOL_CHOICES)
    product = models.CharField(max_length=30, blank=True, verbose_name = "Product Section (WW,Gas,Pumps,etc)")
    replace = models.CharField(max_length=30, blank=True, verbose_name = "Replaces Inst. Sheet(s) (Designate When)")
    co_num = models.CharField(max_length=30, blank=True, verbose_name = "C.O. #")
    delay = models.CharField(max_length=6, blank=True, verbose_name = "Time Delay (Y/N)", choices=BOOL_CHOICES)
    hole_size = models.CharField(max_length=10, blank=True, verbose_name = "Hole Size")
    hole_loc = models.CharField(max_length=20, blank=True, verbose_name = "Hole Location")
    paper_type = models.CharField(max_length=15, blank=True, verbose_name = "Paper Type", choices=PAPER_TYPE_CHOICES)
    paper_color = models.CharField(max_length=10, blank=True, verbose_name = "Paper Color", choices=PAPER_COLOR_CHOICES)
    comments = models.TextField(max_length=100, blank=True,)

    def __str__(self):
        return self.release

class OvertimeRequest(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dberning,dscherbring,gbrown,jschoop,hlangkamp,jmiller,mbasten,jmalek,jremakel,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,msullivan,mkirby,bmorgan,rdryer,rmccullough,jboll,cbrady,dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz,chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,jherrig')
    date = models.DateField(blank=True)
    department = models.CharField(max_length=30, blank=True, verbose_name = "Dept(s) Individual Employee")
    shift = models.CharField(max_length=30, blank=True, verbose_name = "Shift")
    time = models.CharField(max_length=30, blank=True)
    change = models.CharField(max_length=6, blank=True, verbose_name = "Change Start/Finish Time", choices=BOOL_CHOICES)
    post = models.CharField(max_length=6, blank=True, verbose_name = "Post (Y/N)", choices=BOOL_CHOICES)
    post_date = models.DateField(blank=True, verbose_name = "Posting Date")

    def __str__(self):
        return self.date

class PackingStandard(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jheuer,banderson,bgebhard,cchrest,ssabers,hlangkamp,jcabana,jmalek,nlecuas')
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    carton_num = models.CharField(max_length=30, blank=True, verbose_name = "Carton #")
    carton_wgt = models.CharField(max_length=30, blank=True, verbose_name = "Carton Weight")
    pcs_carton = models.CharField(max_length=30, blank=True, verbose_name = "Pieces per Carton")
    pcs_tote = models.CharField(max_length=30, blank=True, verbose_name = "Pieces per Totepan")
    jolts_carton = models.CharField(max_length=30, blank=True, verbose_name = "Jolts per Carton")
    wgt_three_pcs = models.CharField(max_length=30, blank=True, verbose_name = "Weight of 3 Pieces")
    one_hand = models.CharField(max_length=30, blank=True, verbose_name = "1/Hand Simo")
    two_hand = models.CharField(max_length=30, blank=True, verbose_name = "2/Hand Simo")
    two_hand_pc = models.CharField(max_length=30, blank=True, verbose_name = "2 Hands/PC")
    stacked = models.CharField(max_length=30, blank=True, verbose_name = "Stacked")
    random = models.CharField(max_length=30, blank=True, verbose_name = "Random")
    qty_sub = models.CharField(max_length=30, blank=True, verbose_name = "Quantity of Subassemblies")
    qty_inst = models.CharField(max_length=30, blank=True, verbose_name = "Quantity of Instruction Sheets")
    needs = models.CharField(max_length=30, blank=True)
    num_pcs = models.CharField(max_length=30, blank=True, verbose_name = "# of PC's in Order")
    comments = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.part_num


class ProductionOrderChange(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='amehlhorn,ashea,bmorgan,dratterman,dthen,gbrown,jherrig,jremakel,jschoop,jkendell,efaust,gryan,marling,mkirby,msullivan,rmccullough,ssabers,pmartell,tbanwarth,tpiggott')#bbecker
    work = models.CharField(max_length=30, blank=True, verbose_name = "Work Center")
    order_num = models.CharField(max_length=30, blank=True, verbose_name = "Order #")
    date = models.DateField(blank=True, verbose_name = "Due Date")
    order_qty = models.CharField(max_length=30, blank=True, verbose_name = "Order Qty")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    priority = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    description = models.TextField(max_length=100, blank=True, verbose_name = "Descripe What Happened/Current Status")

    def __str__(self):
        return self.work

class ProjectRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jboll,lmiller')
    project = models.CharField(max_length=30, blank=True, verbose_name = "Project Title")
    requestor = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=True, null=True, verbose_name = "Date")
    description = models.TextField(max_length=100, blank=True, default='For Project REquest, Send EMail to Support@aymcdonald.com')
    new = models.BooleanField(blank=True)
    chg = models.BooleanField(blank=True)
    deploy = models.CharField(max_length=100, blank=True)
    reason = models.TextField(max_length=500, blank=True, null=True, verbose_name = "Reason (Including Benefits)")

    def __str__(self):
        return self.project

class FabRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,dscherbring,gbrown,mkirby,pjentz,rmccullough,tbanwarth')
    date = models.DateField(blank=True, verbose_name = "Today's Date")
    req_date = models.DateField(blank=True, verbose_name = "Request Date")
    plate = models.CharField(max_length=30, blank=True, verbose_name = "Plate #")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    quantity = models.CharField(max_length=30, blank=True)
    order_num = models.CharField(max_length=30, blank=True, verbose_name = "Order #")
    fab = models.CharField(max_length=30, blank=True, verbose_name = "Fab From")
    description = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.date

class ToolboxMinutes(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='msullivan,mkirby,rmccullough,jremakel,gbrown,kdavis,adixon,heller,jwoodby,dsimerly,jsommers,tkennett,lbarr,acollins,keller,jkelley,dpendleton,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bfebhard,dschoenberger,ltucker')
    notes = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.notes

class ShiftReport(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='msullivan,dscherbring,mkirby,bmorgan,rmccullough,jjremakel,gbrown,jschoop,kdavis,adixon,heller,jwoodby,dsimerly,jsommers,tkennett,lbarr,acollins,keller,jkelley,jjohnson,dpendlet,cskelton,amehlhorn,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,ltucker,mdobraska,lbrown,pmcdaniel,tmcvey,slampier,gcurtis,mrockwell,kdavis,sperry,dschoenberger,jburdt,rdryer,jherrig')#bbecker
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.message

class AlbiaSetupException(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='kdavis,dpendleton,jkelley,cskelton,ltucker,dschoenberger,msullivan,amehlhorn,tmcvey,kwagner')#jhollatz
    employee = models.CharField(max_length=30, blank=True, verbose_name = "Employee Name")
    shift = models.CharField(max_length=5, blank=True)
    work_center = models.CharField(max_length=10, blank=True, verbose_name = "Work Center #")
    date = models.DateField(blank=True, null=True, verbose_name = "Date of Exception")
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    prev_part_num = models.CharField(max_length=30, blank=True, verbose_name = "Previous Part #")
    begin_setup = models.CharField(max_length=30, blank=True, verbose_name = "Begin Setup (hundreths)")
    end_setup = models.CharField(max_length=30, blank=True, verbose_name = "End Setup (hundreths)")
    cum_time = models.CharField(max_length=30, blank=True, verbose_name = "Cumulative Time")
    excep_time = models.CharField(max_length=30, blank=True, verbose_name = "Exception Time")
    difference = models.CharField(max_length=30, blank=True, verbose_name = "Difference of Actual/Exception")
    time_sup = models.TimeField(blank=True, null=True, verbose_name = "Time Supervisor Notified")
    time_ie = models.TimeField(blank=True, null=True, verbose_name = "Time I.E. Notified")
    breaks = models.CharField(max_length=30, blank=True, verbose_name = "Lunch/Break (Y or N / L or B)")
    explanation = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.employee

class AlbiaMaintRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='ltucker,mdobraska,jkelley,lbrown,pmcdanel,spangburn,msullivan,tmcvey,slampier,dpendleton,gcurtis,mrockwell,cskelton,kdavis,sperry,dschoenberger')#jhollatz
    department = models.CharField(max_length=30, blank=True, verbose_name = "Department")
    department_num = models.CharField(max_length=30, blank=True, verbose_name = "Department #")
    machine = models.CharField(max_length=30, blank=True, verbose_name = "Machine")
    safety = models.CharField(max_length=30, blank=True, verbose_name = "Safety")
    description = models.CharField(max_length=30, blank=True, verbose_name = "Description")
    lout = models.CharField(max_length=30, blank=True, verbose_name = "Lout")
    cell = models.CharField(max_length=30, blank=True, verbose_name = "Cell")
    request = models.TextField(max_length=100, blank=True, verbose_name = "Request")

    def __str__(self):
        return self.department

class AlbiaMachineDownLog(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='msullivan,lotting,marling,jremakel,dschumacher,mbeadle,mrockwell,pmcdanel,gcurtis,dberning,slampier,cskelton,jkelley,dpendleton,ltucker,sperry,dschoenberger,rdryer,amehlhorn,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,kdavis,spangburn,sduncan')#jhollatz
    date = models.DateField()
    machine_num = models.CharField(max_length=20, blank=True, verbose_name = "Machine #")
    cell_num = models.CharField(max_length=10, blank=True, verbose_name = "Cell #")
    machine_desc = models.CharField(max_length=30, blank=True, verbose_name = "Machine Description")
    reason = models.CharField(max_length=300, blank=True, verbose_name = "Reason Down")
    duration = models.CharField(max_length=10, blank=True, verbose_name = "Duration Days")

    def __str__(self):
        return self.date

class AlbiaRejectedParts(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, blank=True, verbose_name = "Send To", default='msullivan,lotting,marling,jremakel,jburdt,mrockwell,tmcvey,rhall,kdavis,bhaas,stefft,shall,rmccullough,dpendleton,ltucker,sperry,dschoenberger,ashea')
    reject_num = models.CharField(max_length=20, blank=True, verbose_name = "Rejection #")
    part_num = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    quantity = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=20, blank=True, verbose_name = "Department #")
    po_num = models.CharField(max_length=20, blank=True, verbose_name = "PO #")
    vendor = models.CharField(max_length=20, blank=True)
    tracking = models.CharField(max_length=20, blank=True, verbose_name = "Tracking Order Required", choices=BOOL_CHOICES)
    tracking_num = models.CharField(max_length=20, blank=True, verbose_name = "Tracking Order #")
    description = models.CharField(max_length=20, blank=True)
    reason = models.CharField(max_length=20, blank=True, verbose_name = "Reason for Rejection")
    disposition = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.reject_num

class AlbiaRejectsToStk(models.Model):
    send_to = models.TextField(max_length=1000, blank=True, verbose_name = "Send To", default='lotting,marling,tmcvey,ashea,sperry,dschoenberger')
    part_num = models.CharField(max_length=20, blank=True, verbose_name = "Part #")
    tracking_num = models.CharField(max_length=20, blank=True, verbose_name = "Tracking Order #")
    returnstk = models.CharField(max_length=20, blank=True, verbose_name = "Return to Stock Ticket #")
    quantity = models.CharField(max_length=20, blank=True, verbose_name = "Quantity Returned to Stock")
    comments = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.part_num

class AlbiaGatePass(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='jremakel,msullivan,mdobraska,lbrown,sperry,dschoenberger,mrockwell')
    name = models.CharField(max_length=30, blank=True)
    date = models.DateField()
    clock_num = models.CharField(max_length=20, blank=True, verbose_name = "Clock #")
    sold = models.CharField(max_length=5, blank=True, choices=BOOL_CHOICES)
    given = models.CharField(max_length=5, blank=True, verbose_name = "Given To", choices=BOOL_CHOICES)
    borrow_date = models.DateField(blank=True, verbose_name = "Borrowed Date")
    return_date = models.DateField(blank=True, verbose_name = "Returned Date")
    approval = models.CharField(max_length=30, blank=True)
    cost = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=50, blank=True, verbose_name = "Description of Item")

    def __str__(self):
        return self.name

class AlbiaScrapNotice(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='tpiggott,msullivan,rmccullough,kdavis,sperry,dschoenberger,dpendlet,lotting,marling,ashea,jgaber,jkelley,cskelton,stefft,jjohnson,tmcvey,ltucker')#jhollatz
    part_num_scp = models.CharField(max_length=20, blank=True, verbose_name = "Part # Scrapped")
    part_num_scp_unt = models.CharField(max_length=20, blank=True, verbose_name = "Part # Scrapped Unit Goes Into")
    order_num = models.CharField(max_length=20, blank=True, verbose_name = "Order # of Production Order")
    quantity = models.CharField(max_length=20, blank=True, verbose_name = "Quantity Scrapped")
    order_qty = models.CharField(max_length=20, blank=True, verbose_name = "Order Quantity")
    cell_num = models.CharField(max_length=20, blank=True, verbose_name = "Cell # Part is Running in")
    reason = models.CharField(max_length=20, blank=True, verbose_name = "Reason for Scrap")

    def __str__(self):
        return self.part_num_scp

class TennMachineDownLog(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='msullivan,keller,rdryer,hlangkamp,jmiller,mbasten,adixon,heller,jwoodby,dsimerly,jsommers,tkennett,lbarr,acollins,jimbus,kgrindstaff,cmorton')
    date = models.DateField()
    machine_num = models.CharField(max_length=20, blank=True, verbose_name = "Machine #")
    cell_num = models.CharField(max_length=10, blank=True, verbose_name = "Cell #")
    machine_desc = models.CharField(max_length=30, blank=True, verbose_name = "Machine Description")
    reason = models.CharField(max_length=300, blank=True, verbose_name = "Reason Down")
    duration = models.CharField(max_length=10, blank=True, verbose_name = "Duration Days")

    def __str__(self):
        return self.date

class ResourceGrpSetup(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='ashea,bfee,bgebhard,cchrest,ssabers,bhaas,bmorgan,bwoods,dberning,dconnolly,dratterman,dscherbring,dthen,ewolter,gbrown,hdao,hlangkamp,jburdt,jcabana,jherrig,jheuer,banderson,jimbus,jmalek,jmiller,mbasten,jschoop,jzurcher,kduex,lotting,marling,mkirby,msullivan,parnold,pnowachek,raspen,rdryer,rmccullough,rrokusek,rwagner,sbrietbach,stefft,thast,tbanwarth,tlucey,tpiggott')#cklein
    plant = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    center = models.CharField(max_length=30, blank=True)
    class_desc = models.CharField(max_length=30, blank=True)
    fdy_mold = models.CharField(max_length=30, blank=True, verbose_name = "FDY Mold")
    short_desc = models.CharField(max_length=30, blank=True, verbose_name = "Short Description")
    contain = models.CharField(max_length=30, blank=True)
    group = models.CharField(max_length=30, blank=True)
    long_desc = models.CharField(max_length=100, blank=True, verbose_name = "Long Description")
    setup_time = models.TimeField(blank=True, verbose_name = "EST Setup Time")

    def __str__(self):
        return self.plant

class BlastSandSieve(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='ashea,dberning,dboleyn,cheim,dwatson,ewolter,jgaber,jscherbring,jremakel,jkirk,msullivan,pludowitz')
    machines = models.CharField(max_length=30, blank=True, verbose_name = "Indicate Which Machines")
    z18screen = models.CharField(max_length=30, blank=True, verbose_name = "#18 Screen %")
    z20screen = models.CharField(max_length=30, blank=True, verbose_name = "#20 Screen %")
    z25screen = models.CharField(max_length=30, blank=True, verbose_name = "#25 Screen %")
    z30screen = models.CharField(max_length=30, blank=True, verbose_name = "#30 Screen %")
    z35screen = models.CharField(max_length=30, blank=True, verbose_name = "#35 Screen %")
    z40screen = models.CharField(max_length=30, blank=True, verbose_name = "#40 Screen %")
    z45screen = models.CharField(max_length=30, blank=True, verbose_name = "#45 Screen %")
    z50screen = models.CharField(max_length=30, blank=True, verbose_name = "#50 Screen %")
    z60screen = models.CharField(max_length=30, blank=True, verbose_name = "#60 Screen %")
    pan = models.CharField(max_length=30, blank=True, verbose_name = "Pan %")

    def __str__(self):
        return self.machines

class ProductionProblemReport(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='parnold,jremakel,dwatson,jgaber,dratterman,msullivan,gbrown,jschoop,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,mkirby,bmorgan,rmccullough,lotting,rwagner,jscherbring,jkirk,stefft,dthen,ashea,rrokusek,jburdt,dboleyn,bhaas,jherrig,pludowitz,bolberding,droush,dcosley,erauen,jimbus,klenz,marling,rdavid,jkendell,efaust,gryan,pmartell,tbanwarth,jrissman,astelken,amehlhorn,tlucey,cheim,ewolter,kcarroll')#bbecker
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    description = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")
    part_num2 = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code2 = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date2 = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    description2 = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported2 = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective2 = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")

    def  __str__(self):
        return self.part_num

class AlbiaProductionProblemReport(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='tpiggott,msullivan,kdavis,sperry,dschoenberger,dpendleton,lotting,marling,ashea,jgaber,jkelley,cskelton,tmcvey,ltucker')#jhollatz
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    description = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")
    part_num2 = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code2 = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date2 = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    description2 = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported2 = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective2 = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")

    def  __str__(self):
        return self.part_num

class TennProductionProblemReport(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='adixon,heller,jwoodby,tkennett,lbarr,dsimerly,jsommers,acollins,ashea,msullivan,jimbus,marling,bhaas,keller,rdavid,dcosley,bolberding,droush,jgaber,bjohnson,ewolter,rwagner')
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    description = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")
    part_num2 = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code2 = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date2 = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    description2 = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported2 = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective2 = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")

    def  __str__(self):
        return self.part_num

class FDYToolRoomRequest(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='dboleyn,cheim,jsteffes,dwatson,jgaber,jscherbr,jremakel,jkirk,msulliva,pludowit,jmiller,mbasten')
    tool = models.CharField(max_length=30, blank=True, verbose_name = "Tool/Fixture")
    description = models.CharField(max_length=30, blank=True)
    work_center = models.CharField(max_length=30, blank=True, verbose_name = "Work Center")
    requestor = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=True)
    date_req = models.DateField(blank=True, verbose_name = "Date Required")
    comments = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.tool

class RCLeaker(models.Model):
    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='astelken,ashea,bhaas,bjohnson,ewolter,jgaber,jkirk,jrissman,pnowachek,qmccullough,rrokusek,rwagner,tlucey,dboleyn,dwatson,pludowitz,jscherbring,cheim')
    rcpartnum = models.CharField(max_length=75, blank=True, verbose_name = "RC Part #")
    machpartnum = models.CharField(max_length=75, blank=True, verbose_name = "Mach Part #")
    percentleakers = models.CharField(max_length=75, blank=True, verbose_name = "Percent Leakers")
    location = models.CharField(max_length=200, blank=True, verbose_name = "Location of the Leak")
    cause = models.CharField(max_length=200, blank=True, verbose_name = "Cause of the Leak (shrink, gas holes, cold shut, etc) if known")
    foundjobnum = models.CharField(max_length=75, blank=True, verbose_name = "Foundry Job #")
    date_poured = models.DateField(blank=True, verbose_name = "Pour Date")
    patternnum = models.CharField(max_length=75, blank=True, verbose_name = "Pattern #")
    patternvent = models.CharField(max_length=5, blank=True, verbose_name = "Pattern Vented?", choices=BOOL_CHOICES)

    def __str__(self):
        return self.rcpartnum

class VendorVisit(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='chuntington,jbettcher,jkohlenberg,eburgmeier,svanek,ebradley,shuschik,sohara,msullivan,jremakel,rmccullough,jgaber,rdryer,dschumacher,dberning,mbeadle,guard1,guard2,guard3,dhein,pnugent,rpetrick')
    vendorname = models.CharField(max_length=100, blank=True, verbose_name = "Vendor Name")
    visitor1 = models.CharField(max_length=100, blank=True, verbose_name = "Visitors Name")
    visitor2 = models.CharField(max_length=100, blank=True, verbose_name = "Visitors Name")
    visitor3 = models.CharField(max_length=100, blank=True, verbose_name = "Visitors Name")
    visitor4 = models.CharField(max_length=100, blank=True, verbose_name = "Visitors Name")
    visitor5 = models.CharField(max_length=100, blank=True, verbose_name = "Visitors Name")
    visiting = models.CharField(max_length=100, blank=True, verbose_name = "Person Visiting")
    purpose = models.CharField(max_length=100, blank=True, verbose_name = "Purpose of Visit")
    duration = models.CharField(max_length=100, blank=True, verbose_name = "Approximate Duration")

    def __str__(self):
        return self.vendorname

class FiveSUpdate(models.Model):
    BOOL_CHOICES = (
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'),
    )
    BOOL_CHOICESTWO = (
        ('Red Tag', 'Red Tag'),
        ('Shine', 'Shine'),
        ('Sort/Set In Order', 'Sort/Set In Order'),
        ('Audit', 'Audit'),
    )
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='bmorgan,dberning,dscherbring,gbrown,jschoop,jherrig,jremakel,mbeadle,msullivan,mkirby,rdryer,rmccullough,tbanwarth,amehlhorn,banderson,bgebhard,hlangkamp,jkendell,jmiller,jmalek,jcabana,jheuer,mbasten,parnaold,cchrest,efaust,gryan,jschmitt,pjentz,pmartelli,ssabers')
    date = models.DateTimeField(blank=True, verbose_name = "Current Date", default=datetime.datetime.now)
    cell = models.CharField(max_length=50, blank=True, verbose_name = "Cell/Area")
    progress = models.CharField(max_length=15, blank=True, choices=BOOL_CHOICES)
    activity = models.CharField(max_length=15, blank=True, choices=BOOL_CHOICESTWO)
    activity2 = models.CharField(max_length=15, blank=True, choices=BOOL_CHOICESTWO)
    activity3 = models.CharField(max_length=15, blank=True, choices=BOOL_CHOICESTWO)
    activity4 = models.CharField(max_length=15, blank=True, choices=BOOL_CHOICESTWO)
    activity5 = models.CharField(max_length=15, blank=True, choices=BOOL_CHOICESTWO)
    activity6 = models.CharField(max_length=15, blank=True, choices=BOOL_CHOICESTWO)
    completed = models.TextField(max_length=500, blank=True)
    employee = models.CharField(max_length=50, blank=True)
    celltwo = models.CharField(max_length=30, blank=True)
    approxhours = models.CharField(max_length=30, blank=True)
    employee2 = models.CharField(max_length=50, blank=True)
    celltwo2 = models.CharField(max_length=30, blank=True)
    approxhours2 = models.CharField(max_length=30, blank=True)
    employee3 = models.CharField(max_length=50, blank=True)
    celltwo3 = models.CharField(max_length=30, blank=True)
    approxhours3 = models.CharField(max_length=30, blank=True)
    employee4 = models.CharField(max_length=50, blank=True)
    celltwo4 = models.CharField(max_length=30, blank=True)
    approxhours4 = models.CharField(max_length=30, blank=True)
    employee5 = models.CharField(max_length=50, blank=True)
    celltwo5 = models.CharField(max_length=30, blank=True)
    approxhours5 = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.cell

class RoughCastReject(models.Model):
    send_to = models.TextField(max_length=1000, verbose_name = "Send To", default='parnold,jremakel,dwatson,jgaber,dratterman,msullivan,gbrown,jschoop,hlangkamp,jmiller,mbasten,jmalek,jcabana,jheuer,banderson,bgebhard,cchrest,ssabers,tcao,mkirby,bmorgan,rmccullough,lotting,rwagner,jscherbring,jkirk,stefft,dthen,ashea,rrokusek,jburdt,dboleyn,bhaas,jherrig,pludowitz,bolberding,droush,dcosley,erauen,jimbus,klenz,marling,rdavid,jkendell,efaust,gryan,pmartell,tbanwarth,jrissman,astelken,amehlhorn,tlucey,cheim,ewolter,kcarroll')#bbecker
    part_num = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    super = models.CharField(max_length=30, blank=True, verbose_name = "Supervisor")
    quality = models.CharField(max_length=30, blank=True, verbose_name = "Quality Personnel")
    ie = models.CharField(max_length=30, blank=True, verbose_name = "IE Personnel")
    description = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")
    part_num2 = models.CharField(max_length=30, blank=True, verbose_name = "Part #")
    job_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Job #")
    resource_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Resource #")
    cast_num2 = models.CharField(max_length=20, blank=True, verbose_name = "Casting #")
    pri_code2 = models.CharField(max_length=30, blank=True, verbose_name = "Priority Code")
    due_date2 = models.DateField(blank=True, null=True, verbose_name = "Due Date")
    job_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Job Qty")
    qty_ran2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Ran")
    good_qty2 = models.CharField(max_length=30, blank=True, verbose_name = "Qty Good")
    super2 = models.CharField(max_length=30, blank=True, verbose_name = "Supervisor")
    quality2 = models.CharField(max_length=30, blank=True, verbose_name = "Quality Personnel")
    ie2 = models.CharField(max_length=30, blank=True, verbose_name = "IE Personnel")
    description2 = models.TextField(max_length=75, blank=True, verbose_name = "Description of Problem")
    reported2 = models.CharField(max_length=30, blank=True, verbose_name = "Reported By")
    corrective2 = models.CharField(max_length=40, blank=True, verbose_name = "Corrective Action By")

    def  __str__(self):
        return self.part_num

class Test(models.Model):
    email = models.CharField(max_length=500, default='KSchmitt@aymcdonald.com', verbose_name = "Send To")
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.message




#def newusersend(sender, instance, created, **kwargs):
#    if created:
#        subject = 'New User Setup'
#        message = 'Please Setup New User...\n \n First Name: %s \n \n Last Name: %s \n \n Start Date: %s \n \n Please logon to AYMAssets/admin to view the ticket' % (instance.first_name, instance.last_name, instance.start_date,)
#        from_addr = 'CommonEmailMessage@aymcdonald.com'
#        recipient_list = (instance.send_to,)
#        send_mail(subject, message, from_addr, recipient_list)
#signals.post_save.connect(newusersend, sender=NewUser)
