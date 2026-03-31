import cv2
import os
import sys
import argparse

def blur_faces_batch(blur_factor):
    # Load Haar Cascade face detector
    cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    if face_cascade.empty():
        print("Error: Could not load the face cascade classifier.")
        sys.exit(1)

    input_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(input_dir, "Output")
    
    # Creates the Output folder automatically if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Scanning for images in: {input_dir}")
    print(f"Outputting censored images to: {output_dir}\n")

    valid_extensions = ('.jpg', '.jpeg', '.png')
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(valid_extensions)]

    if not image_files:
        print("No image files (.jpg, .jpeg, .png) found in the script's directory.")
        return

    print(f"Found {len(image_files)} image(s). Starting batch processing...\n")

    for img_name in image_files:
        input_path = os.path.join(input_dir, img_name)
        output_path = os.path.join(output_dir, img_name)
        
        print(f"Processing: {img_name}")
        img = cv2.imread(input_path)
        
        if img is None:
            print(f" -> Failed to read {img_name}. Skipping.")
            continue

        # Grayscale is required for detection math
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) == 0:
            print(" -> No faces detected. Saving original to Output folder.")
        else:
            print(f" -> Detected {len(faces)} face(s). Applying blur...")
            for (x, y, w, h) in faces:
                roi = img[y:y+h, x:x+w]
                # Ensure kernel size is odd
                kernel_size = (w // blur_factor) | 1 
                blurred_roi = cv2.GaussianBlur(roi, (kernel_size, kernel_size), 0)
                img[y:y+h, x:x+w] = blurred_roi

        cv2.imwrite(output_path, img)
        print(f" -> Saved to Output/{img_name}\n")
        
    print("Batch processing complete! Pass -b <value> to adjust blur(default is 4) or --help to see options.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch CLI Tool to censor faces in all images within the script directory.")
    parser.add_argument("-b", "--blur", type=int, default=4, help="Blur intensity (lower is blurrier, default 4).")
    args = parser.parse_args()
    
    blur_faces_batch(args.blur)