# Instructions for Dataset Usage

## Overview

The dataset used for our experiments is based on the **VisDrone2019 Train Detection Dataset**, which is publicly available. We utilized a **15% subset** of this dataset (970 images) to evaluate and demonstrate the effectiveness of our algorithm at the inference level.

You can access the data in two ways:

---

### 1. Direct Download of Our Pre-Processed 15% Subset

We have pre-selected and organized a 15% subset of the **VisDrone2019 Train Detection Dataset** for immediate use. You can download this subset (images and annotations) directly from the link below:

[Download 15% Subset - Google Drive](https://drive.google.com/drive/folders/12rsLCoPL_7w_oGKurWoDJ8gH1yQ77KJh?usp=drive_link)

---

### 2. Generate a 15% Subset from the Official Dataset

If you prefer to work with the full dataset from the official VisDrone website, you can generate a 15% subset using our provided script `generate15%subset.py`. The script ensures all images and annotations remain correctly aligned.

- **Download the full dataset**:  
  [VisDrone2019 Train Dataset (1.44 GB) - Google Drive](https://drive.google.com/file/d/1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn/view)

- After downloading, run our `generate15%subset.py` script to create a subset with the following structure:
  - Images: `images/`
  - Annotations: `annotations/`

---

### Usage Notes

- After obtaining the dataset (either our subset or the generated subset), provide the paths to the `images` and `annotations` folders in your experiments.  
- Ensure all experimental settings align with the structure provided in our scripts for consistency.

For further assistance, feel free to contact the repository author.
