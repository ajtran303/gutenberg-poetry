# Gutenberg Poetry

3 million lines of poetry from Project Gutenberg

## About

I wrote a script to scrape the text from [Allison Parrish's Gutenberg Poetry Corpus](https://github.com/aparrish/gutenberg-poetry-corpus) so that I could run it through [Max Woolf's gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) on a copy of his Google Colaboratory notebook.

The problem I had was that the original corpus is in a newline-delimited json format and I wanted a giant textfile. So with some string and json manipulation and file input/output in Python, I got it!

I'm fine-tuning the GPT-2 model for 2000 steps and will upload my training sample outputs when completed. After that, I'll make a link to the checkpoint from my Google Drive.

TODO: Make this readme better
