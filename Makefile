package:
	rm -f slack_tz.zip
	`for i in `find -E . -regex ".*\.(pyc|dist-info)"`; do rm $i; done;`
	zip -r slack_tz.zip *

deploy:
	aws lambda update-function-code --function-name slack_tz --zip-file fileb://slack_tz.zip --region us-east-1

