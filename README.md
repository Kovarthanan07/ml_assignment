# Machine Learning Assignment

This repo is created for the interview purpose. Here pre-trained yolov7-tiny was used for the object detection from [hugging face](https://huggingface.co/kadirnar/yolov7-tiny-v0.1). 

## As a first step 
create a directory in the name of **images** as follows,
``` folder
ml_assignment
----- main.py
----- README.md
----- requirements.txt
----- images

```

## Installation 
To install the packages mentioned in the requirements.txt  
```bash
pip install -r requirements.txt
```

## Execution 
To execute the backend API, run the following command in terminal, 

```bash
uvicorn main:app --reload 
```
