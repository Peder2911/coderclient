# coderclient

This is a POC for an information extraction tool for text documents. The tool
frameworks the information extraction process, with a codebook interface that
makes the information extraction process as easy as possible for researchers.

## Requirements

* [llama.ccp](https://github.com/ggerganov/llama.cpp)
* [Mistral Instruct 7B](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

## Usage

Compile and run `./server` from llama.cpp and run the tool with `rye run coderclient`.
To code the example document, run:
```
cat ./examples/doc | rye run coderclient --codebook ./examples/codebook.yaml code
```
