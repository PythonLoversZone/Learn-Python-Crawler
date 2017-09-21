'''
简单介绍scrapycXPATH选择器的使用
'''
from scrapy.selector import Selector 

xml = '''
<html>
    <body>
        <class id=1>
            <name>王尼玛</name>
            <sex>男</sex>
            <age>80</age>
            <favouite>开车</favouite>
        </class>
        <class id=2>
            <name>陈一发</name>
            <sex>母</sex>
            <age>28</age>
            <favouite>开che</favouite>
        </class>
        <class id=3>
            <name>狗贼叔叔</name>
            <sex>公</sex>
            <age>18</age>
            <favouite>土豪战</favouite>
        </class>
    </body>
</html>
'''

a = Selector(text=xml).xpath('/html/body/class[1]').extract()

print(a)