from flask import Flask
import g4f

AVAILBLE_PROVIDERS = [
    # model="gpt-3.5-turbo",
    g4f.Provider.ChatgptAi,
    g4f.Provider.DeepAi,
    # model="gpt-4",
    g4f.Provider.Aivvm,
]

BEFORE_ASKING = """
接下來，你將會和一位疑似精神病患對話
它目前的狀態有可能不穩定，請給予你能力範圍內的協助
如果你發覺情況超出你的能力範圍，請在回答的開頭加上
`###WARNING###`

收到此回覆後請不要回答內容
"""
import logging

logger = logging.Logger("conversation")

import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_handler = logging.FileHandler(f"logs/{today}.log")

logger.addHandler(file_handler)


app = Flask("LineAIBot")


class AI:
    prompt: list[dict[str, str]] = []

    def reset(self) -> list:
        old_prompt = self.prompt
        self.prompt = []
        return old_prompt

    def ask(self, msg: str) -> str:
        self.prompt.append({"role": "user", "content": msg})

        logger.info(f"User asked: {msg}")

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

        logger.info(f"AI responded: {ans}")

        return ans

    def init(self):
        self.prompt.append({"role": "user", "content": BEFORE_ASKING})
        self.prompt.append({"role": "assistant", "content": ""})
