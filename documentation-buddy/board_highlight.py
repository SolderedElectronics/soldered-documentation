import os
import uuid
from PIL import Image, ImageEnhance, ImageDraw

def process_image(image_path, x1, y1, x2, y2):
    """
    Highlight a selected area of an image and darken the rest
    
    Args:
        image_path: Path to the image file
        x1, y1: Top-left coordinates of the rectangle
        x2, y2: Bottom-right coordinates of the rectangle
    
    Returns:
        Path to the processed image
    """
    try:
        # Ensure coordinates are in the right order
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        
        # Normalize path with forward slashes
        image_path = image_path.replace('\\', '/')
        
        # Open the image
        img = Image.open(image_path).convert("RGB")
        
        # Load image as array
        img_array = img.copy()
        
        # Darken entire image by 40%
        enhancer = ImageEnhance.Brightness(img)
        darkened_img = enhancer.enhance(0.6)
        
        # Create a new image to work with
        final_img = darkened_img.copy()
        
        # Copy the bright area from original image
        box = (x1, y1, x2, y2)
        region = img.crop(box)
        final_img.paste(region, box)
        
        # Draw the border around the highlighted area
        draw = ImageDraw.Draw(final_img)
        border_color = "#23b9d6"  # Light blue color
        draw.rectangle([x1-2, y1-2, x2+1, y2+1], outline=border_color, width=4)
        
        # Save the processed image
        output_dir = os.path.dirname(image_path)
        filename, ext = os.path.splitext(os.path.basename(image_path))
        
        # Check if it's already a processed image
        if filename.endswith('_highlighted'):
            output_path = image_path
        else:
            # Use forward slashes for consistency
            output_path = output_dir + '/' + f"{filename}_highlighted{ext}"
        
        final_img.save(output_path)
        return output_path
    
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None

def reset_image(original_path):
    """
    Return the original image path
    
    Args:
        original_path: Path to the original image
    
    Returns:
        Path to the original image
    """
    return original_path

def save_temp_image(file_obj):
    """
    Save an uploaded image file to a temporary location
    
    Args:
        file_obj: The uploaded file object
    
    Returns:
        Path to the saved image
    """
    try:
        # Create uploads directory if it doesn't exist
        upload_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Generate a unique filename
        filename = f"{uuid.uuid4().hex}{os.path.splitext(file_obj.filename)[1]}"
        file_path = os.path.join(upload_dir, filename)
        
        # Save the file
        file_obj.save(file_path)
        
        return file_path
    
    except Exception as e:
        print(f"Error saving image: {str(e)}")
        return None