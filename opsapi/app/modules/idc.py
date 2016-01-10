#_*_coding:utf-8_*_
from app.models import Idc
from app import db
import inspect

def init(**params):
    return "nihao"

def get(**params):
    output = params.get('output',[])
    limit = params.get('limit',10)
    order_by = params.get('order_by','id desc')

    if not isinstance(output, list):
        raise Exception("output必须为列表")

    for field in output:
        if not hasattr(Idc,field):
            raise Exception("{}这个输出字段不存在".format(field))

    data = db.session.query(Idc).order_by(order_by).limit(limit).all()
    db.session.close()

    ret = []
    for obj in data:
        if output:
            tmp = {}
            for f in input:
                tmp[f] = getattr(obj,f)
                ret.append(tmp)
        else:
            tmp = obj.__dict__
            tmp.pop('_sa_instance_state')
            ret.append(tmp)
    print ret
    return ret

def create(**params):
    """
    1. 获取参数信息,
    2. 处理
    3. 通过数据实例化Idc
    4. 插入数据
    """
    for field in params.keys():
        print field
        if not hasattr(Idc,field):
            raise Exception("params error")
        if not params.get(field,None):
            raise Exception("name 不能为空")

    print inspect.getmembers(Idc,predicate=inspect.ismethod())


    idc = Idc(**params)
    db.session.add(idc)
    db.session.commit()
    return idc.id

def update(**params):
    data = params.get('data',{})
    where = params.get('where',{})

    if not data:
        raise Exception("没有需要的no data")

    for field in data.keys():
        if not hasattr(Idc,field):
            raise Exception("需要更新的{}这个字段不存在 no{}")

    if not where:
        raise Exception("需要提供where条件 no where")

    if where.get('id',None) is None :
        raise Exception("需要提供id 作为条件 no con")

    try:
        id = int(where['id'])
        if id <= 0:
            raise Exception("条件id的值不能为负数  id")
    except ValueError:
        raise Exception("条件id的值必须为int  ")

    ret = db.session.query(Idc).filter_by(**where).update(data)
    db.session.commit()

    return ret
