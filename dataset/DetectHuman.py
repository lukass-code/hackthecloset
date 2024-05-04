import cv2
import mediapipe as mp

# Initialize MediaPipe BodyPose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

# Load Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect presence of a head (face) in the image
def detect_head(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return len(faces) > 0

# Load image
image_path = r"C:\Users\roksh\OneDrive\Desktop\GitHub\hackthecloset\dataset\gonna3.jpg"
image = cv2.imread(image_path)

# Process image using MediaPipe
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pose.process(image_rgb)

# Check if the image contains a human based on detected landmarks
contains_human = False
if results.pose_landmarks:
    num_landmarks = len(results.pose_landmarks.landmark)
    if num_landmarks >= 5:  # You can adjust this threshold based on your requirements
        contains_human = True

# Check if the image contains a head (face)
contains_head = detect_head(image)

# Combine results
contains_human = contains_human or contains_head

# Display result
if contains_human:
    print("The image contains a human.")
else:
    print("The image does not contain a human.")

