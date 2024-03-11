# PDF compress and ocr
----

# Docker Build
```bash
$ sudo docker build -t pdfcompocr:0.0.1 .
```
app directory is needed.
app directory include pdfcompocr.py.

# Usage
on bash
```bash
$ sudo docker run -it --rm --name pdfcompocr -v ${pwd}app/:/app pdfcompocr:0.0.1 ./pdfcompocr.py --compress --ocr pdfname
```

on zsh
```zsh
$ sudo docker run -it --rm --name pdfcompocr -v ${PWD}/app/:/app pdfcompocr:0.0.1 ./pdfcompocr.py --compress --ocr pdfname
```