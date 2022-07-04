def myxml(tagname, content='', **kwargs) -> str:
    attrs = ''.join([f' {key}="{value}"'
                     for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'

with open('file.xml', 'w') as xml_file:
    xml_file.write(myxml('foo', 'bar', a=1, b=2, c=3))