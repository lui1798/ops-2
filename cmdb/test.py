#
# count = 1
# while count<=6:
#     print count
#     count += 1
#
# print 'end'
#
# d = {
#     'name' : 'IT',
#     'age': '30'
# }
# d['job'] = 'IT'
# d['city'] = 'hz'
#
# print d
#
# for key in d:
#     print key
#     print d[key]
#     print '_'*30


arr = [1,2,3,4,5,5,53,3,2,1,15,4]
# print arr.index(4,arr.index(53)+1)
#
# arr = list('cmdb')
# arr.insert(2,1)
# print arr
# arr.append('123')
# print arr
# print arr.pop(-1)

# while True:
#     action = raw_input('input your action')
#     if action == 'add':
#         detail = raw_input('input things')
#         arr.append(detail)
#         print arr
#     elif action == 'do':
#         if len(arr) == 0:
#             break
#             arr.remove(0)
#         print arr.pop(0)

# print arr
# arr.reverse()
# print arr

# arr = list('hello')
# arr_diff= []
# arr_reverse = list('hello123')
# # while len(arr)>0:
# #     arr_reverse.append(arr.pop())
# # print arr_reverse
#
# print arr
# print arr_reverse
# for o in arr_reverse:
#     if o  not in arr:
#         arr_diff.append(o)
# print arr_diff

# l1 = [1]
# l2 = [1,2,3,2,12,3,1,3,21,2,2,21,2,2,3,4111,22,3]
#
# for i in l2:
#     for l in range(1,len(l1)):
#         if i <= l1[1]:
#             l1.insert(l,i)
#             print l1
#             print '*'*10
#             break
#         elif i > l1[len(l1)-1]:
#             l1.append(i)
#
# print l1


insert_list = [1,24,13,4,2,12,3,14,3,2,12,3,224]
sorted_list = []

# for i in range(len(insert_list)):
#     min = insert_list[i]
#     for j in range(i+1,len(insert_list)):
#         if insert_list[j] < min:
#             min = insert_list[j]
#     sorted_list.append(min)
#
# print sorted_list

# for i in range(1,len(insert_list)):
#     key = insert_list[i]
#     print key
#     j = i - 1
#     while j >=0 and key < insert_list[j]:
#         insert_list[j+1] = insert_list[j]
#         insert_list[j] = key
#         j -= 1
#
# print insert_list

# arr_list=[5000,4333,3,4,888,12,3,14,3,21]
# init_count=len(arr_list)
# for i in range(0,init_count):
#     init_index=i
#     for j in range(i+1,init_count):
#         if arr_list[init_index]>arr_list[j]:
#             init_index=j
#     temp=arr_list[i]
#     arr_list[i]=arr_list[init_index]
#     arr_list[init_index]=temp
#
# print(arr_list)
#
# init_tuple = ('a','b','c','a')
# print init_tuple[0]
# print init_tuple[1]

d = {'name':'pc','age':'12'}
#
# print d['name'],d['age']
#
# if 'name' not in d:
#     print 'has no name'
# elif 'name' in d:
#     print 'has name'
#
#     print d.get('age')
#
# y = d.copy()
# print y
# y['age'] =31
# print y
# # y.clear()
# # print y
#
#
# for key in d:
#     print key
#     print d[key]

# new_dict = {}
# for key in d:
#     new_dict[key] = d[key]
#
# print new_dict

#
# read_me = '''
# first of all , i want make it clear that
# '''
#
# mydic1={}
# for i in range(len(read_me)):
#
#     num = read_me.count(read_me[i])
#
#     mydic1[read_me[i]]=num
# print mydic1
#
#
# print {}.fromkeys(['name','age'],12)
# print {}.fromkeys(['name','age'])
#
# dict = {'name':'albert','age':'31'}
#
# print dict.items()


# init_dict = {'name':'pc','age':20}
# print init_dict.items()
# for (k,v) in init_dict.items():
#     print 'key is %s value is %s' % (k,v)
#
# print init_dict.pop('name')
# print init_dict
#
#
# print '|'.join(['hello','world'])[1:3]
#
# print '|'.join(['hello','world']).find('r')
#
# print 'dello  '.capitalize()
#
# str = 'hello WORLd'
# print str[0].upper() + str[1:].lower()
#
# print str.count('l')
#
# print str.replace('ll','dd')
#
# str = '    hello*123*world     '
#
# print str.split('*')
#
#
# print str.strip()
#
# a=list('hello')
# a.reverse()
# res = ''
#
# for i in list('hello'):
#     res = i + res
# print res