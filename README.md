# PCA-DrowsinessDetection
Thesis - BCS32 (Villanueva, Granadoz, Flores)


Phase 1:
{

Name_Find.py 
    Passive file (Functions) : 
        Grab Name of User and Generate Data According to the user
        Generate ID
        Display ID in FaceDetection Window (To be Executed in Testing Phase)
        
       
Face_Training.py
    Will Call Name_Find.py for Identification
    Capture Face in Grayscale 
    Extract Faces Using OpenCV
    Align Faces through detection with
              Dlib using 68_Landmarks.dat
        For Loop for Imutils Face Alignment
        
}


Phase 2(Under Development):
{

*****Generate Trained Data Sets from Raw Data Sets in Phase 1********
PCA For the Faces/Eyes
  Extract Features
    Generate Data (Blink/Not Blinking), (MicroSleep Patterns)
}

