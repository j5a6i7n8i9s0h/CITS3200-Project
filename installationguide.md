#How to install Telos on Heroku
####Introduction
Heroku is an online hosting service which can be used to host the Telos UWA app. This provides a way for users of the app to connect, whether they are on campus or off-campus. 
<p>
Heroku provides both paid and free services depending on the needs of the app. Pricing for the paid services can be found here: <br>
[www.heroku.com/pricing](https://www.heroku.com/pricing)

As part of this package, we are using the free version of Heroku which allows 3 simultaneous people to use the app at any one time. This free version also goes to sleep after 30 minutes of activity. This requires any user that uses the app after it has gone into sleep mode to wait up to 30 seconds for it to come back online.

If another hosting service is to be used, it will need to be able to host Python projects and utilise the Django framework. This would have to be verified before. From there the app can be pushed onto the server from this repository. The instructions for this would vary depending on the host, so you will have to check with them for their own instructions on how to do this.

####Django
Django is a high level framework used to underpin the workings of this app. It provides most of the backend services that the Telos app utilises. From the user authentication to the database. 

####Installation
To ease the process of installation, this app will come pre-installed on Heroku. This will also include a database using Heroku's build in Postgres database with includes a backup option to save the data in case of an emergency or accident (The backup feature of the free option has to be manually started, however the paid options allow for automatic backups to occur).

Included in the app is the ability for users to download a copy of their cover sheets and individual recording sheets for their own archiving purposes in the event that they lose access to the app.

If the app needs to be re-installed on Heroku, there is a convenient button that will take care of the installation process. This will install the app to the default url: telos-uwa.heroku.com

If a different domain is required, this will need to be purchased and linked to Heroku on the settings dashboard manually after the app has been installed. Further instructions can be found [here](https://devcenter.heroku.com/articles/custom-domains). In addition to this, the new domain will need to be added to the hollowed hosts of

If a SSL certificate is required, this isn't supported by the free version of Heroku. The hosting service will need to be upgraded to one of the paid versions. A SSL certificate is used to encrypt the data between the app and the users and provides a more secure connection.

Free SSL certificates can be acquired from [Let's encrypt](https://letsencrypt.org). Instructions for installing one of these certificates can be found in the Heroku help centre [here](https://devcenter.heroku.com/articles/ssl).

To deploy Telos on Heroku using the default settings, just click the button below. 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Once the button has been clicked, it will ask for a few settings. The first is the app name, this is where the app will be deployed. The app will be deployed to app-name.herokuapp.com where app-name is the name given. The name should only contain lowercase letters, numbers, and dashes. Next choose a region. The US is generally the best as it provides a closer connection to Australia.

Heroku will then go through the steps of deploying the app. This may take a couple of minutes. Once it is done it will say: You app was successfully deployed. Underneath this message is two buttons:

Manage app - Go to the app settings to manage the app

View - View the app
######Note: 
This button can also be used to create a default deploy that can be modified afterwards.

####Dyno Hours
Hosting on Heroku runs on a dyno, which is a type of server provisioned to run a specific application. 
A free account on Heroku is entitled to 550 hours per month. This is used when the dyno is running, however the dyno will swithc to a offline mode after it has been idle for 30 minutes. This feature preserves the number of hours but means that if a user tries to use the app after it has gone to sleep, it may take up to 30 seconds for the application to come back online.

Paid Heroku plans don't have such limitations and as such are always online.

The nunber of free dyno hours remaining in any given month can be found [here](https://dashboard.heroku.com/account/billing) or by looking at the billing section of the manage account page on Heroku.




