import sys, os
sys.path.insert(0,'/var/www/public_html/apps')
os.environ["HOME"]= '/home/luis'
from hello import app as application
