# for i in range(10):
#     nums = input()
#     num.append(1)
#     summary += int(nums)
#     count += 1
#     num[i] = nums
nums = 0
count = -1
median = 0
summary = 0
num = []
i = 0
n = 0
while 1:
    nums = input()
    if nums == '0':
        break
    num.append(1)
    summary += int(nums)
    count += 1
    n += 1
    num[count] = int(nums)

average = summary / n


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0


def listToStringWithoutBrackets(list1):
    return str(list1).replace('[', '').replace(']', '').replace(',','')


num.sort(reverse=True)

print('Average :', round(average, 2))
print('Median :', round(median(num), 2))
print('Descending :', listToStringWithoutBrackets(num))
