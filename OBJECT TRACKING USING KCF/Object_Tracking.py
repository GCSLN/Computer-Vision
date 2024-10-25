import cv2


#tracker = cv2.legacy.TrackerKCF.create()
tracker = cv2.legacy.TrackerKCF.create()

video = cv2.VideoCapture('street.mp4')
ok, frame = video.read()


bbox = cv2.selectROI(frame)
print(bbox)

# Initialize tracker with the first frame and bounding box
ok = tracker.init(frame, bbox)
print(ok)

while True:
    # Read a new frame
    ok, frame = video.read()
    print(ok)
    if not ok:
        break

    # Update tracker
    ok, bbox = tracker.update(frame)
    print(bbox)
    print(ok)

    # Draw bounding box
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, 'MISSED', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)

    # Display result
    cv2.imshow('Tracking', frame)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
