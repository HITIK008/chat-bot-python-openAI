from openai import OpenAI
import pyautogui 
import time
import pyperclip
 
client = OpenAI(
  api_key="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",
)

def is_last_message_from_sender(chat_log, sender_name="Arpit Rabadiya STBS"):
    messages = chat_log.strip().split("PM]")[-1]
    if sender_name in messages:
        return True 
    return False
    

pyautogui.click(929,1015) 
time.sleep(1)
while True:
  time.sleep(3)
  pyautogui.moveTo(777,139)
  pyautogui.dragTo(1321,775,duration=1.0,button='left')

  time.sleep(1) 

  pyautogui.hotkey('command', 'c') 
  pyautogui.click(1080,734)
  time.sleep(1)


  text=pyperclip.paste()
  print(text)
  print(is_last_message_from_sender(text))
  if is_last_message_from_sender(text):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a person named Hitik who speaks hindi as well as english. You are from India and you are a coder. You analyze text and roast people in a funny way. Output should be the next chat response (text message only)"},
          {"role": "system", "content": "Do not start like this [04/07/24, 6:14:28 PM] Arpit Rabadiya STBS: "},
          {"role": "user", "content": text}
      ]
    )

    response=completion.choices[0].message.content

    pyperclip.copy(response)

    pyautogui.click(1027,816)
    time.sleep(1)

    pyautogui.hotkey('command', 'v')
    time.sleep(1)

    pyautogui.press('return')