from llama_cpp import Llama


def tokenize(llama, prompt):
    return llama.tokenize(bytes(prompt, "utf-8"))

def count_tokens(llama,prompt):
    return len(tokenize(llama,prompt)) + 5

def clip_history(llama, prompt, history, n_ctx, max_tokens):
    prompt_len = count_tokens(llama, prompt)
    history_len = sum([count_tokens(llama, x["content"]) for x in history])
    input_len = prompt_len + history_len
    print(input_len)
    while input_len >= n_ctx-max_tokens:
        print("Clipping")
        history.pop(1)
        history_len = sum([count_tokens(llama, x["content"]) for x in history])
        input_len = history_len + prompt_len
        print(input_len)
    return history
