from django.shortcuts import render
from django.http import HttpResponse
from FreeCourse.models import FreeCourse
from AdminManage.models import Organization
import json

def index(request):
	if request.GET.get('id'):
		organic = Organization.objects.get(id=request.GET.get('id'))
<<<<<<< HEAD
		data = {"id": request.GET['id']}
=======
		data = {"id": request.GET['id'], 'organic_name': organic.organic_name}
>>>>>>> 3370ac6aff8a144f24ff63e47d53ab6044855f8b
		if organic.free_course_open=='1' or request.session.get('id'):
			data['open'] = '1'
		else:
			data['open'] = '0'
		return render(request, "FreeCourse/index.html", data)
	else:
		return render(request, "FreeCourse/error.html")

def submit(request):
	name = request.POST["name"]
<<<<<<< HEAD
=======
	contact = request.POST["contact"]
>>>>>>> 3370ac6aff8a144f24ff63e47d53ab6044855f8b
	organic_id = request.POST["id"]
	organic = FreeCourse.objects.get(organic_id=organic_id)
	course = json.loads(organic.data)
	for course_k, course_v in request.POST.items():
		if "course" in course_k:
			if name in course[course_k]:
				return HttpResponse("2")      # 该用户已提交
			else:
<<<<<<< HEAD
				course[course_k] = course[course_k] + course_v.replace("空", name).replace(' ', '') + " "
	organic.data = json.dumps(course)
	organic.save()
	return HttpResponse("1")     # 提交成功
=======
				course[course_k] = course[course_k] + course_v.replace("空", name+contact) + " "
	organic.data = json.dumps(course)
	organic.save()
	return HttpResponse("1")     # 提交成功
>>>>>>> 3370ac6aff8a144f24ff63e47d53ab6044855f8b
