# @author_='lcc'
# @date:2020/7/9 16:58
from local_lib.client.XdClient import XdClient
# from local_lib.common.webdriver.xpath_2_css import xpath_2_css
from local_lib.common.webdriver.by import By
import random


def create_session(session_len=9):
    ret = ""
    for i in range(session_len):
        # num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([letter, Letter]))
        ret += s
    return ret


class BasePage(object):
    """
    tab:
        'top_bar_mini':顶部导航栏收缩
        'top_bar_index': # 顶部导航栏展开
        'right_func_bar': # 右侧功能栏
        'to_reply_list': # 待回复列表
    """

    def __init__(self, tab='right_func_bar'):
        self._timeout = 30
        self._XdC = XdClient()
        self._ws_url = self._XdC.get_websocket(tab)['message']
        self._valueDict = {}

    def _excute(self, by, value):
        ele_session = create_session()
        if by == By.XPATH:
            js = "var " + ele_session + " = document." + by[1] % value + ".iterateNext()"
        else:
            js = "var {ele_session} = document.{method}('{value}')".format(ele_session=ele_session, method=by[1],
                                                                           value=value)
        res = self._XdC.run_js(self._ws_url, js, ws_session=ele_session, close=False)
        if res.get('code') == 'success':
            return WebElement(ele_session, self._ws_url, self._XdC)
        else:
            return "WebElment not found!"

    def _excutes(self, by, value):
        ele_session = create_session()

        if by == By.XPATH:
            js = "var " + ele_session + " = document." + by[2] % value
            self._XdC.run_js(self._ws_url, js=js, ws_session=ele_session, close=False)  # 创建连接
            js_search_len = "{}.snapshotLength".format(ele_session)
            res = self._XdC.run_js(self._ws_url, js=js_search_len, ws_session=ele_session, close=False)
            res_type = 'XpathResult'
        else:
            js = "var {ele_session} = document.{method}('{value}')".format(ele_session=ele_session, method=by[1],
                                                                           value=value)
            self._XdC.run_js(self._ws_url, js, ws_session=ele_session, close=False)
            js_search_len = "%s.length" % ele_session
            res = self._XdC.run_js(self._ws_url, js=js_search_len, ws_session=ele_session, close=False)
            res_type = 'other'

        if res.get('code') == 'success':
            res_len = res['message']['result']['result']['value']
            return [(WebElements(ele_session, self._ws_url, self._XdC, res_len, x, res_type)) for x in range(res_len)]
        else:
            return "WebElment not found!"

    def find_element(self, by, value):
        # if by == By.XPATH:
        #     value = xpath_2_css(value)
        return self._excute(by=by, value=value)

    def find_elements(self, by, value):
        # if by == By.XPATH:
        #     value = xpath_2_css(value)
        return self._excutes(by=by, value=value)

    def find_element_by_xpath(self, xpath):
        return self.find_element(by=By.XPATH, value=xpath)

    def find_elements_by_xpath(self, xpath):
        return self.find_elements(by=By.XPATH, value=xpath)

    # def find_element_by_id(self, id):
    #     return self.find_element(by=By.ID, value=id)

    # def find_element_by_tag_name(self, tag_name):
    #     return self.find_element(by=By.TAG_NAME, value=tag_name)

    # def find_element_by_class_name(self, class_name):
    #     return self.find_element(by=By.CLASS_NAME, value=class_name)

    # def find_element_by_css_selector(self, css_selector):
    #     return self.find_element(by=By.CLASS_NAME, value=css_selector)

    # def slide_scroll_bar(self, scroll):
    #     # scroll = 10000,滑到底部,scroll = 0,滑到顶部
    #     js = "document.getElementBy.scrollTop=%d" % scroll
    #     res = self._XdC.run_js(self._ws_url, js)
    #     return res


class WebElement:
    def __init__(self, ele_session, _ws_url, XdC):
        self._ele_session = ele_session
        self._XdC = XdC
        self._ws_url = _ws_url

    def click(self):
        js = "{ele_session}.click()".format(ele_session=self._ele_session)
        # js = "%s.click()" % self._ele_session
        return self._XdC.run_js(self._ws_url, js=js, ws_session=self._ele_session, close=False)

    def send_keys(self, value, _type=0):
        """

        :param value: 需要发送的值
        :param _type: 输入框的类型:
        :return:
        """
        _type_dict = {0: "value",
                      1: "innerText"}
        js = "{ele_session}.{key_type}='{value}'".format(ele_session=self._ele_session, key_type=_type_dict[_type],
                                                         value=value)
        # js = "%s.value='%s'" % (self._ele_session, value)
        return self._XdC.run_js(self._ws_url, js=js, ws_session=self._ele_session, close=False)

    def text(self):
        js = "{0}.innerText".format(self._ele_session)
        return self._XdC.run_js(self._ws_url, js=js, ws_session=self._ele_session, close=False)


class WebElements(WebElement):
    def __init__(self, _ele_session, _ws_url, XdC, ele_len=None, index=0, res_type='Xpath'):
        super().__init__(_ele_session, _ws_url, XdC)
        self._type = res_type
        self.len = ele_len
        self.index = index

    def click(self):
        js = "{ele_session}{index}.click()".format(ele_session=self._ele_session, index=self.index)
        # js = "%s(%d).click()" % (self._ele_session, self.index)
        return self._XdC.run_js(self._ws_url, js=js, ws_session=self._ele_session, close=False)

    def send_keys(self, value, _type=0):
        _type_dict = {0: "value", 1: "innerText"}
        js = "{ele_session}{index}.{key_type}='{value}'".format(ele_session=self._ele_session, index=_type,
                                                                key_type=_type_dict[_type],
                                                                value=value)
        return self._XdC.run_js(self._ws_url, js=js, ws_session=self._ele_session, close=False)

    def text(self):
        js = "{0}{1}.innerText".format(self._ele_session, self.index)
        return self._XdC.run_js(self._ws_url, js=js, ws_session=self._ele_session, close=False)

# XDC = XdClient()
# _ws_url = XDC.get_websocket('right_func_bar')[""]
# a = BasePage()
# ele = a.find_element_by_xpath('//em[text()="嘎嘎"]')
# ele.click()
