import streamlit as st
import cv2

st.title("Audio to Sign & Sign to Text System")

# -------- TEXT TO SIGN --------
st.header("Text to Sign Language")

text = st.text_input("Enter text:")

if text:
    if text.lower() == "hello":
        st.image("hello.jpg", caption="HELLO Sign")
    else:
        st.write("Sign not available")

# -------- SIGN TO TEXT --------
st.header("Sign to Text (Demo)")

if st.button("Start Camera"):
    cap = cv2.VideoCapture(0)

    st.write("Press H for HELLO | Q to Quit")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)

        if key == ord('h'):
            st.write("Predicted: HELLO")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()