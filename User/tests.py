from django.test import TestCase

# Create your tests here.

import json




a = {'1': '普通会员','2':'超级会员'}
b = '超级会员'

for i in a.items():
    print(i)
    if b == i[1]:
        print(i[0])

