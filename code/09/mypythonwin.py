﻿import myindexerror
import myvalueerror
userList=['maxianglin','wanglili','malingling','fanxiaoxuan']
user_str=''
user_name=''
input_selectIndex=0
user_name=0
try:
    input_selectIndex=int(raw_input('Please input your inquires the user name Numbers:'))
    user_str=userList[input_selectIndex]
    input_selectName=raw_input('Please input your inquires the user name:')
    user_name=userList.index(input_selectName)
except IndexError,e:
    print 'Mistakes information Numbers for:',myindexerror.MyIndexError('1').value
except ValueError,e:
    print 'Mistakes information Numbers for:',myvalueerror.MyValueError('2').value
else:
    print 'The Numbers for you input'+str(input_selectIndex)+'User for:'+user_str
    print 'The customer that you input'+input_selectName+'On the list for the corresponding index:'+str(user_name)



