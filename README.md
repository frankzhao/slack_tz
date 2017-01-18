slacktz
=======

Slack timezone converter

An experimental serverless app for AWS Lambda. I made this app for my small team
who are distributed across different time zones. A new slack command `/tz` is used 
to convert between human readable timezones, no mental math needed!

Example usage

```
frank [11:31 PM] 
/tz 4pm PST to Australia/Sydney

Timezone Converter BOT [11:31 PM] 
4pm PST is Thursday, 19 Jan 2017 11:00 AM AEDT+1100
```

The important bits are in the Makefile and `slack_tz.py`. The rest are just 
dependencies required for packaging. I really need to update the Makefile to
pull straight from `site-packages`.

