# PROJECT Z

@author: hyobinyou


### Usage

Add a regular cron job to update the data on the server by running the following command:
```
python3 cronJob.py
```

Set up your server to handle data requests: 
```
python3 DataServer.py
```

Now you can send GET requests to receive the JSON data corresponding to the query:
```
/info?county=orange&state=california
```

Sample JSON data response:
```
{
	"county": "orange", 
	"countyCases": "321", 
	"countyDeaths": "3", 
	"countyAsOf": "2020-03-27", 
	"state": "california", 
	"stateCases": "4914", 
	"stateDeaths": "102", 
	"stateAsOf": "2020-03-27"
}
```

Empty or invalid county results in only state data. 
Invalid state results in an empty json response. 

### Notes

By default, the server will be set up as `localhost:9000`. 

To correctly add the cron job to the crontab, modify the workspace() method in Util.py with your work directory path. 

### Contact

Contact with comments/questions/concerns at hyobinyou@gmail.com
