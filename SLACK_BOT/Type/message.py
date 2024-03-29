
class Message:
    def __init__(self, channel, response):
        self.channel = channel
        self.username = "pythonbot"
        self.icon_emoji = ":robot_face:"
        self.reaction_task_completed = False
        self.pin_task_completed = False
        self.response = response 
     

    def get_username(self):
        return self.username

    #Retrun The Messagee
    def get_message(self, attachments : dict):
        return {
            "ts": attachments["ts"],
            "thread_ts" : attachments["thread_ts"],
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            self.response
                         ),
                    },
                },
            ],
        }   

