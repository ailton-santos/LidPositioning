# Bottle Cap Positioning System (Computer Vision)
By Ailton Dos Santos

## Overview
This project is a Computer Vision application developed to detect, identify, and determine the precise positioning of bottle caps in static images.

Using image processing algorithms, the system isolates the objects of interest from the background, filters noise, and calculates the geometric center of each cap. This type of logic is foundational for industrial automation tasks, such as quality control and robotic picking systems.

## Technologies Used
* **Python 3**
* **OpenCV (cv2):** Used for all image processing tasks (filtering, edge detection, drawing).
* **NumPy:** Used for matrix operations and array handling.

## How It Works
The detection pipeline follows these steps:

1.  **Preprocessing:** The image is converted to grayscale and a **Gaussian Blur** is applied to reduce high-frequency noise.
2.  **Edge Detection:** The **Canny** algorithm is used to identify the structural edges of the objects.
3.  **Contour Analysis:** The system finds contours and filters them based on area size (ignoring objects that are too small or too large) to isolate only the bottle caps.
4.  **Localization:**
    * **Bounding Box:** A rectangle is drawn around the detected object.
    * **Centroid Calculation:** The exact center is calculated, and a circle is drawn to visualize the positioning coordinate.

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/ailton-santos/LidPositioning.git](https://github.com/ailton-santos/LidPositioning.git)
    cd LidPositioning
    ```

2.  Install the required dependencies:
    ```bash
    pip install opencv-python numpy
    ```

## Usage

1.  Ensure you have a reference image (e.g., `reference.jpg`) available.
2.  Open the script `Lid_Positioning.py` and update the image path if necessary:
    ```python
    # Example update inside the script:
    imagem = cv2.imread('path/to/your/reference.jpg')
    ```
3.  Run the script:
    ```bash
    python Lid_Positioning.py
    ```
4.  A window will open displaying the detected caps with green bounding boxes and red center indicators.

## Potential Applications
* Industrial Quality Assurance (checking if caps are present).
* Robotic Arm Guidance (providing x,y coordinates for grasping).
* Inventory Counting.
