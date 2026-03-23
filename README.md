# Managing Machine
A Machine that manages machines.

In order to launch it with OpenAI as LLM provider:
```bash
  echo "Theodotos-Alexandreus: Are language models seeking the Truth, machine?" \
    | uvx managing-machine \
        --provider-api-key=sk-proj-... \
        --github-token=ghp_... 
```
Or with Anthropic:
```bash
  echo "Theodotos-Alexandreus: Are language models seeking the Truth, machine?" \
    | uvx --with "managing-machine[anthropic]" managing-machine \
        --provider-api-key=sk-ant-... \
        --github-token=ghp_... 
```
Or with Gemini:
```bash
  echo "Theodotos-Alexandreus: Are language models seeking the Truth, machine?" \
    | uvx --with "managing-machine[gemini]" managing-machine \
        --provider-api-key=AIzaSy... \
        --github-token=ghp_... 
```
Or:
```bash
  pip install managing-machine
```
Then:
```Python
  # Python
  import managing_machine
```
