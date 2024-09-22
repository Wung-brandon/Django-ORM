from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q, Count, Sum
from datetime import date

# Create your views here.
# retrieves the user with the exact name pogba
queryname = User.objects.filter(Q(username__exact="pogba"))

# Q query with the & (AND) operator. returns the user which name starts with o and ends with i else it returns an empty queryset
nameAnd = User.objects.filter(Q(username__startswith="o") & Q(username__endswith="i"))

# # Q query with the | (OR) operator. returns the user which name starts with a or ends with n else it returns an empty queryset
nameOR = User.objects.filter(Q(username__startswith="and") | Q(username__endswith="n")) 

# fetch all users except the user with the id of 2
query = User.objects.filter( ~ Q(id__lt=2))

print("query", query)
# combining two queries from the same model and combining them using union
q1 = User.objects.filter(Q(id__gt=2))
q2 = User.objects.filter(Q(id__lt=2))
q3 = q1.union(q2)
# print("union query", q3)

# values_list returns the selected fields as a turple
q_list = User.objects.filter(username__startswith="p").values_list("first_name", "last_name", "email", named=True)

print("values_list", q_list)
# values-returns the selected fields as a dictionary
q = User.objects.filter(username__startswith="p").values("first_name", "last_name", "email")

# get the total number of users 
# print(User.objects.all().count())

# print("values", q)
q_annotate = User.objects.annotate(total_users=Count("username"))
# print("annotate", q_annotate)

currentdate = date.today().strftime("%A")
print("current date", currentdate)