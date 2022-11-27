def build_xml_element(tag, content, elements):
    xml_string = "<" + str(tag)
    for key, value in elements.items():
        xml_string += " " + str(key) + "=" + str(value)
    xml_string += ">" + str(content) + "</" + str(tag) + ">"
    return xml_string
