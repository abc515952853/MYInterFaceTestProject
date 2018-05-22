import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
print(proDir)
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_xls(self,name):
        value = self.cf.get("TESTCASE",name)
        return value
        

# if __name__ == "__main__":
#     a = ReadConfig()
#     a.get_url('url')