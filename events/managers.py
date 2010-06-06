import datetime
from django.db import models

class WhenManager(models.Manager):
    def user_planning(self, user, what, start_date, end_date):
        if what == "me":
            return self.personal_planning(user,
            start_date, end_date)
        if what == "classgroup":
            from ipdb import set_trace
            set_trace()
            return  self.classgroup_planning(user.get_profile().classgroup,
            start_date, end_date)
        if what == "campus":
            return self.campus_planning(user.get_profile().classgroup.campus,
            start_date, end_date)
        if what == "university":
            return self.university_planning(user.get_profile().classgroup.\
            campus.university,
            start_date, end_date)

    # -- User planning access methods -------------------------------------
    
    def personal_planning(self, user, start_date, end_date):
        return super(WhenManager, self).get_query_set().filter(event__who__user=user).\
                     filter(date__gte=start_date).\
                     filter(date__lte=end_date).select_related(depth=1)

    def campus_planning(self, campus, start_date, end_date):
        return super(WhenManager, self).get_query_set().filter(event__who__campus=campus).\
                     filter(date__gte=start_date).\
                     filter(date__lte=end_date).select_related(depth=1)

    def university_planning(self, university, start_date, end_date):
        return super(WhenManager, self).get_query_set().\
                     filter(event__who__university=university).\
                     filter(date__gte=start_date).\
                     filter(date__lte=end_date).select_related(depth=1)

    def studyperiod_planning(self, studyperiod_id, start_date, end_date):
        pass

    def classgroup_planning(self, classgroup, start_date, end_date):
        return super(WhenManager, self).get_query_set().\
                     filter(event__who__classgroup=classgroup).\
                     filter(date__gte=start_date).\
                     filter(date__lte=end_date).select_related(depth=1)
