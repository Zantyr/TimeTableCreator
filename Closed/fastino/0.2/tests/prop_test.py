import properties

properties.PROPERTIES.new("testdev","temp0-255")
properties.PROPERTIES.new("testdev","temp0-1023")
properties.PROPERTIES.new("arduino","temp+-3k")
prop_list = properties.PROPERTIES.dump()
conversion = properties.PROPERTIES.convert(*prop_list[0:2])
print conversion
conversion = properties.PROPERTIES.convert(prop_list[0],prop_list[2])
print conversion