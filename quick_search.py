import subprocess
import openai
from pynput import keyboard

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

def perform_action(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    generated_text = response.choices[0].text.strip()

    print("Generated Response:", generated_text)

# Function to handle the hotkey press event
def on_hotkey_press():
    process = subprocess.Popen(['xclip', '-out', '-selection', 'clipboard'], stdout=subprocess.PIPE)
    highlighted_text, _ = process.communicate()

    highlighted_text = highlighted_text.decode().rstrip('\n')

    perform_action(highlighted_text)

hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+h'), on_hotkey_press)

with keyboard.Listener(on_press=hotkey.press, on_release=hotkey.release) as listener:
    listener.join()

