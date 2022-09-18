import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

handsList = []

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    max_num_hands=10,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True

    h, w, c = image.shape

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
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
        coordinates = (x_min, y_min, x_max, y_max)
        handsList.append(coordinates)
        cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
        #if (glove):
          #cv2.putText(image, "glove",(x_max, y_min - 10), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 200), 2)
        #else:
          #cv2.putText(image, "no glove",(x_max, y_min - 10), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 200), 2)
    
    # Flip the image horizontally for a selfie-view display.
    print(handsList)
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()