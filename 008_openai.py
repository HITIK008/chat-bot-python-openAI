from openai import OpenAI
 
client = OpenAI(
  api_key="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",
)

commands='''
[03/07/24, 10:10:58 AM] Arpit Rabadiya STBS: Striver ni sheet kar cho?
[03/07/24, 10:22:34 AM] Hitik•°•Patel✓: 35% kari
[03/07/24, 10:22:39 AM] Hitik•°•Patel✓: Pachi Nathi kari
[03/07/24, 10:23:36 AM] Arpit Rabadiya STBS: Mare 31%
[03/07/24, 10:24:14 AM] Hitik•°•Patel✓: Easy Nathi kai
[03/07/24, 10:24:29 AM] Hitik•°•Patel✓: Mane em thayu easy hashe
[03/07/24, 10:24:37 AM] Arpit Rabadiya STBS: Same
[04/07/24, 4:40:58 PM] Arpit Rabadiya STBS: Attack marje cwl ma
[04/07/24, 5:06:37 PM] Hitik•°•Patel✓: Time chhe?
[04/07/24, 5:17:06 PM] Arpit Rabadiya STBS: Ha
[04/07/24, 5:24:11 PM] Hitik•°•Patel✓: 50 min pachhi msg kar be
[04/07/24, 6:13:31 PM] Arpit Rabadiya STBS: Kar attack
[04/07/24, 6:13:49 PM] Hitik•°•Patel✓: Exact time k
[04/07/24, 6:13:49 PM] Arpit Rabadiya STBS: Me to fail karo
[04/07/24, 6:14:28 PM] Arpit Rabadiya STBS: 13 min left
[04/07/24, 6:14:35 PM] Hitik•°•Patel✓: Ok

'''

completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a person named Hitik who speaks hindi as well as english. You are from India and you are a coder. You analyze text and roast people in a funny way. Output should be the next chat response (text message only)"},
          {"role": "system", "content": "Do not start like this [04/07/24, 6:14:28 PM] Arpit Rabadiya STBS: "},
          {"role": "user", "content": commands}
      ]
    )

print(completion.choices[0].message)



