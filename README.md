# ImageScribe-BLIP

Rationale:

"ImageScribe" evokes the idea of an AI scribe interpreting visual content.

"BLIP" references the model architecture (BLIP) known for captioning.

# Image-to-Text Caption Generator

This model generates descriptive captions for images using the BLIP model (`Salesforce/blip-image-captioning-large`) hosted on DeepInfra.

## 🛠 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```
🚀 Usage

python itt_model.py --image path/to/image.jpg

🔑 Output
Returns a caption like:

"A small dog lying on a couch."

⚙ Configuration
Make sure to replace <YOUR_API_KEY> in the script with your DeepInfra API key.

Model: Salesforce/blip-image-captioning-large is default; can be updated if needed.
