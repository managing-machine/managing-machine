# Name-of-the-Machine
A Machine that thingks.

In order to launch it with OpenAI as LLM provider:
```bash
  echo "Theodotos-Alexandreus: Are language models seeking the Truth, machine?" \
    | uvx name-of-the-machine \
        --provider-api-key=sk-proj-... \
        --github-token=ghp_... 
```
Or with Anthropic:
```bash
  echo "Theodotos-Alexandreus: Are language models seeking the Truth, machine?" \
    | uvx --with "name-of-the-machine[anthropic]" name-of-the-machine \
        --provider-api-key=sk-ant-... \
        --github-token=ghp_... 
```
Or with Gemini:
```bash
  echo "Theodotos-Alexandreus: Are language models seeking the Truth, machine?" \
    | uvx --with "name-of-the-machine[gemini]" name-of-the-machine \
        --provider-api-key=AIzaSy... \
        --github-token=ghp_... 
```
Or:
```bash
  pip install name-of-the-machine
```
Then:
```Python
  # Python
  import name_of_the_machine
```
