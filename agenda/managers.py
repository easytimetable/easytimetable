import datetime

from django.db import models

class WhenManager(models.Manager):
    


    
    
    def user_planning(self, user, what):
        if what == "classgroup":
            return  self.classgroup_planning(user.get_profile.classgroup.id)



    #User planning access methods
    def personal_planning(self, user):
        pass

    def campus_planning(self, campus_id):
        pass

    def university_planning(self, university_id):
        pass

    def studyperiod_planning(self, studyperiod_id):
        pass

    def classgroup_planning(self, classgroup_id):
        pass
