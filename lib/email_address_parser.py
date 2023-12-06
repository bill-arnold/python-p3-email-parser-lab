# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Use regex to find all email addresses
        emails = re.findall(r'\S+@\S+', self.email_addresses)

        # Remove duplicates and sort alphabetically
        unique_emails = sorted(set(emails))

        return unique_emails
