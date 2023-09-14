import g4f


while True:
    ask = input("Ask AI >")

    response = g4f.ChatCompletion.create(
        messages=[{"role": "user", "content": ask}],
        model="gpt-4",
        provider=g4f.Provider.Bing,
        stream=True,
    )

    print(response)
