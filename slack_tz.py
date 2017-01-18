from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError
from dateparser import parse
from dateparser.date import DateDataParser

def lambda_handler(event, context):
    fmt = '%A, %d %b %Y %l:%M %p %Z%z'
    dp_settings = {'RETURN_AS_TIMEZONE_AWARE': True}
    
    # Handle request params
    token = event['token']
    request_str = event['text']
    
    if 'to' in request_str:
        request_str = request_str.split('to')
    elif 'as' in request_str:
        request_str = request_str.split('as')
    else:
        return 'Could not parse destination timezone.'
    
    request_tz = request_str[1].strip().split('/')

    dest_tz = request_tz[0].title() + '/' + request_tz[1].title()
    request_str = request_str[0].strip()
    
    loc_dt = parse(request_str, settings=dp_settings)
    
    if loc_dt is not None:
        try:
            dest_dt = loc_dt.astimezone(timezone(dest_tz))
        except UnknownTimeZoneError:
            return "Unknown timezone: " + dest_tz
        response =  {
                        "response_type": "in_channel",
                        'text': request_str + ' is ' + dest_dt.strftime(fmt)
                    }
        return response
    else:
        return 'Could not parse the requested timestamp.'

if __name__ == "__main__":
    result = lambda_handler(
        {
            'token': 'test_token',
            'text': '4pm AEST to US/Pacific'
        },
        None
    )
    print(result)
