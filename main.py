#!/usr/bin/python3
import os
import glob
import begin
from unsec import Email, EmailCollection, Cleaner, TfidfVectorizer, LogicVectorizer, Clustering
import logging
import random

from cmeans import *


print("salut")



a = [[3,4], [5,4], [56,76], [67,89], [5,2], [45,87]]

b = random.sample(a, 6)

print(a, b)


cmean = FuzzyCMeans(a,b)

