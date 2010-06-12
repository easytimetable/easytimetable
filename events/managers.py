import datetime
from django.db import models
from locations.models import Campus
from profiles.models import ClassGroup
from django.db.models import Q

class WhenManager(models.Manager):
    
    def must_display(self, user, start_date, end_date):
        classgroup = user.get_profile().classgroup
        if classgroup:
            campus = classgroup.campus
        else:
            campus = None
        if campus:
            university = campus.university
        else:
            university = None
        return super(WhenManager, self).get_query_set().\
                    filter(Q(event__who__user=user) |
                           Q(event__who__campus=campus,
                             event__who__campus__isnull=False) | 
                           Q(event__who__university=university,
                             event__who__university__isnull=False) |
                           Q(event__who__classgroup=classgroup,
                             event__who__classgroup__isnull=False)).\
                    filter(date__gte=start_date).\
                    filter(date__lte=end_date).\
                    filter(event__force_display=True).select_related(depth=1)

    def user_planning(self, user, what, start_date, end_date, what_arg=None):
        if what == "mandatory":
            return self.must_display(user, start_date, end_date)
        if what == "my_user":
            return self.personal_planning(user,
            start_date, end_date)
        if what == "my_classgroup":
            return  self.classgroup_planning(user.get_profile().classgroup,
            start_date, end_date)
        if what == "my_campus":
            return self.campus_planning(user.get_profile().classgroup.campus,
            start_date, end_date)
        if what == "my_university":
            return self.university_planning(user.get_profile().classgroup.\
            campus.university,
            start_date, end_date)
       
       #If we don't have a what arg, we won't be able to go further
        if what_arg is None:
            return []
        
        if what == "campus":
            return self.campus_planning(Campus.objects.get(id=what_arg),
                                            start_date, end_date, False)
        if what == "classgroup":
            return self.classgroup_planning(ClassGroup.objects.get(id=what_arg),
                                            start_date, end_date, False)

    # -- User planning access methods -------------------------------------
    
    def personal_planning(self, user, start_date, end_date,
    skip_mandatory=True):
        qs = super(WhenManager, self).get_query_set().\
                    filter(event__who__user=user).\
                    filter(date__gte=start_date).\
                    filter(date__lte=end_date).\
                    select_related(depth=1)
        if skip_mandatory:
            qs = qs.filter(event__force_display=False)
        return qs

    def campus_planning(self, campus, start_date, end_date,
    skip_mandatory=True):
        qs = super(WhenManager, self).get_query_set().\
                    filter(event__who__campus=campus).\
                    filter(date__gte=start_date).\
                    filter(date__lte=end_date).\
                    select_related(depth=1)
        if skip_mandatory:
            qs = qs.filter(event__force_display=False)
        return qs

    def university_planning(self, university, start_date, end_date,
    skip_mandatory=True):
        qs = super(WhenManager, self).get_query_set().\
                    filter(event__who__university=university).\
                    filter(date__gte=start_date).\
                    filter(date__lte=end_date).\
                    select_related(depth=1)
        if skip_mandatory:
            qs = qs.filter(event__force_display=False)
        return qs
                    

    def studyperiod_planning(self, studyperiod_id, start_date, end_date):
        pass

    def classgroup_planning(self, classgroup, start_date, end_date,
    skip_mandatory=True):
        if classgroup is None:
            return []
        qs = super(WhenManager, self).get_query_set().\
                    filter(event__who__classgroup=classgroup).\
                    filter(date__gte=start_date).\
                    filter(date__lte=end_date).\
                    select_related(depth=1)
        if skip_mandatory:
            qs = qs.filter(event__force_display=False)
        return qs


