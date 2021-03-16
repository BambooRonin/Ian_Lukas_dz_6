source = open('nginx_logs.txt', 'r', encoding='utf-8')
res =[]
for line in source:
    line_spl = line.split(' ')
    remote_addr = line_spl[0]
    request_type = line_spl[5][1:]
    requested_resource = line_spl[6]
    res_int = [remote_addr, request_type, requested_resource]
    res_int_tup = tuple(res_int)
    res.append(res_int_tup)
print(res)
