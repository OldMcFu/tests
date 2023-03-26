
jsonRequests = ["Start", "Stop"]

defaultReturn = "std::string"
defaultParams = "std::string a"

parentClass = "DefaultModule"
parentClassHeader = "default_module.h"

def createWrapper():
    #Create header file
    className = "ModuleRequestWrapper"
    
    with open('module_request_wrapper.h', 'w') as f:
        
        f.write('#include "{}"\n'.format(parentClassHeader))
        f.write("class {}\n".format(className))
        f.write("{\n")
        f.write("public:\n")
        for jR in jsonRequests:
            f.write("static {} {}({});\n".format(defaultReturn, jR, defaultParams))
            f.write("\n")
        f.write("private:\n")
        f.write(className+"() {"+"};\n")
        f.write("const {}* moduleObj = new {}();\n".format(parentClass, parentClass))
        f.write("};\n")

    #create c file
    with open('module_request_wrapper.cpp', 'w') as f:
        for jR in jsonRequests:
            f.write("{} {}::{}({})\n".format(defaultReturn,className, jR, defaultParams))
            f.write("{\n")
            f.write("\t{} ret = moduleObj->{}({});\n".format(defaultReturn, jR, defaultParams.split(' ')[1]))
            f.write("\treturn ret;\n")
            f.write("}\n")
            f.write("\n")
        

def createParentClass():
    className = parentClass
    with open(parentClassHeader, 'w') as f:
        f.write('#include {}\n\n'.format("<string>"))
        f.write("class {}\n".format(className))
        f.write("{\n")
        f.write("public:\n")
        for jR in jsonRequests:
            f.write("virtual {} {}({})\n".format(defaultReturn, jR, defaultParams))
            f.write("{\n")
            f.write("\t{} ret;\n".format(defaultReturn))
            f.write("\treturn ret;\n")
            f.write("}\n")
            f.write("\n")
        f.write("private:\n")
        f.write("};\n")

def createChiledClass():
    classNames = ["res_module", "sat_module"]
    for className in classNames:
        cN = className.replace('_', '')    
        with open(className+".hpp", 'w') as f:
            f.write('#include "{}"\n\n'.format(parentClassHeader))
            f.write("class {} : public {}\n".format(cN, parentClass))
            f.write("{\n")
            f.write("public:\n")
            for jR in jsonRequests:
                f.write("{} {}({}) override;\n".format(defaultReturn, jR, defaultParams))
                f.write("\n")
            f.write("private:\n")
            f.write("};\n")

        #create c file
        with open(className+".cpp", 'w') as f:
            for jR in jsonRequests:
                f.write("{} {}::{}({})\n".format(defaultReturn, cN, jR, defaultParams))
                f.write("{\n")
                f.write("\t{} ret;\n".format(defaultReturn))
                f.write("\treturn ret;\n")
                f.write("}\n")
                f.write("\n")


createWrapper()
createParentClass()
createChiledClass()
