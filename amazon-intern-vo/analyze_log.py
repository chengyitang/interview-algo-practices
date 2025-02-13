# OOD: Let's say you're building a distributed system on AWS. Every single component (EC2, Lambda, S3, etc.) of the system generates logs. 
# The logs are sent to Amazon CloudWatch Logs. Design a function to read the logs from a certain time range and count the occurence of certain keywords like "Error" or "Warning". 
# analyze_log(componenet_name, start_time, end_time, keywords) -> dict{keyword, count}


# Clarify questions:
# 1. What is the format of the log (timestamp, log level, message)??
# 2. What is the file extension of the log? (e.g. .log, .txt, .csv, etc.)
# 3. Are the logs in a single log group or multiple log groups?
# 4. What is the timestamp format?
# 5. What is the log level?
# 6. What is the message?
# 7. Where to read the keywords from? (log message or log level)
# 8. Case sensitive?
# 9. How to handle invalid query? (e.g. invalid component name, invalid time range)


# Implmentation:
from datetime import datetime
from typing import List, Dict
import boto3
from botocore.exceptions import ClientError

class LogAnalyzer:
    def __init__(self, cloudwatch_client=None):
        self.client = cloudwatch_client or boto3.client('logs')

    def analyze_log(self, component_name: str, start_time: datetime, end_time: datetime, keywords: List[str]) -> Dict[str, int]:
        """
        Analyze logs for a specific component within a given time range and count occurrences of specified keywords.
        """

        # TO-DO: query validation function
        self._validate_query(component_name, start_time, end_time, keywords)

        # Output
        result = {keyword: 0 for keyword in keywords}

        # Query CloudWatch Logs
        try:
            paginator = self.client.get_paginator('filter_log_events')

            for page in paginator.paginate(
                logGroupName=f"/aws/{component_name}",
                startTime=int(start_time.timestamp() * 1000),
                endTime=int(end_time.timestamp() * 1000)
            ):
                # Process each log event
                for event in page['events']:
                    message = event['message']
                    # Count keyword occurrences
                    for keyword in keywords:
                        result[keyword] += message.count(keyword)
                    
            return result
        
        except ClientError as e:
            raise LogAnalyzerError(f"Error querying CloudWatch Logs: {e}")
                
    def _validate_query(self, component_name: str, start_time: datetime, end_time: datetime, keywords: List[str]):
        pass
                












