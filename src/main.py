import requests

class Bypass:
    def __init__(self, token, user_id):
        self.channel_id = None
        self.user_id = user_id
        self.api_url = 'https://discord.com/api/v8/' # Not tested on newer apis
        self.headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }

    def send_message_bypass(self):
        """Creates a DM channel with the specified user."""
        response = requests.post(
            f'{self.api_url}users/@me/channels',
            json={'recipients': [self.user_id]},
            headers=self.headers
        )

        if response.status_code == 200:
            print('Successfully created the channel.')
            self.channel_id = response.json().get('id')
        else:
            print('Failed to create the channel:', response.status_code, response.json())
            exit(1)

    def send_message(self, message):
        """Sends a message to the created DM channel."""
        if not self.channel_id:
            print('Channel ID not set. Cannot send message.')
            return

        response = requests.post(
            f'{self.api_url}channels/{self.channel_id}/messages',
            json={'content': message},
            headers=self.headers
        )

        if response.status_code == 200:
            print('Successfully sent the message.')
        else:
            print('Failed to send the message:', response.status_code, response.json())

    def send_message(self):
        """send_messages the interactive messaging process."""
        while True:
            try:
                message = input('[Message To Send] -> ')
                self.send_message(message)
            except KeyboardInterrupt:
                exit(0)

if __name__ == '__main__':
    token = input('Token: ').strip()
    user_id = input('Target User ID: ').strip()

    bypass = Bypass(token, user_id)
    bypass.send_message_bypass()
    bypass.send_message()
