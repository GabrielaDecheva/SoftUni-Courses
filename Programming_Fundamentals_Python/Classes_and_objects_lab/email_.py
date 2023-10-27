class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


info = input()
final_emails = []
while info != 'Stop':
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)
    final_emails.append(email_info)
    info = input()
    
indexes = [int(i) for i in input().split(', ')]
for i in indexes:
    final_emails[i].send()

for email in final_emails:
    print(email.get_info())
