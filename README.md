# GPT Tuning

[Official Documentation](https://platform.openai.com/docs/guides/fine-tuning)

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
For financial and testing purposes, I chose the cheapest model, ada.

![image](https://user-images.githubusercontent.com/48280799/235599700-43be23c1-e5fb-4d89-9793-2d1e1022a677.png)

Once model is complete, we run the program and enter prompt text to generate the completion text.

```sh
import tkinter as tk
import openai
import re

# Replace FINE_TUNED_MODEL with the name of your fine-tuned model
model_name = "FINE_TUNED_MODEL"


def on_submit():
    # Get the prompt from the input field
    original_prompt = input_field.get()
    
    # Modify the prompt to ask for the genre
    prompt = f"Analyze the following text and provide one relevant genre from the list: [thriller, fantasy, science fiction, history, horror, crime, romance, psychology, sports, travel].\n\nText: \"{original_prompt}\"\n\nGenre:"

    # Make the completion request
    completion = openai.Completion.create(model=model_name, prompt=prompt, max_tokens=100, temperature=0.8)

    print("Completion:", completion)

    # Clear the input field
    input_field.delete(0, "end")

    # Get the completion text from the first choice in the choices list
    text = completion.choices[0]["text"].strip()

    # Extract the genre from the text using a regular expression
    genre = re.findall(r'\b(?:thriller|fantasy|science fiction|history|horror|crime|romance|psychology|sports|travel)\b', text)[:2]

    # Join the genres found in the text (if any) and display them in the result text area
    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("end", ', '.join(genre))
    result_text.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("Fine-tuned GPT-3 for Genre Classification")

# Create the input field and submit button
input_field = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=on_submit)

# Create the result text area
result_text = tk.Text(window, state="normal", width=80, height=20)

# Add the input field, submit button, and result text area to the window
input_field.pack()
submit_button.pack()
result_text.pack()

# Run the main loop
window.mainloop()
```

To run the program:

```sh
python3 main.py
```

Results of the program:
![Response](https://user-images.githubusercontent.com/48280799/235793022-72732e5a-187a-4953-9a75-c189e649d52a.png)

## Next Steps:
- [ ] Create a web app to run the program
- [ ] Connect the program to node using flask or express using jsx version of the program
- [ ] More fine tuning to improve accuracy
- [ ] More testing by inputting more text to see if the program can properly detect the genre
