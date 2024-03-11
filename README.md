# PDF compress and ocr
----

# Docker Build
```bash
$ sudo docker build -t pdfcompocr:0.0.1 .
```

# Usage
```bash
$ sudo docker run -it --rm --name pdfcompocr -v ${pwd}app/:/app pdfcompocr:0.0.1 ./pdfcompocr.py --compress --ocr pdfname
```