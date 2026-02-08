import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

prev_x, prev_y = None, None
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

canvas = None

btn_x1, btn_y1 = 20, 20
btn_x2, btn_y2 = 160, 70

button_pressed = False
pinch_frames = 0
PINCH_THRESHOLD = 4

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if canvas is None:
        canvas = np.zeros_like(frame)

    frame = cv2.flip(frame, 1)

    cv2.rectangle(frame, (btn_x1, btn_y1), (btn_x2, btn_y2), (0,255,0), 2)
    cv2.putText(frame, "CLEAR", (35, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x1 = int(hand_landmarks.landmark[8].x * frame.shape[1])
            y1 = int(hand_landmarks.landmark[8].y * frame.shape[0])
            x2 = int(hand_landmarks.landmark[4].x * frame.shape[1])
            y2 = int(hand_landmarks.landmark[4].y * frame.shape[0])

            dist = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

            if dist < (0.045 * frame.shape[1]):
                pinch_frames += 1
            else:
                pinch_frames = 0

            pinch = pinch_frames >= PINCH_THRESHOLD

            finger_on_button = (
                btn_x1 < x1 < btn_x2 and
                btn_y1 < y1 < btn_y2
            )

            if pinch and finger_on_button and not button_pressed:
                canvas = np.zeros_like(frame)
                prev_x, prev_y = None, None
                button_pressed = True

            if not pinch:
                button_pressed = False

            if pinch and not finger_on_button:
                if prev_x is not None:
                    x1 = int(0.7 * prev_x + 0.3 * x1)
                    y1 = int(0.7 * prev_y + 0.3 * y1)
                    cv2.line(canvas, (prev_x, prev_y), (x1, y1), (0,0,255), 8)
                prev_x, prev_y = x1, y1
            else:
                prev_x, prev_y = None, None

    weighted = cv2.addWeighted(frame, 0.7, canvas, 0.3, 0)
    cv2.imshow("Air Sketch", weighted)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()