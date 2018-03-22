## README

Throw your files into ./data  
This project should have the following structure
.  
├── data  
│   ├── test  (contains 1.png, 2.png, etc)  
│   └── train  (contains folders for each category)  
└── fastai (symlink to your fastai location)  

Just dump your notebooks in root, following the following convention:

Naming convention is a number (for ordering), the creator's initials, and a short `-` delimited description,  
e.g `1.0-jqp-initial-data-exploration`.

A validation set will be up in a bit, we should all use the same set to properly compare model performance

If not using fastai, include some instructions in a readme somewhere
