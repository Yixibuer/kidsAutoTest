class By(object):
    """
    Set of supported locator strategies.
    """
    # 通用元素定位方式(主要web端)
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
    # ios元素定位方式
    IOS_PREDICATE = '-ios predicate string'
    IOS_UIAUTOMATION = '-ios uiautomation'
    IOS_CLASS_CHAIN = '-ios class chain'
    ACCESSIBILITY_ID = 'accessibility id'
    # android元素定位方式
    ANDROID_UIAUTOMATOR = '-android uiautomator'
    ANDROID_VIEWTAG = '-android viewtag'
    ANDROID_DATA_MATCHER = '-android datamatcher'
    ANDROID_VIEW_MATCHER = '-android viewmatcher'
    # windows元素定位方式
    WINDOWS_UI_AUTOMATION = '-windows uiautomation'
    # 其他
    IMAGE = '-image'
    CUSTOM = '-custom'
