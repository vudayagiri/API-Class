from datetime import datetime

fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime('2010-01-01 17:31:22', fmt)
d2 = datetime.strptime('2010-01-03 17:31:22', fmt)
diff = (d2-d1)*24*60
print (f'({diff} minutes')
