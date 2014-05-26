from django.db import models
from django.contrib.auth.models import User

class Effect(models.Model):
    name = models.CharField(unique=True, max_length=32)
    def __unicode__(self):
        return u'%s' % (self.name)
        
class Duration(models.Model):
    time = models.CharField(unique=True, max_length=45)
    def __unicode__(self):
        return u'%s' % (self.time)
        
class Prefix(models.Model):
    prefix = models.CharField(unique=True, max_length=45)
    def __unicode__(self):
        return u'%s' % (self.prefix)
        
class Call(models.Model):
    effect = models.ForeignKey(Effect) 
    duration = models.ForeignKey(Duration, blank=True, null=True,) 
    firstPre = models.ForeignKey(Prefix, blank=True, null=True, related_name='Mass') 
    secondPre = models.ForeignKey(Prefix, blank=True, null=True, related_name='Global')  
    thirdPre = models.ForeignKey(Prefix, blank=True, null=True, related_name='Through')  
    fourthPre = models.ForeignKey(Prefix, blank=True, null=True, related_name='Enchanted')  
    amount = models.IntegerField(blank=True, null=True) 
    targeteffect = models.ForeignKey(Effect, blank=True, null=True, related_name='TargetEffect') 
    def __unicode__(self):
        first = ''
        if self.firstPre is not None:
            first = self.firstPre           
        sec = ''
        if self.secondPre is not None:
            sec = self.secondPre           
        third = ''
        if self.thirdPre is not None:
            third = self.thirdPre   
        fourth = ''
        if self.fourthPre is not None:
            fourth = self.fourthPre
        duration = ''
        if self.duration is not None:
            duration = self.duration
        amount = ''
        if self.amount is not None:
            amount = self.amount 
        target = ''
        if self.targeteffect is not None:
                target = self.targeteffect
        return u'%s %s %s %s %s %s %s %s' % (first, sec, third, fourth, self.effect, duration, amount, target)

class Species(models.Model):
    name = models.CharField(unique=True, max_length=45)
    playable = models.BooleanField(default=True)
    visable = models.BooleanField(default=True)
    displayname = models.ForeignKey('self', blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.name)    
        
class Character(models.Model):
    iduser = models.ForeignKey(User) 
    idspecies = models.ForeignKey(Species) 
    name = models.CharField(max_length=45)
    isalive = models.BooleanField(default=True) 
    isfinished = models.BooleanField(default=False) 
    xp = models.IntegerField(default=0)
    def __unicode__(self):
        return u'%s' % (self.name)
        
class FeatType(models.Model):
    type = models.CharField(max_length=45)
    def __unicode__(self):
        return u'%s' % (self.type)
        
class Class(models.Model):
    name = models.CharField(max_length=45)
    level = models.IntegerField()
    idclassprerequisite = models.ForeignKey('self', blank=True, null=True) 
    playable = models.BooleanField(default=True)
    visable = models.BooleanField(default=True)
    body = models.BooleanField()
    mana = models.BooleanField()
    bodyormana = models.BooleanField()
    armour = models.BooleanField()
    openfeat = models.BooleanField()
    clasfeat = models.BooleanField()
    craftingfeat = models.BooleanField()
    lore = models.BooleanField()
    firstspell = models.IntegerField()
    secspell = models.IntegerField()
    thridspell = models.IntegerField()
    fourthspell = models.IntegerField()
    fifthspell = models.IntegerField()
    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.level)
        
class Feat(models.Model):
    idclass = models.ForeignKey(Class, blank=True, null=True) 
    idrace = models.ForeignKey(Species, blank=True, null=True) 
    idfeatsprerequisite = models.ForeignKey('self', blank=True, null=True) 
    name = models.CharField(max_length=45)
    quantity = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    type = models.ForeignKey(FeatType)
    stackable = models.BooleanField(default=False)
    playable = models.BooleanField(default=True)
    visable = models.BooleanField(default=True)
    thislevelonly = models.BooleanField(default=False) 
    def __unicode__(self):
        quantity = ''
        if self.quantity is not None:
                quantity = self.quantity
        return u'%s %s' % (quantity, self.name)

class CharacterClass(models.Model):
    idcharacter  = models.ForeignKey(Character) 
    idclass = models.ForeignKey(Class) 
    locked = models.BooleanField(default=False)
    visable = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s %s' % (self.idcharacter, self.idclass)
    
class CharacterFeat(models.Model):
    idcharacter  = models.ForeignKey(Character) 
    idfeat = models.ForeignKey(Feat) 
    effect = models.ForeignKey(Effect, blank=True, null=True)   
    source = models.ForeignKey(CharacterClass, blank=True, null=True) 
    sourceother = models.CharField(max_length=256, blank=True, null=True)
    locked = models.BooleanField(default=False)
    visable = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s %s' % (self.idcharacter, self.idfeat)   

class ClassFeat(models.Model):
    idclass = models.ForeignKey(Class) 
    idfeat = models.ForeignKey(Feat) 
    choiceopen = models.BooleanField(default=False)
    choiceclass = models.BooleanField(default=False)
    choicefeat = models.ForeignKey('self', blank=True, null=True)
    def __unicode__(self):
        return u'%s %s' % (self.idclass, self.idfeat)  
        
class Spell(models.Model):
    idclass = models.ForeignKey(Class) 
    idcall = models.ForeignKey(Call)
    def __unicode__(self):
        return u'%s %s' % (self.idclass, self.idcall) 
    
class ClassSpell(models.Model):
    idclass = models.ForeignKey(Class) 
    idspell = models.ForeignKey(Spell)
    choiceopen = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s %s' % (self.idclass, self.idspell)

class CharacterSpell(models.Model):
    idcharacter = models.ForeignKey(Character) 
    idspell = models.ForeignKey(Spell)
    effect = models.ForeignKey(Effect, blank=True, null=True)   
    source = models.ForeignKey(CharacterClass, blank=True, null=True) 
    sourceother = models.CharField(max_length=256, blank=True, null=True)
    locked = models.BooleanField(default=False)
    visable = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s %s' % (self.idcharacter, self.idspell)  
        
class UsersDetails(models.Model):
    iduser = models.ForeignKey(User)
    number = models.CharField(max_length=45)
    emergencycontactname = models.CharField(max_length=45) # Field name made lowercase.
    emergencycontactnumber = models.CharField(max_length=45) # Field name made lowercase.
    homeaddressline1 = models.CharField(max_length=256) # Field name made lowercase.
    homeaddressline2 = models.CharField(max_length=256, blank=True) # Field name made lowercase.
    town = models.CharField(max_length=256, blank=True)
    county = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    carregistration = models.CharField(max_length=45, blank=True) # Field name made lowercase.
    medicalinformation = models.CharField(max_length=256, blank=True) # Field name made lowercase.
    donotcontact = models.BooleanField() # Field name made lowercase.
    
class Lore(models.Model):
    name = models.CharField(max_length=45)
    playable = models.BooleanField(default=True)
    visable = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s' % (self.name)
        
class ClassLore(models.Model):
    idclass = models.ForeignKey(Class) 
    idlore = models.ForeignKey(Lore)
    choiceopen = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s %s' % (self.idclass, self.idlore) 

class CharacterLore(models.Model):
    idcharacter = models.ForeignKey(Character)
    idlore = models.ForeignKey(Lore)
    source = models.ForeignKey(CharacterClass, blank=True, null=True) 
    sourceother = models.CharField(max_length=256, blank=True, null=True)
    locked = models.BooleanField(default=False)
    visable = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s %s' % (self.idcharacter, self.idlore)  