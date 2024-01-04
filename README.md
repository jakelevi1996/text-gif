# text-gif

Make GIF of given text file, letter by letter or word by word.

The text files used in these examples are taken from https://en.wikipedia.org/wiki/Reading_comprehension

## Example usage

Display command line options:

```
python make_text_gif.py -h
```

Make GIFs containing words from text file:

```
python make_text_gif.py --input_filename examples/text/example1.txt --output_dir examples/gifs --output_name example1
python make_text_gif.py --input_filename examples/text/example2.txt --output_dir examples/gifs --output_name example2
```

Make GIFs containing letters from text file:

```
python make_text_gif.py --input_filename examples/text/example1.txt --output_dir examples/gifs --output_name example1_by_letter --by_letter
python make_text_gif.py --input_filename examples/text/example2.txt --output_dir examples/gifs --output_name example2_by_letter --by_letter
```

Make GIFs with shorter frame durations:

```
python make_text_gif.py --input_filename examples/text/example3.txt --output_dir examples/gifs --frame_duration_ms 250 --output_name example3
python make_text_gif.py --input_filename examples/text/example3.txt --output_dir examples/gifs --frame_duration_ms 250 --output_name example3_by_letter --by_letter
```

Make GIFs containing words from `STDIN`:

```
python make_text_gif.py --output_dir examples/gifs --output_name stdin
python make_text_gif.py --output_dir examples/gifs --output_name stdin_by_letter --by_letter
This is an example calling of the `make_text_gif.py` script
```

## Example outputs

First example text file, by word and by letter:

![](examples/gifs/example1.gif)

![](examples/gifs/example1_by_letter.gif)

Second example text file, by word and by letter:

![](examples/gifs/example2.gif)

![](examples/gifs/example2_by_letter.gif)

Third example text file, by word and by letter, with faster frame duration:

![](examples/gifs/example3.gif)

![](examples/gifs/example3_by_letter.gif)

`STDIN` example, by word and by letter:

![](examples/gifs/stdin.gif)

![](examples/gifs/stdin_by_letter.gif)
