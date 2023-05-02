# GPT Turning

![Official Documentation](https://platform.openai.com/docs/guides/fine-tuning)

Installation

```sh
pip install --upgrade openai
```

OpenAI API Key

```sh
export OPENAI_API_KEY="<OPENAI_API_KEY>"
```

Preparing training data - nmust be in JSONL format
Check prompt_pair.py for more details

```sh
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
...
```

CLI data preparation

```sh  
openai tools fine_tunes.prepare_data -f cli_ready.json
```

Uploading cli ready json to OPENAI
```sh
openai api files.create -f prompt_completion_pairs_prepared_train.jsonl -p fine-tune
openai api files.create -f prompt_completion_pairs_prepared_valid.jsonl -p fine-tune

openai api fine_tunes.create -t prompt_completion_pairs_prepared_train.json -v prompt_completion_pairs_prepared_valid.jsonl -m davinci
```

Create a fine-tuning run

```sh
gpt_tuning % openai api fine_tunes.create -t cli_ready_prepared_train.jsonl -v cli_ready_prepared_valid.jsonl -m davinci

openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID> // to follow the progress
```

Now we just wait for the fine-tuning to finish. This can take a while depending on the size of the dataset and the model you chose.
![image](https://user-images.githubusercontent.com/48280799/235599700-43be23c1-e5fb-4d89-9793-2d1e1022a677.png)
