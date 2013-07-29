# -*- coding: utf-8 -*-
__author__ = 'dollar'
import urllib2
import cookielib
import urllib
import time

class CheckIn(object):
    username = ''
    pwd = ''
    cookie = None
    cookiefile = './cookie.dat'
    login_header = {'Host': 'emuch.net',
                    'Connection': 'keep-alive',
                    # 'Content-Length': '122',
                    # 'Cache-Control': 'max-age=0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Origin': 'http://emuch.net',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Referer': 'http://emuch.net/bbs/logging.php?action=login',
                    'Accept-Encoding': 'gzip,deflate,sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    }
    checkin_header = {'Host': 'emuch.net',
                      'Connection': 'keep-alive',
                      'Content-Length': '74',
                      'Cache-Control': 'max-age=0',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Origin': 'http://emuch.net',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
                      'Content-Type': 'application/x-www-form-urlencoded',
                      'Referer': 'http://emuch.net/bbs/memcp.php?action=getcredit&uid=2571434',
                      'Accept-Encoding': 'gzip,deflate,sdch',
                      'Accept-Language': 'zh-CN,zh;q=0.8}',}
    # body = {}
    query = ()

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        self.query = (('formhash', 'e1c294fc'),
                      ('referer',''),
                      ('username', username),
                      ('password', pwd),
                      ('cookietiem', '31536000'),
                      ('loginsubmit', ''),)
        # self.body = {'formhash': 'e1c294fc',
        #              'referer': '',
        #              'username': username,
        #              'password': pwd,
        #              'cookietiem': '31536000',
        #              'loginsubmit': '',
        #              }
        self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)

    def login(self):
        # post_data = self.body
        post_data = self.query
        post_data = urllib.urlencode(post_data)
        post_data = post_data + '%BB%E1%D4%B1%B5%C7%C2%BC'
        print post_data
        print 'login...'
        reqURL = 'http://emuch.net/bbs/logging.php?action=login&t=' + str(int(time.time()))
        req = urllib2.Request(url=reqURL, data=post_data, headers=self.login_header)
        resp = urllib2.urlopen(req)
        headers = resp.info()
        print '################ login in header #################'
        print str(headers)
        print '################ login in header #################'
        result = resp
        # if headers['Content-Encoding'] == 'gzip':
        #     result =self.unzip(result)

        result.read()

        self.cookie.save(self.cookiefile)
        # result = str(result).decode('utf-8').encode('gbk')
        # result = str(result).decode('utf-8')
        # resp = urllib2.urlopen("http://emuch.net/bbs/logging.php?action=login")
        # print resp.read()
        # print "#################"
        # print result
        print "#################"
        print self.cookie
        print 'Login successfully'

    def checkin(self):
        checkin_post_data = (('formhash', '0aca7050'),
                             ('getmode', '1'),
                             ('message', ''),
                             ('creditsubmit', ''),)
        post_data = urllib.urlencode(checkin_post_data) + '%C1%EC%C8%A1%BA%EC%B0%FC'
        checkin_url = 'http://emuch.net/bbs/memcp.php?action=getcredit'
        print 'checkin...'
        req = urllib2.Request(url=checkin_url, data=post_data, headers=self.checkin_header)
        resp = urllib2.urlopen(req)
        resp_header = resp.info()
        print '################ check in header #################'
        print resp_header
        print '################ check in header #################'
        print 'checkin successfully!'


    def unzip(self,data):
        import gzip
        import StringIO
        data = StringIO.StringIO(data)
        gz = gzip.GzipFile(fileobj=data)
        data = gz.read()
        gz.close()
        return data

# if __name__ == '__main__':
#     user = Login('fzb763', 'fzb19870924')
#     user.login()
#     user.checkin()