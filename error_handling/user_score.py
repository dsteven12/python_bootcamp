class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0
    
    def __repr__(self):
        return f'<self {self.name}>'

def email_engaged_user(self):
    try:
        self.score = perform_calculation(self.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
    else:
        if self.score > 500:
            send_engagement_notification(self)

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(self):
    print(f'Notification sent to {self}.')

my_user = User('Rolf', {'clicks': 61, 'hits': 100})
email_engaged_user(my_user)