import g4f
import pprint

prompt: list[dict[str, str]] = []

AVAILBLE_PROVIDERS = [
    # model="gpt-3.5-turbo",
    g4f.Provider.ChatgptAi,
    g4f.Provider.DeepAi,

    # model="gpt-4",
    g4f.Provider.Aivvm,
]

while True:
    ask = input("Ask AI > ")

    prompt.append({"role": "user", "content": ask})

    response = g4f.ChatCompletion.create(
        messages=prompt,
        model="gpt-4",
        provider=g4f.Provider.Aivvm,
        stream=False,
    )

    ans = ""

    for i in response:
        if i == "":
            ans += "\n"
        else:
            ans += i

    prompt.append({"role": "assistant", "content": ans})

    pprint.pprint(prompt)

    print()

    print(ans)
