README
======
* Download the latest Google App Engine SDK from https://developers.google.com/appengine/downloads

* Extract the SDK. Copy app.yaml and assets/ directory into it.

* Launch the webserver by typing below command within the SDK directory.
<pre>./dev_appserver.py .</pre>

* After running the above command, you should be able to access the site at http://localhost:8080

* Make sure that you are added as a developer for unc-desi.appspot.com by emailing me at "rkjanardhana (at) gmail.com" before you can push changes to the site. 

* For developmental purposes, I would suggest creating a new appengine site and modify app.yaml file to get it working.

* To update the production site, you need to run below command,
<pre>./appcfg.py --email=YOUR_GMAIL_ID update APP_ENGINE_SDK_FOLDER</pre>

* If you want to learn the details about App Engine (Python), take a look at the documentation at https://developers.google.com/appengine/docs/python/overview.

7) You can remove unused libraries (django) in <APP_ENGINE_SDK_FOLDER>/lib folder to overcome max blob and file limit.
<pre>rm -rf APP_ENGINE_SDK_FOLDER/lib/django*</pre>

