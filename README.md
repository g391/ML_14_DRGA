# ML_14_DRGA
Đồ án môn học máy nâng cao. Chạy lại code DRGA


## Cài đặt thực nghiệm
### Download model glove
link: https://nlp.stanford.edu/data/glove.6B.zip

Tạo thư mục WordVector và Extract zip file glove.6B.zip trong đo

Cấu trúc thư mục 

```
.
├── code
│   ├── engines.py
│   └── helpers.py
|   └── main.py
|   
├── TrainData
|   └── SUBJ   
└── WordVector
│   ├── glove.6B.50d.txt
│   └── glove.6B.100d.txt
|   └── glove.6B.200d.txt
|   └── glove.6B.300d.txt
└── dockerfile
```

### Chạy chương trình thông qua docker (https://docs.docker.com/engine/install/) 

- Bước 1: Build ra image 
```
 docker build -t drga .
```
- Bước 2: Run container và quan sát log huấn luyện.
```
 docker run drga
```