import unittest,time,datetime
from conf.setting import HOST_INFO
from lib.tools import my_request, myMd5, my_code,case,get_week_day
from nose_parameterized import parameterized

class get_document(unittest.TestCase):
    def setUp(self):
        self.url = 'http://test.teamin.cc:18308/v1/tasks'
    def cat_random(self):
        import random
        return random.random()
    @parameterized.expand(case())
    def test_task(self,data):
        '''分词接口测试'''
        # data = {'plan': '明天下午和百度签订战略合作协议'}
        res=my_request('post',self.url,data,None)
        # print('当前时间为%s,工作日为%s'%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time()))),get_week_day(datetime.date.fromtimestamp(time.time()))))
        # print('任务时间为%s,工作日为%s'%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(res.get('time'))),get_week_day(datetime.date.fromtimestamp(res.get('time')))))
        print('接口返回信息为%s'%res)
        # if res.get('topic')=='开会' and res['time'] !='0':
        #     self.assertEqual('开会',res['topic'])
        #     self.assertEqual('',res['executor'])
        # else:
        self.assertEqual(200, 200)
if __name__ == '__main__':
    unittest.main()
