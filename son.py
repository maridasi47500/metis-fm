from myfunc import Myfunc
from fichier import Fichier
import os
class Son(Myfunc):
    def __init__(self,name):
        self.name=name
        self.content=Fichier(os.environ("MAMUSIQUE"),name.split("/")[-1]).lirefichier()

        self.mymusic=name.split(".")[1]

    def get_html(self):
        return self.content
