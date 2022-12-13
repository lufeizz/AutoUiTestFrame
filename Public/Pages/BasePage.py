from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BasePage():
    """
    BasePage封装所有页面的公共方法
    """
    #初始化方法，如果不是Firefox则抛出异常
    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception:
            raise NameError("Not Firefox")

    #打开浏览器地址，并最大化
    def open(self,url):
        if url != '':
          self.driver.get(url)
          self.driver.maximize_window()
        else:
            raise ValueError("Please input a url!")

    #封装WebDriver本身定位元素的方法，简化WebDriver自身定位元素的方法
    def findElement(self,element):
        try:
            type = element[0]
            value = element[1]
            if type == 'id' or type == 'ID' or type == 'Id':
                elem = self.driver.find_element("id",value)
            elif type == 'name' or type == 'NAME' or type == 'Name':
                elem = self.driver.find_element("name",value)
            elif type == 'class' or type == "CLASS" or type == 'Class':
                elem = self.driver.find_element("class",value)
            elif type == 'link_text' or type =='LINK_TEXT' or type == 'Link_text':
                elem = self.driver.find_element("link_text",value)
            elif type == 'xpath' or type == 'XPATH' or type == 'Xpath':
                elem = self.driver.find_element("xpath",value)
            elif type == 'css' or type == 'CSS' or type == 'Css':
                elem = self.driver.find_element("css selector",value)
            else:
                raise NameError("请输入正确的参数类型")
        except Exception:
            raise NameError("元素未发现！"+str(element))
        return elem

    #定位一组方法
    def findElements(self,element):
        try:
            type = element[0]
            value = element[1]
            if type == 'id' or type == 'ID' or type == 'Id':
                elem = self.driver.find_element("id",value)
            elif type == 'name' or type == 'NAME' or type == 'Name':
                elem = self.driver.find_element("name",value)
            elif type == 'class' or type == "CLASS" or type == 'Class':
                elem = self.driver.find_element("class",value)
            elif type == 'link_text' or type =='LINK_TEXT' or type == 'Link_text':
                elem = self.driver.find_element("link_text",value)
            elif type == 'xpath' or type == 'XPATH' or type == 'Xpath':
                elem = self.driver.find_element("xpath",value)
            elif type == 'css' or type == 'CSS' or type == 'Css':
                elem = self.driver.find_element("css selector",value)
            else:
                raise NameError("请输入正确的参数类型")
        except Exception:
            raise NameError("元素未发现！"+str(element))
        return elem

    def type(self,element,text):
        element.send_keys(text)

    def click(self,element):
        element.click()

    def enter(self,element):
        element.send_keys(Keys.RETURN)

    def quit(self):
        self.driver.quit()

    #获取指定元素的属性
    def getAttribute(self,element,attribute):
        return element.get_attribute(attribute)

    #js操作diaplay的值
    def display(self,id):
        self.driver = webdriver.Firefox()
        js = 'document.getElementById(list[id]).style.display="block"'
        self.driver.execute(js)
