import xml.dom.minidom
from xml.etree import ElementTree as ET

def yewubanliprofile():
    filename="F:\\myboce.xml"
    phone=""
    passwd=""
    item={}
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for child in root:
            print(child.tag, ":", child.attrib)
            if child.tag == "yewubanli":
                for nodeinfo in child:
                    print(str(nodeinfo))
                    if nodeinfo.tag == 'phone':
                        item['phone'] = nodeinfo.text
                    if nodeinfo.tag == "passwd":
                        item['passwd'] = nodeinfo.text
                break

        print("phone======" + phone)
        print("passwd======" + passwd)
        return(item)

    except Exception as err:
        print(err)
        return(None,None)

