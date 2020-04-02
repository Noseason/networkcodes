
# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def bin2dec(string_num):
    return str(int(string_num, 2))

def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

def checksum(sourcestring):
    sum = 0
    for i in range(0, len(sourcestring), 4):
        substring=sourcestring[i:i + 4]
        inte = int(substring, 16)
        sum = sum + inte
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    if sum > 65535:
        sum = (sum >> 16) + (sum & 0xffff)
    checksum=65535-sum
    return checksum

if __name__ == '__main__':
    bits1 = input('第一个16比特字：')
    bits2 = input('第二个16比特字：')
    bits3 = input('第三个16比特字：')
    bits=bits1+bits2+bits3
    #print(bin2hex(bits))
    print("校验和计算结果： ")
    print(bin(checksum(bin2hex(bits)))[2:])