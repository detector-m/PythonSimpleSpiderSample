# *-* coding: utf-8 *-
import re

if __name__ == '__main__':
    '''
    re.match
    param1: 匹配的规则
    param2: 需要匹配的文本
    '''
    content = 'Xiaoshuaib has 100 bananas'
    print(re.match.__name__)
    res = re.match(r'^Xi.*(\d+)\s.*s$', content)
    print(res.group(1)) #0
    res = re.match(r'^Xi.*?(\d+)\s.*s$', content)
    print(res.group(1)) #100

    content = """Xiaoshuaib has 100 
    bananas"""
    # re的匹配模式 re.S
    '''
    修饰符	    描述
    re.I	使匹配对大小写不敏感
    re.L	做本地化识别（locale-aware）匹配
    re.M	多行匹配，影响 ^ 和 $
    re.S	使 . 匹配包括换行在内的所有字符
    re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
    '''
    res = re.match(r'^Xi.*?(\d+)\s.*s$', content, re.S)
    print(res.group(1)) #100

    '''
    匹配一个东西还要写开头结尾,有点麻烦，这个时候可以使用re.rearch
    re.rearch 扫描字符串 然后把匹配成功后的第一个结果返回
    '''
    print(re.search.__name__) # search
    res = re.search(r'Xi.*?(\d+)\s.*s', content, re.S)
    print(res.group(1)) #100

    '''
    多个结果
    '''
    content = """Xiaoshuaib has 100 bananas; 12341234
    Xiaoshuaib has 100 bananas; 1234
    Xiaoshuaib has 100 bananas; 12345
    Xiaoshuaib has 100 bananas;"""
    print(re.findall.__name__) # findall
    res = re.findall(r'Xi.*?(\d+)\s.*?s;', content, re.S)
    print(res) #100  
    # sub
    print(re.sub.__name__) # sub
    content = re.sub(r'\d{4,5}', '120', content)
    print(content)  

    '''
    complile 
    这个主要就是把我们的匹配符封装一下, 便于以后复用
    '''
    content = "Xiaoshuaib has 100 bananas"
    print(re.compile.__name__) # sub
    pattern = re.compile(r'Xi.*?(\d+)\s.*s', re.S)
    res = re.match(pattern, content)
    print(res.group(1))

