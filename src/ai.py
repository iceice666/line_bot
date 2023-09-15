import g4f

AVAILBLE_PROVIDERS = [
    # model="gpt-3.5-turbo",
    g4f.Provider.ChatgptAi,
    g4f.Provider.DeepAi,
    # model="gpt-4",
    g4f.Provider.Aivvm,
]


class AI:
    prompt: list[dict[str, str]] = []
    def reset(self) -> list:
        old_prompt = self.prompt
        self.prompt: list[dict[str, str]] = []
        return old_prompt

    def ask(self, msg: str) -> str:
        self.prompt.append({"role": "user", "content": msg})

        response = g4f.ChatCompletion.create(
            messages=self.prompt,
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

        self.prompt.append({"role": "assistant", "content": ans})

        return ans
