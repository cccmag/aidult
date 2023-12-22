# 用 Python 呼叫 ChatGPT API

要用 Python 呼叫 ChatGPT 的 API，你需要先上 openai 網站申請一個帳號，然後取得一組通關金鑰 api_key。

在程式呼叫時，我們通常會把 api_key 設在《環境變數》裏，這樣就不怕程式公開時被別人看到你的 api_key ，讓你的荷包失血了。

OpenAI 的 api 使用，前三個月是免費的，不過如果你已經使用 ChatGPT 一陣子了，那麼免費期間很可能已經過了，這時就要註冊信用卡付費使用了。

您可以到下列網址去註冊申請

* https://openai.com/blog/openai-api


接著我們就能寫程式呼叫 ChatGPT 了，以下是一個簡易範例

```py
from openai import OpenAI
import sys

ai = OpenAI(
    # api_key=os.environ.get("OPENAI_API_KEY"),
)

def chat(question):
    try:
        response = ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"使用繁體中文，以台灣人的角色回答"},
                {"role": "user", "content": f"{question}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as error:
        return "Error: openai chat api fail!"

print('問題:', sys.argv[1])
print(chat(sys.argv[1]))
```

執行結果

```
$ python chatgpt1.py "請問如何用 python 做符號微分與積分?"

問題: 請問如何用 python 做符號微分與積分?

    在Python中，您可以使用不同的函式庫來執行符號微分和積分的計算。以下是使用SymPy函式庫來進行符號微分和積分的示例：

    1. 符號微分：

    首先，您需要安裝SymPy函式庫。您可以使用以下程式碼安裝它：

    ```
    pip install sympy
    ```

    接著，下面的程式碼示範了如何使用SymPy來進行符號微分：

    ```python
    import sympy as sp

    # 定義符號變數
    x = sp.symbols('x')

    # 定義函數
    f = x**2 + 2*x + 1

    # 進行微分
    df = sp.diff(f, x)

    print(df)
    ```

    輸出結果會是：`2*x + 2`

    2. 符號積分：

    與符號微分類似，您可以使用SymPy來進行符號積分。以下是示例程式碼：

    ```python
    import sympy as sp

    # 定義符號變數
    x = sp.symbols('x')

    # 定義函數
    f = x**2 + 2*x + 1

    # 進行積分
    integral = sp.integrate(f, x)

    print(integral)
    ```

    輸出結果會是：`x**3/3 + x**2 + x`

    這些是使用SymPy函式庫在Python中執行符號微分和積分的基本示例。您可以根據您的需求進一步探索SymPy的功能和選項。
```

很厲害吧！


由於 ChatGPT API 的函式庫已經有更新過了，如果你上網路尋找 openai api 的用法，可能會看到一些舊的用法，但是那些用法已經過時了，上面的程式是我們更新過的結果，在 2023/12/23 的時候是可以用的。

現在、您也學會如何寫 AI 大型語言模型的程式了吧！
