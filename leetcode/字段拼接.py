query = "88"
condition_field = ['name', 'qq']
q_str = ''
for field in condition_field:
    q = "Q({0}__contains={1})&".format(field, query)
    q_str = q_str + q
q_str=''
q_str = q_str + "Q(consultant__isnull=True)"
print(q_str)
