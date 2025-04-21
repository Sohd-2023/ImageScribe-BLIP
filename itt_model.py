---

## 📄 `imagescribe.py` (Main Script)

```python
# imagescribe.py

import argparse
import requests
import base64

API_URL = "https://api.deepinfra.com/v1/inference"
HEADERS = {"Authorization": "Bearer <YOUR_API_KEY>"}  # Replace with your DeepInfra key
MODEL_ID = "Salesforce/blip-image-captioning-large"

def caption_image(image_path: str):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")

    payload = {
        "model": MODEL_ID,
        "inputs": {"image": encoded}
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        result = response.json()
        print("Caption:", result.get("caption", "No caption returned"))
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a caption for an image using BLIP.")
    parser.add_argument("--image", type=str, required=True, help="Path to the image file")
    args = parser.parse_args()
    caption_image(args.image)

