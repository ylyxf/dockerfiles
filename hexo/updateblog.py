#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os 
import shutil  
import subprocess
import time

buildDir = '/var/tmp/blog'
distDir = '/var/blog'
#生成博客
pull = subprocess.Popen(['git','pull'],cwd=buildDir)
pull.wait()
gen = subprocess.Popen(['hexo','generate'],cwd=buildDir)
gen.wait()
