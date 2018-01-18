README
======
* Download the latest Google App Engine SDK from https://cloud.google.com/appengine/downloads and extract it to your $HOME folder.

* Copy app.yaml and assets/ directory into it.

```bash
rsync -avu . $HOME/google-cloud-sdk/

```

* Launch the webserver by typing below command within the SDK directory.
```bash
cd $HOME && $HOME/google-cloud-sdk/bin/dev_appserver.py google-cloud-sdk
```

* After running the above command, you should be able to access the site at http://localhost:8080

* Make sure that you are added as a developer for unc-desi.appspot.com by emailing me at "rkjanardhana (at) gmail.com" before you can push changes to the site. 

* For developmental purposes, I would suggest creating a new appengine site and modify app.yaml file to get it working.

* Delete unnecessary django files to reduce the app footprint

```
rm -rf $HOME/google-cloud-sdk/platform/google_appengine/lib/django*
```

* To update the production site, you need to run below command,

```bash
# Login to gcloud
$HOME/google-cloud-sdk/bin/gcloud auth login
# Set current project
$HOME/google-cloud-sdk/bin/gcloud config set project unc-desi

# Deploy
cd $HOME/google-cloud-sdk/ && $HOME/google-cloud-sdk/bin/gcloud app deploy
```

* If you want to learn the details about App Engine (Python), take a look at the documentation at https://cloud.google.com/appengine/docs/python/
