import cv2
import mediapipe as mp
import pyttsx3
import time

# =========================
# Initialize Text-to-Speech
# =========================
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# =========================
# MediaPipe setup
# =========================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# =========================
# Gesture Recognition Logic
# =========================
def recognize_gesture(landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb (right hand logic)
    fingers.append(1 if landmarks[4].x < landmarks[3].x else 0)

    # Other fingers
    for tip in tips[1:]:
        fingers.append(1 if landmarks[tip].y < landmarks[tip - 2].y else 0)

    if fingers == [1, 1, 1, 1, 1]:
        return "Hi 👋"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up 👍"
    elif fingers == [0, 0, 0, 0, 0]:
        return "Fist ✊"
    elif fingers == [0, 1, 1, 0, 0]:
        return "Peace ✌️"
    else:
        return None

# =========================
# Gesture → Speech Mapping
# =========================
gesture_speech = {
    "Hi 👋": "Hello there",
    "Thumbs Up 👍": "Good job",
    "Fist ✊": "Ready",
    "Peace ✌️": "Peace"
}

last_gesture = None
last_time = 0
cooldown = 1.5  # seconds

# =========================
# Main Loop
# =========================
with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        gesture_text = "Show a gesture..."

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            gesture = recognize_gesture(hand.landmark)

            if gesture:
                gesture_text = gesture
                current_time = time.time()

                if gesture != last_gesture and current_time - last_time > cooldown:
                    last_gesture = gesture
                    last_time = current_time
                    speak(gesture_speech.get(gesture, gesture))

        cv2.putText(
            frame,
            gesture_text,
            (40, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0, 255, 0),
            4
        )

        cv2.imshow("🤖 AI Gesture to Speech", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()