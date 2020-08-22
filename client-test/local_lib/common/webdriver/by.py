# @author_='lcc'
# @date:2020/7/14 17:49
class By(object):
    """
    对应元素选择方法,暂时支持xpath,其与的方法有返回多个参数的时候有bug
    """
    # ID = ("id", "getElementById")
    XPATH = ("xpath",
             "evaluate('%s', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null)",
             "evaluate('%s', document.documentElement, null,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null)")
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = ("name", "getElementsByName")
    # TAG_NAME = ("tag name", "getElementsByTagName")
    # CLASS_NAME = ("class name", "getElementsByClassName")
    # CSS_SELECTOR = ("css selector", "querySelector")
