import os
import sys
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
import io
from contextlib import redirect_stdout

# Import functionality modules
from create_files import create_files_process
from board_highlight import process_image, reset_image, save_temp_image

app = Flask(__name__)
# For local development use only - in production, use environment variable instead
# You can set the FLASK_SECRET_KEY environment variable to override this default
app.secret_key = os.environ.get('FLASK_SECRET_KEY', os.urandom(24).hex())

# Create the uploads directory if it doesn't exist
uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/create-files', methods=['GET'])
def create_files():
    return render_template('create_files.html', active_page='create_files')

@app.route('/create-files/submit', methods=['POST'])
def create_files_submit():
    keyword = request.form.get('keyword', '').strip().lower()
    category = request.form.get('category', '')
    
    if not keyword:
        return render_template('create_files.html', active_page='create_files', 
                              message="Please enter a keyword", success=False)
    
    if category not in ['sensors', 'actuators', 'communication']:
        return render_template('create_files.html', active_page='create_files', 
                              message="Invalid category selected", success=False)
    
    # Capture stdout to get the log output
    log_output = io.StringIO()
    success = False
    
    with redirect_stdout(log_output):
        # Navigate to the parent directory of the current Python file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        
        # Path to the soldered-documentation directory
        doc_dir = os.path.join(parent_dir, 'soldered-documentation')
        
        if not os.path.exists(doc_dir):
            print(f"Error: soldered-documentation directory not found at {doc_dir}")
            return render_template('create_files.html', active_page='create_files',
                                  message="soldered-documentation directory not found", 
                                  success=False, log_output=log_output.getvalue())
        
        # Process file creation
        success = create_files_process(keyword, category, doc_dir)
    
    return render_template('create_files.html', active_page='create_files',
                          message="Files created successfully!" if success else "Error creating files",
                          success=success, log_output=log_output.getvalue())

@app.route('/board-highlight')
def board_highlight():
    return render_template('board_highlight.html', active_page='board_highlight')

@app.route('/board-highlight/upload', methods=['POST'])
def board_highlight_upload():
    if 'boardImage' not in request.files:
        return render_template('board_highlight.html', active_page='board_highlight',
                              message="No image file provided", success=False)
    
    file = request.files['boardImage']
    if file.filename == '':
        return render_template('board_highlight.html', active_page='board_highlight',
                              message="No image selected", success=False)
    
    if file:
        try:
            # Save the uploaded file
            image_path = save_temp_image(file)
            if not image_path:
                return render_template('board_highlight.html', active_page='board_highlight',
                                      message="Error saving image", success=False)
            
            # Get relative path for display
            rel_path = 'uploads/' + os.path.basename(image_path)
            display_path = url_for('static', filename=rel_path)
            
            # Ensure forward slashes for the original path
            original_path_fixed = image_path.replace('\\', '/')
            
            return render_template('board_highlight.html', active_page='board_highlight',
                                  image_path=display_path, original_path=original_path_fixed,
                                  message="Image uploaded successfully. Click to select area to highlight.", 
                                  success=True)
        
        except Exception as e:
            return render_template('board_highlight.html', active_page='board_highlight',
                                  message=f"Error processing image: {str(e)}", success=False)
    
    return render_template('board_highlight.html', active_page='board_highlight',
                          message="Invalid image file", success=False)

@app.route('/board-highlight/process', methods=['POST'])
def board_highlight_process():
    try:
        data = request.json
        x1 = int(data.get('x1', 0))
        y1 = int(data.get('y1', 0))
        x2 = int(data.get('x2', 0))
        y2 = int(data.get('y2', 0))
        image_path = data.get('imagePath', '')
        
        if not image_path or not os.path.exists(image_path):
            return jsonify({'success': False, 'message': 'Image file not found'})
        
        # Process the image with highlighting
        output_path = process_image(image_path, x1, y1, x2, y2)
        if not output_path:
            return jsonify({'success': False, 'message': 'Error processing image'})
        
        # Get relative path for display
        rel_path = 'uploads/' + os.path.basename(output_path)
        display_path = url_for('static', filename=rel_path)
        
        return jsonify({'success': True, 'imagePath': display_path})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/board-highlight/reset', methods=['POST'])
def board_highlight_reset():
    try:
        data = request.json
        image_path = data.get('imagePath', '')
        
        if not image_path or not os.path.exists(image_path):
            return jsonify({'success': False, 'message': 'Image file not found'})
        
        # Get original image path (remove "_highlighted" if present)
        filename, ext = os.path.splitext(image_path)
        if filename.endswith('_highlighted'):
            original_path = filename[:-12] + ext
        else:
            original_path = image_path
        
        if not os.path.exists(original_path):
            return jsonify({'success': False, 'message': 'Original image not found'})
        
        # Get relative path for display
        rel_path = 'uploads/' + os.path.basename(original_path)
        display_path = url_for('static', filename=rel_path)
        
        return jsonify({'success': True, 'imagePath': display_path})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/board-highlight/save')
def board_highlight_save():
    image_url = request.args.get('image', '')
    
    if not image_url:
        return redirect(url_for('board_highlight'))
    
    # Extract filename from URL
    filename = os.path.basename(image_url.split('?')[0])
    image_path = os.path.join(uploads_dir, filename)
    
    if not os.path.exists(image_path):
        return redirect(url_for('board_highlight'))
    
    # Send the file for download with a browser-friendly filename
    download_name = "highlighted_board.png"
    return send_file(image_path, as_attachment=True, download_name=download_name)

@app.route('/generate-pages')
def generate_pages():
    return render_template('generate_pages.html', active_page='generate_pages')

@app.route('/config', methods=['GET'])
def config():
    return render_template('config.html', active_page='config')

@app.route('/config/save', methods=['POST'])
def save_config():
    api_key_path = request.form.get('api_key_path', '').strip()
    log_output = io.StringIO()
    success = False
    
    with redirect_stdout(log_output):
        print(f"Checking API key path: {api_key_path}")
        
        # Validate that the file exists and is a .txt file
        if not api_key_path.endswith('.txt'):
            print("Error: API key path must point to a .txt file")
        elif not os.path.exists(api_key_path):
            print(f"Error: File not found at {api_key_path}")
        else:
            # Try to read the file to verify it contains an API key
            try:
                with open(api_key_path, 'r') as f:
                    api_key = f.read().strip()
                
                if not api_key:
                    print("Error: API key file is empty")
                else:
                    # Import the function to save the API key path
                    from cgpt_functions import save_api_key_path
                    
                    # Save the configuration
                    if save_api_key_path(api_key_path):
                        print(f"API key path successfully saved")
                        success = True
                    else:
                        print(f"Error saving API key path")
            except Exception as e:
                print(f"Error reading API key file: {str(e)}")
    
    return render_template('config.html', active_page='config',
                          message="Configuration saved successfully!" if success else "Error saving configuration",
                          success=success, log_output=log_output.getvalue())

@app.route('/spell-check', methods=['GET'])
def spell_check():
    return render_template('spell_check.html', active_page='spell_check')

@app.route('/spell-check/submit', methods=['POST'])
def spell_check_submit():
    text_to_check = request.form.get('textToCheck', '').strip()
    
    if not text_to_check:
        return render_template('spell_check.html', active_page='spell_check',
                              error_message="Please enter some text to check")
    
    # Import spell_check function
    from cgpt_functions import spell_check_text
    
    # Perform spell check
    corrected_text, changes, error = spell_check_text(text_to_check)
    
    if error:
        return render_template('spell_check.html', active_page='spell_check',
                              error_message=error, original_text=text_to_check)
    
    # Clean the corrected text if it has markdown code blocks
    if corrected_text and isinstance(corrected_text, str):
        # Remove markdown code blocks if present
        if corrected_text.startswith("```") and corrected_text.endswith("```"):
            corrected_text = corrected_text.split("```", 2)[1]
            if corrected_text.startswith("markdown"):
                corrected_text = corrected_text[9:].strip()
    
    # Add a debug log of changes
    print(f"Spell check changes: {changes}")
    
    return render_template('spell_check.html', active_page='spell_check',
                          original_text=text_to_check,
                          corrected_text=corrected_text,
                          changes=changes,
                          success=True)

if __name__ == '__main__':
    app.run(debug=True)