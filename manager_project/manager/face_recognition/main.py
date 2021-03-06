import face_recognition
import cv2
import numpy as np
from camera import camera

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
def main():
    camera()
    video_capture = cv2.imread("manager/face_recognition/pic_sub/photo.jpg")


    # Load a sample picture and learn how to recognize it.
    matumoto_image = face_recognition.load_image_file("manager/face_recognition/pic_sample/matumoto.jpg")
    matumoto_face_encoding = face_recognition.face_encodings(matumoto_image)[0]

    # Load a second sample picture and learn how to recognize it.
    aiba_image = face_recognition.load_image_file("manager/face_recognition/pic_sample/aiba.jpg")
    aiba_face_encoding = face_recognition.face_encodings(aiba_image)[0]

    # Load a second sample picture and learn how to recognize it.
    oono_image = face_recognition.load_image_file("manager/face_recognition/pic_sample/oono.jpg")
    oono_face_encoding = face_recognition.face_encodings(oono_image)[0]

    # Load a second sample picture and learn how to recognize it.
    nino_image = face_recognition.load_image_file("manager/face_recognition/pic_sample/nino.jpg")
    nino_face_encoding = face_recognition.face_encodings(nino_image)[0]

    # Load a second sample picture and learn how to recognize it.
    sakurai_image = face_recognition.load_image_file("manager/face_recognition/pic_sample/sakurai.jpg")
    sakurai_face_encoding = face_recognition.face_encodings(sakurai_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        matumoto_face_encoding,
        aiba_face_encoding,
        oono_face_encoding,
        nino_face_encoding,
        sakurai_face_encoding
    ]
    known_face_names = [
        "matumoto",
        "aiba",
        "oono",
        "nino",
        "sakurai"
    ]


    frame = video_capture

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame, model="hog") #, model="cnn"???rgb_rame????????????????????????????????????????????????gpu??????????????????????????????????????????gpu?????????????????????model="hog"
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    
    name_array = []

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            name_array.append(name)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

    # write the resulting image
    f = open("manager/face_recognition/name_list/name_list.txt", "w")
    names = ",".join(name_array)
    f.write(names)
    f.close()
    cv2.imwrite('manager/face_recognition/pic_result/num01.jpg', frame)
    cv2.imwrite('manager/static/num01.jpg', frame)


# Hit 'q' on the keyboard to quit!
#if cv2.waitKey(1) & 0xFF == ord('q'):


# Release handle to the webcam
#video_capture.release()
#cv2.destroyAllWindows()