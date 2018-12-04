
import xml.etree.ElementTree as ET
import Const
import re


path = Const.PathGenerator(Const.path_to_data_FCA_fulltext, "06_1.xml")
print(path)

text = open(path).read()
text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+",u"",text)
text = re.sub('"id=', 'id="', text)
text = re.sub(u"\s[\w]*&#?[\w]*;[\w]*\s", u"\w", text)
# print(text)
tree = ET.fromstring(text)

print(tree.tag)
print(tree[3])
for ele in tree:
    print(ele)