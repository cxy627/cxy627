
def get_ping_result(ip_address):
    import subprocess
    import re
    p = subprocess.Popen("ping.exe -n 1 -w 500 "+ip_address, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out = p.stdout.read().decode('gbk')
    reg_receive = '已接收 = \d'
    match_receive = re.search(reg_receive, out)

    receive_count = -1

    if match_receive:
        receive_count = int(match_receive.group()[6:])

    if receive_count > 0:  # 接受到的反馈大于0，表示网络通
        return 1
    else:
        print('%s不可达！' % ip_address)
        return 0


if __name__ == '__main__':
    ping_result = get_ping_result('119.75.217.185')
    print(ping_result)
