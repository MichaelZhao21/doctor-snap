#Created by MediaPipe
#Modified by Augmented Startups 2021
#Pose-Estimation in 5 Minutes
#Watch 5 Minute Tutorial at www.augmentedstartups.info/YouTube
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
import time

# For static images:
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=6,
    min_detection_confidence=0.5) as hands:
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.imread('hand.jpg')  #Insert your Image Here
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.multi_hand_landmarks:
        print("Continue")

    # Print handedness and draw hand landmarks on the image.
    h, w, c = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
        x_max = 0
        y_max = 0
        x_min = w
        y_min = h
        for lm in hand_landmarks.landmark:
            x, y = int(lm.x * w), int(lm.y * h)
            if x > x_max:
                x_max = x + 20
            if x < x_min:
                x_min = x - 20
            if y > y_max:
                y_max = y + 20
            if y < y_min:
                y_min = y - 20
        if(x_max - x_min) > (y_max - y_min):
            c = (((x_max - x_min) - (y_max - y_min))) / 2
            y_max += c
            y_min -= c
        else:
            c = (((y_max - y_min) - (x_max - x_min))) / 2
            x_max += c
            x_min -= c
    print(x_max)
    print(x_min)
    print(y_max)
    print(y_min)
    cv2.imwrite('hands.png', annotated_image)

