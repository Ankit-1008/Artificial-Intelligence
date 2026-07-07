import cv2
import os

student_name = input("Enter Student Name: ").strip()

if not student_name:
    print("Invalid name!")
    exit()

save_dir = os.path.join("dataset", student_name)
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0
max_images = 20

print("\nPress 's' to save image")
print("Press 'q' to quit\n")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error!")
        break

    cv2.putText(
        frame,
        f"Images: {count}/{max_images}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Register Student", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        img_path = os.path.join(save_dir, f"{count}.jpg")
        cv2.imwrite(img_path, frame)

        count += 1
        print(f"Saved Image {count}")

        if count >= max_images:
            print("Image collection complete!")
            break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()