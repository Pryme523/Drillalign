

# Drillalign

### Description

DrillAlign is a Python-based tool designed to help engineers and drilling professionals calculate the change in drilling angles based on a given depth, offset, and designed angle. The tool computes the change in angle in degrees and estimates the expected drilling angle needed to achieve the desired alignment. 


### Features

- Calculates the angle change due to offset and depth using trigonometric functions.
- Estimates the expected drilling angle based on the designed angle and the calculated offset.
- Easy-to-use command-line interface for quick inputs and results.

---

### Installation

To run this project, you need to have Python installed on your machine. Follow these steps to set up and run the project:

1. Clone the repository or download the script:
    ```bash
    git clone https://github.com/Pryme523/Drillalign
    
    ```

2. Make sure you have Python 3 installed on your system. You can check by running:
    ```bash
    python3 --version
    ```

3. Install any necessary dependencies (although this project currently uses only standard Python libraries):
    ```bash
    pip install -r requirements.txt
    ```

---

### Usage

To run the program, simply execute the script in the terminal or command line:
```bash
python3 drillalign.py
```

The program will prompt you for the following inputs:
- Depth (in meters)
- Offset (in meters)
- Designed angle (in degrees)

Once you enter the required values, the program will calculate:
- The change in angle based on the provided depth and offset.
- The expected drilling angle to achieve the design specifications.

#### Example

$ python3 drill_align.py

Enter the depth (in meters): 100
Enter the offset (in meters): 10
Enter the designed angle (in degrees): 30

The change in angle for a depth of 100m and offset of 10m is: 5.71 degrees
The expected drilling angle to achieve the design is: 35.71 degrees
```

---

### How It Works

- The tool uses basic trigonometric calculations, where the angle change is calculated using the `atan()` function from the `math` library:
    \[
    \text{angle change} = \arctan\left(\frac{\text{offset}}{\text{depth}}\right)
    \]
- The result is converted from radians to degrees using the `degrees()` function.
- The expected drilling angle is the sum of the designed angle and the calculated angle change.

---


