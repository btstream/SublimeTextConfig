import os
import platform

ENV = os.environ

if platform.system() == "Darwin":

        def plugin_loaded():
                ENV["PATH"] = "/opt/local/bin:" + ENV["PATH"] + ":/usr/texbin"
                print(ENV["PATH"])