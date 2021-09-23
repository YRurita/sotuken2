from django.core.management.base import BaseCommand
import os
import sys
import pprint
import time

path_face = os.getcwd()
sys.path.append(path_face + "\\manager\\face_recognition")
#pprint.pprint(sys.path)

from main import main

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        num = 0
        try:
            while True:
                num = num + 1
                print(num)
                main()
                time.sleep(30)
        except KeyboardInterrupt:
            print('!!FINISH!!')