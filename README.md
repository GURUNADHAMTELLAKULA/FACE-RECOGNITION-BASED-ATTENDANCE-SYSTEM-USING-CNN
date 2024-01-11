# FACE-RECOGNITION-BASED-ATTENDANCE-SYSTEM-USING-CNN

How CNN Works for Face Recognition :

When it comes to face recognition using CNNs, certain factors play a crucial role in optimal performance. 
Here are some key points to consider: 
1. **CNN Architecture and Loss Function:** - Choosing the right CNN architecture is essential. Popular choices like ResNet or EfficientNet have proven effective for image recognition. - The loss function is critical for minimizing errors between real and predicted outputs. In face recognition, commonly used loss functions include triplet loss and AM-SoftMax.

2. **Triplet Loss:** - Triplet loss uses three images: an anchor, a positive image for one person, and a negative image for another - The network learns to bring images of the same person closer in the feature space while separating those of different people.

3. . **AM-SoftMax Function:** - AM-SoftMax is an improved version of the basic SoftMax function, incorporating a specific regularization based on an additive margin. - This function enhances class separability, leading to improved accuracy in face recognition systems.

4. **Neural Network Improvement Approaches:** - Several techniques can enhance neural network performance in face recognition systems. - Knowledge distillation involves training a smaller network by having a larger network teach it. The smaller network works faster but provides similar results. - Transfer learning improves accuracy by training the entire network or specific layers on a given dataset. It's useful, instance, in addressing race bias issues in face recognition systems.

5. These strategies, along with the optimization of inference time and the power of the hardware, contribute to the effectiveness of a face recognition system. It's essential to carefully select the CNN architecture, and loss function, and employ advanced techniques for better accuracy and efficiency in recognizing faces.


•	Depth-wise separable convolutions a type of subcaste that helps produce CNNs with smaller parameters compared to regular CNNs. This means lower computational work, making it great for facial recognition on mobile bias. The pivotal thing in deep literacy is the need for an important tackle. When we use Deep Neural Networks for developing face recognition system, the end isn't just to ameliorate delicacy but also to make the system respond briskly.

Capturing-Image: Taking a picture involves using a camera that can capture facial images instantly. This camera could be part of a device like a tablet or smartphone, or it might be a separate unit on its own.

Face Detection: The first important task is Face Detection. This step is all about finding and singling out the areas of faces within pictures or video frames. It's a crucial process because it helps pull out the required information for the next step, which is facial recognition.One widely used and effective method for real-time face detection is through something called Haar cascades. These are sets of trained classifiers that are good at spotting features like edges, corners, and lines that are commonly associated with faces. OpenCV, a computer vision library, provides tools using Haar cascades, making it handy for detecting faces in real-time applications.

Pre-Processing:Before recognizing a face, the image goes through a pre-processing step. These involve cropping and aligning the person's face at the center of the frame. Additionally, to simplify the processing, the image is converted to grayscale. This ensures that the system gets a clear and standardized view of the face, making it easier to analyze and identify unique features.


Face Recognition: Face recognition is a technology that uses computer algorithms to pick out unique facial features from a picture. It then checks these ures using a database of recognized faces to figure out who the person is. When a camera detects a face, a facial recognition algorithm compares that face to all the others in its database to find the best match. Tools like HOG and Dlib come in handy during this process.

Attendance Marking: : For attendance marking, when the system recognizes a student's face, it automatically records the student's details in a . CSV file and marks them as present, streamlining the attendance process
