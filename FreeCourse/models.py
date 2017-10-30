from django.db import models
from AdminManage.models import Organization

class FreeCourse(models.Model):
	organic_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
	data = models.CharField(max_length=10000, default='{"course_1": "", "course_2": "", "course_3": "", "course_4": "", "course_5": "", "course_6": "", "course_7": "", "course_8": "", "course_9": "", "course_10": "", "course_11": "", "course_12": "", "course_13": "", "course_14": "", "course_15": "", "course_16": "", "course_17": "", "course_18": "", "course_19": "", "course_20": "", "course_21": "", "course_22": "", "course_23": "", "course_24": "", "course_25": "", "course_26": "", "course_27": "", "course_28": "", "course_29": "", "course_30": "", "course_31": "", "course_32": "", "course_33": "", "course_34": "", "course_35": ""}')
