Currently Elastic Beanstalk only supports Python 2.6 projects out of the box. The .ebextensions/python27.config
file does everything required to get Python 2.7 setup for your application on elastic beanstalk.

To test this out you can git clone this project.

Run:

```
eb init
eb start
``` 


Once the application is up and running vist the eb url in your browser and you should see this output:

```
2.7.3 (default, May 18 2012, 22:11:36) 
[GCC 4.4.6 20110731 (Red Hat 4.4.6-3)]
```

Happy days!
